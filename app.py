import streamlit as st

from services.bedrock import bedrock, MODEL_ID, SYSTEM_PROMPT
from services.chat_storage import save_chat, new_chat_id
from ui.chat import show_messages, hide_chat_icons
from ui.sidebar import show_sidebar

st.set_page_config(
    page_title="AWS Cloud Practitioner Assistant",
    page_icon="img/icon.svg"
)

hide_chat_icons()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_id" not in st.session_state:
    st.session_state.chat_id = new_chat_id()

show_sidebar()

st.title("AWS Cloud Practitioner Assistant")
st.caption("Asistente especializado en AWS Cloud Practitioner")

show_messages()

user_input = st.chat_input("Escribe tu pregunta...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar=None):
        st.markdown(user_input)

    try:
        response = bedrock.converse(
            modelId=MODEL_ID,
            system=[
                {"text": SYSTEM_PROMPT}
            ],
            messages=[
                {
                    "role": message["role"],
                    "content": [{"text": message["content"]}]
                }
                for message in st.session_state.messages
            ]
        )
        
        answer = response["output"]["message"]["content"][0]["text"]

    except Exception as error:
        answer = f"No fue posible obtener una respuesta: {error}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant", avatar=None):
        st.markdown(answer)

    save_chat(
        st.session_state.messages,
        st.session_state.chat_id
    )