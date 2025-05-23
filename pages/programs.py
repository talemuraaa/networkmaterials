import streamlit as st

from utils import sideber_title
from module.network_models.VIS_network import VIS_model
from module.experiments.ex_hist import experiment_hist_ver2
from module.experiments import main_attack_net

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
        ("random network","watts-strogatz model","Barabasi-Albert model", "random walk","ex random walk")
    )
    
    

    if page == "random network":
        VIS_model.random_network_page()

    elif page =="watts-strogatz model":
        VIS_model.WS_model_page()

    elif page=="Barabasi-Albert model":
        VIS_model.BA_model_page()    

    elif page=="random walk":
        VIS_model.RW_page()
        
    elif page=="ex random walk":
        VIS_model.step_RW_page()



st.set_page_config(
    page_title="ネットワーク保管庫"
    ,layout="centered"
)

sideber_title.sideber_title()

main_pages=st.sidebar.selectbox("a",("Nerwrok model","Degree Distribution","Attack on network"),label_visibility= "collapsed")

#ページ頭

st.title("🔨ネットワーク保管庫")

if main_pages=="Nerwrok model":
    main_VIS_network()
    
elif main_pages=="Degree Distribution":
    experiment_hist_ver2()
    
elif main_pages=="Attack on network":
    main_attack_net.multi_attack_to_network()
    







