
'''
This file is part of Dataset-Compression.

Dataset-Compression is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 2.1 of the License, or
any later version.

Dataset-Compression is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Dataset-Compression. See the full license text in the file LICENSE.
'''



from PIL import Image
import PIL
import os
import cv2
import math
import numpy
import argparse
from glob import glob
from time import sleep
import logging
import pandas as pd
import numpy as np
from tabulate import tabulate
from tqdm import tqdm
from datetime import datetime  # Import datetime module

def Mod1_compression_pyramid(image_tst, num_layers):
    """
    Apply compression pyramid to the input image.

    Parameters:
    - image_tst: Input image to be compressed.
    - num_layers: Number of layers in the pyramid.

    Returns:
    - compressed_image: Compressed image (the last layer in the pyramid).
    - result_IsCorrect: Result of the compression process ('Success' or 'Failed').
    - detail: Details about the compression process.
    """
    result_IsCorrect = "Failed"

    # Check if image dimensions are valid
    if image_tst.shape[0] / 2 < 0 or image_tst.shape[1] / 2 < 0:
        detail = "Size error: Image dimensions are too small"
        result_IsCorrect = "Failed"
        return "Size error: Image dimensions are too small", result_IsCorrect, detail

    # Initialize the compressed image with the original image
    compressed_image = image_tst.copy()

    # Apply compression pyramid
    for i in range(num_layers):
        # Compress the current layer using pyrDown
        compressed_image = cv2.pyrDown(compressed_image)
        detail=("In the Mod1_pyramid, output image becomes pyrDown layer {}".format(compressed_image.shape))
        result_IsCorrect = "Success"

        # Check if the resized image does not meet the minimum size
        if compressed_image.shape[0] < 30 or compressed_image.shape[1] < 30:
            result_IsCorrect = "Failed but saved"
            detail = ("In the Mod1_pyramid, output image becomes pyrDown layer {} ".format(compressed_image.shape))
            print("\nSize error: Image dimensions do not meet the minimum size but we saved. ")
            return compressed_image, result_IsCorrect , detail

    # # Provide details about the compression process
    # detail = f"In the Mod1_pyramid, output image becomes {compressed_image.shape[0]}×{compressed_image.shape[1]} image"
    # Return the compressed image (the last layer in the pyramid) as success
    return compressed_image, result_IsCorrect , detail
def Mod2_compression_resize(image_tst, new_width, is_deeplearning):
    """
    Apply compression resize to the input image.

    Parameters:
    - image_tst: Input image to be compressed.
    - new_width: the new width in the resize.
    - is_deeplearning: If true, use a square resize; otherwise, maintain aspect ratio.

    Returns:
    - resized_image: Compressed image after resizing and result_IsCorrect.
    """
    result_IsCorrect = "Faild but saved"
    if is_deeplearning:
        resized_image = cv2.resize(image_tst, (new_width, new_width))
        result_IsCorrect = "Success"
        # Log success
        detail=("Mod2_compression_resize completed successfully. Resized image dimensions: {}".format(resized_image.shape))
        # return resized_image, result_IsCorrect ,detail
        if new_width < 30:
            # Log size error
            result_IsCorrect = "Faild but saved"
            # detail=("Size error: Image dimensions do not meet the minimum size")
            resized_image = cv2.resize(image_tst, (new_width, new_width))
            detail=("Mod2_compression_resize completed successfully. Resized image dimensions. but too small: {}".format(resized_image.shape))
    else:
        height, width, _ = image_tst.shape
        ratio = new_width / width
        new_height = int(height * ratio)
        resized_image= cv2.resize(image_tst, (new_width, new_height))
        result_IsCorrect = "Success"
        detail=("Mod2_compression_resize completed successfully. Resized image dimensions: {}".format(resized_image.shape))
        # Check if the new height is below the minimum size
        if new_width < 30 or new_height < 30:
            # Log size error
            resized_image= cv2.resize(image_tst, (new_width, new_height))
            result_IsCorrect = "Faild but saved"
            detail=("Mod2_compression_resize completed successfully. Resized image dimensions. but too small: {}".format(resized_image.shape))
    return resized_image, result_IsCorrect ,detail
def Mod3_compresion_quality(image_tst, quality):
    """
    Apply compression with quality to the input image.

    Parameters:
    - image_tst: Input image to be compressed.
    - quality: Image compression quality (0-100).

    Returns:
    - compressed_image: Compressed image.
    """
    # Encode the image with JPEG compression using the specified quality
    result_IsCorrect = "Sucsess"
    _, compressed_image = cv2.imencode('.jpg', image_tst, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
   # Decode the compressed image
    compressed_image = cv2.imdecode(compressed_image, 1)
    # Check if the quality parameter is within the valid range (0-100)
    if 0 < quality < 100:
        detail = f"Image successfully compressed with quality {quality}."
        result_IsCorrect = "Sucsess"

    else:
        result_IsCorrect = "Faild but saved"
        detail = "Compression failed: Invalid quality parameter."

    return compressed_image, result_IsCorrect ,detail

def Mode4_crop(image_tst, end_x, end_y):
    """
    Apply compression with crop images.

    Parameters:
    - image_tst: Input image to be compressed.
    - end_x: The first dimension is always the number of rows or the height of the image.
    - end_y: The second dimension is the number of columns or the width of the image.

    Returns:
    - cropped_image: Cropped image.
    """
    result_IsCorrect = "Success"
    
    # Calculate the center coordinates of the image
    center_x = image_tst.shape[0] // 2
    center_y = image_tst.shape[1] // 2
    
    # Calculate starting coordinates for cropping
    start_x = center_x - end_x // 2
    start_y = center_y - end_y // 2
    
        # Calculate endpoint coordinates
    end_x = start_x + end_x
    end_y = start_y + end_y
    # Cropping an image from the calculated starting point
    cropped_image = image_tst[start_x:start_x + end_x, start_y:start_y + end_y]
    
    # Check if the specified dimensions are valid
    if end_x <= 0 or end_y <= 0:
        result_IsCorrect = "Failed"
        detail = "Invalid dimensions: end_x and end_y must be positive."
        return None, result_IsCorrect, detail
    else:
        detail = f"Image successfully cropped from center ({start_x},{start_y}) to ({end_x},{end_y})."
    
    return cropped_image, result_IsCorrect, detail


def write_logFile(old_image_path, new_image_path, image_name, function, status, detail):
    data_print = []
    time = datetime.now()  # Use datetime module to get the current time
    data_print.append((str(time)))
    # print(str(time))
    data_print.append((image_name))
    old_image = cv2.imread(old_image_path)
    size = f"{old_image.shape[0]}×{old_image.shape[1]}"  # Corrected size retrieval
    data_print.append((size))

    old_mass = os.path.getsize(old_image_path)
    data_print.append((str(old_mass)))

    new_mass = os.path.getsize(new_image_path)
    data_print.append((str(new_mass)))

    data_print.append((str(function)))

    data_print.append((str(status)))

    data_print.append((str(detail)))

    return data_print
log_counter = 1  # Initialize log_counter outside the function

def write_log(path, log_data, is_first=False):
    global log_counter
# log_counter = 1 

    log_entry = f"{log_counter}. {log_data}"
    if is_first:
        with open(path, "w",encoding='utf-8') as log_file:
            log_file.write(log_entry + "\n")
    else:
        with open(path, "a",encoding='utf-8') as log_file:
            log_file.write(log_entry + "\n")
    log_counter += 1
def Managment_compresse():
    not_saved_count=0
    output_path="output_path"
    LOG_FILE_PATH=r'datalog.txt'
    log_data_list = []
    input_path = input("Input path-folder for images: ")

    while not os.path.exists(input_path) or not os.path.isdir(input_path) :
        print(f"Error: Invalid input path. Please provide a valid directory path.")
        input_path = input("Input path folder of images: ")
    
    # Validate image files in the input path
    images = glob(os.path.join(input_path, '*.jpg')) + glob(os.path.join(input_path, '*.jpeg')) + glob(
        os.path.join(input_path, '*.png'))
    if not images:
        print(f"No images found with format: jpg, jpeg, png in {input_path}")
        return
        
    # output_path = os.path.join(output_path)
    # os.makedirs(output_path, exist_ok=True)

    not_saved_count = len(os.listdir(input_path)) - len(images)
    # print(len(os.listdir(input_path)))
    
    output_folder_start = 1
    output_folder = f"output_folder_{output_folder_start}"
    while os.path.exists(os.path.join(output_path, output_folder)):
        output_folder_start += 1
        output_folder = f"output_folder_{output_folder_start}"
    # output_folder = "output_folder_" + str(len(os.listdir(input_path)))
    output_path = os.path.join(output_path, output_folder)
    output_text_path = os.path.join(output_path, LOG_FILE_PATH)
    os.makedirs(output_path, exist_ok=True)

    choice = None

    while choice not in {'1', '2', '3', '4'}:
        choice = input(
            "Choose a mode:\n    1 (Mod1_compression_pyramid)\n or 2 (Mod2_compression_resize)\n or 3 (Mod3_compresion_quality)\n or 4 (Mode4_crop):    ")


    total_size = sum(os.path.getsize(input_path) for input_path in images)
    Kbytes_total_size=f"{total_size/1000}"
    write_log(output_text_path, f"Total size of the original dataset: {Kbytes_total_size} kbytes", True)
    print(f"We make a new folder for each run and save the images in there.")
    print(f"Saving processed images to folder: {output_folder}")

    if choice == '1':
        num_layers = int(input("Enter the number of layers: "))
    elif choice == '2':
        is_deeplearning = input("Do you need to use deep learning? (yes/no): ").lower() == 'yes'
        new_width = int(input("Enter the new image width: "))
    elif choice == '3':
        print("hint >>> No.1: Low image quality, very high compression.| No. 100: Very high image quality, very low compression.")
        quality = int(input("Enter the image quality (1-100): "))
    elif choice == '4':
        end_x = int(input("Enter the value for end_x: "))
        end_y = int(input("Enter the value for end_y: "))
    count=0
    for input_path in tqdm(images, desc='Processing Images'):
        image_tst = cv2.imread(input_path)
        output_path1 = os.path.join(output_path, os.path.basename(input_path))
        count+=1
        image=f"image({count})"
        if choice == '1':
          image_outPut, result, detail = Mod1_compression_pyramid(image_tst, num_layers)
          saved = cv2.imwrite(output_path1, image_outPut)
        elif choice == '2':
            image_outPut, result, detail = Mod2_compression_resize(image_tst, new_width, is_deeplearning)
            saved = cv2.imwrite(output_path1, image_outPut)
        elif choice == '3':
            image_outPut, result, detail = Mod3_compresion_quality(image_tst, quality)
            saved = cv2.imwrite(output_path1, image_outPut)
        elif choice == '4':
            image_outPut, result, detail = Mode4_crop(image_tst, end_x, end_y)
            saved = cv2.imwrite(output_path1, image_outPut)

        log_data = write_logFile(input_path, output_path1 , image, choice, result, detail)
        log_data_list.append(log_data)

    compressed_size = sum(
        os.path.getsize(os.path.join(output_path, os.path.basename(input_path))) for input_path in images)
    Kbytes_compressed_size= f"{compressed_size/1000}"
    percent= (1-compressed_size / total_size) * 100  
    write_log(output_text_path, f"Total size of the compressed dataset: {Kbytes_compressed_size} Kbytes")
    write_log(output_text_path, f"Reduce dataset size: {percent :.2f}%.")
    write_log(output_text_path, f"All images processed and saved in ({output_folder}) that has in output_path")
    write_log(output_text_path, f"{not_saved_count} images were not saved because they are not in jpg, jpeg, png format.")
    print(f"{not_saved_count} images were not saved because they are not in jpg, jpeg, png format. \n")

    write_log(output_text_path, f"{len(images)} number of images compressed.\n") 
    df1 = pd.DataFrame(data=log_data_list, columns=["Time", "Image Name", "Size", "Old file size", "New file size", "Mode", "Result", "Detail"])
    # Format the DataFrame as a table using tabulate
    table = tabulate(df1, headers='keys', tablefmt='fancy_grid')
    # Write the table to a text file with explicit encoding (e.g., utf-8)
    with open(output_text_path, 'a', encoding='utf-8') as file:
        file.write(table+'\n')

if __name__ == "__main__":
    Managment_compresse()
    print("Process was done.")
