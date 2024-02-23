import streamlit as st
import requests
import json
import os 

st.title("Loyalty Cloud Services Guru")

# Use a hardcoded session ID or generate one as needed
sessionId = "None"
# sessionId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
print(sessionId)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize session id
if 'sessionId' not in st.session_state:
    st.session_state['sessionId'] = sessionId

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user input in chat message container
    question = prompt
    st.chat_message("user").markdown(question)

    # Prepare the payload for the HTTP request
    payload = json.dumps({"question":prompt,"sessionId": st.session_state['sessionId']})
    print(payload)
    
    # Specify the function URL
    function_url = "https://5wdtvz36sjv73xcl3uruea5j4i0oqblh.lambda-url.us-west-2.on.aws/"

    # Make a POST request to the function URL
    response = requests.post(function_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        print(result)

        answer = result['answer']
        sessionId = result.get('sessionId', 'None')  # Update this line based on the actual key returned for session ID

        st.session_state['sessionId'] = sessionId

        # Add user input to chat history
        st.session_state.messages.append({"role": "user", "content": question})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(answer)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})
    else:
        print(response.json())
        st.error('Failed to get a response from the chat service.')
