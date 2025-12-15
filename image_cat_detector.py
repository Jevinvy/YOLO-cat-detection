from ultralytics import YOLO
import cv2

model = YOLO("models/best.pt")

def detect_image(image_path: str):
    img = cv2.imread(image_path)
    if img is None:
        print("Can't load image")
        return

    results = model(img)

    annotated = results[0].plot()

    max_width = 1000
    h, w = annotated.shape[:2]
    if w > max_width:
        scale = max_width / w
        annotated = cv2.resize(annotated,
                               (int(w*scale), int(h*scale)),
                               interpolation=cv2.INTER_AREA)

        cv2.imshow("Cat Detector (Webcam)", annotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_image(r"") # enter image path