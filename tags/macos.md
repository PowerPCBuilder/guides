---
layout: default
title: "Tag: MacOS"
tag: MacOS
permalink: /tags/macos/
---
<h1>Pages tagged with "MacOS"</h1>
<ul>
{% for post in site.pages %}
  {% if post.tags contains "MacOS" %}
  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
