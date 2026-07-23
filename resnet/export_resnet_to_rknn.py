from rknn.api import RKNN

ONNX_MODEL = "resnet50.onnx"
RKNN_MODEL = "resnet50.rknn"

rknn = RKNN(verbose=True)

ret = rknn.config(
    target_platform="rk3588",
    mean_values=[[123.675, 116.28, 103.53]],
    std_values=[[58.395, 57.12, 57.375]],
)
if ret != 0:
    raise RuntimeError("RKNN config failed")

ret = rknn.load_onnx(model=ONNX_MODEL)
if ret != 0:
    raise RuntimeError("Failed to load ONNX")

ret = rknn.build(do_quantization=False)
if ret != 0:
    raise RuntimeError("Build failed")

ret = rknn.export_rknn(RKNN_MODEL)
if ret != 0:
    raise RuntimeError("Export failed")

print("RKNN model saved as:", RKNN_MODEL)

rknn.release()
