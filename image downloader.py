import csv
import random
import requests
import os
from slugify import slugify
from PIL import Image
from concurrent.futures import ThreadPoolExecutor


def csv_to_dict_list(file_path):
    dict_list = []
    try:
        with open(file_path, mode='r') as file:
            csvFile = csv.DictReader(file)
            for lines in csvFile:
                dict_list.append(lines)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    return dict_list

def download_image(url, dest_path):
    dest_path = os.path.join('images', dest_path)
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers,stream=True)
        response.raise_for_status()  # Ensure we got a valid response
        with open(dest_path, 'wb') as file:
            file.write(response.content)
        
        return True, dest_path  # return True and path if successful
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False, None  # return False and None if download failed


def slugify_name_with_suffixes(name):
    suffixes = ['picture.jpg', 'pic.jpg', 'image.jpg', 'images.jpg', 'snapshot.jpg', 'photograph.jpg', 'photo.jpg']
    slugified_name = slugify(name)
    slugified_names = [f'{slugified_name}-{suffix}' for suffix in suffixes]
    return random.sample(slugified_names, 3)



def write_to_csv(data, file_path):
    fieldnames = data.keys()
    file_exists = os.path.isfile(file_path)
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

data = csv_to_dict_list(input("Enter your CSV File Name: ")


with ThreadPoolExecutor(max_workers=3) as executor:  # Adjust max_workers as needed
    for single_data in data:
        celeb_name = single_data['celeb_name']
        image_urls = [single_data['first_image'], single_data['second_image'], single_data['third_image']]
        image_names = slugify_name_with_suffixes(celeb_name)
        unique_urls = list(set(image_urls))
        unique_urls_count = len(unique_urls)

        # Submit the tasks to the thread pool executor
        futures = [executor.submit(download_image, url, name) 
                   for url, name in zip(unique_urls, image_names[:unique_urls_count])]

        # Collect the results as they become available
        results = [f.result() for f in futures]

        successful_images = [res[1] for res in results if res[0]]
        while len(successful_images) < 3:
            successful_images.append(None)  # Add None if less than 3 images were successful
        single_data['first_image'], single_data['second_image'], single_data['third_image'] = successful_images[:3]
        write_to_csv(single_data, 'updated_data.csv')

