import streamlit as st
import matplotlib.pylab as plt
from pages.network_models.select_model import model_select
from pages.experiments.select_stra import select_strategy,ig_select_strategy

def attack_to_network():
    st.header("ネットワークへのアタック")
    st.write("""
             ノード数が大きいと若干時間がかかります。
             気が向いたら同時に複数の崩壊を描画できるようにします。
             完成したらネットワーク保管庫のセレクトボックスに統合します。
             """)
    col1,col2=st.columns([1,1])
    with col1:
        st.write("１．アタック対象の設定")
        N=st.slider("N_value",10,1000,100,step=10)
    with col2:
        st.write("")
    G=model_select(N,1)
    
    if G:
        st.write("２. 攻撃方法の選択")
        cllopse_list=ig_select_strategy(G)
        if  cllopse_list:
            fig, ax = plt.subplots(figsize=(7, 6))
            ax.plot(range(N+1),cllopse_list,markersize=5,label='random')
            ax.grid(True)
            ax.set_xlabel("Number of nodes removed")
            ax.set_ylabel("Percentage of nodes in giant connected component")
            
            st.pyplot(fig)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    