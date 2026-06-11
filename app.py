import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load secret API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Layout configuration
st.set_page_config(page_title="Tactician Pro AI", page_icon="⚽", layout="centered")

st.title("⚽ Tactician Pro AI")
st.caption("Unofficial Companion for Elite FC Mobile Squad Building")
st.write("---")

SYSTEM_INSTRUCTION = """
You are "Tactician Pro", an elite, independent AI mastermind built for hardcore EA SPORTS FC Mobile players. Your goal is to help users optimize squads up to the 125+ OVR endgame tier and maximize their coin balance.

Current Game Meta Framework (2026):
1. Ratings Context: Top tier individual cards are at 118, 119, and 120 OVR (e.g., TOTS Mbappe, Ronaldo, Prime Icons). Teams are pushing 125-128 OVR ceilings. 
2. PlayStyles Matter: Evaluate cards based on PlayStyles+ (like Finesse Shot+, Bruiser, or Incisive Pass+) rather than just raw OVR.

Tone Rules:
- Speak with high-level gaming authority. Use terms like: Rank Up, VSA, H2H Meta, Mascheranos, and Scripting.
- Always conclude with a sharp, tactical football sign-off line.
"""

st.subheader("🤖 Ask the Tactician Engine")
user_query = st.text_area("Paste your squad details, budget, or event questions here:", placeholder="e.g., Should I rank up my 118 Mbappe or sell him before the market crash?")

if st.button("Run Tactical Analysis", type="primary"):
    if user_query.strip():
        with st.spinner("Analyzing market volatility..."):
            try:
                client = genai.Client(api_key=API_KEY)
                response = client.models.generate_content(
                    model="models/gemini-2.5-flash",
                    contents=user_query,
                    config={"system_instruction": SYSTEM_INSTRUCTION}
                )
                st.write("---")
                st.success("Analysis Complete!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Engine Error: {e}")
    else:
        st.warning("Please type a question first!")