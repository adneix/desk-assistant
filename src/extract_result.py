from ultralytics import YOLO

model = YOLO("yolov8n.pt")
res = model("https://ultralytics.com/images/bus.jpg")

for r in res:
    boxes = r.boxes
    for box in boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        cls_name = r.names[cls_id]
        print(f"物品：{cls_name}，置信度：{conf:.2f}")