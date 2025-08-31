---
layout: default
title: VitalidadeAgora
description: Informações e dicas de saúde e bem-estar
---

<section class="hero">
  <h2>Viva com mais saúde, energia e equilíbrio.</h2>
  <p>Descubra dicas práticas e confiáveis para melhorar sua qualidade de vida.</p>
</section>

<section class="articles">
  <div class="card">
    <h3>Alimentação Saudável</h3>
    <p>Como montar uma dieta equilibrada para fortalecer a imunidade.</p>
  </div>
  <div class="card">
    <h3>Exercícios em Casa</h3>
    <p>Dicas de treinos simples para aumentar energia e bem-estar.</p>
  </div>
  <div class="card">
    <h3>Saúde Mental</h3>
    <p>Práticas diárias para reduzir o estresse e melhorar o foco.</p>
  </div>
</section>

## Últimos Artigos
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>({{ post.date | date: "%d/%m/%Y" }})</small>
    </li>
  {% endfor %}
</ul>
