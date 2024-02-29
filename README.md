
# Dataset-Compression

**Dataset Compression Library is a powerful tool for compressing image datasets using four different methods. With a single command, you can easily process all photos in a folder, making it an efficient solution for managing and optimizing your image datasets.**


*****



**sample of datalog.txt**

![Alt text](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/Capture.PNG)


*****
## Table of Contents

- [Dataset-Compression](#Dataset-Compression)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Description](#description)
  - [Example](#example)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [About Us](#about-us)

*****

## Introduction
Image Compression is a versatile and efficient solution for manipulating and optimizing images in various ways. Whether you're preparing images for deep learning, enhancing web performance, or managing storage resources, this tool provides a range of compression modes to meet your specific requirements.

******

## Features
- **Scalability for Large Datasets:** Our image compression tool is optimized to handle large datasets seamlessly. Whether you're dealing with massive image collections or high-resolution data, the tool ensures efficient processing and compression.

- **Comprehensive Reporting System:** Gain insights into the compression process with our detailed reporting system. Track compression ratios, file sizes, and other relevant metrics, empowering you to make informed decisions about image optimization.

- **Disk Space Optimization:** Save valuable disk space by utilizing our advanced compression modes. The tool intelligently reduces image sizes without compromising quality, contributing to efficient storage management.

- **Resource-Efficient Learning Algorithms:** Enable faster and more resource-efficient machine learning algorithms by preprocessing your image data with our compression tool. By reducing the computational load, you can accelerate model training and enhance overall performance.
  
- **Batch Processing:** Streamline your workflow with batch processing capabilities, allowing you to compress multiple images simultaneously. Ideal for managing large datasets efficiently.

- **Cross-Platform Compatibility:** The Image Compression Tool supports various platforms, making it adaptable to different environments. Whether you're working on Windows, macOS, or Linux, our tool ensures consistent performance.

- **Customizable Compression Parameters:** Tailor compression parameters to suit your specific requirements. Adjust quality settings, resize dimensions, and fine-tune other parameters based on your optimization goals.

****

## Description

Our project has 4 modes for the compression of images.


**Mode 1:`Pyramid Size Compression`**

The first mode to compress is pyramid size. The pyramid size changes each layer's size of (height/2) and (width/2).
For instance, if the original image size is 1920x1080 and the compression is applied at layer 5, the resulting image dimensions become `60x34`. In mathematical terms, the algorithm operates as `(image / 2^n)`, with 'n' representing the layer number. This process effectively creates a pyramid of images, with each layer representing a progressively smaller version of the original.

**Mode 2:`Compression Resize`**

The second mode to compress is resizing. resize is a Python script designed for image compression and resizing, offering flexibility in adjusting the width of an input image. This script is particularly useful in scenarios where images need to be prepared for deep learning applications or when resizing while maintaining the aspect ratio is crucial.
The script employs the OpenCV library to compress and resize input images efficiently.
  
Aspect Ratio Control: Users have the option to maintain the aspect ratio during the resizing process or enforce a square resize, making it suitable for various use cases, including deep learning applications
 
**Mode 3:`Compression with Quality`**

This function applies JPEG compression to an input image with a specified quality parameter. It returns the compressed image along with the compression result and additional details.

hint >>> No.1: Low image quality, very high compression.| No. 100: Very high image quality, very low compression.

**Mode 4: `Mode4-compresion_crop`**

The Mode4_crop function is designed to crop an input image based on specified endpoints, providing flexibility in selecting regions of interest within the image. The crop starts from the center of the image.

***

## Example

we have 4 images for 4 modes to example and show each image how to look after compressing.


| Image 1 | result of image  in    `Mod1_compression_pyramid` in                 layer 3  (122 * 57)   |
|---------|--------------------------------------------------------------------------------------------|
| ![IMG_4767](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/input_path/IMG_4767.JPEG) | ![Result](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/output_path/output_folder_1/IMG_4767.JPEG)|

| Image 2 | result of image  in   `Mod2_compression_resize`  in                (170 * 170)    |
|---------|-----------------------------------------------------------------------------------|
| ![paris-street-musicians](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/input_path/paris-street-musicians.jpg) |![paris-street-musicians](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/output_path/output_folder_2/paris-street-musicians.jpg) |



 
| Image 3 | result of image in   'Mod3_compresion_quality' in              10    |
|---------|----------------------------------------------------------------------|
|![57940_370990626304408_407247883_n](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/input_path/57940_370990626304408_407247883_n.jpg)|![[57940_370990626304408_407247883_n]](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/output_path/output_folder_3/57940_370990626304408_407247883_n.jpg)|





| Image 4 | result of image 1 in  'Mode4-compresion_crop` in                   (468 * 562) |
|---------|--------------------------------------------------------------------------------| 
|![1c45a63c47d89c6fd583c75b067b13d9](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/input_path/1c45a63c47d89c6fd583c75b067b13d9.jpg)|![1c45a63c47d89c6fd583c75b067b13d9](https://github.com/neonicX-Tech/Dataset-Compression/blob/main/output_path/output_folder_4/1c45a63c47d89c6fd583c75b067b13d9.jpg)|


***
**Example Data Log for Image28 in Each Mode. this example is in output_path.**

 - For Mode 1: Pyramid Size Compression
 
 ```python
num_layers = ("Enter the number of layers: ")
```
 
| Image Name | Original Size | Old File Size | New File Size | Mode | Result  | Details                                                    |
|------------|---------------|---------------|---------------|------|---------|------------------------------------------------------------|
| image(28)  | 450x970       | 163537        | 4260          | 1    | Success | In the Mod1_pyramid, the output image becomes 57x122 image |




- For Mode 2: Compression Resize

 ```python
 is_deeplearning = ("Do you need to use deep learning? (yes/no): ")
 new_width = ("Enter the new image width: ")
```


| Image Name | Original Size | Old File Size | New File Size | Mode | Result  | Details                                                                         |
|------------|---------------|---------------|---------------|------|---------|---------------------------------------------------------------------------------|
| image(28)  | 450x970       | 163537        | 21057         | 2    | Success | Mod2_compression_resize completed successfully. Resized image dimensions: (170, 170, 3) |



- For Mode 3: Mod3_compresion_quality
 
 ```python
quality = ("Enter the image quality (1-100): ")
```


| Image Name | Original Size | Old File Size | New File Size | Mode | Result  | Details                                       |
|------------|---------------|---------------|---------------|------|---------|-----------------------------------------------|
| image(28)  | 450x970       | 163537        | 146921        | 3    | Success | Image successfully compressed with quality 30. |


- For Mode 4: Mode4-compresion_crop

 ```python
end_x = ("Enter the value for end_x: ")
end_y = ("Enter the value for end_y: ")
```


| Image Name | Original Size | Old File Size | New File Size | Mode | Result  | Details                                                       |
|------------|---------------|---------------|---------------|------|---------|---------------------------------------------------------------|
| image(28)  | 450x970       | 163537        | 113740        | 4    | Success | Image successfully cropped from center (150,385) to (300,585).|




****

## Getting Started


Our project is organized into one main components:

1. **Main Compression File:**
   - This file contains the primary logic for image compression.


- we put a sample image directory for testing.

***
### Prerequisites

Before you start using the Image Compression Tool, make sure you have the following software and libraries installed:

1. **Python:** The tool is built using Python, so you'll need to have it installed on your machine. If you don't have Python installed, download it
from the Python site below.

   [![Python Logo](https://www.python.org/static/community_logos/python-logo.png)](https://www.python.org/downloads/).

3. **Development Environment (Optional):**
   - **VS Code:** If you prefer a powerful and feature-rich code editor, consider using Visual Studio Code (VS Code). Download it from [here](https://code.visualstudio.com/).
   - **Google Colab (Optional):** For a cloud-based, collaborative Python environment, you can use Google Colab. Access it at [Google Colab](https://colab.research.google.com/).

****
### Installation

**Dependencies:** Install the necessary Python libraries

You can install from the requirements text file:

**`pip install -r  requirements.txt `**


**If you can't install the requirement above we write all the libraries you need to install in Windows  and Mac**


|     pip install opencv-python  | pip install matplotlib    |
|--------------------------------|---------------------------|
|     pip install numpy          |    pip install tqdm       | 
|     pip install pandas         |    pip install tabulate   |
|     pip install glob2          |    pip install pillow     |

*****

### Limitations

Before you start using the code, here are some important considerations:

1. **Supported Image Formats:** The algorithm accepts input images in the formats JPG, PNG, and JPEG. Images in other formats won't be compressed by our algorithm.

2. **Minimum Image Dimensions:** It is recommended to avoid using images with dimensions shorter than 30 pixels. Although the algorithm can compress such images, be aware that very short images may result in a significant size reduction.

3. **Compression Quality Setting:** For optimal quality, it is advised to set the compression quality parameter to a value lower than 30. Lower-quality settings may result in higher levels of compression but may also lead to a noticeable loss in image quality.

  

## Usage

Our project offers four compression modes, each with a set of questions to guide you through the configuration process. Here's a brief overview:


- **Give the directory of the image**

choose Mode:

**Mode 1: Pyramid Size Compression**

- Choose the number of layers for pyramid size compression:

    - Specify the desired number of layers to obtain the compressed image.

**Mode 2: Compression Resize**

- Do you want to choose deep learning or specify a resize ratio?

    - **Deep Learning:** Set `deeplearning=True`

        - Get the width size from your configuration.

        - Change your image to the same size of height and width.

    - **Resize Ratio:** Set `deeplearning=False`

        - Get the width size from your configuration.

        - Change your image with a ratio of size of height and width.
     
      
**Mode 3: Compression with Quality**

- Get the quality for compressing your images.

hint >>> No.1: Low image quality, very high compression.| No. 100: Very high image quality, very low compression.

**Mode 4: Crop Images**

- Get the endpoint coordinates:
  - `end_x`: Specify the ending point in the X dimension.
  - `end_y`: Specify the ending point in the Y dimension.

- Crop the image based on the specified coordinates.

## In The End

For configuration tables, create an `output_folder` in the `output-path` adjacent to the `input-path`. Compressed images will be saved in this folder.

Additionally:

- Data logs will be stored in the `output folder`.

- If you wish to run each code to try another mode, a new folder with a unique identifier (e.g., a new number) will be created in the `output_path`. Each run will have its dedicated folder for organized outputs.

 check the respective folders for the results and logs corresponding to each run.

*****

## Contributing

Explain how people can contribute to your project. Include guidelines for pull requests and reporting issues.

***
## License

[![License](https://img.shields.io/badge/License-GNU%20LGPL%20v2.1-blue.svg)](LICENSE)

***
## About Us

[Provide information about the team or individuals behind the project. Share your vision, mission, or goals.]
