from ultralytics import YOLO

model = YOLO('yolov8m')

results = model.predict('input_videos/clip.mp4', save = True)
