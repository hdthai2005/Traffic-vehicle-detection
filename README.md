# Traffic-vehicle-detection
traffic vehicle detection using yolov8

This is a model using yolo v8s for object detection to detect and label vehicle through traffic images.
Since the raw data is label with (0 - 3) for daytime class, and (4 - 7) for nighttime class, with
0 - motorbike
1 - family or small car
2 - holiday or business car
3 - truck and container,... etc

I have use data augmentation for the dataset and balacing the data because the original data is not good(unbalance) yet
