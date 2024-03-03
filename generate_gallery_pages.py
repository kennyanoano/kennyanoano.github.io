
import json
import os

# _data/photos_index.json����t�H���_���̃��X�g��ǂݍ���
with open("_data/photos_index.json", "r") as json_file:
    folders = json.load(json_file)

# �e�t�H���_�ɑΉ�����Markdown�t�@�C���𐶐�
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
    # �t�H���_���Ƃ̉摜���X�g���܂ރf�[�^�t�@�C���̃p�X
    data_file_path = f"_data/photos_{folder}.json"
    # �t�H���_���̉摜�t�@�C�����̃��X�g�𐶐�
    images = os.listdir(f"photos/{folder}")
    # JSON�`���ŕۑ�
    with open(data_file_path, "w") as data_file:
        json.dump(images, data_file, indent=4)
    
    # Markdown�t�@�C���𐶐�
    with open(file_path, "w") as md_file:
        md_file.write(content)
