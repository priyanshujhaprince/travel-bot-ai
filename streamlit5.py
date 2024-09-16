import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client with the API key
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)

def is_travel_related(question):
    """
    Checks if the question is related to travel or hospitality.
    """
    travel_keywords = ['hotel', 'flight', 'travel', 'booking', 'destination', 'trip', 'tour', 'vacation', 'resort', 'restaurant']
    return any(keyword in question.lower() for keyword in travel_keywords)

def chat(prompt):
    """
    Sends a prompt to the Groq API and returns the response.
    """
    try:
        # Make the API call
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-70b-8192"
        )

        # Extract choices from the response
        choices = chat_completion.choices if hasattr(chat_completion, 'choices') else []
        if choices:
            first_choice = choices[0]
            message = first_choice.message if hasattr(first_choice, 'message') else {}
            message_content = message.content if hasattr(message, 'content') else 'No content available'
            return message_content
        return 'No response available'
    except Exception as e:
        return f"Error: {e}"

def main():
    # Set up the Streamlit page configuration
    st.set_page_config(page_title="TravelVibe 🌈", layout="wide")

    # Apply custom styles to the Streamlit app
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Poppins:wght@300;600&display=swap');

        /* Overall dark gradient background */
        body {
            background: linear-gradient(135deg, #2e2e2e, #0f0f3d, #18185a, #161629);
            background-size: 400% 400%;
            animation: gradientAnimation 10s ease infinite;
        }

        /* Gradient animation */
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Main Heading with animated glow */
        .main-title {
            font-family: 'Poppins', sans-serif;
            color: #f7ff00;
            font-size: 4rem;
            text-align: center;
            text-shadow: 0 0 20px #ff7f50, 0 0 30px #ff7f50;
            animation: neonGlowing 2s alternate infinite ease-in-out;
        }

        /* Neon glow animation for the heading */
        @keyframes neonGlowing {
            from {
                text-shadow: 0 0 10px #ff7f50, 0 0 20px #ff4500, 0 0 30px #ff7f50;
            }
            to {
                text-shadow: 0 0 30px #ff4500, 0 0 40px #ff7f50, 0 0 50px #ff4500;
            }
        }

        /* Sidebar styling - rich colors */
        .stSidebar {
            background: #0f0f2d;
            color: white;
            font-family: 'Roboto', sans-serif;
        }

        /* Button styling - multicolor hover */
        .stButton button {
            background: linear-gradient(45deg, #ff7f50, #ff4500, #ffa500);
            color: white;
            font-size: 1.2rem;
            font-weight: 600;
            padding: 12px 25px;
            border-radius: 30px;
            box-shadow: 0 4px 15px rgba(255, 69, 0, 0.4);
            transition: all 0.4s ease;
        }
        .stButton button:hover {
            background: linear-gradient(45deg, #ffa500, #ff4500, #ff7f50);
            transform: scale(1.08);
            box-shadow: 0 6px 20px rgba(255, 69, 0, 0.6);
        }

        /* Input box with rainbow glow */
        .stTextInput input {
            background-color: #181826;
            color: white;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid transparent;
            box-shadow: 0 0 10px #ff4500, 0 0 20px #ffa500;
            transition: all 0.3s ease;
        }
        .stTextInput input:focus {
            border-color: #ff7f50;
            box-shadow: 0 0 15px #ff4500, 0 0 25px #ffa500;
        }

        /* Keyframe for input glow effect */
        @keyframes inputGlow {
            0% { box-shadow: 0 0 10px #ff4500, 0 0 20px #ffa500; }
            100% { box-shadow: 0 0 20px #ff4500, 0 0 30px #ffa500; }
        }

        /* Subheader Styling */
        .subheading {
            font-family: 'Roboto', sans-serif;
            color: #ffd700;
            font-size: 2rem;
            text-align: center;
            margin-bottom: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 class='main-title'>TravelVibe 🌈</h1>", unsafe_allow_html=True)

    st.markdown(""" 
    ### 🌍 Where will your next adventure take you?  
    **TravelVibe** is your colorful, AI-powered travel companion that delivers fun, personalized travel recommendations!
    """)

    # User input for their travel-related question
    with st.form(key='travel_query'):
        user_question = st.text_input("💬 Tell me where you're heading or what you're looking for:")
        submit_button = st.form_submit_button(label='🎉 Get the Best Travel Deals!')

    if submit_button:
        if user_question:
            if is_travel_related(user_question):
                with st.spinner("⚡ Finding the best flights, hotels, and destinations just for you..."):
                    prompt = f"Act as a travel assistant and answer '{user_question}' based on general travel and hospitality knowledge."
                    response = chat(prompt)
                st.success("✨ Here's a personalized travel recommendation for you!")
                st.write(response)
            else:
                st.error("🚫 Hmm, it looks like your question isn't travel-related. Try asking about trips, hotels, or destinations!")
        else:
            st.warning("🔍 You gotta ask me something! What's your next trip?")

if __name__ == "__main__":
    main()
