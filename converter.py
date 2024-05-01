import argparse
from PIL import Image
import os

def convert_to_png(image_path):
    img = Image.open(image_path)
    if img.format == 'PNG':
        return img
    else:
        new_path = os.path.splitext(image_path)[0] + '.png'
        img.save(new_path, 'PNG')
        return Image.open(new_path)

parser = argparse.ArgumentParser(description='Convert images to 512x512 PNG images with transparent padding.')
parser.add_argument('-i', '--input', type=str, required=True, help='Input folder containing images')
parser.add_argument('-o', '--output', type=str, required=True, help='Output folder for converted images')
parser.add_argument('-c', '--convert', action='store_true', help='Convert images to PNG format if not already in PNG format')
args = parser.parse_args()

input_folder = args.input
output_folder = args.output
convert_to_png_flag = args.convert

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        img_path = os.path.join(input_folder, filename)

        if convert_to_png_flag:
            img = convert_to_png(img_path).convert('RGBA')
        else:
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

        output_filename = os.path.splitext(filename)[0] + '.png'
        output_path = os.path.join(output_folder, output_filename)
        new_image.save(output_path, 'PNG')

print("Done")
