import cv2

# Open DroidCam (camera index = 1)
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Check whether camera opened
if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:

    # Capture one frame
    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    # Display some text
    cv2.putText(frame,
                "Gateway of India",
                (40, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (0, 0, 255),
                2)


    cv2.rectangle(frame,
              (200,120),
              (500,380),
              (0,0,255),
              3)




    # Show frame
    cv2.imshow("AR Step 1", frame)

    # Quit when Q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
