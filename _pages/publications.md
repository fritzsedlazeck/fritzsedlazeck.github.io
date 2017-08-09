---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
header:
  image: test2.jpg
---


  You can also find my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=KNZTJ40AAAAJ&hl=en){: .btn .btn--success}


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
