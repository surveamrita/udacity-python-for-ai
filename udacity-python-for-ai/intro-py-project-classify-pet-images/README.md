# CNN Model Architecture Comparison

This report compares the performance of three CNN model architectures—**AlexNet**, **ResNet**, and **VGG**—on a set of 40 images, consisting of both dog and non-dog images.

---

## Instructions to Run the Model Comparison

Follow the steps below to run the comparison script for the three models (AlexNet, ResNet, and VGG) using the `run_models_batch.sh` script.

### Prerequisites:
1. **Python** and required libraries (e.g., PyTorch, torchvision) must be installed.
2. **ImageNet labels file** (`imagenet1000_clsid_to_human.txt`) should be available in the same directory as the script.
3. Ensure the images to be classified are in the correct directory and follow the expected format.

### Steps to run:
1. Clone or navigate to the directory containing the model comparison files.
2. Make sure the `run_models_batch.sh` file has execution permission. If not, run:
   ```bash
   chmod +x run_models_batch.sh
