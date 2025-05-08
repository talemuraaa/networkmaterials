import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random as rd
from pages.chapter import no1_page

st.set_page_config(
    page_title="MATERIAL" ,
    layout="centered"
)

with st.sidebar:
    st.page_link("app.py",label="HOME",icon="🏠")
    st.page_link("pages/MATERIALS.py",label="発表資料",icon="📖")
    st.page_link("pages/programs.py",label="ネットワーク保管庫",icon="🔨")
    st.page_link("pages/RECORD.py",label="アーカイブ",icon="📚")

st.sidebar.divider()    

#ページ頭

st.title("📖発表資料")
st.divider()

st.write("""
         ## 第一回（5月5日）
         ### 0.作ったもの紹介
         ### 1.BAモデル\n
         ### 2.ランダムウォークモデル
         
         ずっとstreamlitを弄ってたので実験とかはあんまりないです。レイアウトとかディレクトリの構成とかで悩んでました。
         次回は新しい書籍の内容かネットワークへのアタックの話をするかも。
         
         """)
st.divider()
#サイドバー頭

page=st.sidebar.radio("Chapter",["Chapter1","Chapter2"])

if page == "Chapter1":
    no1_page.chapter1()
    
elif page =="Chapter2":
    no1_page.chapter2()


