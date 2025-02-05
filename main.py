import threading
import time
import streamlit as st
#from  afsun_ai_runner import run_llama_answer


st.set_page_config(page_title="Afsun Chat-Bot")

st.title("Afsun Chat Bot")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"])

user_input = st.chat_input("What is up?")

if user_input:
    print(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if user_input.lower() == "what is your name":
        with open("creator.txt", "r") as file:
            value = file.read()
            value_splite_value = value.split()
            value_splite_value = int(len(value_splite_value))
            print(value_splite_value)
            if value_splite_value >= 100:
                time_delay = 0.0001

    else:
        #value = run_llama_answer(user_input)
        value = " I do not understant your **promt**"
        time_delay = 0.001



    response = value
    print(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    time.sleep(0.5)
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        displayed_text = ""
        for char in response:
            displayed_text += char
            response_placeholder.markdown(displayed_text)
            time.sleep(time_delay)
