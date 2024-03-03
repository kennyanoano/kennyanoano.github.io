import os

# 'photos'ディレクトリ内のフォルダをリストアップ
folders = [name for name in os.listdir("_photos_Articles") if os.path.isdir(os.path.join("_photos_Articles", name))]

for folder in folders:
    file_path = f"{folder}.md"  # Changed the file_path to generate markdown files in the parent directory
    images = os.listdir(f"_photos_Articles/{folder}")
    # 隠しファイルやサブディレクトリを除外
    images = [image for image in images if not image.startswith('.') and not os.path.isdir(os.path.join("_photos_Articles", folder, image))]
    images_md = "\n".join([f"![{image}]({{ site.baseurl }}/photos/{folder}/{image})" for image in images])
    content = f"""---
layout: subpage
title: "{folder} Gallery"
description: "Images from {folder}"
---

# {folder} Gallery

{images_md}
"""
    
    with open(file_path, "w") as md_file:
        md_file.write(content)