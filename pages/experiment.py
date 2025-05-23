import streamlit as st
from utils import sideber_title
from module.experiments import main_attack_net


sideber_title.sideber_title()
st.title("🚀動作テスト")

st.divider()

main_attack_net.multi_attack_to_network()