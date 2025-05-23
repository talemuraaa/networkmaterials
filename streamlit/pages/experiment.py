import streamlit as st
from utils import sideber_title
from pages.experiments import ex_hist


sideber_title.sideber_title()
st.title("🚀実験場")
st.write("""
         ### 🔧工事中🔧
         """)

st.divider()

page = st.sidebar.selectbox(
    "実験を選択",
    ("次数分布","最短経路長、クラスター係数")
    )

if page == "次数分布":
    ex_hist.experiment_hist()