import streamlit as st
import anthropic

# Page configuration
st.set_page_config(page_title='AI Interview Assistant', page_icon='🤖')

# Custom CSS styling
st.markdown('<style>/* Add your custom CSS here */</style>', unsafe_allow_html=True)

# Constants
ROLES = ['Software Engineer', 'Data Scientist', 'Product Manager']
DIFFICULTY = ['Easy', 'Medium', 'Hard']
CATEGORIES = ['Technical', 'HR', 'Behavioral']

# System prompt generation
def generate_prompt(role, difficulty, category):
    return f"You are conducting an interview for the role of {role} with {difficulty} difficulty in {category} category."

# Session state management
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Claude API integration function
def get_ai_response(prompt):
    response = anthropic.Completion.create(
        model='claude-v1',
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text']

# Message rendering with evaluation cards
def render_messages():
    for message in st.session_state.chat_history:
        st.write(message)

# Setup screen
st.title('AI Interview Assistant')
role = st.selectbox('Select Role:', ROLES)
difficulty = st.selectbox('Select Difficulty:', DIFFICULTY)
category = st.selectbox('Select Category:', CATEGORIES)
if st.button('Start Interview'):
    prompt = generate_prompt(role, difficulty, category)
    st.session_state.chat_history.append(f'Interview started for {role} at {difficulty} difficulty in {category}.')
    render_messages()

# Interview screen with chat history
user_input = st.text_input('Your message:')
if st.button('Send'):
    st.session_state.chat_history.append(f'User: {user_input}')
    ai_response = get_ai_response(user_input)
    st.session_state.chat_history.append(f'AI: {ai_response}')
    render_messages()