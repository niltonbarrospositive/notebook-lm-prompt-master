#!/usr/bin/env python3
"""
Scraper para extrair prompts do site https://prompts.aidrop.news/
Parseia o HTML da página e extrai todos os prompts com título, modelo, conteúdo e tags.
"""

import json
import re
from bs4 import BeautifulSoup

# HTML da página (copiado diretamente do source)
# Como é um SPA React, vamos parsear o HTML renderizado

html_content = """
<!-- O HTML será lido do stdin ou de um arquivo -->
"""

def extract_prompts_from_html(html_str):
    """Extrai prompts do HTML renderizado da página AiDrop."""
    soup = BeautifulSoup(html_str, 'html.parser')

    prompts = []

    # Encontrar todos os cards de prompt
    cards = soup.find_all('div', class_=lambda c: c and 'rounded-lg' in c and 'hover-lift' in c)

    for card in cards:
        prompt = {}

        # Título
        h3 = card.find('h3')
        if h3:
            prompt['title'] = h3.get_text(strip=True)

        # Modelo
        model_p = card.find('p', class_=lambda c: c and 'text-muted-foreground' in c and 'text-xs' in c)
        if model_p:
            prompt['model'] = model_p.get_text(strip=True)

        # Conteúdo do prompt
        content_div = card.find('div', class_=lambda c: c and 'whitespace-pre-line' in c)
        if content_div:
            prompt['content'] = content_div.get_text(strip=True)

        # Tags
        tags = []
        tag_elements = card.find_all('div', class_=lambda c: c and 'rounded-full' in c and 'bg-secondary' in c)
        for tag_el in tag_elements:
            tag_text = tag_el.get_text(strip=True)
            if tag_text:
                tags.append(tag_text)
        prompt['tags'] = tags

        if prompt.get('title'):
            prompts.append(prompt)

    return prompts


def main():
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            html = f.read()
    else:
        html = sys.stdin.read()

    prompts = extract_prompts_from_html(html)

    print(f"Total de prompts extraídos: {len(prompts)}")
    print(json.dumps(prompts, ensure_ascii=False, indent=2))

    # Salvar em arquivo JSON
    with open('prompts_data.json', 'w', encoding='utf-8') as f:
        json.dump(prompts, ensure_ascii=False, indent=2, fp=f)

    print(f"\nDados salvos em prompts_data.json")


if __name__ == '__main__':
    main()
