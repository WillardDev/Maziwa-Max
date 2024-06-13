import streamlit as st
import retrieval_augmented_generation as rag
import time

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return [question.strip() for question in questions]

def display_typing_effect(bot_message, delay=0.05):
    bot_message_container = st.empty()
    bot_message_display = ""
    for char in bot_message:
        bot_message_display += char
        bot_message_container.markdown(f'<div class="stMarkdown bot-message"><b>Maziwa Max</b> <br> {bot_message_display}</div>', unsafe_allow_html=True)
        time.sleep(delay)
    return bot_message_container

def main():
    st.set_page_config(page_title="MaziwaMax", page_icon=":cow:")

    # Load CSS from file
    with open('./style/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown("<h1 class='header'>MaziwaMax</h1>", unsafe_allow_html=True)

    # Initialize the conversation history if not already done
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Suggested questions for first-time users
    suggested_questions = load_questions('./data/questions.txt')

    if 'first_visit' not in st.session_state:
        st.session_state.first_visit = True

    if st.session_state.first_visit:
        st.markdown("<h3>Suggested Questions</h3>", unsafe_allow_html=True)
        for question in suggested_questions:
            if st.button(question):
                st.session_state.user_query = question
                st.session_state.first_visit = False

    # Display the conversation history
    for turn in st.session_state.conversation_history:
        if "user" in turn:
            st.markdown(f'<div class="stMarkdown user-message"><b>Farmer</b> <br> {turn["user"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="stMarkdown bot-message"><b>Maziwa Max</b> <br> {turn["MaziwaMax"]}</div>', unsafe_allow_html=True)

    # Placeholder for the spinner
    spinner_placeholder = st.empty()

    # Text input box at the bottom
    with st.form(key='user_query_form', clear_on_submit=True):
        user_query = st.text_input(" ", key='user_query', placeholder="Message Maziwa...")
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_query:
            # Append the user query to the conversation history
            st.session_state.conversation_history.append({"user": user_query})

            # Show the spinner just below the conversation output
            with spinner_placeholder.container():
                with st.spinner('Processing...'):
                    result = rag.LLM_Run(user_query)

            # Append the model response to the conversation history
            st.session_state.conversation_history.append({"MaziwaMax": result})

            # Clear the spinner
            spinner_placeholder.empty()

            # Refresh the display to show the latest user query
            st.experimental_rerun()

if __name__ == '__main__':
    main()
