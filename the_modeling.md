---
layout: page
title: "modelkits"
description: "character model kits"
order: 4
---

# プラモデル塗装履歴

いろいろ塗装して遊んだよというのを掲載するよてい
テスト中

{% assign photo_folders = site.static_files | where: "path", "photos/" | group_by: "folder" %}
<ul>
  {% for folder in photo_folders %}
    <li><a href="{{ folder.path }}">{{ folder.name }}</a></li>
  {% endfor %}
</ul>

