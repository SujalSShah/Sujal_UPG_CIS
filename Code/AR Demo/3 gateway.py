import cv2
import numpy as np

# --------------------------------------------------
# Load reference image
# --------------------------------------------------
reference = cv2.imread("gateway.jpg")

if reference is None:
    print("Could not find gateway.jpg")
    exit()

# Convert reference image to grayscale
gray_reference = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)


# --------------------------------------------------
# Create ORB detector
# --------------------------------------------------
orb = cv2.ORB_create(nfeatures=1000)

# Find keypoints and descriptors in reference image
kp1, des1 = orb.detectAndCompute(gray_reference, None)

if des1 is None:
    print("Could not find features in gateway.jpg")
    exit()


# --------------------------------------------------
# Create Brute Force Matcher
# --------------------------------------------------
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)


# --------------------------------------------------
# Open DroidCam
# --------------------------------------------------
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not open camera")
    exit()


# --------------------------------------------------
# Function to draw dotted polygon
# --------------------------------------------------
def draw_dotted_line(img, p1, p2, color, thickness=2, gap=10):

    p1 = np.array(p1, dtype=float)
    p2 = np.array(p2, dtype=float)

    distance = np.linalg.norm(p2 - p1)

    if distance == 0:
        return

    direction = (p2 - p1) / distance

    current = 0

    while current < distance:

        start = p1 + direction * current
        end = p1 + direction * min(current + gap, distance)

        cv2.line(
            img,
            tuple(start.astype(int)),
            tuple(end.astype(int)),
            color,
            thickness
        )

        current += gap * 2


def draw_dotted_polygon(img, points, color=(0, 0, 255), thickness=3):

    points = [tuple(point) for point in points]

    for i in range(len(points)):

        p1 = points[i]
        p2 = points[(i + 1) % len(points)]

        draw_dotted_line(
            img,
            p1,
            p2,
            color,
            thickness,
            gap=12
        )


# --------------------------------------------------
# Main camera loop
# --------------------------------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    # Convert camera frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find ORB features in camera frame
    kp2, des2 = orb.detectAndCompute(gray_frame, None)

    detected = False

    if des2 is not None:

        # Match reference image with camera frame
        matches = bf.knnMatch(des1, des2, k=2)

        # Lowe's ratio test
        good_matches = []

        for m, n in matches:

            if m.distance < 0.75 * n.distance:
                good_matches.append(m)


        # Need enough matches for homography
        if len(good_matches) >= 10:

            # Coordinates of matching points
            src_pts = np.float32(
                [kp1[m.queryIdx].pt for m in good_matches]
            ).reshape(-1, 1, 2)

            dst_pts = np.float32(
                [kp2[m.trainIdx].pt for m in good_matches]
            ).reshape(-1, 1, 2)


            # Find homography
            H, mask = cv2.findHomography(
                src_pts,
                dst_pts,
                cv2.RANSAC,
                5.0
            )


            if H is not None:

                # Four corners of gateway.jpg
                h, w = gray_reference.shape

                corners = np.float32([
                    [0, 0],
                    [w, 0],
                    [w, h],
                    [0, h]
                ]).reshape(-1, 1, 2)


                # Transform corners into camera image
                transformed_corners = cv2.perspectiveTransform(
                    corners,
                    H
                )


                # Check number of reliable matches
                inliers = mask.ravel().sum()

                if inliers >= 8:

                    detected = True

                    # Convert points to integer
                    pts = transformed_corners.reshape(-1, 2).astype(int)


                    # ------------------------------------------
                    # Draw RED DOTTED FLOATING FRAME
                    # ------------------------------------------
                    draw_dotted_polygon(
                        frame,
                        pts,
                        color=(0, 0, 255),
                        thickness=3
                    )


                    # ------------------------------------------
                    # Put text above detected image
                    # ------------------------------------------
                    x = pts[0][0]
                    y = pts[0][1] - 15

                    if y < 30:
                        y = pts[0][1] + 30

                    cv2.putText(
                        frame,
                        "Gateway of India",
                        (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 0, 255),
                        2
                    )


    # --------------------------------------------------
    # Display camera frame
    # --------------------------------------------------
    cv2.imshow("AR Gateway Detection", frame)


    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# --------------------------------------------------
# Release camera
# --------------------------------------------------
cap.release()
cv2.destroyAllWindows()
