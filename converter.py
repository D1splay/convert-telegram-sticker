import argparse
from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import sys

def convert_to_png(image_path):
    img = Image.open(image_path)
    if img.format == 'PNG':
        return img
    else:
        new_path = os.path.splitext(image_path)[0] + '.png'
        img.save(new_path, 'PNG')
        return Image.open(new_path)

def process_image(img_path):
    img = Image.open(img_path).convert('RGBA')

    max_size = 512
    if img.width > max_size or img.height > max_size:
        scaling_factor = min(max_size / img.width, max_size / img.height)
        new_width = int(img.width * scaling_factor)
        new_height = int(img.height * scaling_factor)
        img = img.resize((new_width, new_height), Image.LANCZOS)

    new_image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    x = (512 - img.width) // 2
    y = (512 - img.height) // 2
    new_image.paste(img, (x, y), img)

    output_filename = os.path.splitext(os.path.basename(img_path))[0] + '.png'
    output_path = os.path.join(output_folder, output_filename)
    new_image.save(output_path, 'PNG')

    return output_filename

def print_info():
    print("Name: convert-telegram-sticker")
    print("Version: 0.2-b")
    print("Author: D1splay")
    print("Project Link: https://github.com/D1splay/convert-telegram-sticker")
    print("License: GNU General Public License v3.0")
    sys.exit()

parser = argparse.ArgumentParser(description='Convert images to 512x512 PNG images with transparent padding.')
parser.add_argument('-i', '--input', type=str, help='Input folder containing images')
parser.add_argument('-o', '--output', type=str, help='Output folder for converted images')
parser.add_argument('-c', '--convert', action='store_true', help='Convert images to PNG format if not already in PNG format')
parser.add_argument('-t', '--threads', type=int, default=1, help='Number of threads for parallel processing')
parser.add_argument('-a', '--about', action='store_true', help='Show information about the program')
args = parser.parse_args()

if args.about:
    print_info()

if args.input is None or args.output is None:
    parser.error("You must specify both input and output folders.")

input_folder = args.input
output_folder = args.output
convert_to_png_flag = args.convert
num_threads = args.threads

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

images = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(process_image, img_path) for img_path in images]

    for future in tqdm(as_completed(futures), total=len(images), desc='Processing images'):
        result = future.result()

print("Done")
