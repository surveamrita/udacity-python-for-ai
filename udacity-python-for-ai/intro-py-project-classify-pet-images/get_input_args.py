#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: [Your Name]    
# DATE CREATED: [Date Created]                                 
# REVISED DATE: [Date of Revision]
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# Define get_input_args function
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
      
    This function returns these arguments as an ArgumentParser object.
    """
    
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Classify pet images using a pretrained CNN model.")
    
    # Add 3 command line arguments:
    # --dir (Image folder with default 'pet_images')
    parser.add_argument('--dir', type=str, default='pet_images', 
                        help='Path to the folder of pet images (default: pet_images)')
    
    # --arch (CNN model architecture with default 'vgg')
    parser.add_argument('--arch', type=str, default='vgg', 
                        choices=['vgg', 'alexnet', 'resnet'], 
                        help='Model architecture to use for classification (default: vgg)')
    
    # --dogfile (File with dog names with default 'dognames.txt')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='Text file containing dog breed names (default: dognames.txt)')
    
    # Parse the arguments
    in_args = parser.parse_args()
    
    # Return the parsed arguments
    return in_args
