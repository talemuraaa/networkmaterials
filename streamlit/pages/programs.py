import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random as rd

from pages.n_model import VIS_model

st.set_page_config(
    page_title="ネットワーク保管庫"
    ,layout="centered"
)

with st.sidebar:
    st.page_link("app.py",label="HOME",icon="🏠")
    st.page_link("pages/MATERIALS.py",label="発表資料",icon="📖")
    st.page_link("pages/programs.py",label="ネットワーク保管庫",icon="🔨")
    st.page_link("pages/RECORD.py",label="アーカイブ",icon="📚")
st.sidebar.divider()

page = st.sidebar.selectbox(
    "モデルを選択",
    ("random network","watts-strogatz model","Barabasi-Albert model", "random walk","step random walk")
)

#ページ頭

st.title("🔨ネットワーク保管庫")
st.write("""
         発表で利用したモデルやプログラムをここにまとめます。\n
         - スライドバーで各パラメータを調整することができます。
         - 「特徴量」に☑を入れると各種パラメータが同時に表示されます。
         - ノード数が大きすぎるとmatplotlibが怒るので最大ノード数は300固定。\n
         """)
st.divider()



if page == "random network":
    VIS_model.random_network_page()

elif page =="watts-strogatz model":
    VIS_model.WS_model_page()

elif page=="Barabasi-Albert model":
    VIS_model.BA_model_page()    

elif page=="random walk":
    VIS_model.RW_page()
    
elif page=="step random walk":
    VIS_model.step_RW_page()



