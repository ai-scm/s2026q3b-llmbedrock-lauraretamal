import streamlit as st

def hide_chat_icons():
    st.markdown("""
    <style>
    /* Ocultar iconos */
    [data-testid="stChatMessageAvatarUser"],
    [data-testid="stChatMessageAvatarAssistant"] {
        display: none;
    }

    /* Contenedor completo del mensaje del usuario */
    [data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageContent"][aria-label="Chat message from user"]
    ) {
        width: fit-content !important;
        max-width: 75% !important;
        margin-left: auto !important;
    }
    </style>
    """, unsafe_allow_html=True)

def show_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=None):
            st.markdown(message["content"])
