import streamlit as st

from utils import sideber_title
from pages.network_models import VIS_model
from pages.experiments.ex_hist import experiment_hist

def main_VIS_network():
    st.write("""
            発表で利用したモデルやプログラムをここにまとめます。\n
            
            - スライドバーで各パラメータを調整できます。
            - 「特徴量」に☑を入れると特徴量が同時に表示されます。
            - ノード数が大きくなると可視化されたネットワークがごちゃごちゃするので気休め程度に。
            - downloadボタンを押すと生成したネットワークの隣接リストがcsvでダウンロードできるます。けど可視化したデータが同時にリセットされるので要改善。
            """)
    st.divider()

    page = st.sidebar.radio(
        "モデルを選択",
        ("random network","watts-strogatz model","Barabasi-Albert model", "random walk","step random walk")
    )
    
    

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



st.set_page_config(
    page_title="ネットワーク保管庫"
    ,layout="centered"
)

sideber_title.sideber_title()

main_pages=st.sidebar.selectbox("a",("Network model","Degree Distribution"),label_visibility= "collapsed")

#ページ頭

st.title("🔨ネットワーク保管庫")

if main_pages=="Network model":
    main_VIS_network()
    
if main_pages=="Degree Distribution":
    experiment_hist()
    







