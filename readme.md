# Parallel Image Downloader from CSV

This Python script provides a hassle-free way to download and save images from URLs listed in a CSV file. It addresses the problem of manually downloading

This Python script provides a hassle-free way to download and save images from URLs listed in a CSV file. It addresses the problem of manually downloading and storing images, offering an automated solution that is ideal for large-scale image processing tasks.

## Problem Statement

Downloading numerous images from URLs and keeping track of their local paths can be a cumbersome task. Manual downloads are not only time-consuming but also susceptible to errors, especially when dealing with large datasets.

## Solution

This script streamlines the image downloading process by automating the entire task. It reads the data from a CSV file containing image URLs, downloads these images, and writes back their local paths into a new CSV file. In case of any download failures, the script smartly marks these entries as `None` in the CSV file.

## Key Features

- **Parallel Downloads**: Uses Python's `concurrent.futures` module to perform downloads in parallel, significantly reducing the total download time.
- **Unique Naming**: Uniquely names each downloaded image to avoid any overlap or overwriting of files.
- **CSV Updates**: Creates a new CSV file after downloading, replacing the URLs with the local paths of the downloaded images.

## Installation

Ensure that you have Python 3 installed on your system. You can download it from the official [Python website](https://www.python.org/).

The script requires the following Python libraries:

- requests
- slugify
- PIL

You can install these libraries using pip:

```bash
pip install requests python-slugify Pillow
```
## Usage

Follow these steps to use this script:

1. **Prepare your CSV file**: The CSV file should have the columns 'celeb_name', 'first_image', 'second_image', and 'third_image'. Each row should contain a name and up to three corresponding image URLs.

2. **Run the script**: Use the following command in your terminal to run the script with Python 3:

```bash
   python your_script.py
```
3. **Check the 'images' folder**: The script will download the images and save them in a folder named 'images' in the same directory as the script.

4. **Check the output CSV file**: A new CSV file named 'updated_data.csv' will be created in the same directory. This file will contain the local paths of the downloaded images in place of the original URLs. If an image could not be downloaded, its entry will be marked as None.

Please replace `your_script.py` with the actual filename of your Python script.