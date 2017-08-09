---
header:
  image: test2.jpg
layout: archive
title: "People"
permalink: /people/
author_profile: true
---


{% include base_path %}

{% for post in site.people %}
  {% include archive-single.html %}
{% endfor %}
