# 📚 Docstóteles - IA SEMPRE ATUALIZADA (Web Scraping + RAG)

Transforme qualquer documentação em um assistente de IA atualizado!  
Crie um chat que responde sobre qualquer tecnologia, usando scraping inteligente e RAG, com ferramentas 100% gratuitas.

## ✨ O que é o Docstóteles?

O Docstóteles é uma aplicação que junta Web Scraping inteligente (Fire Crawl) com RAG (LangChain + Groq) para criar um assistente de IA que conhece qualquer documentação da web.  
Você cola o link de uma documentação (Django, React, Vue, etc), o app baixa tudo, indexa e cria um chat para perguntas e respostas super atualizadas.

## 🚀 Tecnologias Usadas

- [Streamlit](https://streamlit.io/) — Interface gráfica
- [Fire Crawl](https://firecrawl.dev/) — Web Scraping inteligente
- [Open API](https://openai.com/pt-BR/api/) — LLM
- [LangChain](https://python.langchain.com/) — RAG e embeddings
- [Hugging Face](https://huggingface.co/) — Embeddings
- [FAISS](https://github.com/facebookresearch/faiss) — Vector store

## 🛠️ Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/asimov-academy/video-docstoteles-material.git
   cd video-docstoteles-material
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   > No Windows, use: `.venv\Scripts\activate`

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as chaves de API:**
   - Crie um arquivo `.env` na raiz do projeto e preencha com suas chaves:
     ```
     GROQ_API_KEY=sua_chave_groq
     FIRECRAWL_API_KEY=sua_chave_firecrawl
     FIRECRAWL_API_URL=url_firecrawl
     ```

5. **Crie as pastas necessárias:**
   ```bash
   mkdir -p data/collections
   ```

## 🏃‍♂️ Como rodar

```bash
streamlit run docstoteles/app.py
```

Acesse o app no navegador pelo link que aparecer no terminal.

---

## 📝 Como usar

### 1. Scraping

- Vá para o modo "Scraping" na barra lateral.
- Cole a URL da documentação (ex: https://docs.streamlit.io).
- Dê um nome para a coleção.
- Clique em "Iniciar Scraping".
- Aguarde o download dos arquivos.

### 2. Chat

- Selecione o modo "Chat" na barra lateral.
- Escolha a coleção que você criou.
- Pergunte qualquer coisa sobre a documentação!

---

## 🌐 Sugestões de sites para testar

- https://docs.streamlit.io
- https://python.langchain.com/docs
- https://docs.python.org/3/tutorial

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
requirements.txt
README.md
.env (você deve criar)
```

---

## 💡 Dicas

- O projeto é base: você pode expandir, conectar outros modelos, adicionar uploads, etc.
- Fire Crawl e Groq são gratuitos (Groq não pede cartão).
- O scraping baixa até 10 páginas por padrão (ajuste no código se quiser mais).

---

## 🧑‍💻 Contribua!

Sugestões, issues e PRs são bem-vindos!

---

# 🚦 Passo a Passo Docstóteles

## 1️⃣ Setup Básico

### 1.1 Instale as dependências

```bash
pip install streamlit python-dotenv openai firecrawl langchain langchain-community langchain-openai faiss-cpu sentence-transformers
```

### 1.2 Crie o arquivo `.env`

```env
OPEN_API_KEY=sua_chave_openai
FIRECRAWL_API_KEY=sua_chave_firecrawl
FIRECRAWL_API_URL=url_firecrawl
```

