import os
from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    with Image.open(input_path) as img:
        output = remove(img)
        output.save(output_path)

def process_images():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    for filename in os.listdir(current_dir):
        if filename.lower().endswith('.jpg'):
            input_path = os.path.join(current_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '_nobg.png'
            output_path = os.path.join(current_dir, output_filename)
            
            print(f"Processing: {filename}")
            remove_background(input_path, output_path)
            print(f"Saved as: {output_filename}")

if __name__ == "__main__":
    process_images()