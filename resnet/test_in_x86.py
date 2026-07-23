import cv2
import json
import numpy as np
from rknn.api import RKNN

# --------------------------------------------------
# Configuration
# --------------------------------------------------
ONNX_MODEL = "resnet50.onnx"
RKNN_MODEL = "resnet50.rknn"
IMAGE_PATH = "cat.jpg"
CONFIG_JSON = "config.json"

# --------------------------------------------------
# Load ImageNet labels from config.json
# --------------------------------------------------
with open(CONFIG_JSON, "r") as f:
    config = json.load(f)

id2label = config["id2label"]

# --------------------------------------------------
# Create RKNN object
# --------------------------------------------------
rknn = RKNN(verbose=True)

print("=" * 60)
print("RKNN CONFIG")
print("=" * 60)

ret = rknn.config(
    target_platform="rk3588",
    mean_values=[[123.675, 116.28, 103.53]],
    std_values=[[58.395, 57.12, 57.375]],
)

assert ret == 0

# --------------------------------------------------
# Load ONNX
# --------------------------------------------------
print("=" * 60)
print("LOAD ONNX")
print("=" * 60)

ret = rknn.load_onnx(model=ONNX_MODEL)
assert ret == 0

# --------------------------------------------------
# Build RKNN
# --------------------------------------------------
print("=" * 60)
print("BUILD RKNN")
print("=" * 60)

ret = rknn.build(do_quantization=False)
assert ret == 0

# --------------------------------------------------
# Export RKNN
# --------------------------------------------------
print("=" * 60)
print("EXPORT RKNN")
print("=" * 60)

ret = rknn.export_rknn(RKNN_MODEL)
assert ret == 0

print("Saved:", RKNN_MODEL)

# --------------------------------------------------
# Initialize Simulator
# --------------------------------------------------
print("=" * 60)
print("INIT RUNTIME")
print("=" * 60)

ret = rknn.init_runtime()
assert ret == 0

# --------------------------------------------------
# Read Image
# --------------------------------------------------
img = cv2.imread(IMAGE_PATH)

if img is None:
    raise RuntimeError("Cannot open image")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.resize(img, (224, 224))

img = np.expand_dims(img, axis=0)

print("Input Shape:", img.shape)

# --------------------------------------------------
# Inference
# --------------------------------------------------
outputs = rknn.inference(
    inputs=[img],
    data_format=["nhwc"]
)

scores = outputs[0].reshape(-1)

print("Output Shape:", outputs[0].shape)



print("\n")
# Find the class with the highest score
predicted_class = np.argmax(scores)

print("\n" + "=" * 60)
print("Prediction")
print("=" * 60)

print(f"Class ID : {predicted_class}")
print(f"Score    : {scores[predicted_class]:.4f}")
print(f"Label    : {id2label[str(predicted_class)]}")

print("=" * 60)

print("=" * 70)

# --------------------------------------------------
# Release
# --------------------------------------------------
rknn.release()
