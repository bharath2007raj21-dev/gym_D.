
import streamlit as st
from google import genai

st.set_page_config(page_title="D Gym Assistant", page_icon="💪")

st.title("💪 The D Gym Assistant")
st.markdown("---")

members = [
    {"name": "Ravi", "paid": True, "goal": "weight loss"},
    {"name": "Kumar", "paid": False, "goal": "muscle gain"},
    {"name": "Priya", "paid": True, "goal": "fitness"},
    {"name": "Anjali", "paid": False, "goal": "weight loss"},
    {"name": "Rahul", "paid": True, "goal": "muscle gain"},
    {"name": "Sneha", "paid": False, "goal": "fitness"},
    {"name": "Amit", "paid": True, "goal": "weight loss"},
    {"name": "Neha", "paid": False, "goal": "muscle gain"},
    {"name": "Vikram", "paid": True, "goal": "fitness"},
    {"name": "Sonal", "paid": False, "goal": "weight loss"}
]

ct=st.text("Welcome to The D Gym! Ask me anything about our members, their goals, or their payment status. I'm here to help you with all the information you need to make the most of your gym experience!")
mb=st.text("Here are our members: Ravi, Kumar, Priya, Anjali, Rahul, Sneha, Amit, Neha, Vikram, and Sonal. Feel free to ask about any of them or their fitness goals!")

question = st.text_input("🔍 Ask about your gym members:")

if question:
    with st.spinner("Thinking..."):
       client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"You are a gym assistant. Member data: {members}. Answer briefly and clearly: {question}"
        )
    st.success(response.text)