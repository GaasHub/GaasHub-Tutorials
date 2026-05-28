# -*- coding: utf-8 -*-
from ultralytics import YOLO
import cv2
import numpy as np
import os

class ObjectDetector:
    def __init__(self, model_name='yolo11n.pt', device='cuda:0'):
        print(f"[INFO] Loading YOLOv11 Model: {model_name}...")
        # This will auto-download the weights if not present
        self.model = YOLO(model_name)
        self.device = device
        self.model.to(device)
        print(f"[INFO] Model loaded successfully on {device}!")

    def detect(self, image_input, output_folder='output_images', conf_threshold=0.5):
        # Normalize input -- accept a single path OR a list of paths
        if isinstance(image_input, str):
            image_paths = [image_input]
        else:
            image_paths = list(image_input)

        print(f"[INFO] Running batch inference on {len(image_paths)} image(s)...")

        # Ultralytics handles batching natively when you pass a list
        results = self.model(image_paths, conf=conf_threshold, device=self.device)

        # Make sure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Process EACH result, not just results[0]
        all_detections = []
        for img_path, result in zip(image_paths, results):
            num_boxes = len(result.boxes) if result.boxes is not None else 0
            print(f"[INFO] {os.path.basename(img_path)} -- Detected {num_boxes} object(s).")

            # Save with unique filename per image (no more overwriting)
            output_path = os.path.join(output_folder, f"det_{os.path.basename(img_path)}")
            result.save(filename=output_path)
            print(f"[INFO] Saved annotated image to: {output_path}")

            # Collect detections (x1, y1, x2, y2, conf, cls)
            dets = result.boxes.data.cpu().numpy() if result.boxes is not None else np.empty((0, 6))
            all_detections.append(dets)

        return all_detections
