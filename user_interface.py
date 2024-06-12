import streamlit as st
import retrieval_augmented_generation as rag

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
            width: 100%;
            padding: 10px;
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
            st.markdown(f'<div class="stMarkdown bot-message"><b>Maziwz Max</b> <br> {turn["MaziwaMax"]}</div>', unsafe_allow_html=True)

    # spinner placeholder
    spinner_placeholder = st.empty()

    # Text input box at the bottom
    with st.form(key='user_query_form', clear_on_submit=True):
        user_query = st.text_input(" ", key='user_query', placeholder="Message Maziwa...")
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_query:
            # Append the user query to the conversation history
            st.session_state.conversation_history.append({"user": user_query})

            with st.spinner('Processing...'):
                result = rag.LLM_Run(user_query)

            # Append the model response to the conversation history
            st.session_state.conversation_history.append({"MaziwaMax": result})

            # clear the spinner
            spinner_placeholder.empty()

if __name__ == '__main__':
    main()
