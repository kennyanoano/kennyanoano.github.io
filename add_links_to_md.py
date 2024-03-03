
import os

def add_links_to_md(md_path, photos_path):
    folders = [name for name in os.listdir(photos_path) if os.path.isdir(os.path.join(photos_path, name))]
    links = "\n".join([f"- [{folder}](/photos/{folder}/)" for folder in folders])
    with open(md_path, 'a') as md_file:
        md_file.write("\n\n## ギャラリーフォルダ\n" + links)

md_path = "the_modeling.md"
photos_path = "photos"
add_links_to_md(md_path, photos_path)
