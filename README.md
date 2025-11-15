# 📚 Docstóteles - IA SEMPRE ATUALIZADA (Web Scraping + RAG)

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.24-orange)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-red)](https://openai.com/pt-BR/api/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://python.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

Transforme qualquer documentação em um **assistente de IA atualizado**!  
Crie um chat que responde sobre qualquer tecnologia, usando scraping inteligente e RAG, com ferramentas **100% gratuitas**.

---

## 🎯 Sobre o Projeto

O Docstóteles combina **Web Scraping inteligente (Fire Crawl)** com **RAG (LangChain + Groq)** para criar um assistente de IA que conhece qualquer documentação da web.  

Funciona assim:

1. Cole o link de uma documentação (React, Django, Vue, Streamlit, etc.).  
2. O app coleta todo o conteúdo e transforma em **conhecimento estruturado**.  
3. Pergunte qualquer coisa no chat, e o Docstóteles responde usando o conteúdo real da web!  

Este projeto mostra na prática como combinar **scraping, LLMs, embeddings e busca vetorial**, ideal para criar **assistentes de conhecimento, bots de suporte técnico ou ferramentas de aprendizado interno**.

---

## 🚀 Tecnologias Usadas

- [Streamlit](https://streamlit.io/) — Interface gráfica interativa  
- [Fire Crawl](https://firecrawl.dev/) — Web Scraping inteligente  
- [OpenAI API](https://openai.com/pt-BR/api/) — LLM para geração de respostas  
- [LangChain](https://python.langchain.com/) — RAG e embeddings  
- [Hugging Face](https://huggingface.co/) — Embeddings de alta qualidade  
- [FAISS](https://github.com/facebookresearch/faiss) — Armazenamento e busca vetorial  

---

## 🖼️ Demonstração

![Exemplo de uso](https://media.giphy.com/media/your-gif-placeholder/giphy.gif)  
*GIF mostrando scraping e chat funcionando em tempo real*  

---

## 📝 Como Usar

### 1️⃣ Scraping

1. Vá para o modo **"Scraping"** na barra lateral.  
2. Cole a URL da documentação (ex: [https://docs.streamlit.io](https://docs.streamlit.io)).  
3. Dê um nome para a **coleção**.  
4. Clique em **"Iniciar Scraping"**.  
5. Aguarde o download e indexação dos arquivos.  

> O scraping baixa até 10 páginas por padrão — você pode ajustar este limite no código.

### 2️⃣ Chat

1. Selecione o modo **"Chat"** na barra lateral.  
2. Escolha a coleção que você criou.  
3. Pergunte qualquer coisa sobre a documentação — o Docstóteles responde usando o conteúdo real da web!  

---

## 🌐 Sites para Testar

- [Streamlit Docs](https://docs.streamlit.io)  
- [LangChain Docs](https://python.langchain.com/docs)  
- [Python Tutorial](https://docs.python.org/3/tutorial)  

---

## 📦 Estrutura do Projeto


---

## 📦 Estrutura do Projeto

```
docstoteles/
  app.py
  presentation/
    scraping.py
    chat.py
  service/
    scraping.py
    rag.py
data/
  collections/
README.md
.env
```

---

## 💡 Dicas

- O projeto pode expandir, conectar outros modelos, adicionar uploads, etc.
- Fire Crawl é gratuitos (não pede cartão).
- O scraping baixa até 10 páginas por padrão (ajuste no código se quiser mais).

