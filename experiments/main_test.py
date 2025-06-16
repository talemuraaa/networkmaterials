import streamlit as st
import plotly.io as pio
import networkx as nx

from module.experiments_comp.select_model import model_select_ver3
from module.experiments_comp.draw_plot import draw_3Dplot_go
from module.experiments_comp import net_parameter



def filterd_node(G,degree=0):
    filtered_nodes = [n for n in G.nodes() if G.degree(n) > degree]
    return  G.subgraph(filtered_nodes)

def plot_3d():
    with st.container(height=400):
        col_3,col_4=st.columns([5,2])
        with col_3:
            G = model_select_ver3()

        with col_4:
            if G is None:
                return
            net_parameter.net_parameter(G)
    
    filter_degree = st.slider("次数フィルター", 0,10,key="filter")
    pos_select=st.selectbox("mapping",('spring','kamada_kawai'),key="pos_select")
    
    fig = None 
    
    
    if st.button("3Dオブジェクトを生成",key="gene_3d"):
        with st.spinner("生成中"):
            
            if pos_select == 'spring':
                full_pos = nx.spring_layout(G, dim=3, iterations=10, scale=2.0, seed=42)
            else:
                full_pos = nx.kamada_kawai_layout(G, dim=3, scale=2.0)
        
            full_centrality = dict(nx.degree_centrality(G))
            H = filterd_node(G, filter_degree)
            fixed_pos_H = {n: full_pos[n] for n in H.nodes()}   
            
            fig = draw_3Dplot_go(
                H,
                node_size=5,
                layout_type=pos_select,
                custom_pos=fixed_pos_H,
                custom_centrality=full_centrality
                )        
            fig.update_layout(height=800)
            st.plotly_chart(fig)

        
    if fig is not None:
        
        html_str = pio.to_html(fig, full_html=True, include_plotlyjs='cdn')
        st.download_button(label="HTML",
            data=html_str,
            file_name="3d_sample_graph.html",
            mime="text/html"
        )

    
    
