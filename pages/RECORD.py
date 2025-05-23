import streamlit as st
from pages.materials_modu import material_1
from utils import sideber_title

st.set_page_config(
    page_title="archive"
    ,layout="centered"
)


sideber_title.sideber_title()


st.markdown("# 📚発表資料アーカイブ")
st.divider()

page_id=st.sidebar.selectbox(
    '日付けを選択',
    ['第１回'])

if page_id == "第１回":
    material_1.material20250509()