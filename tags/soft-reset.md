---
layout: default
title: "Tag: Soft reset"
tag: Soft reset
permalink: /tags/soft-reset/
---
<h1>Pages tagged with "Soft reset"</h1>
<ul>
{% for post in site.pages %}
  {% if post.tags contains "Soft reset" %}
  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
