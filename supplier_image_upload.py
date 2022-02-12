#!/usr/bin/env python3

import requests
import os

def main():
    url = "http://localhost/upload/"
    path = "supplier-data/images/"

    # Iterates over files in directory and uploads images to URL
    for file in os.listdir(path):
        if file.endswith(".jpeg"):
            im = open(path + file, 'rb')
            r = requests.post(url, files={'file': im})

if __name__ == '__main__':
    main()