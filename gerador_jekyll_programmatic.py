import os
import csv
import random
from datetime import date
from bs4 import BeautifulSoup
import requests

# Pasta onde os posts vão ser gerados
POSTS_DIR = "_posts"
os.makedirs(POSTS_DIR, exist_ok=True)

# Data de hoje (YYYY-MM-DD)
hoje = date.today().isoformat()

# Template Markdown Jekyll
TEMPLATE_MD = """---
layout: post
title: "{title}"
description: "{description}"
keywords: "{keywords}"
date: {date}
---

# {title}

{intro}

## Principais {type_}:
{benefits}

### Observações
Sempre consulte um profissional de saúde antes de mudanças significativas.

<!-- Anúncio -->
<div class="ad-placeholder">[Anúncio aqui]</div>
"""

# Função para buscar resumo da Wikipedia
def wiki_summary(keyword):
    try:
        url = f"https://pt.wikipedia.org/wiki/{keyword.replace(' ', '_')}"
        r = requests.get(url)
        if r.status_code != 200:
            return f"Informações sobre {keyword} não encontradas."
        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = soup.select("p")
        for p in paragraphs:
            text = p.get_text().strip()
            if len(text) > 100:
                return text
        return f"Informações sobre {keyword} não encontradas."
    except:
        return f"Informações sobre {keyword} não encontradas."

# Função para gerar variações de keywords
def generate_variations(keyword):
    variations = [keyword]
    words = keyword.split()
    if len(words) > 1:
        variations.append(" ".join(reversed(words)))
        variations.append("-".join(words))
    return list(set(variations))

# Função para gerar benefícios automáticos
def generate_benefits(keyword, type_):
    base = [
        f"Melhora a saúde geral com o uso de {keyword}.",
        f"Contribui para mais energia e bem-estar diário.",
        f"Auxilia na prevenção de doenças relacionadas com {type_}.",
        f"Pode ser incluído em dietas ou regimes de saúde.",
        f"Promove um estilo de vida mais saudável quando combinado com hábitos adequados."
    ]
    random.shuffle(base)
    return "\n".join([f"- {b}" for b in base[:4]])

# Ler CSV
with open("keywords.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        keyword = row["keyword"].strip()
        type_ = row["type"].strip()

        # Variações de SEO
        variations = generate_variations(keyword)
        keywords_meta = ", ".join(variations)

        # Buscar resumo Wikipedia (primeira variação)
        intro = wiki_summary(variations[0])

        # Benefícios automáticos
        benefits = generate_benefits(keyword, type_)

        # Criar posts para todas as variações
        for var in variations:
            title = f"{type_.capitalize()} do {var.capitalize()}"
            filename = f"{hoje}-{var.lower().replace(' ', '-')}-{type_.lower()}.md"
            filepath = os.path.join(POSTS_DIR, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(TEMPLATE_MD.format(
                    title=title,
                    description=f"Descubra os principais {type_} do {var} para a saúde.",
                    keywords=keywords_meta,
                    date=hoje,
                    intro=intro,
                    type_=type_,
                    benefits=benefits
                ))

            print(f"Criado: {filepath}")

print("\n✅ Todos os posts programmatic SEO foram gerados em", POSTS_DIR)
