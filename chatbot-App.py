import openai
import streamlit as st

# Set the OpenAI API key
openai.api_key = "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"

# Define the Streamlit app
# Define the title
st.title("GPT-3 Chatbot")

# Define a text input for the user to enter their message
user_input = st.text_input("Enter your message:")

# Use OpenAI's GPT-3 to generate a response to the user's message
if user_input:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=50
    )

    # Display the generated response to the user
    bot_response = response.choices[0].text
    st.text_area("Bot's response:", value=bot_response, height=100)
