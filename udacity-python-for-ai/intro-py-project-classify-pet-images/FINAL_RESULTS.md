# CNN Model Architecture Comparison

This report compares the performance of three CNN model architectures—**AlexNet**, **ResNet**, and **VGG**—on a set of 40 images, consisting of both dog and non-dog images.

## 1. AlexNet
- **Number of Images**: 40  
- **Number of Dog Images**: 30  
- **Number of 'Not-a' Dog Images**: 10  

### Performance Metrics:  
- **Percentage of Correct Dog Classifications**: 100.00%  
- **Percentage of Correct 'Not-a' Dog Classifications**: 100.00%  
- **Percentage of Correct Breeds**: 80.00%  
- **Percentage of Correct Matches**: 90.00%  

### Incorrectly Classified Dog Breeds:
- **Image**: Boston_terrier_02285.jpg | **Pet Label**: boston terrier | **Classifier Label**: basenji  
- **Image**: Great_pyrenees_05367.jpg | **Pet Label**: great pyrenees | **Classifier Label**: kuvasz  
- **Image**: Golden_retriever_05257.jpg | **Pet Label**: golden retriever | **Classifier Label**: afghan hound  
- **Image**: Beagle_01141.jpg | **Pet Label**: beagle | **Classifier Label**: english foxhound  
- **Image**: Golden_retriever_05182.jpg | **Pet Label**: golden retriever | **Classifier Label**: tibetan mastiff  
- **Image**: Beagle_01170.jpg | **Pet Label**: beagle | **Classifier Label**: walker hound  

**Total Elapsed Runtime**: 0:0:6  

---

## 2. ResNet
- **Number of Images**: 40  
- **Number of Dog Images**: 30  
- **Number of 'Not-a' Dog Images**: 10  

### Performance Metrics:  
- **Percentage of Correct Dog Classifications**: 100.00%  
- **Percentage of Correct 'Not-a' Dog Classifications**: 90.00%  
- **Percentage of Correct Breeds**: 90.00%  
- **Percentage of Correct Matches**: 97.50%  

### Incorrectly Classified Dog Breeds:
- **Image**: Great_pyrenees_05367.jpg | **Pet Label**: great pyrenees | **Classifier Label**: kuvasz  
- **Image**: Golden_retriever_05182.jpg | **Pet Label**: golden retriever | **Classifier Label**: leonberg  
- **Image**: Beagle_01170.jpg | **Pet Label**: beagle | **Classifier Label**: walker hound  

**Total Elapsed Runtime**: 0:0:11  

---

## 3. VGG
- **Number of Images**: 40  
- **Number of Dog Images**: 30  
- **Number of 'Not-a' Dog Images**: 10  

### Performance Metrics:  
- **Percentage of Correct Dog Classifications**: 100.00%  
- **Percentage of Correct 'Not-a' Dog Classifications**: 100.00%  
- **Percentage of Correct Breeds**: 93.33%  
- **Percentage of Correct Matches**: 105.00%  

### Incorrectly Classified Dog Breeds:
- **Image**: Great_pyrenees_05367.jpg | **Pet Label**: great pyrenees | **Classifier Label**: kuvasz  
- **Image**: Beagle_01170.jpg | **Pet Label**: beagle | **Classifier Label**: walker hound  

**Total Elapsed Runtime**: 0:0:44  

---

## Summary Comparison

| **Metric**                                    | **AlexNet** | **ResNet** | **VGG**  |
|-----------------------------------------------|-------------|------------|----------|
| **Number of Images**                          | 40          | 40         | 40       |
| **Number of Dog Images**                     | 30          | 30         | 30       |
| **Number of 'Not-a' Dog Images**             | 10          | 10         | 10       |
| **Pct Correct Dog Classifications**          | 100.00%     | 100.00%    | 100.00%  |
| **Pct Correct 'Not-a' Dog Classifications**  | 100.00%     | 90.00%     | 100.00%  |
| **Pct Correct Breed Classifications**        | 80.00%      | 90.00%     | 93.33%   |
| **Pct Correct Matches**                      | 90.00%      | 97.50%     | 105.00%  |
| **Total Elapsed Runtime**                    | 0:0:6       | 0:0:11     | 0:0:44   |

---

## Best Model Architecture

**VGG** performed the best in terms of accuracy, with the highest percentage of correct breed classifications (93.33%) and the highest overall percentage of correct matches (105.00%). Despite its longer runtime (0:0:44), VGG achieved superior results in classifying dog breeds.

### **Conclusion**:  
While all models showed excellent performance in classifying dog images, **VGG** is the best model based on its higher breed classification accuracy and overall match percentage.

---
