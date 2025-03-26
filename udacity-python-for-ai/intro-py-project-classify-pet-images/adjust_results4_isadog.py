# adjust_results4_isadog.py

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjust the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """  
    
    # Create a dictionary to store the dog names from the dogfile
    dognames_dic = {}
    
    # Open and read the dog names file
    with open(dogfile, 'r') as file:
        for line in file:
            dog_name = line.rstrip()  # Remove trailing newline characters
            dognames_dic[dog_name] = 1  # Use 1 to mark that this is a dog name
    
    # Iterate through the results_dic and adjust for whether labels are of a dog or not
    for key in results_dic:
        pet_label = results_dic[key][0]  # Pet image label (string)
        classifier_label = results_dic[key][1]  # Classifier label (string)
        
        # Check if the pet label is a dog
        if pet_label in dognames_dic:
            results_dic[key].append(1)  # Index 3: Pet label is a dog (1)
        else:
            results_dic[key].append(0)  # Index 3: Pet label is NOT a dog (0)
        
        # Check if the classifier label is a dog
        if classifier_label in dognames_dic:
            results_dic[key].append(1)  # Index 4: Classifier label is a dog (1)
        else:
            results_dic[key].append(0)  # Index 4: Classifier label is NOT a dog (0)
