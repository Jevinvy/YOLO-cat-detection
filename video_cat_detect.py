from ultralytics import YOLO
import cv2

model = YOLO("models/best.pt")

def main():
    video_path = r""  # add your video path
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Failed to open video")
        return

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter("cat_video_detected.mp4", fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated = results[0].plot()

        cv2.imshow("Cat Detector(Video)", annotated)
        out.write(annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()