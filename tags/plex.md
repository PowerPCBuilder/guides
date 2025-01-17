---
layout: default
title: "Tag: Plex"
tag: Plex
permalink: /tags/plex/
---
<h1>Pages tagged with "Plex"</h1>
<ul>
{% for post in site.pages %}
  {% if post.tags contains "Plex" %}
  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
