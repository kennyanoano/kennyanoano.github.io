---
layout: page
title: "AIごっこ"
description: "AI楽しいねというだけのページ"
order: 2
---

# AIに関するメモ

ここにAIに関するメモや情報を記述します。
## AI関連記事

{% for article in site.AI_Articles %}
- [{{ article.title }}]({{ article.url }}) - {{ article.description }}
{% endfor %}
