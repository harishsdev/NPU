import torch
from transformers import ResNetForImageClassification

# Load the model from your local directory
model = ResNetForImageClassification.from_pretrained("models/resnet50")
model.eval()

# Dummy input (ResNet-50 expects 224x224 RGB images)
dummy_input = torch.randn(1, 3, 224, 224)

# Export to ONNX
torch.onnx.export(
    model,
    dummy_input,
    "resnet50.onnx",
    input_names=["images"],
    output_names=["logits"],
    opset_version=12,
    do_constant_folding=True,
)

print("Export completed: resnet50.onnx")
