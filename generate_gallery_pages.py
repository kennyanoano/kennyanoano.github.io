import json
import os

with open("_data/photos_index.json", "r") as json_file:
    folders = json.load(json_file)

for folder in folders:
    file_path = f"photos/{folder}/{folder}.md"
    images = os.listdir(f"photos/{folder}")
    images_md = "\n".join([f"![{image}]({{ '{{' }} site.baseurl {{ '}}' }}/photos/{folder}/{image})" for image in images])
    content = f"""---
layout: page
title: "{folder} Gallery"
description: "Images from {folder}"
---

# {folder} Gallery

{images_md}
"""
    
    with open(file_path, "w") as md_file:
        md_file.write(content)