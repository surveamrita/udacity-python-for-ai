import ast
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
from torch import __version__

# Load models with updated weight arguments
resnet18 = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
alexnet = models.alexnet(weights=models.AlexNet_Weights.IMAGENET1K_V1)
vgg16 = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)

models_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Obtain ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    # Load the image
    img_pil = Image.open(img_path)

    # Define transforms
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Preprocess the image
    img_tensor = preprocess(img_pil)
    
    # Resize the tensor (add dimension for batch)
    img_tensor = img_tensor.unsqueeze(0)
    
    # Check pytorch version
    pytorch_ver = __version__.split('.')
    
    # No need for Variable in PyTorch 0.4+ or higher
    # In newer versions, just set requires_grad_ to False if needed
    img_tensor.requires_grad_(False)
    
    # Get the model
    model = models_dict[model_name]

    # Put the model in evaluation mode
    model = model.eval()

    # Apply data to model (directly for PyTorch 0.4+)
    output = model(img_tensor)

    # Get the predicted class index
    pred_idx = output.argmax(dim=1).item()

    # Get the class label from the dictionary
    classifier_label = imagenet_classes_dict.get(pred_idx, None)

    if classifier_label is None:
        raise ValueError(f"Class index {pred_idx} is not found in the class dictionary.")

    # Ensure the returned class label is a string
    if not isinstance(classifier_label, str):
        raise TypeError(f"Expected a string label, but got {type(classifier_label)}: {classifier_label}")

    # Return the class label
    return classifier_label
