import streamlit as st
import retrieval_augmented_generation as rag

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return [question.strip() for question in questions]

def main():
    st.set_page_config(page_title="MaziwaMax", page_icon=":cow:")

    # CSS styling for messages
    st.markdown("""
        <style>
        .header{
            text-align: center;
        }
        .user-message {
            background-color: #999999;
            border-radius: 5px;
            padding: 10px;
            margin-top: 10px;
            color: black;
            float: right;
            display: inline-block;
        }
        .bot-message {
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            text-align: left;
            display: inline-block;
        }
        .input-box {
            position: fixed;
            bottom: 0;
            width: 70%;
            padding: 10px;
            display: flex;
        }
        .input-box input {
            width: 50%;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h1 class='header'>MaziwaMax</h1>", unsafe_allow_html=True)

    # Initialize the conversation history if not already done
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Display the conversation history
    for turn in st.session_state.conversation_history:
        if "user" in turn:
            st.markdown(f'<div class="stMarkdown user-message"><b>Farmer</b> <br> {turn["user"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="stMarkdown bot-message"><b>Maziwa Max</b> <br> {turn["MaziwaMax"]}</div>', unsafe_allow_html=True)

    # Placeholder for the spinner
    spinner_placeholder = st.empty()

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

if __name__ == '__main__':
    main()
