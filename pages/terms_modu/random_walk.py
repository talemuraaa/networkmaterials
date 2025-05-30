import streamlit as st

def RW_page():
    st.write("""
             ### _ランダムウォークモデル_
             ライブラリになかったのでとりあえずナイーブな実装をしました。\n
             アルゴリズムは調整予定です。
             
             初期状態はN=4の完全グラフにしたけど諸説あり。
             """)
    
    code='''
    import networkx as nx
    import random as rd
    '''
    st.code(code,language='python')

    st.code('random_walk_graph(N,p)',language='python')
    st.caption("N:ノード数 　p:隣接ノードへの接続確率")
    code_RW='''
def random_walk_graph(N,m,p):
    G=nx.complete_graph(4)
    for i in range(4,N): 
        l=list(nx.nodes(G))
        j=rd.choice(l)
        G.add_edge(i,j)
        selected=set([i])
        for _ in range(m-1):
            random_value = rd.random() #確率ｐで隣接ノードに接続するかしないか場合分け。
            if random_value<p:
                unvisited_neighbors = [n for n in G.neighbors(j) if (n not in selected )]
                if not unvisited_neighbors:
                    break
                s=rd.choice(unvisited_neighbors)
                G.add_edge(i,s)
                selected.add(s)  
            else:
                unvisited_nodes = [n for n in G.nodes if (n not in selected)]
                if not unvisited_nodes:
                    break
                s=rd.choice(unvisited_nodes)
                G.add_edge(i,s)
                selected.add(s)
    return G
        '''  
    with st.expander("実装コード"):
        st.write("## _ランダムウォークモデル_")
        st.code(code_RW,language='python')            

def step_RW_page():
    st.write("""
             ### _拡張ランダムウォークモデル_
             ノード$j$から最大$l$ステップまでのランダムウォークを実行し、ノード$i$と接続する。
             """)

    code='''
    import networkx as nx
    import random as rd
    '''
    st.code(code,language="python")
    st.code('step_RW_graph(N,p,l)',language='python')
    st.caption("N:ノード数 　p:未訪問の隣接ノードへの接続確率　l:最大ウォーク数")
    code='''
    
    def step_RW_graph(N,p,l=None):
    
    #最大ステップ数を設定したい場合のみｌを入力
    
    if not l:
        l=N
    
    G=nx.complete_graph(4)　#初期状態N＝４の完全グラフ
    for i in range(4,N):  
        node_list=list(nx.nodes(G))　#Gのノードリストを取得。
        j=rd.choice(node_list)#ノードiを追加、ノードリストからランダムに一つノードｊを選択。
        G.add_edge(i,j) #リンクｉｊを生成。               
        random_value = rd.random() #乱数を生成。      
        if random_value<p:　#確率ｐで隣接ノードに接続するかしないか場合分け。
            current_node=j
            walk=[current_node]#ウォークを格納
            visited = set(walk)#到達済み判定
            for _ in range(l):
                if rd.random()<p:
                    unvisited_neighbors = [n for n in G.neighbors(current_node) if (n not in visited and n!=i)]
                    if unvisited_neighbors:
                        next_node = rd.choice(unvisited_neighbors)
                        walk.append(next_node)
                        visited.add(next_node)
                        current_node = next_node
                    else :   
                        break #移動先無しで終了
                else:
                    break #1-pで終了       
            for k in walk:
                G.add_edge(i,k)        
        else: 
            node_list.remove(j)
            s=rd.choice(node_list)
            G.add_edge(i,s)        
    return G    
    '''
    with st.expander("実装コード"):
        st.write("## _ランダムウォークモデル(ver.2)_")
        st.code(code,language="python")
