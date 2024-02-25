---
layout: page
title: "AI"
description: "AI楽しいねというだけのページ"
order: 2
---

# AIたのしいね

楽しいねというだけだよ

## AI関連記事

{% for article in site.AI_Articles %}
- [{{ article.title }}]({{ article.url }}) - {{ article.description }}
{% endfor %}
