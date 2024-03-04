import os
import json

# folder_mapping.jsonからフォルダ名のマッピングを読み込む
with open("folder_mapping.json", "r", encoding="utf-8") as f:
    folder_mapping = json.load(f)

# マッピングの逆引き辞書を作成
reverse_folder_mapping = {value: key for key, value in folder_mapping.items()}

folders = [name for name in os.listdir("_photos_Articles") if os.path.isdir(os.path.join("_photos_Articles", name))]

for folder in folders:
    file_path = f"_photos_Articles/{folder}.md"
    images = os.listdir(f"_photos_Articles/{folder}")
    images = [image for image in images if not image.startswith('.') and not os.path.isdir(os.path.join("_photos_Articles", folder, image))]
    images_md = "\n".join([f"![{image.split('.')[0]}]({folder}/{image})" for image in images])
    
    # マッピング後の名前からオリジナルのフォルダ名を取得
    original_folder_name = reverse_folder_mapping.get(folder, folder)  # マッピングがない場合は元の名前を使用
    
    # オリジナルのフォルダ名をプリント（デバッグ用）
    print(f"Original folder name for '{folder}': {original_folder_name}")
    
    content = f"""---
layout: subpage
title: "{folder} Gallery"
description: "Images from {original_folder_name}"
---

# {folder} Gallery

{images_md}
"""
    
    with open(file_path, "w", encoding="utf-8") as md_file:
        md_file.write(content)