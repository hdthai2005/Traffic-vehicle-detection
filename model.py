from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8s.pt")

    model.train(data = "dataset.yaml", epochs = 100, imgsz = 640)
    metrics = model.val()
    print(metrics)