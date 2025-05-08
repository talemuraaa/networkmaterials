import streamlit as st
from utils.image_loader import get_image_path

def chapter1():
    st.title("優先的選択モデル")

    


    st.header("_Barabasi-Albert model_ (BAモデル)", divider=True)
    st.write(""" 

            ハブを持つネットワークを再現するためには、あるノードが他のノードよりも有利になる仕組みが必要になる。
            このようなメカニズムの1つが優先的選択（preferential attachment）と呼ばれるもので、簡単に言うと、
            「金持ちはより金持ちに、貧乏人はより貧乏になる」という仕組みのこと。\n
            
            Barabasi-Albert model(BAモデル)は次数に基づく優先的選択を行いネットワークを生成する。
            つまり、次数が高いノードはより多くのリンクを獲得し、さらに次数が大きくなる。
            一方で、次数の低いノードは新しいリンクを獲得できず、次数はほとんど増加しない。\n
            
            ＢＡモデルは以下のように既存のネットワークに新しいノードｉを追加し、その間に優先的選択に基づきリンクを接続する。
            この手順を繰り返すことでネットワークを生成する。
            
                        
                 """)
    
    image_path1 =get_image_path("takemura_01.png")
    st.image(image_path1)
    

    with st.container(border=True):
        
        st.header(" _定式化_　_Barabasi-Albert model_ ", divider=True)
        st.write("""
            
            BAモデルはパラメータN,mを持つ。\n
            $N$ ：最終的なノード数\n
            $m$  ：新しいノードが接続されるリンク数（平均次数を決定）

            BAモデルは $𝑚_0$ 個のノードを持つ完全グラフ$G$からスタートする\n
            
            """)
            
        col1, col2 = st.columns([1, 20])
        with col1:
            st.write("")
        with col2:
            st.write("""
                ステップ１.　新しいノード$i$が$G$に追加され、$ m\leq m_0 $個の新しいリンクが付与される。\n
                ステップ２.　各リンクは古いノード$j$に確率
                     """)  
        st.latex(r'''
        \prod (i\leftrightarrow	j)=
        \frac{k_j}{\sum_{l}(k_j)}
        ''')
        col1, col2 = st.columns([1, 20])
        with col1:
            st.write("")
        with col2:
            st.write("""
                     で接続される。式の分母は$i$を除く全てのノードの次数の和であり、全ての確率の和が$1$になることを示している。
                     """)
            
            st.write("この手順を目的のノード数$N$に達するまで繰り返す。")

  
    
    col1,col2=st.columns([3,5])
    with col1:
        st.write("""
                 右図は実際にBAモデルでネットワークを生成し、可視化した例。
                 今回は$m=3$なので各ノードからは3本以上のリンクが伸びている。
                 リンクが集まり色が濃くなったノード、つまりハブの存在が確認できる。
                 """)
    
    with col2:
        image_path1=get_image_path("BAmodel_VIS.png")
        st.image(image_path1,width=800)      
    
    col1,col2=st.columns([2,5])
    with col1:
        st.write("""
                 $N=1000$のBAモデルの次数分布表。\n
                 生成せたネットワークの次数分布は明らかにべき乗則に従っている。
                 """)
    with col2:
        image_path2 =  get_image_path("BAmodel_2.png")
        st.image(image_path2,width=800)
        
    
    
    with st.container(border=True):
            st.header("BAモデルの限界", divider=True)
            st.write("""
                     
                     BAモデルは次数に基づく優先的選択によりスケールフリー性を再現している。
                     一方でＢＡモデルには以下のような欠点がある。\n
                     - 次数0のノードは次数は増加しない。
                     - 次数分布のパターンが1つしかない。
                     - 最も古いノードがハブになり、新しいノードが次数的に古いノードを超えてハブになれない。
                     - 三角形を作る仕組みがないので、クラスター係数が低い。
                     - 自発的に繋げるリンクの数が固定されている。
                     
                    さらに、このモデルでは新しく追加されたノードは、ネットワーク全体の次数に関する情報を持っている必要がある。\n
                    （新しくコミュニティにやってきた人物が、そのコミュニティの中の全ての交友関係を把握している？）
                    
                     """)
            
    st.write("BAモデルは次数（次数中心性）に基づく優先的選択を行うが、別の中心性に基づいた優先的選択を行うモデルを考えても面白そう？")    
            
       
def chapter2():
    st.title("ランダムウォークモデル")
    st.write("（rwモデルと表記）")
    
    st.divider()
    
    st.header("強い三者閉包の原則")
    st.write("""
            aがb,cと強い繋がり持っているならば、b,cは友達になるか,何れ友達になる可能性が極めて高い。
            この三者閉包を取り入れたモデルの１つであるランダムウォークを紹介する。\n
            アイデアはランダムな繋がりだけではなく、新しい隣接ノードのさらに隣り合ったノードと繋がる。
             """)
    
    image_path = get_image_path("takemura_02.png")
    st.image(image_path)
    
    with st.container(border=True):
        
        st.header(" _定式化_　_random walk model_ ", divider=True)
        st.divider()
        st.write("""
            
            rwモデルはパラメータN,pを持つ。\n
            $N$ ：最終的なノード数\n
            $m$ : 新しいノードが接続されるリンク数\n
            $p$ ：隣接ノードへの接続確率

            rwモデルは $𝑚_0$ 個のノードを持つ完全グラフ$G$からスタートする\n
            
            """)
            
        col1, col2 = st.columns([1, 20])
        with col1:
            st.write("")
        with col2:
            st.write("""
                ステップ１.　新しいノード$i$が$G$に追加され、$ m\leq m_0 $個の新しいリンクが付与される。\n
                ステップ２.　ノード$i$の最初のリンクはランダムに選ばれた古いノード$j$に接続される\n
                ステップ３.　他の各リンクは確率$p$で、$j$の隣接ノードからランダムに接続され、確率$p-1$で、全体からランダムに選ばれた他のノードに接続される。
                     """)  

        st.write("この手順を目的のノード数$N$に達するまで繰り返す。")            
    
    st.header("各特徴量")
    
    image_path =  get_image_path("random_walk_hist1_2.png")
    st.image(image_path)    
    
    st.write("""
             $l=0$の場合は、三角形を閉じる仕組みは一切働かないのでクラスター係数は低い。優先的選択のないBAモデルと考えることもできる。\n
             lの増加に伴い平均経路長、平均クラスター係数がともに増加している。平均経路長は安定しない。""")
    
    
    image_path = get_image_path("random_walk_hist1_1.png")
    st.image(image_path)        
    
    st.write("""ランダムウォークモデルは優先的選択？
             """)
    
    st.write("以上のランダムウォークモデルを踏まえ、別のモデルを考えてみた。")
    
    st.divider()
    st.header("ランダムウォークモデル（別ver）")
    
    st.write("""
             ランダムウォークモデルは、ノード$j$から１ステップのランダムウォークしか行っていない。\n
             なので、ノード$j$から１ステップ以上のランダムウォークを行いそのウォークが通過したノードとノード$i$を接続するモデルを考えてみた。
             """)
    

    image_path = get_image_path("takemura_03.png")
    st.image(image_path,width=1000)

    image_path = get_image_path("takemura_04.png")
    st.image(image_path,width=1000)
    
    with st.container(border=True):
        
        st.header(" _定式化_　_random walk model(別ver)仮称_ ", divider=True)
        st.divider()
        st.write("""
            
            rwモデルはパラメータN,p,lを持つ。\n
            $N$ ：最終的なノード数\n
            $p$ ：隣接ノードへの接続確率\n
            $l$ ：ランダムウォークの最大移動回数

            rwモデルは $𝑚_0$ 個のノードを持つ完全グラフ$G$からスタートする\n
            
            """)
            
        col1, col2 = st.columns([1, 20])
        with col1:
            st.write("")
        with col2:
            st.write("""
                ステップ１.　新しいノード$i$が$G$に追加される\n
                ステップ２.　ノード$i$の最初のリンクはランダムに選ばれた古いノード$j$に接続される\n
                     """)  
            
            col3,col4= st.columns([1, 8])
            with col3:
                st.write("ステップ３.")
            with col4:
                st.write("""
                確率$p$で、$j$からランダムウォークを行う。ウォークは確率$p$でランダムな$i$を除く未到達な
                隣接ノードに移動し、確率$p-1$でウォークを終了する。移動回数が$l$を超える、または移動可能な隣接が無い場合もウォークを終了する。\n
                確率$1-p$で、全体からランダムに選ばれた他のノードに接続される。（ランダムウォークは行わない。）
                         """)        

        st.write("この手順を目的のノード数$N$に達するまで繰り返す。")    
    
    st.write("""
             ウォークが大きくなりすぎる場合に備えて$l$を実装したが、必要性は薄かったかも。
             """)
    
    st.header("各特徴量")
    
    feature1,feature2=st.columns([3,1])
    
    
    with feature2:
        st.write("""
            \n
             pが大きくなれば1度のループで接続するリンク数が増え、クラスター係数は増加すると思ってたけど
             なぜか平均クラスター係数はpが0.8を超えると減少を始める。
             
             """)
   
    
    with feature1:
        image_path = get_image_path("step_RW_hist.png")
        st.image(image_path)
    
        image_path = get_image_path("step_RW_hist2.png")
        st.image(image_path)
        
        
    image_path = get_image_path("step_RW_deg_VIS.png")
    st.image(image_path)            