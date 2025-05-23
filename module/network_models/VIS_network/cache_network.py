import streamlit as st
import networkx as nx

@st.cache_data
def cache_network(G):
    return G.copy()