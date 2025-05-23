import networkx as nx
import random as rd

#自作モデル

def random_walk_graph(N,m,p):
    G=nx.complete_graph(4)
    for i in range(4,N):   
        l=list(nx.nodes(G))
        j=rd.choice(l)
        G.add_edge(i,j)
        
        selected=set([i])
        
        for _ in range(m-1):
            random_value = rd.random()
            #確率ｐで隣接ノードに接続するかしないか場合分け。
            if random_value<p:
                
                #ｎからランダムに一つノードｓを選択。
                #リンクｉｓを生成。
                
                unvisited_neighbors = [n for n in G.neighbors(j) if (n not in selected )]
                
                if not unvisited_neighbors:
                    break
                
                s=rd.choice(unvisited_neighbors)
                G.add_edge(i,s)
                selected.add(s)
              
            else:

                #リストからランダムにノードｓを選択。リンクｉｓを生成。
                unvisited_nodes = [n for n in G.nodes if (n not in selected)]
                if not unvisited_nodes:
                    break
                s=rd.choice(unvisited_nodes)  
                G.add_edge(i,s)
                selected.add(s)
           
    return G

def step_RW_graph(N,p,l=None):
    
    if not l:
        l=N
    
    G=nx.complete_graph(4)
    #初期状態N＝４の完全グラフ
    for i in range(4,N):
        #ノードリストｌを取得。
        #ノードiを追加、ノードリストｌからランダムに一つノードｊを選択。
        #リンクｉｊを生成。
        node_list=list(nx.nodes(G))
        j=rd.choice(node_list)
        G.add_edge(i,j)
        
        #ノードｊの隣接ノードリストｎを取得。
                
        #乱数を生成。
        
        random_value = rd.random()
        
        #確率ｐで隣接ノードに接続するかしないか場合分け。
        
        if random_value<p:
            #到達済み判定
            #ウォークを格納
            current_node=j
            walk=[current_node]
            visited = set(walk)
            for _ in range(l):
                if rd.random()<p:
                    unvisited_neighbors = [n for n in G.neighbors(current_node) if (n not in visited and n!=i)]
                    if unvisited_neighbors:
                        next_node = rd.choice(unvisited_neighbors)
                        walk.append(next_node)
                        visited.add(next_node)
                        current_node = next_node
                    else :
                        #移動先無しで終了
                        break
                else:
                    #1-pで終了
                    break
            
            for k in walk:
                G.add_edge(i,k)    
            
    
        else: 
            node_list.remove(j)
            s=rd.choice(node_list)
            G.add_edge(i,s)
            
    return G