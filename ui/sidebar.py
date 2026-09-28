import streamlit as st

from services.chat_storage import (
    get_saved_chats,
    load_chat,
    delete_chat,
    get_chat_title,
    new_chat_id,
)

def sidebar_styles():
    st.markdown("""
    <style>
    /* Ícono - colapsar/expandir sidebar: siempre visible */
    [data-testid="stSidebarCollapseButton"],
    [data-testid="stSidebarCollapseButton"] * {
        opacity: 1 !important;
        visibility: visible !important;
        pointer-events: auto !important;
    }

    /* Reducir espacio entre el ícono y el título "Chats" */
    [data-testid="stSidebarHeader"] {
        height: auto !important;
        min-height: 0 !important;
        margin-bottom: 0 !important;
        padding-top: 0.5rem !important;
    }

    section[data-testid="stSidebar"] h2 {
        padding-top: 0 !important;
        padding-bottom: 0.25rem !important;
    }

    /* Espaciado vertical */
    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] > div > [data-testid="stVerticalBlock"] {
        gap: 0.35rem !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stLayoutWrapper"] {
        margin: 0 !important;
        padding: 0 !important;
        min-height: 0 !important;
    }

    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        margin-bottom: 0 !important;
    }
    
    section[data-testid="stSidebar"] .st-emotion-cache-1bwu7md {
        margin-bottom: 0 !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] > div > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"]:first-child {
        display: none !important;
    }

    section[data-testid="stSidebar"] hr {
        margin: 0 !important;
    }

    /* Texto justificado a la izquierda */
    section[data-testid="stSidebar"] button[data-testid^="stBaseButton"] > div {
        justify-content: flex-start !important;
    }
    section[data-testid="stSidebar"] button[data-testid^="stBaseButton"] p {
        text-align: left !important;
    }

    /* BOTÓN "+ Nuevo chat": sin borde/fondo por defecto */
    div[class*="st-key-new_chat_button"] button {
        background-color: transparent !important;
        border-color: transparent !important;
        transition: background-color 0.15s ease, border-color 0.15s ease;
    }
    
    div[class*="st-key-new_chat_button"] button:hover {
        background-color: rgba(250, 250, 250, 0.12) !important;
        border-color: transparent !important;
    }

    /* Chat: título + eliminar en un solo contenedor */
    div[class*="st-key-chat_row_"] {
        position: relative;
        border-radius: 0.5rem;
        background-color: transparent;
        transition: background-color 0.15s ease;
        margin: 0 !important;
        overflow: hidden;
    }
    div[class*="st-key-chat_row_"]:hover {
        background-color: rgba(250, 250, 250, 0.12);
    }

    div[class*="st-key-chat_row_"] [data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
        align-items: center !important;
        gap: 0 !important;
    }

    div[class*="st-key-chat_row_"] button {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    div[class*="st-key-chat_row_"] [data-testid="stColumn"]:first-child {
        width: 100% !important;
        flex: 1 1 auto !important;
    }
    div[class*="st-key-chat_row_"] [data-testid="stColumn"]:first-child button[data-testid^="stBaseButton"] > div {
        padding-right: 1.75rem !important;
    }
    div[class*="st-key-chat_row_"] [data-testid="stColumn"]:first-child button p {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    div[class*="st-key-chat_row_"] [data-testid="stColumn"]:last-child {
        position: absolute !important;
        right: 0.35rem;
        top: 50%;
        transform: translateY(-50%);
        width: auto !important;
        min-width: 0 !important;
        flex: 0 0 auto !important;
    }

    div[class*="st-key-chat_row_"] [data-testid="stColumn"]:last-child button {
        opacity: 0;
        transition: opacity 0.15s ease;
        padding: 0.25rem 0.4rem !important;
    }
    div[class*="st-key-chat_row_"]:hover [data-testid="stColumn"]:last-child button {
        opacity: 1;
    }
    </style>
    """, unsafe_allow_html=True)

def show_sidebar():
    with st.sidebar:
        sidebar_styles()

        st.header("Chats")

        if st.button("+ Nuevo", use_container_width=True, key="new_chat_button"):
            st.session_state.messages = []
            st.session_state.chat_id = new_chat_id()
            st.rerun()

        st.divider()

        chats = get_saved_chats()

        if not chats:
            st.caption("Aún no hay chats guardados.")

        for chat_id in chats:
            title = get_chat_title(chat_id) or "Nueva conversación"
            is_active = chat_id == st.session_state.get("chat_id")

            with st.container(key=f"chat_row_{chat_id}"):
                col_select, col_delete = st.columns([5, 1])

                with col_select:
                    label = f"**{title}**" if is_active else title
                    if st.button(
                        label,
                        key=f"select_{chat_id}",
                        use_container_width=True,
                    ):
                        st.session_state.chat_id = chat_id
                        st.session_state.messages = load_chat(chat_id)
                        st.rerun()

                with col_delete:
                    if st.button("✕", key=f"delete_{chat_id}"):
                        delete_chat(chat_id)
                        if is_active:
                            st.session_state.messages = []
                            st.session_state.chat_id = new_chat_id()
                        st.rerun()