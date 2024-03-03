---
layout: page
title: "3Dprint"
description: "3Dプリンター遊び"
order: 5
---

3Dプリンターパーツを販売するウェブショップ
[https://kenny1307.booth.pm/](https://kenny1307.booth.pm/)




### 3Dprinting_articles

{% for article in site.threeD_Articles %}
- [{{ article.title }}]({{ article.url }}) - {{ article.description }}
{% endfor %}


{% for article in site.threeD_Articles %}
  <h2>{{ article.title }}</h2>
  <p>{{ article.url }}</p>
  <p>{{ article.description }}</p>
{% endfor %}


