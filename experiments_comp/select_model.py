import streamlit as st
import networkx as nx
from module.experiments_comp.models import models
from module.experiments_comp import build_labels

def generate_graph(model_name, N, params):
    """指定モデルのグラフを生成する"""
    if model_name == "random(erdős-Rényi) model":
        return nx.gnm_random_graph(N, params["m"])
    elif model_name == "random(gilbert) model":
        return nx.gnp_random_graph(N, params["p"])
    elif model_name == "watts-strogatz model":
        return nx.watts_strogatz_graph(N, params["k"], params["p"])
    elif model_name == "Barabasi-Albert model":
        return nx.barabasi_albert_graph(N, params["m"])
    elif model_name == "Holme-Kim model":
        return nx.powerlaw_cluster_graph(N, params["m"], params["p"])
    elif model_name == "ex random walk model":
        # 自作モデル呼び出し。models モジュールが必要
        return models.step_RW_graph(N, params["p"])
    else:
        raise ValueError("Unknown model")

def clear_saved(idx):
    """セッションから保存済みグラフを削除"""
    key = f"{idx}_graph"
    if key in st.session_state:
        del st.session_state[key]
    meta_key = f"{key}_meta"
    if meta_key in st.session_state:
        del st.session_state[meta_key]

def get_model_params(model_name, N, index):
    """モデルごとのパラメータ入力UIを作成（変更時に保存解除を呼び出す）"""
    params = {}
    if model_name == "random(erdős-Rényi) model":
        max_edges = N * (N - 1) / 50
        params["m"] = st.number_input(
            "リンク数 m", 0, int(max_edges), 100,
            key=f"{index}_er_m", on_change=clear_saved, args=(index,)
        )
    elif model_name == "random(gilbert) model":
        params["p"] = st.number_input(
            "接続確率 p", 0.0, 1.0, 0.01,
            key=f"{index}_gil_p", on_change=clear_saved, args=(index,)
        )
    elif model_name == "watts-strogatz model":
        params["k"] = st.number_input(
            "近傍数 K", 2, 300, 3,
            key=f"{index}_ws_k", on_change=clear_saved, args=(index,)
        )
        params["p"] = st.number_input(
            "再接続確率 p", 0.0, 1.0, 0.3,
            key=f"{index}_ws_p", on_change=clear_saved, args=(index,)
        )
    elif model_name == "Barabasi-Albert model":
        params["m"] = st.number_input(
            "接続リンク数 m", 1, 20, 3,
            key=f"{index}_ba_m", on_change=clear_saved, args=(index,)
        )
    elif model_name == "Holme-Kim model":
        params["m"] = st.number_input(
            "接続リンク数 m", 1, 20, 3,
            key=f"{index}_hk_m", on_change=clear_saved, args=(index,)
        )
        params["p"] = st.number_input(
            "確率 p", 0.0, 1.0, 0.5,
            key=f"{index}_hk_p", on_change=clear_saved, args=(index,)
        )
    elif model_name == "ex random walk model":
        params["p"] = st.number_input(
            "確率 p", 0.0, 1.0, 0.5,
            key=f"{index}_srw_p", on_change=clear_saved, args=(index,)
        )
    return params

def save_graph_to_session(key, graph):
    """グラフを session_state に保存"""
    st.session_state[key] = graph

def reset_graph(key, index):
    """ネットワークの能動的リセット"""
    if key in st.session_state:
        if st.button("リセット", key=f"{index}_reset"):
            clear_saved(index)

def model_select_ver3(N=None, index=0):
    """
    Streamlit UI: ネットワークモデルを選択し、パラメータ設定後にグラフを生成・保存・表示。
    保存済みであればヘッダーにマークを表示。
    パラメータを変更すると自動で保存解除。
    戻り値: networkx.Graph または None
    """
    container = st.container()
    col1, col2 = container.columns([4, 5], border=True)

    graph_key = f"{index}_graph"

    with col1:
        st.write(f"#### _Network{index}_")
        # ノード数スライダー（変更時に保存解除）
        if N is None:
            N = st.number_input(
                "ノード数 (N)", 0, 3000, 500, step=50,
                key=f"{index}_nodes", on_change=clear_saved, args=(index,)
            )
        model_name = st.selectbox(
            "モデルを選択",
            [
                "random(erdős-Rényi) model",
                "random(gilbert) model",
                "watts-strogatz model",
                "Barabasi-Albert model",
                "Holme-Kim model",
                "ex random walk model"
            ],
            key=f"{index}_model", on_change=clear_saved, args=(index,)
        )
        
        
    with col2:

        # モデルと N を使ってパラメータ取得
        params = get_model_params(model_name, N, index)


        graph = None
        # 生成済みの場合は保持
        if graph_key in st.session_state:
            graph = st.session_state[graph_key]
        # 生成ボタン押下で保存
        
        
        
        if st.button("生成", key=f"{index}_gen"):
            graph = generate_graph(model_name, N, params)
            save_graph_to_session(graph_key, graph)
    
        reset_graph(graph_key, index)

    # 保存済みマーク表示

        if graph_key in st.session_state:
            st.markdown("**✅ 保存済み**")

    return st.session_state.get(graph_key, None)
    
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
                "ノード数 (N)", 0, 3000, 500,step=50,
                key=f"{index}_nodes"
            )
        network = st.selectbox(
            "モデルを選択",
            [
                "random(erdős-Rényi) model",
                "random(gilbert) model",
                "watts-strogatz model",
                "Barabasi-Albert model",
                "Holme-Kim model",
                "ex random walk model"
            ],
            key=f"{index}_model"
        )

    # 右カラム: パラメータ設定と生成ボタン
    with col2:
        
        if network == "random(erdős-Rényi) model":
            max=N*(N-1)/50
            m = st.slider(
                "リンク数 m", 0,int(max),100,
                key=f"{index}_m"
            )
            if st.checkbox("生成", key=f"{index}_rand_check"):
                return nx.gnm_random_graph(N,m)
        
        
        if network == "random(gilbert) model":
            p = st.slider(
                "接続確率 p", 0.0, 1.0, 0.01,
                key=f"{index}_p"
            )
            if st.checkbox("生成", key=f"{index}_rand_check"):
                return nx.gnp_random_graph(N, p)

        elif network == "watts-strogatz model":
            k = st.slider(
                "近傍数 K", 2, 300, 3,
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
            
        elif network == "Holme-Kim model":
            m = st.slider(
                "接続リンク数 m", 1, 20, 3,
                key=f"{index}_rw_m"
            )
            p = st.slider(
                "確率 p", 0.0, 1.0, 0.5,
                key=f"{index}_rw_p"
            )
            if st.checkbox("生成", key=f"{index}_rw_check"):
                return nx.powerlaw_cluster_graph(N, m, p)

        elif network == "ex random walk model":
            p = st.slider(
                "確率 p", 0.0, 1.0, 0.5,
                key=f"{index}_srw_p"
            )

            if st.checkbox("生成", key=f"{index}_srw_check"):
                return models.step_RW_graph(N, p)
