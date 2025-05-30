import streamlit as st
from utils import sideber_title
from module.experiments.main_analysis import main_analysis



st.set_page_config(
    page_title="HOME"
    ,layout="wide"
)

st.title("ネットワーク解析(製作中)")

st.write("- 実行には時間を要する場合があるので注意")

sideber_title.sideber_title()

main_analysis()