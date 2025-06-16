import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def filterd_node(G,degree=1):
    filtered_nodes = [n for n in G.nodes() if G.degree(n) > degree]
    return  G.subgraph(filtered_nodes)


def draw_plot_plt(G:nx.Graph):
    fig,ax = plt.subplots([7,6])
    
    pr1 = dict(nx.degree_centrality(G))
    pos1 =nx.kamada_kawai_layout(G)
    ax.draw_networkx_edges(G, pos1,edge_color='Gray')
    ax.draw_networkx_nodes(G, pos1,node_color=list(pr1.values()), cmap=plt.cm.Reds,node_size=120,edgecolors='Gray')

    ax.axis('off')
    ax.tight_layout()
    
    return fig


def draw_2Dplot_go(G: nx.Graph, 
                node_size:int = 8, 
                layout_type='kamada_kawai',
                custom_pos: dict = None,
                custom_centrality: dict = None):
    
    if custom_centrality is None:
        # fallback: サブグラフで再計算
        pr1 = dict(nx.degree_centrality(G))
    else:
        # 全体グラフで計算した値をサブグラフのノードだけ抜き出す
        pr1 = {n: custom_centrality[n] for n in G.nodes()}
    
    
    if custom_pos is not None:
        pos = custom_pos
    else:
        if layout_type == 'spring':
            pos = nx.spring_layout(G,dim=2, iterations=10, scale=2.0)
        else:
            pos = nx.kamada_kawai_layout(G,dim=2, scale=2.0) 

    # エッジ座標
    edge_x ,edge_y = [],[]
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    # ノード座標と色
    node_x ,node_y ,node_color = [],[],[]
    hover_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x);node_y.append(y)
        node_color.append(pr1[node])
        c = pr1[node]
        node_color.append(c)
        hover_text.append(f'Node {node}<br>Centrality: {c:.4f}')

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='Reds',
            color=node_color,
            size=node_size,
            colorbar=dict(
                thickness=15,
                title='Degree Centrality',
                xanchor='left'
            ),
            line_width=2,
            line_color='gray'
        ),
        text=hover_text
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(

                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                    ))

    return fig

def draw_3Dplot_go(G: nx.Graph,
                   node_size:int =8,
                   layout_type='kamada_kawai',
                   custom_pos: dict = None,
                   custom_centrality: dict = None):
    
    if custom_centrality is None:
        # fallback: サブグラフで再計算
        pr1 = dict(nx.degree_centrality(G))
    else:
        # 全体グラフで計算した値をサブグラフのノードだけ抜き出す
        pr1 = {n: custom_centrality[n] for n in G.nodes()}
    
    
    if custom_pos is not None:
        pos = custom_pos
    else:
        if layout_type == 'spring':
            pos = nx.spring_layout(G, dim=3, iterations=10, scale=2.0)
        else:
            pos = nx.kamada_kawai_layout(G, dim=3, scale=2.0) 
        
    # エッジ座標
    edge_x = []
    edge_y = []
    edge_z = []
    for edge in G.edges():
        x0, y0 ,z0= pos[edge[0]]
        x1, y1 ,z1= pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_z += [z0, z1, None]

    edge_trace = go.Scatter3d(
        x=edge_x, y=edge_y,z=edge_z,
        line=dict(width=1, color='gray'),
        hoverinfo='none',
        mode='lines',
    )

    # ノード座標と色
    node_x, node_y, node_z, node_color = [], [], [], []
    hover_text = []
    for node in G.nodes():
        x,y,z = pos[node]
        node_x.append(x); node_y.append(y); node_z.append(z)
        c = pr1[node]
        node_color.append(c)
        hover_text.append(f'Node {node}<br>Centrality: {c:.4f}')

    node_trace = go.Scatter3d(
        x=node_x, y=node_y,z=node_z,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='Reds',
            color=node_color,
            size=node_size,
            colorbar=dict(
                thickness=15,
                title='Degree Centrality',
                xanchor='left'
            ),
            line_width=2,
            line_color='gray'
        ),
        text=hover_text
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(

                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        
                        scene=dict(
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        zaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                        )
                    ))
    
    return fig