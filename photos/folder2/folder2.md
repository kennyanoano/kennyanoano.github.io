---
layout: page
title: "folder2 Gallery"
description: "Images from folder2"
---

# folder2 Gallery

{% for image in site.data.photos_folder2 %}
![{image}]({ '{' } site.baseurl { '}' }/photos/folder2/{image})
{% endfor %}
