import streamlit as st
from utils import sideber_title

#streamlit run app.py

st.set_page_config(
    page_title="HOME"
    ,layout="centered"
)

sideber_title.sideber_title()

st.title(" _HOME_ 🏠")
st.write("""
          - 発表資料:本日の発表資料
          - ネットワーク保管庫:使用したネットワーク、その可視化、使用したプログラムなど随時追加。
          - アーカイブ: 過去の発表資料を公開。2回目以降から随時追加予定。
         """)

st.divider()

st.header("参考（にしたい）先行研究資料")

st.write("https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2022.823564/full")
st.write("https://www.nature.com/articles/s41598-017-07878-2")
st.write("https://journals.aps.org/pre/abstract/10.1103/PhysRevE.65.056109")
st.write("https://arxiv.org/pdf/1103.1741")


st.header("参考書籍")

st.markdown(
        """
        #### 1. _ネットワーク科学入門_ 
        https://www.maruzen-publishing.co.jp/book/b10123080.html
        #### 2. _ゲーム理論からの社会ネットワーク分析_  (申請中)
        https://www.ohmsha.co.jp/book/9784274230899/

        """
    )




