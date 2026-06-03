import cv2
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects
    results = model(frame, verbose=False)

    # Print detected objects
    detected_objects = []

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        object_name = model.names[cls_id]

        if object_name not in detected_objects:
            detected_objects.append(object_name)

    print("Detected:", detected_objects)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLO Detection", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(100) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
