import streamlit as st
from utils import sideber_title
from pages.materials_modu import material_2

st.set_page_config(
    page_title="archive"
    ,layout="centered"
)


st.title("📖発表資料")
st.divider()

sideber_title.sideber_title()

material_2.material20255030()
