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
// JavaScript code for dynamic link generation
// This script will read the structure of the photo folders and generate links to pages dynamically
document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.getElementById('gallery');
    fetch('photos/index.json')
        .then(response => response.json())
        .then(folders => {
            folders.forEach(folder => {
                const link = document.createElement('a');
                link.href = `/photo_gallery_template?folder=${folder}`;
                link.textContent = folder;
                gallery.appendChild(link);
            });
        });
});
</script>

