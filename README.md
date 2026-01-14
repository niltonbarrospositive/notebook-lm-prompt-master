# **Guia de Estratégias de Prompt: NotebookLM (NotebookLM Prompt Master)**

Este projeto é uma **Single Page Application (SPA)** interativa desenvolvida para auxiliar pesquisadores, estudantes e criadores de conteúdo a utilizarem o **Google NotebookLM** com máxima eficiência.

A aplicação serve como um repositório central de prompts de "alta fidelidade" (baseados em relatórios de pesquisa avançada) e inclui uma ferramenta de Inteligência Artificial para gerar novos prompts personalizados.

## **✨ Funcionalidades Principais**

1. **Biblioteca de Prompts Curada:**  
   * Acervo de instruções complexas e testadas (em inglês) para garantir que o modelo do NotebookLM siga regras de *Roleplay*, *Restrição Negativa* e *Estrutura*.  
   * Categorias: Audio/Podcast (Deep Dive), Fichamento & Análise, Estudo Ativo.  
   * Busca em tempo real e filtros por categoria.  
2. **Gerador de Prompts com IA (Gemini API):**  
   * Integração direta com a API do **Google Gemini**.  
   * Transforma uma intenção simples em português (ex: "Quero entender a economia da china") em um prompt técnico e estruturado em inglês, pronto para uso.  
3. **Visualização de Dados:**  
   * Gráfico interativo (Chart.js) que exibe a distribuição tipológica dos prompts mais utilizados no mercado.  
4. **Experiência do Usuário (UX):**  
   * **One-Click Copy:** Sistema robusto de cópia para a área de transferência (compatível com iframes e ambientes seguros).  
   * **Design Responsivo:** Interface moderna construída com Tailwind CSS.  
   * **Feedback Visual:** Toasts de notificação e estados de carregamento.

## **🚀 Como Usar**

### **1\. Execução Simples**

Como o projeto é um arquivo HTML único (index.html), basta abri-lo em qualquer navegador moderno (Chrome, Edge, Firefox, Safari). Não é necessário instalar Node.js ou servidores complexos para visualização básica.

### **2\. Configuração da API do Gemini (Obrigatório para o Gerador)**

Para que o botão "Gerar Prompt Mágico ✨" funcione, você precisa inserir sua chave de API do Google Gemini.

1. Obtenha uma chave gratuita em [Google AI Studio](https://aistudio.google.com/).  
2. Abra o arquivo .html em um editor de texto (VS Code, Notepad++, etc).  
3. Localize a linha (aprox. linha 280\) dentro da tag \<script\>:  
   const apiKey \= ""; // Insira sua chave aqui

4. Cole sua chave entre as aspas:  
   const apiKey \= "AIzaSy...";

5. Salve e recarregue a página.

## **🛠️ Tecnologias Utilizadas**

* **HTML5 & CSS3:** Estrutura semântica.  
* **Tailwind CSS (via CDN):** Estilização utilitária e responsividade.  
* **JavaScript (Vanilla ES6+):** Lógica de filtragem, chamadas de API e manipulação do DOM.  
* **Chart.js (via CDN):** Renderização de gráficos.  
* **FontAwesome (via CDN):** Ícones vetoriais.  
* **Google Gemini API:** Modelo gemini-2.5-flash-preview para geração de texto.

## **🐛 Solução de Problemas Comuns**

**Erro: "Falha ao copiar automaticamente"**

* **Causa:** Navegadores modernos bloqueiam o acesso à área de transferência (navigator.clipboard) se a página não estiver sendo servida via HTTPS ou se estiver dentro de certos iframes.  
* **Solução Implementada:** O código inclui um fallback automático usando document.execCommand('copy'), garantindo que o botão de copiar funcione em 99% dos ambientes.

**Erro: O Gerador de IA não responde**

* Verifique se a variável apiKey foi preenchida corretamente no código.  
* Verifique o console do navegador (F12) para erros de rede (CORS ou Quota Exceeded).

## **📄 Licença**

Este projeto é de código aberto e livre para uso educacional, mas não comercial.