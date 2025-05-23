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
          - 実験場: 生成したネットワークに対し、アタックなどの実験を行う。(未完成)
          - ネットワーク保管庫:使用したネットワーク、その可視化、使用したプログラムなど随時追加。
          - アーカイブ: 過去の発表資料を公開。2回目以降から随時追加予定。
         """)

st.divider()

with st.container(border=True):
    st.header("更新内容",divider=True)
    st.write("""
            
        #### 実験場\n
        - 新しく「実験場」ページを追加。
        - 任意のモデルの次数分布を表示。同時に異なるネットワークの次数分布の表示も可能。
          
        #### ネットワーク保管庫\n
        - 生成したネットワークから隣接リストをcsvでダウンロードできるように。
          """)

st.write("""
         メモ\n
         クラスター係数、最短経路長のヒストグラムの横軸をNで表示する。
         """)

st.header("参考書籍")
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown(
        """
        #### 1. _ネットワーク科学入門_ 
        #### 2. _ゲーム理論からの社会ネットワーク分析_

        """
    )

with col2:
    st.link_button("link", "https://www.maruzen-publishing.co.jp/book/b10123080.html")
    st.link_button("link", "https://www.ohmsha.co.jp/book/9784274230899/")

st.write("風船")

if st.button("🎈"):
    st.balloons()


