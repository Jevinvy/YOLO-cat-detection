from ultralytics import YOLO
import cv2

# load the trained model
model = YOLO("models/best.pt")

def main():
    cap = cv2.VideoCapture(0) # opens webcam
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame")
            break

            results = model(frame)

            annotate_frame = results[0].plot()

            cv2.imshow("Cat Detector (Webcam)", annotate_frame)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()