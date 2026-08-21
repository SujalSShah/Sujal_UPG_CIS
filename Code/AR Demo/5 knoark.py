import cv2

# -------------------------------
# Load Konark Sun Temple image
# -------------------------------
konark = cv2.imread("konark.jpg")

gray_konark = cv2.cvtColor(konark, cv2.COLOR_BGR2GRAY)

# ORB detector
orb = cv2.ORB_create()

# Find features in konark image
kp1, des1 = orb.detectAndCompute(gray_konark, None)

# Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)


# -------------------------------
# Open DroidCam
# -------------------------------
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not open camera")
    exit()


while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Convert camera image to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find features in camera image
    kp2, des2 = orb.detectAndCompute(gray_frame, None)

    if des2 is not None:

        # Match konark image with camera image
        matches = bf.match(des1, des2)

        # Sort matches
        matches = sorted(matches, key=lambda x: x.distance)

        # Check if enough good matches
        if len(matches) > 20:

            # Get positions of matched points
            points = []

            for match in matches[:20]:

                x, y = kp2[match.trainIdx].pt
                points.append((int(x), int(y)))

            # Find rectangle around matched points
            x_values = [p[0] for p in points]
            y_values = [p[1] for p in points]

            x1 = min(x_values)
            y1 = min(y_values)
            x2 = max(x_values)
            y2 = max(y_values)

            # Draw RED rectangle
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 0, 255),
                3
            )

            # Display text
            cv2.putText(
                frame,
                "Konark Sun Temple",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

    # Show camera
    cv2.imshow("AR konark", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
