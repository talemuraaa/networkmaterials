import streamlit as st
import matplotlib.pylab as plt
import pandas as pd
import io
from module.experiments_comp.select_model import model_select_ver3
from module.experiments_comp.attack_comp import select_stra
from module.experiments_comp.attack_comp import criterions
from module.experiments_comp import build_labels
from module.experiments_comp import net_parameter

#１つの攻撃戦略に対して複数のネットワークを用意する。

def single_attack_to_muluti_network():

        
    st.header("１つの攻撃戦略に対して複数のネットワークで比較する。")
    
    col_1,col_2=st.columns([1,1])
    
    with col_1:
        network_count = st.slider(
        "用意するネットワークの数", 1, 5, 1, key='n_m'
    )
    
    with col_2:
        strategy=st.selectbox("攻撃戦略",
                    ["random failures",
                     "targeted attack(degree)",
                     "targeted attack(closeness)",
                     "targeted attack(betweenness)"],
                    key='strategy')    
        
    networks = []
    # モデル選択と生成
    
    for i in range(network_count):
        # model_selectで生成
        with st.container(height=360,key=f"{i}_con"):
            col_3,col_4=st.columns([5,2])
            with col_3:
                G = model_select_ver3(index=i)
                if G is not None:
                    networks.append(G)

            with col_4:
                if G is None:
                    return
                net_parameter.net_parameter(G)
            
            
    plot_labels=build_labels.build_labels(st.session_state,network_count)
            
            
    if len(networks) != network_count:
        st.warning("⚠️ すべてのネットワークが生成されていません")
        return
    
    if None in networks:
        return

    
    if st.button("シュミレーションを実行",key='strategy2'):
        progress_bar = st.progress(0)
        
        def update_progress(percent):
            progress_bar.progress(percent)
        
        with st.spinner("計算中..."):
            result=select_stra.select_single_strategy(networks,strategy)
           
           
            
        fig, ax = plt.subplots(figsize=(7, 6))
        R={}
        i=0
        for label, values in result.items():
                ax.plot(range(len(values)), values, label=f'{plot_labels[i]}')
                R[plot_labels[i]]=criterions.robustness(values)
                i=i+1
                update_progress(int(i/network_count)*100)
                
        update_progress(100)

        ax.grid(True)
        ax.set_title(f"{strategy}")
        ax.set_xlabel("Number of nodes removed")
        ax.set_ylabel("Percentage of nodes in giant connected component")
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        
        fn = 'plot.png'
        img = io.BytesIO()
        fig.savefig(img, format="png", bbox_inches='tight')
        img.seek(0)
        
        st.pyplot(fig)        
        
        st.download_button(   
                           label="Download as PNG",
                            data=img,
                            file_name=fn,
                            mime="image/png"
                            )
        
        df = pd.DataFrame.from_dict(
            {"rubstness": R}, orient='index'
        ).T
        
        st.dataframe(df, width=200)        

#１つのネットワークに対して複数の攻撃戦略を指定して同時に表示する。

def multi_attack_to_network():
    
    st.header("ネットワークへのアタック")
    st.write("ノード数1,000以上は非推奨。計算時間が数分以上かかる場合があります。")
    st.divider()

    
    G=model_select_ver3()
    
    if G:
        st.write("2. 攻撃方法の選択")
        strategy_list=st.multiselect("攻撃戦略",
                    ["random failures",
                     "targeted attack(degree)",
                     "targeted attack(closeness)",
                     "targeted attack(betweenness)"],
                          key='strategy')
        
    if G is None:
        st.warning("⚠️ ネットワークが生成されていません")
        return
        
    if st.button("シュミレーションを実行",key='strategy2'):
        progress_bar = st.progress(0)
        
        def update_progress(percent):
            progress_bar.progress(percent)

        with st.spinner("計算中..."):
            result = select_stra.select_strategys_prog(G, strategy_list, progress_callback=update_progress)
            
        
        fig, ax = plt.subplots(figsize=(7, 6))
        R={}
        for label, values in result.items():
                ax.plot(range(len(values)), values, label=label)
                
                R[label]=criterions.robustness(values)

        ax.grid(True)
        ax.set_xlabel("Number of nodes removed")
        ax.set_ylabel("Percentage of nodes in giant connected component")
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        st.pyplot(fig)
        
        df = pd.DataFrame.from_dict(
            {"rubstness": R}, orient='index'
        ).T
        
        st.dataframe(df, width=200)

        

    
    
    
    
    
    
    
    
    
    
    
    
    