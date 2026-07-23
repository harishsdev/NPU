import cv2
import json
import numpy as np
from rknnlite.api import RKNNLite

RKNN_MODEL = "resnet50.rknn"
IMAGE_PATH = "cat.jpg"
CONFIG_JSON = "config.json"

# Load labels
with open(CONFIG_JSON, "r") as f:
    id2label = json.load(f)["id2label"]

# Create RKNNLite object
rknn = RKNNLite()

# Load RKNN model
ret = rknn.load_rknn(RKNN_MODEL)
if ret != 0:
    raise RuntimeError("Failed to load RKNN model")

# Initialize NPU runtime
ret = rknn.init_runtime()
if ret != 0:
    raise RuntimeError("Failed to initialize runtime")

print("RKNN Runtime initialized successfully.")

# Read image
img = cv2.imread(IMAGE_PATH)

if img is None:
    raise RuntimeError("Cannot read image")

# BGR -> RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Resize
img = cv2.resize(img, (224, 224))

# NHWC
img = np.expand_dims(img, axis=0)

# Inference
outputs = rknn.inference(inputs=[img])

scores = outputs[0].reshape(-1)

# Top-1 prediction
pred = np.argmax(scores)

print("\n==============================")
print("Prediction")
print("==============================")
print("Class ID :", pred)
print("Score    :", float(scores[pred]))
print("Label    :", id2label[str(pred)])
print("==============================")

rknn.release()
