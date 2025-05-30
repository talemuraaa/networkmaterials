import streamlit as st

from module.network_models.select_model import model_select_ver2
from module.network_models.draw_plot import draw_plot_go
from module.network_models.VIS_network import downloud_adjacency
from module.network_models.VIS_network import net_parameter


def main_analysis(): 
    col1,col2=st.columns([2,3])
    
    with col1:
        G=model_select_ver2()
        
    with col2:

        other_tab=st.checkbox("別タブでネットワークを表示",key='other_tab_check')
        strat=st.button("計算",key='start_button')
        
    col3,col4=st.columns([1,4])
    if (G is not None) and strat:    
        with st.spinner("計算中..."):
            fig=draw_plot_go(G,open_in_new_tab=other_tab,layout_type='community')

            with col4:
                fig.update_layout(width=1200, height=800)
                st.plotly_chart(fig, use_container_width=False)

            with col3:
                net_parameter.net_parameter(G)
        downloud_adjacency.downloud_adjacency_list_button(G)           
    else:
        return

