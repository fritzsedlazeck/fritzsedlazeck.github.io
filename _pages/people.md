---
header:
  image: test2.png
layout: archive
title: "People"
permalink: /people/
author_profile: true
---


{% include base_path %}

{% for post in site.people %}
  {% include archive-single.html %}
{% endfor %}
