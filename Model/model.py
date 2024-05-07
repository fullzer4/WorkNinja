import torch
import torchvision.models as models

resnet_model = models.resnet50(pretrained=True)

input_example = torch.randn(1, 3, 224, 224)

torch.onnx.export(resnet_model, input_example, "resnet50.onnx", export_params=True)
