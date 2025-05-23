import streamlit as st
import matplotlib.pylab as plt
from module.network_models.select_model import model_select_ver2,model_select
from module.experiments import select_stra

#１つのネットワークに対して複数の攻撃戦略を指定して同時に表示する。（ver2）

def multi_attack_to_network():
    
    st.header("ネットワークへのアタック")
    
    st.divider()
    
    col1,col2=st.columns([3,2])
    with col1:
        st.write("１．アタック対象の設定")
        N=st.slider("N_value",10,3000,500,step=10)
    with col2:
        st.write("")
    
    G=model_select_ver2(N,index=0)
    
    if G:
        st.write("2. 攻撃方法の選択")
        strategy_list=st.multiselect("攻撃戦略",
                          ["ランダム障害","標的型攻撃(degree)","標的型攻撃(closeness)","標的型攻撃(betweenness)"],
                          key='strategy')
        
    if G is None:
        st.warning("⚠️ ネットワークが生成されていません。チェックボックスを確認してください。")
        return
        
    if st.button("シュミレーションを実行",key='strategy2'):
        progress_bar = st.progress(0)
        def update_progress(percent):
            progress_bar.progress(percent)

        with st.spinner("計算中..."):
            result = select_stra.select_strategys_prog(G, strategy_list, progress_callback=update_progress)
            
        
        fig, ax = plt.subplots(figsize=(7, 6))
        
        for label, values in result.items():
                ax.plot(range(len(values)), values, label=label)

        ax.grid(True)
        ax.set_xlabel("Number of nodes removed")
        ax.set_ylabel("Percentage of nodes in giant connected component")
        ax.legend()
        st.pyplot(fig)

#1つのネットワークに対して１つの攻撃戦略を指定する。（ver1）

def attack_to_network():
    
    st.header("ネットワークへのアタック")
    st.write("""
             ランダムネットワークモデルは全体的に処理が重いです。
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
        st.write("2. 攻撃方法の選択")
        strategy=st.selectbox("攻撃戦略",
                          ("ランダム障害","標的型攻撃(degree)","標的型攻撃(closeness)","標的型攻撃(betweenness)"),
                          key='strategy')
        
    if st.button("実行",key='strategy2'):
        cllopse_list=select_stra.ig_select_strategy2(G,strategy)
        
        fig, ax = plt.subplots(figsize=(7, 6))
        ax.plot(range(N+1),cllopse_list,markersize=5,label='random')
        ax.grid(True)
        ax.set_xlabel("Number of nodes removed")
        ax.set_ylabel("Percentage of nodes in giant connected component")
        
        st.pyplot(fig)

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    