import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from module.network_models.select_model import model_select_ver2

def main_centrality():
    st.header("中心性の分布")
    
    G=model_select_ver2()
    
    if G is None:
        st.warning("⚠️ ネットワークが生成されていません。チェックボックスを確認してください。")
        return
    if st.button("各中心性の分布を表示",key='histbutton1'):
        
        fig, ax = plt.subplots(figsize=(6, 4))    
        
        degree_centrality = nx.degree_centrality(G)
        betweenness_centrality = nx.betweenness_centrality(G)
        closeness_centrality = nx.closeness_centrality(G)

        degree_values = list(degree_centrality.values())
        betweenness_values = list(betweenness_centrality.values())
        closeness_values = list(closeness_centrality.values())
        
        
        # 全データをまとめる
        all_data = degree_values + betweenness_values + closeness_values

        # 最大値を取得（横軸の範囲として使う）
        max_val = max(all_data)    
        
        data = [degree_values, betweenness_values, closeness_values]
        labels = ['Degree', 'Betweenness', 'Closeness']


        ax.hist(data, bins=30, range=(0, max_val), label=labels, density=True,stacked=False)


        
        ax.set_xlabel('Centrality Value')
        ax.set_ylabel('Frequency')
        ax.legend()
        ax.grid(linestyle='--')



        fig.tight_layout()
        st.pyplot(fig)