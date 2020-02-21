import argparse
import os
import requests

IMAGE_HOST_ADDRESS = 'http://localhost:8000'
ALLOWED_FILE_TYPES = {'JPEG', 'JPG', 'PNG', 'BMP', 'GIF', 'NEF', }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    for filename in os.listdir(args.path):
        if os.path.isfile(os.path.join(args.path, filename)) and filename.split('.')[-1].upper() in ALLOWED_FILE_TYPES:
            with open(os.path.join(args.path, filename)) as f:
                requests.post(IMAGE_HOST_ADDRESS + '/images', files={
                    filename: f})

