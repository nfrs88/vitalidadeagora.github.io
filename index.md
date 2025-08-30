---
layout: default
title: VitalidadeAgora
description: Informações e dicas de saúde e bem-estar
---

# Bem-vindo ao VitalidadeAgora

Aqui você encontra artigos sobre saúde, suplementos e hábitos de vida saudáveis.

## Últimos Artigos
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>({{ post.date | date: "%d/%m/%Y" }})</small>
    </li>
  {% endfor %}
</ul>
