import streamlit as st
from utils import sideber_title
from pages.experiments.main_attack_net import attack_to_network


sideber_title.sideber_title()
st.title("🚀動作テスト")
st.write("""
         ### 🔧工事中🔧
         """)

st.divider()

attack_to_network()