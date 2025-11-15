import os
import streamlit as st
from service.rag import RAGService

def show():
    st.header("💬 Chat com a Documentação")
    
    # Inicializa a lista de mensagens se não existir
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if not st.session_state.get("collection"):
        st.info("Nenhuma coleção carregada. Selecione primeiro uma coleção na barra lateral.")
        return
    
    st.success(f"📂 Coleção carregada: {st.session_state.collection}")
    
    # Inicializa o RAGService
    if "rag_service" not in st.session_state:
        st.session_state.rag_service = RAGService()
    
    # Carrega documentos se a coleção mudou
    if ("current_collection" not in st.session_state or 
        st.session_state.current_collection != st.session_state.collection):
        with st.spinner("Carregando documentos ..."):
            success = st.session_state.rag_service.load_collection(st.session_state.collection)
            if success:
                st.session_state.current_collection = st.session_state.collection
                st.success("Documentos carregados com sucesso!")
            else:
                st.error("Falha ao carregar os documentos.")
                return
    
    # Exibe histórico de mensagens
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
   
    # Input do usuário
    if prompt := st.chat_input("Faça uma pergunta sobre a documentação ..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Consultando IA / Pensando ..."):
                response = st.session_state.rag_service.ask_question(prompt)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.write(response)
                
    # Botão para limpar histórico
    if st.button("🗑️ Limpar Histórico de Chat"):
        st.session_state.messages = []
        st.rerun()