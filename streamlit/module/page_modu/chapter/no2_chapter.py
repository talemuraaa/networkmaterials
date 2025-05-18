import streamlit as st
from utils.image_loader import get_image_path

def intro():
    st.write("""
             
         ## 第2回（5月?日）
         ### 0.拡張ランダムウォークモデル
         ### 1.中心性
         ### 2.ネットワークに対するアタック
         ### 3.プログラムの話（時間があれば）
         
         """)
    
    st.divider()
    
def chapter0():
    st.header("拡張ランダムウォークモデル")
    
    st.write("""
             前回の発表の残り3分くらいで軽く触れたモデルについていくつか。
             ランダムウォークモデルから着想を得たので、便宜上「拡張ランダムウォークモデル」と呼ぶことにします。
             （頑張って探せば同じモデルは存在しそうだし、正式名称があればそれに修正します。）
             
             このモデルがなかなかいい振る舞いをしてくれるので紹介します。
             
             ＢＡモデルやランダムウォークモデルと違い、接続するノードの数を指定しない。
             つまり新しく追加されたノードは1~lのリンクを得る。その上でネットワーク上の探索により優先的選択効果を持つ。
             
             
             なかなか可能性を感じるのでこのモデルのことも考えていきたい。
             
             """)
    
def chapter1():
    st.header("1.中心性",divider=True)
    st.write("""
             ### 1.1 中心性とは
             
             　ネットワークにおける中心性とは、ネットワーク内でそのノードがどれほど中心的か、あるいは重要であるかを
             示す指標である。後に紹介する「ネットワークに対するのアタック」においても重要な特徴量になる。
             
             
             """)
    st.write("""
             ### 1.2 中心性の種類\n
             
            代表的な中心性には以下のようなものがある。
             
            - 次数中心性(degree centrality)
            - 近接中心性(closenes centrality)
            - 媒介中心性(betweenness centreality)
            - 固有ベクトル中心性(eigenvector centrality)
             """)
    
    st.write("""
             ### 1.3.1 次数中心性(degree centrality)
             """)
    
    st.write("""
             ### 1.3.2 近接中心性(closenes centrality)
             """)

    st.write("""
             ### 1.3.3 媒介中心性(betweenness centreality)
             """)

    st.write("""
             ### 1.3.4 固有ベクトル中心性(eigenvector centrality)
             """)
    
def chapter2():
    st.write("chapter2")