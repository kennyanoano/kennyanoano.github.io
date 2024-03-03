
import json
import os

# _data/photos_index.jsonからフォルダ名のリストを読み込む
with open("_data/photos_index.json", "r") as json_file:
    folders = json.load(json_file)

# 各フォルダに対応するMarkdownファイルを生成
for folder in folders:
    file_path = f"photos/{folder}/{folder}.md"
    content = f"""---
layout: page
title: "{folder} Gallery"
description: "Images from {folder}"
---

# {folder} Gallery

{{% for image in site.data.photos_{folder} %}}
![{{image}}]({{ '{{' }} site.baseurl {{ '}}' }}/photos/{folder}/{{image}})
{{% endfor %}}
"""
    # フォルダごとの画像リストを含むデータファイルのパス
    data_file_path = f"_data/photos_{folder}.json"
    # フォルダ内の画像ファイル名のリストを生成
    images = os.listdir(f"photos/{folder}")
    # JSON形式で保存
    with open(data_file_path, "w") as data_file:
        json.dump(images, data_file, indent=4)
    
    # Markdownファイルを生成
    with open(file_path, "w") as md_file:
        md_file.write(content)
