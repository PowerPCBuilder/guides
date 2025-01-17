---
layout: default
title: "Tag: Backups"
tag: Backups
permalink: /tags/backups/
---
<h1>Pages tagged with "Backups"</h1>
<ul>
{% for post in site.pages %}
  {% if post.tags contains "Backups" %}
  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
