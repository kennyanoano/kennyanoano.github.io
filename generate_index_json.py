import os
import json

def generate_index_json(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            # .jpg と .jpeg の両方を対象にする
            jpg_files = [f for f in os.listdir(dir_path) if f.endswith('.jpg') or f.endswith('.jpeg')]
            index_json_path = os.path.join(dir_path, 'index.json')
            with open(index_json_path, 'w') as json_file:
                json.dump(jpg_files, json_file, indent=4)

generate_index_json('photos')
