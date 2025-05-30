import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def draw_plot_plt(G:nx.Graph):
    fig,ax = plt.subplots([7,6])
    
    pr1 = dict(nx.degree_centrality(G))
    pos1 =nx.kamada_kawai_layout(G)
    ax.draw_networkx_edges(G, pos1,edge_color='Gray')
    ax.draw_networkx_nodes(G, pos1,node_color=list(pr1.values()), cmap=plt.cm.Reds,node_size=120,edgecolors='Gray')

    ax.axis('off')
    ax.tight_layout()
    
    return fig

def draw_plot_go(G: nx.Graph, open_in_new_tab: bool = False, layout_type='kamada_kawai'):
    # 中心性（degree centrality）
    pr1 = dict(nx.degree_centrality(G))
    
    if layout_type == 'spring':
        pos = nx.spring_layout(G)
    elif layout_type == 'circular':
        pos = nx.circular_layout(G)
    elif layout_type == 'shell':
        pos = nx.shell_layout(G)
    elif layout_type == 'spectral':
        pos = nx.spectral_layout(G)
    elif layout_type == 'random':
        pos = nx.random_layout(G)
    else:
        pos = nx.kamada_kawai_layout(G)  # デフォルト

    # エッジ座標
    edge_x = []
    edge_y = []
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
    node_x = []
    node_y = []
    node_color = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_color.append(pr1[node])

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='Reds',
            color=node_color,
            size=12,
            colorbar=dict(
                thickness=15,
                title='Degree Centrality',
                xanchor='left'
            ),
            line_width=2,
            line_color='gray'
        ),
        text=[f'Node {n}<br>Centrality: {pr1[n]:.2f}' for n in G.nodes()]
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(

                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                    ))
    
    if open_in_new_tab:
        fig.show()

    return fig

