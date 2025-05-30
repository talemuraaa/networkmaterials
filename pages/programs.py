import streamlit as st

from utils import sideber_title
from module.network_models import VIS_model_sample
from module.experiments.main_hist import experiment_hist_ver2
from module.experiments import main_attack_net,main_centrality





def main_VIS_network():
    

    
    st.header("ネットワークモデル概要")
    st.write("""
            
            - スライドバーで各パラメータを調整できます。
            - 「特徴量」に☑を入れると特徴量が同時に表示されます。
            - ノード数が大きくなると可視化されたネットワークがごちゃごちゃするので気休め程度に。
            - downloadボタンを押すと生成したネットワークの隣接リストがcsvでダウンロードできるます。けど可視化したデータが同時にリセットされるので要改善。
            """)
    st.divider()

    page = st.sidebar.radio(
        "モデルを選択",
        ("random network","watts-strogatz model","Barabasi-Albert model", "Holme-Kim model","ex random walk")
    )
    
    

    if page == "random network":
        VIS_model_sample.random_network_page()

    elif page =="watts-strogatz model":
        VIS_model_sample.WS_model_page()

    elif page=="Barabasi-Albert model":
        VIS_model_sample.BA_model_page()    

    elif page=="Holme-Kim model":
        VIS_model_sample.HK_model_page()
        
    elif page=="ex random walk":
        VIS_model_sample.step_RW_page()

st.set_page_config(
    page_title="ネットワーク保管庫"
    ,layout="wide"
)

sideber_title.sideber_title()

st.markdown("""
    <style>
    /* メインコンテンツ部分だけ幅制限＋中央寄せ */
    [data-testid="stVerticalBlock"] {
        max-width: 900px;
        margin: 0 auto;
        padding: 0rem;
    }
    </style>
""", unsafe_allow_html=True)

main_pages=st.sidebar.selectbox("a",("Nerwrok model","Degree Distribution","Centrality","Attack on network"),label_visibility= "collapsed")

#ページ頭

st.title("🔨ネットワーク保管庫")

if main_pages=="Nerwrok model":
    main_VIS_network()
    
elif main_pages=="Degree Distribution":
    experiment_hist_ver2()
    
elif main_pages=="Centrality":
    main_centrality.main_centrality()
    
elif main_pages=="Attack on network":
    main_attack_net.multi_attack_to_network()
    







