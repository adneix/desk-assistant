from ultralytics import YOLO

class YoloDetector:
    def __init__(self, model_path="../models/yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, img_path, threshold=0.5):
        result = self.model(img_path, conf=threshold)
        obj_list = []
        for r in result:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                name = r.names[cls_id]
                obj_list.append({
                    "name": name,
                    "conf": conf
                })
        return obj_list