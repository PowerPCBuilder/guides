---
layout: default
title: "Tag: Synology"
tag: Synology
permalink: /tags/synology/
---
<h1>Pages tagged with "Synology"</h1>
<ul>
{% for post in site.pages %}
  {% if post.tags contains "Synology" %}
  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
