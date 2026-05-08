import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Mock ChatGPT Chat",
    layout="centered"
)

st.title("ChatGPT-Style")

def mock_response(user_message):
    message = user_message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hello! I am a local mock assistant."
    elif "how are you" in message:
        return "I am doing well. I generate replies locally using Python."
    elif "streamlit" in message:
        return "Streamlit is used here to build the chat interface with st.chat_message and st.chat_input."
    elif "time" in message:
        return f"The current local time is {datetime.now().strftime('%H:%M:%S')}."
    elif "help" in message:
        return "Try asking about Streamlit, time, or type any message to see a simulated reply."
    elif "api" in message or "llm" in message:
        return "This app does not use any external API or LLM. All replies come from a Python function."
    else:
        return f"You said: '{user_message}'. This is a simulated local response."

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I am a local mock assistant. How can I help you?"
        }
    ]

with st.sidebar:


    if st.button("Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared. Start a new conversation!"
            }
        ]
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    assistant_reply = mock_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    with st.chat_message("assistant"):
        st.write(assistant_reply)