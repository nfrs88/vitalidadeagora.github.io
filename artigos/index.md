---
layout: default
title: Artigos
---

<h2>Todos os Artigos</h2>
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a> - {{ post.date | date: "%d %b %Y" }}
    </li>
  {% endfor %}
</ul>
