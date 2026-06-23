import cv2
from ultralytics import YOLO

model = YOLO("best3.pt")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("無法讀取影像畫面")
        break

    results = model(frame, conf=0.8)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Extinguisher Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
