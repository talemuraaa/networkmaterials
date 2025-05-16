import streamlit as st

from utils import sideber_title
from pages.network_models import VIS_model

st.set_page_config(
    page_title="ネットワーク保管庫"
    ,layout="centered"
)

sideber_title.sideber_title()

page = st.sidebar.selectbox(
    "モデルを選択",
    ("random network","watts-strogatz model","Barabasi-Albert model", "random walk","step random walk")
)

#ページ頭

st.title("🔨ネットワーク保管庫")
st.write("""
         発表で利用したモデルやプログラムをここにまとめます。\n
         
         - スライドバーで各パラメータを調整できます。
         - 「特徴量」に☑を入れると特徴量が同時に表示されます。
         - ノード数が大きくなると可視化されたネットワークがごちゃごちゃするので気休め程度に。
         - downloadボタンを押すと生成したネットワークの隣接リストがcsvでダウンロードできます。
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



