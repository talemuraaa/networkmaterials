import streamlit as st
import networkx as nx
from module.network_models.models import models
from module.network_models import nerwork_models_cache

#ver3 隣接ファイルのアップロードに対応。

#ver2
def model_select_ver2(N=None, index=0):
    """
    Streamlit UI: ネットワークモデルを選択し、パラメータ設定後にグラフを生成します。
    N: ノード数（None の場合はスライダーで入力）
    index: UIコンポーネントのキー重複回避用インデックス
    戻り値: networkx のグラフオブジェクト、または None
    """
    # レイアウト
    container = st.container()
    col1, col2 = container.columns([3, 5], border=True)

    # 左カラム: モデル選択と N の入力
    with col1:
        st.write(f"#### _Network{index}_")
        if N is None:
            N = st.slider(
                "ノード数 (N)", 0, 3000, 500,
                key=f"{index}_nodes"
            )
        network = st.selectbox(
            "モデルを選択",
            [
                "random network",
                "watts-strogatz model",
                "Barabasi-Albert model",
                "random walk",
                "ex random walk"
            ],
            key=f"{index}_model"
        )

    # 右カラム: パラメータ設定と生成ボタン
    with col2:
        if network == "random network":
            p = st.slider(
                "接続確率 p", 0.0, 1.0, 0.1,
                key=f"{index}_p"
            )
            if st.checkbox("生成", key=f"{index}_rand_check"):
                return nx.gnp_random_graph(N, p)

        elif network == "watts-strogatz model":
            k = st.slider(
                "近傍数 K", 2, 30, 3,
                key=f"{index}_k"
            )
            p = st.slider(
                "再接続確率 p", 0.0, 1.0, 0.3,
                key=f"{index}_ws_p"
            )
            if st.checkbox("生成", key=f"{index}_ws_check"):
                return nx.watts_strogatz_graph(N, k, p)

        elif network == "Barabasi-Albert model":
            m = st.slider(
                "接続リンク数 m", 1, 20, 3,
                key=f"{index}_ba_m"
            )
            if st.checkbox("生成", key=f"{index}_ba_check"):
                return nx.barabasi_albert_graph(N, m)

        elif network == "random walk":
            m = st.slider(
                "接続リンク数 m", 1, 20, 3,
                key=f"{index}_rw_m"
            )
            p = st.slider(
                "確率 p", 0.0, 1.0, 0.5,
                key=f"{index}_rw_p"
            )
            if st.checkbox("生成", key=f"{index}_rw_check"):
                return models.random_walk_graph(N, m, p)

        elif network == "ex random walk":
            p = st.slider(
                "確率 p", 0.0, 1.0, 0.5,
                key=f"{index}_srw_p"
            )

            if st.checkbox("生成", key=f"{index}_srw_check"):
                return models.step_RW_graph(N, p)
#ver1
def model_select(N,i):
    with st.container(height=310):
        col1,col2=st.columns([3,5],border=True)

        
        with col1:
            st.write(f"#### _Network{i}_")
            network=st.selectbox("モデルを選択",
                                 ("random network","watts-strogatz model","Barabasi-Albert model",
                                  "random walk","step random walk"),
                                 key=f'{i}mainbox')
        with col2:
            if N==None:
                N=st.slider("N_value",0,3000,500,key=f'{i}Nslider')
            if network == "random network":
                              
                p_value = st.slider("p_value", 0.0, 1.0, 0.3,key=f'{i}rundom_slider')
                p=float(p_value)
                button=st.checkbox("check",key=f'{i}rd_button',label_visibility="collapsed") 
                if button:
                    G=nerwork_models_cache.rd_model(N,p)
                    return G
                
            if network == "watts-strogatz model":
                
                k_value = st.slider("K_value", 2, 30, 3,key=f'{i}WS_slider1')
                p_value = st.slider("m_value", 0.0, 1.0, 0.3,key=f'{i}WS_slider2')
                k=int(k_value)
                p=float(p_value)
                button=st.checkbox("check",key=f'{i}ws_button',label_visibility="collapsed")
                if button:
                    G=nerwork_models_cache.ws_model(N,k,p)     
                    return G           
                
                
            if network =="Barabasi-Albert model":
                
                m_value = st.slider("m_value", 1, 20, 3,key=f'{i}BA_slider2')
                m=int(m_value)
                button=st.checkbox("check",key=f'{i}ba_button',label_visibility="collapsed")
                if button:
                    G=nerwork_models_cache.ba_model(N,m)
                    return G
                
            if network == "random walk":
                
                m_RW_value = st.slider("m_value",1,20,3,key=f'{i}RW_slider1')
                p_RW_value = st.slider("p_value", 0.0, 1.0, 0.5,key=f'{i}RW_slider2')
                m=int(m_RW_value)
                p=float(p_RW_value)
                button=st.checkbox("check",key=f'{i}rw_button',label_visibility="collapsed")
                if button:
                    G=nerwork_models_cache.rw_network(N,m,p)
                    return G              
                
                
            if network =="step random walk":
                
                p_value = st.slider("p_value", 0.0, 1.0, 0.5,key=f'{i}SRW_slider2')

                p=float(p_value)

                button=st.checkbox("check",key=f'{i}srw_button',label_visibility="collapsed")
                if button:
                    G=nerwork_models_cache.exrw_network(N,p,l=None)
                    return G
    
                   