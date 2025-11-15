# 📚 Docstóteles - IA SEMPRE ATUALIZADA (Web Scraping + RAG)

Transforme qualquer documentação em um **assistente de IA atualizado**!  
Crie um chat que responde sobre qualquer tecnologia, usando scraping inteligente e RAG, com ferramentas **100% gratuitas**.

Com o projeto Docstóteles, você vai aprender a criar um assistente de IA capaz de responder perguntas sobre qualquer tecnologia diretamente a partir da documentação oficial — e o melhor: sempre com informações atualizadas.


---

## ✨ O que é o Docstóteles?

O Docstóteles é uma aplicação que combina **Web Scraping inteligente (Fire Crawl)** com **RAG (LangChain + Groq)** para criar um assistente de IA que conhece qualquer documentação da web.

Funciona assim: você cola o link de uma documentação (como Django, React, Vue, Streamlit, etc.), o app coleta todo o conteúdo, organiza e transforma em **conhecimento estruturado**, e cria um chat para perguntas e respostas em tempo real — respondendo como se fosse um expert no assunto.

Este projeto vai além da teoria e mostra na prática como combinar:

- **Web Scraping** para coletar informações diretamente da fonte.  
- **LLMs (Large Language Models)** via OpenAI para responder perguntas com linguagem natural.  
- **Embeddings e busca vetorial (FAISS + Hugging Face)** para indexar e consultar conteúdos grandes.  
- **RAG (Retrieval-Augmented Generation)** para gerar respostas precisas usando o conteúdo real da documentação.  

Ideal para quem quer criar **assistentes de conhecimento**, **bots de suporte técnico** ou integrar IA em processos de aprendizado e suporte interno.

---

## 🚀 Tecnologias Usadas

- **Streamlit** — Interface gráfica interativa  
- **Fire Crawl** — Web Scraping inteligente  
- **OpenAI API** — LLM para geração de respostas  
- **LangChain** — RAG e embeddings  
- **Hugging Face** — Embeddings de alta qualidade  
- **FAISS** — Armazenamento e busca vetorial  

---

## 📝 Como usar

### 1️⃣ Scraping

1. Vá para o modo **"Scraping"** na barra lateral.  
2. Cole a URL da documentação (ex: [https://docs.streamlit.io](https://docs.streamlit.io)).  
3. Dê um nome para a **coleção**.  
4. Clique em **"Iniciar Scraping"**.  
5. Aguarde o download e indexação dos arquivos.  

> O scraping baixa até 10 páginas por padrão — você pode ajustar este limite no código se quiser mais.

### 2️⃣ Chat

1. Selecione o modo **"Chat"** na barra lateral.  
2. Escolha a coleção que você criou.  
3. Pergunte qualquer coisa sobre a documentação — o Docstóteles vai responder usando o conteúdo real da web!

---

## 🌐 Sugestões de sites para testar

- [Streamlit Docs](https://docs.streamlit.io)  
- [LangChain Docs](https://python.langchain.com/docs)  
- [Python Tutorial](https://docs.python.org/3/tutorial)  

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

## 💡 Dicas e Possíveis xpansões

- O projeto pode ser expandido para suportar **uploads de documentos, PDFs**, ou até integração com outros modelos de IA.  
- **Fire Crawl** é totalmente gratuito e não pede cartão de crédito.  
- Ideal para criar **assistentes de conhecimento**, **bots de suporte técnico** ou **ferramentas de aprendizado interno**.  
- Perfeito para aprender na prática como juntar **scraping, LLMs, RAG, embeddings e busca vetorial** em um projeto real.

