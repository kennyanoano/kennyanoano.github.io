import io  # この行を追加
from PIL import Image
import os
def compress_image(image_path, max_width, max_size_kb):
    with Image.open(image_path) as img:
        # 画像のサイズを調整
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # 画像の品質を調整してファイルサイズを減らす
        quality = 95  # 初期品質
        while True:
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG', quality=quality)
            size_kb = img_bytes.tell() / 1024
            if size_kb <= max_size_kb or quality <= 10:
                break
            quality -= 5  # 品質を下げて再試行
        
        # 圧縮した画像を元のファイルに上書き保存
        with open(image_path, 'wb') as f_out:
            f_out.write(img_bytes.getvalue())
def compress_images_in_folder(folder_path, max_width=1024, max_size_kb=100):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.jpg'):
                image_path = os.path.join(root, file)
                compress_image(image_path, max_width, max_size_kb)
                print(f"Compressed and saved: {image_path}")
# 'test' フォルダ内の画像を圧縮
compress_images_in_folder('_photos_Articles')