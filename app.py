import streamlit as st
import requests
import json
import os 

st.title("Loyalty Cloud Services Guru")

# Sidebar or another section for instructions or summary information
st.sidebar.title("Sample questions to get started")
st.sidebar.markdown("""
- What is LCS? 
- How do I replace a loyalty card using LCS? 
- Does LCS talk to any SAP systems? 
- How is a loyalty customer created online?
""")


# Initialize chat history and session ID if not already in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if 'sessionId' not in st.session_state:
    st.session_state['sessionId'] = "None"

# Using columns to layout the chat and potential additional info or actions
col1, col2 = st.columns([3, 1])  # Adjust the ratio as needed

with col1:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What would you like to know?"):
        question = prompt
        st.chat_message("user").markdown(question)

        payload = {"question": prompt, "sessionid": st.session_state['sessionId']}
        function_url = os.environ.get('FUNCTION_URL')

        with st.spinner('LCS Guru is thinking...'):
            response = requests.post(function_url, json=payload)

        if response.status_code == 200:
            result = response.json()
            answer = result['answer']
            st.session_state['sessionId'] = result.get('sessionId', 'None')

            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("assistant"):
                st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            st.error('Failed to get a response from the chat service.')


