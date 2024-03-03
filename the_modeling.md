---
layout: page
title: "modelkits"
description: "character model kits"
order: 4
---

# プラモデル塗装履歴

いろいろ塗装して遊んだよというのを掲載するよてい
テスト中

<div id="gallery"></div>
<script>
// JavaScript code for dynamic gallery generation
// This script will read the structure of the photo folders and generate the gallery dynamically
document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.getElementById('gallery');
    fetch('photos/index.json')
        .then(response => response.json())
        .then(data => {
            data.forEach(folder => {
                const folderDiv = document.createElement('div');
                folderDiv.className = 'folder';
                fetch(`photos/${folder}/index.json`)
                    .then(response => response.json())
                    .then(images => {
                        images.forEach(image => {
                            const img = document.createElement('img');
                            img.src = `photos/${folder}/${image}`;
                            folderDiv.appendChild(img);
                        });
                        gallery.appendChild(folderDiv);
                    });
            });
        });
});
</script>
