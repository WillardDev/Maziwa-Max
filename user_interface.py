import streamlit as st
from htmlTemplates import css
import retrieval_augmented_generation as rag

def main():
    st.set_page_config(page_title="MaziwaMax", page_icon=":cow:")
    st.write(css, unsafe_allow_html=True)

    st.header(":cow: MaziwaMax")

    # Initialize an empty list to hold the conversation history
    conversation_history = []

    user_query = st.text_input("Message Maziwa... ")
    if user_query:
        # Append the user query to the conversation history
        conversation_history.append({"user": user_query})

        result = rag.LLM_Run(user_query)

        # Append the model response to the conversation history
        conversation_history.append({"MaziwaMax": result})

        # Display the conversation history
        for turn in conversation_history:
            if "user" in turn:
                st.write(f"User: {turn['user']}")
            else:
                st.write(f"MaziwaMax: {turn['MaziwaMax']}")

if __name__ == '__main__':
    main()
