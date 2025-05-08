import streamlit as st
import os



#streamlit run app.py

st.set_page_config(
    page_title="HOME"
    ,layout="centered"
)

with st.sidebar:
    st.page_link("app.py",label="HOME",icon="🏠")
    st.page_link("pages/MATERIALS.py",label="発表資料",icon="📖")
    st.page_link("pages/programs.py",label="ネットワーク保管庫",icon="🔨")
    st.page_link("pages/RECORD.py",label="アーカイブ",icon="📚")

st.sidebar.divider()

st.title(" _HOME_ 🏠")
st.write("""
          - 発表資料:本日の発表資料
          - ネットワーク保管庫:使用したネットワーク、その可視化、使用したプログラムなど随時追加。
          - アーカイブ: 過去の発表資料を公開。2回目以降から随時追加予定。
         """)

st.divider()

st.header("参考書籍")
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown(
        """
        #### 1. _ネットワーク理論入門_ 
        #### 2. _ゲーム理論からの社会ネットワーク分析_

        """
    )

with col2:
    st.link_button("link", "https://www.maruzen-publishing.co.jp/book/b10123080.html")
    st.link_button("link", "https://www.ohmsha.co.jp/book/9784274230899/")
 
st.write("風船")

if st.button("🎈"):
    st.balloons()


