#!/usr/bin/env python3

from PIL import Image
import os

def main():
    # Iterates over image files in directory and converts to 60x400 JPEGs
    path = 'supplier-data/images/'

    for file in os.listdir(path):
        if 'tiff' in file:
            imPath = path + file
            outFile = file.split('.')[0] + ".jpeg"
            outPath = path + outFile
            im = Image.open(imPath)
            im.convert('RGB').resize((600,400)).save(outPath, "JPEG")

if __name__ == '__main__':
    main()