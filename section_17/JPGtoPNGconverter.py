# create a jpg to png converter that takes an input folder and output folder
# the output folder does not have to exist
# read all jpg files in the input folder, create output folder if needed and save converted image files there
# script should be called like this:
# python3 JPGtoPNGconverter.py Pokedex/ new/

from sys import argv
from glob import glob
from PIL import Image
from os import path, mkdir


def create_folder(folder):
    if not path.isdir(folder):
        mkdir(folder)
        print(f"Created folder {folder}")
    else:
        print(f"Good, folder {folder} already exists!")


def convert_image(filename, out_folder):
    print(f'importing file {filename}')
    img = Image.open(filename)
    # create new file path (not the nicest way likely ;) )
    # course solution uses path.splitext but also uses os.listdir. I'm accepting my solution
    base_name = filename.split("\\")[-1].replace(".jpg", ".png")
    full_path = f"{out_folder}{base_name}"
    print(f'exporting file {full_path}')
    img.save(full_path, "png")


input_folder = argv[1]
output_folder = argv[2]

input_jpg_files = glob(f"{input_folder}*.jpg")
# course solution uses os.listdir():
#   - no wildcard or extension
#   - does provide the basename of the file

if len(input_jpg_files) > 1:
    # since we have files to process, lets see if the destination folder exists or create it
    create_folder(output_folder)
    for file in input_jpg_files:
        convert_image(file, output_folder)
else:
    print(
        f"input folder {input_folder} does not exist or does not contain any *.jpg files"
    )
