# Import necessary modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
                 
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create an empty dictionary to store the results
    results_dic = dict()

    # Retrieve all filenames from the image directory
    filenames = listdir(image_dir)
    
    # Iterate over each filename in the directory
    for filename in filenames:
        # Skip dotfiles (files starting with a dot)
        if filename.startswith('.'):
            continue

        # Initialize an empty string for the pet label
        pet_label = ""
        
        # Convert the filename to lowercase and split by underscores
        word_list = filename.lower().split('_')
        
        # Loop through the words and build the pet label with alphabetic words
        for word in word_list:
            if word.isalpha():  # Check if the word is alphabetic
                pet_label += word + " "
        
        # Strip the trailing whitespace from the label
        pet_label = pet_label.strip()
        
        # Add the filename and its corresponding pet label to the dictionary
        results_dic[filename] = [pet_label]
    
    # Return the results dictionary
    return results_dic
