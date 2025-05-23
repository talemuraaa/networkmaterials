import streamlit as st
import networkx as nx
from module.network_models.models import models


@st.cache_data
def rd_model(n,p):
    G=nx.gnp_random_graph(n,p)
    return G
@st.cache_data
def ws_model(n,k,p):
    G=nx.watts_strogatz_graph(n,k,p)
    return G
@st.cache_data
def ba_model(n,m):
    G=nx.barabasi_albert_graph(n,m)
    return G
@st.cache_data
def rw_network(n,m,p):
    G=models.random_walk_graph(n,m,p)
    return G
@st.cache_data
def exrw_network(n,p,l=None):
    G=models.step_RW_graph(n,p,l)
    return G
