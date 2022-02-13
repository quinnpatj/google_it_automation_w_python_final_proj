#!/usr/bin/env python3

import os
import requests

def main():
    path = 'supplier-data/descriptions/'
    files = os.listdir(path)
    ip = 'localhost'
    url = 'http://{}/fruits/'.format(ip)

    # Iterates over files in directory and uploads data to URL
    for file in files:
        if file.endswith("txt"):
            dict = {}
            fruit_name = file.split('.')[0]
            f = open(path + file)
            val = f.readlines()
            dict['name'] = val[0]
            weight = val[1].split(" ")
            dict['weight'] = int(weight[0])
            dict['description'] = val[2]
            dict['image_name'] = fruit_name + ".jpeg"

            response = requests.post(url, json=dict)

if __name__ == '__main__':
    main()