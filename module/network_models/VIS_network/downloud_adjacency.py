import pandas as pd
import streamlit as st
import networkx as nx
from io import StringIO


def downloud_adjacency_list_button(G:nx.graph, filename: str = "adjlist.csv", key: str = "download"):
    rows = []
    for u in G.nodes():
            neighbors = sorted(G.neighbors(u))
            neighbor_str = ",".join(map(str, neighbors))
            rows.append({"node": u, "neighbors": neighbor_str})

    
    df = pd.DataFrame(rows)
    
    csv_buffer = StringIO()
    df.to_csv(csv_buffer,index=False,header=False)
    csv_data=csv_buffer.getvalue()
    
    st.download_button(
        label="download",
        data=csv_data,
        file_name=filename,
        mime="text/csv",
        type='primary',
        key=key
        )

def upload_graph_from_csv(label: str = "隣接リストCSVをアップロード",
                          key: str = "upload") -> nx.Graph | None:
    """
    ユーザーがヘッダー行なしの隣接リストCSVをアップロードし、
    NetworkX グラフを構築して返します。
    CSV は各行が「ノード,隣接ノード1,隣接ノード2,...」の形式。
    アップロードがなければ None を返します。
    """
    
    uploaded = st.file_uploader(label=label, type=["csv"], key=key)
    if uploaded is None:
        return None

    # ヘッダーなしで読み込む
    df = pd.read_csv(uploaded, header=None, dtype=str)
    G = nx.Graph()
    for idx, row in df.iterrows():
        # 0列目がノード、以降が隣接ノードリスト
        u = row.iloc[0]
        # 空文字を除去し、ノードと隣接リストを追加
        neighbors = [v for v in row.iloc[1:].dropna().astype(str) if v != ""]
        for v in neighbors:
            G.add_edge(u, v)
    st.success(f"グラフを読み込みました: ノード数={G.number_of_nodes()}, リンク数={G.number_of_edges()}")
    return G
    

#adj_list=nx.to_pandas_edgelist(G)

#adj_list={node: list(G.adj[node])for node in G.nodes}
#df = pd.DataFrame([(k, v) for k, vs in adj_list.items() for v in vs])