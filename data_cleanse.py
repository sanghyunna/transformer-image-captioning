import os
import json

def clean_images_and_json(json_file_path, image_directory, modified_json_file_path):
    # Step 1: Load the JSON file and extract the keys
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    json_keys = set(data.keys())

    print("Deleted images:")
    # Step 2: Iterate through the files in the given directory
    for filename in os.listdir(image_directory):
        # Check if the file is an image
        if filename.lower().endswith('.jpg'):
            # Check if the file name matches any key in the JSON
            if filename not in json_keys:
                # If no match found, delete the image file
                file_path = os.path.join(image_directory, filename)
                os.remove(file_path)
                print(f"{file_path} ", end="")

    # Step 3: Iterate through the keys in the JSON file to remove orphaned keys
    keys_to_check = list(data.keys())

    print("\nRemoved keys from JSON:")
    for key in keys_to_check:
        # Construct the expected image file name
        image_filename = key
        image_path = os.path.join(image_directory, image_filename)

        # Check if the image file exists
        if not os.path.exists(image_path):
            # If the image doesn't exist, remove the key from the JSON data
            del data[key]
            print(f"{key} ", end="")

    # Step 4: Save the modified JSON data to the specified file
    with open(modified_json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
json_file_path = './source/sorted_captions.json'  # Path to your JSON file
image_directory = './temp'  # Path to your image directory
modified_json_file_path = './source/modified_captions.json'  # Path for the modified JSON file

clean_images_and_json(json_file_path, image_directory, modified_json_file_path)
