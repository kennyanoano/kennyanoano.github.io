---
layout: page
title: "modelkits"
description: "character model kits"
order: 4
---

# プラモデル塗装履歴

いろいろ塗装して遊んだよというのを掲載するよてい
テスト中

## ギャラリー

{% for article in site.photos_Articles %}
- [{{ article.title }}]({{ article.url }}) - {{ article.description }}
{% endfor %}


