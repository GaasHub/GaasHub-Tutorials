# -*- coding: utf-8 -*-
import os
import glob
import torch
import sys
from yolo_utils import ObjectDetector

def main():
    print("[INFO] YOLOv11 Batch Inference Started")
    print(f"[INFO] Execution Environment: {os.uname().sysname}")

    # Device selection
    if torch.cuda.is_available():
        device = 'cuda:0'
        print(f"[INFO] GPU DETECTED: {torch.cuda.get_device_name(0)}")
    else:
        device = 'cpu'
        print("[WARN] NO GPU DETECTED! Inference will run on CPU.")

    # Input folder containing images
    input_folder = "input_images"
    output_folder = "output_images"
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # Collect image paths
    valid_ext = ('*.jpg', '*.jpeg', '*.png', '*.bmp')
    image_paths = []
    for ext in valid_ext:
        image_paths.extend(glob.glob(os.path.join(input_folder, ext)))
    image_paths = sorted(image_paths)

    # If fewer than 3 images, generate dummy images to fill the batch
    if len(image_paths) < 3:
        import numpy as np
        import cv2
        print(f"[WARN] Found only {len(image_paths)} image(s). Generating dummies to reach batch size of 3...")
        for i in range(len(image_paths), 3):
            dummy_path = os.path.join(input_folder, f"dummy_{i}.jpg")
            dummy = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
            cv2.imwrite(dummy_path, dummy)
            image_paths.append(dummy_path)

    batch_paths = image_paths[:3]
    print(f"\n[INFO] Batch of {len(batch_paths)} images:")
    for p in batch_paths:
        print(f"   - {p}")

    # Initialize detector
    detector = ObjectDetector(model_name='yolo11n.pt', device=device)

    # Run batch detection
    batch_detections = detector.detect(batch_paths, output_folder=output_folder)

    # Print summary per image
    print("\n[INFO] Detection Summary:")
    for img_path, detections in zip(batch_paths, batch_detections):
        print(f"\n[IMG] {os.path.basename(img_path)} -- {len(detections)} detections")
        for det in detections:
            print(f"   - Class ID: {int(det[5])}, Confidence: {det[4]:.2f}")

    print(f"\n[DONE] Check '{output_folder}/' for annotated images.")

if __name__ == "__main__":
    main()
