import streamlit as st
from utils.image_loader import get_image_path
from module.network_models.select_model import model_select_ver2


code_close='nx.closeness_centrality(G)'
code_between='nx.betweenness_centrality(G)'

def intro():
    st.write("""
             
         ## 第2回（5月30日）
         ### 0.作ったもの紹介と前回の補足
         ### 1.中心性の定義
         ### 2.ネットワークに対するアタック 
         
         修士でのメインテーマです。
         """)
    
    st.divider()
    
def chapter0():
    st.header("0.1 作ったもの紹介",divider=True)
    
    st.write("いろいろ作りました")
    
    with st.container(border=True):
        st.subheader("更新内容",divider="violet")
        st.write("""
                 
                 ネットワーク保管庫
                 - network model のネットワーク可視化ライブラリをplotpyに変更。
                 - network modelで生成したネットワークの隣接リストをcsvでダウンロード可能に。
                 - degree distributionで複数のネットワークの次数分布を表示。
                 - attack on network でネットワークの崩壊をヒストグラムで表示。(chapter2で紹介)
                 - Centrality で中心性を表示。
                 """)
        
    st.header("0.2 前回の補足",divider=True) 
        
    st.subheader("ランダムウォークモデルについて")
    st.write("""
            前回、networkxの中にはランダムウォークモデルに基づいたグラフ生成関数がないと紹介しましたが、普通にありました。  
             """)
    
    st.code('nx.powerlaw_cluster_graph(N, m, p)',language="python")
    
    st.write("""
             色々調べてみると、そもそもランダムウォークモデルではなく、Holme-Kim モデルと呼ぶのが一般的らしいです。
             わざわざ自作のモデルを使う理由もないので全てHolme-Kim modelに置き換えました。
             """) 
    
    image_path=get_image_path("5030_0_1.png")
    st.image(image_path)
        
    st.write("""
             最後に自作モデルと次数分布で戦わせてみたけど完敗でした。
             """)
 
   
def chapter1():
    st.header("1.中心性",divider=True)
    st.write("""
             ### 1.1 中心性とは
             
             　ネットワークにおける中心性とは、ネットワーク内でそのノードがどれほど中心的か、あるいは重要であるかを
             示す指標である。後に紹介する「ネットワークに対するのアタック」においても重要な特徴量になる。
             基本的に中心性は正規化したものを考える。
             
             
             """)
    
    
    st.subheader("1.2.1 次数中心性(degree centrality)")
    st.write("""
             社会敵ネットワークにおいて次数とは、ノード（個人）の次数とは、そのノードと他のノードを結ぶ社会的なリンクの数を意味する。
             次数が高い理由が、人気者なのか権力者なのかはわからないが、何らかの意味で重要なのは間違いない。
            
             あるコミュニティにおける重要人物を推定する場合、次数に着目するのは自然な指標と言える。
             
             例：SNSにおけるインフルエンサー
             """)
    

    
    with st.container(border=True):
        st.subheader("次数中心性$d_i$",divider=  "gray")
        
        st.latex(r'''
            d_{i}=k_{i} 
            \\　
            \\
            \tilde{d_{i}}=\frac{k_{i}}{N}
            ''')
    
    st.code('nx.degree_centrality(G,node)',language='python')
    
    st.subheader("1.2.2 近接中心性(closenes centrality)")
    st.write("""
             あるノードが他の（全ての）ノードにどれだけ近いか、
             つまりどれくらいネットワークの中央にいるかを指標としたものが近接中心性である。
             
             他の全てのノードとの距離が短ければ中心性が高いということになる。
             近接中心性はあるノードと他の全てのノードの距離の総和の単純な逆数として定義される。
             
             例：？
             """)
    with st.container(border=True):
        st.subheader("近接中心性$g_i$",divider=  "gray")
        
        st.latex(r'''
            g_{i}=\frac{1}{\sum_{i\neq j} l_{ij}} 
            
            
            \\　
            \\
            
            \tilde{g_{i}}=(N-1)g_{i} = \frac{N-1}{\sum_{i\neq j} l_{ij}} =
            
            \frac{1}{\frac{\sum_ {i\neq j} l_{ij}}{N-1}} 
            
            ''')
    
    st.code('nx.closeness_centrality(G,node)',language='python')

    st.subheader(" 1.2.3 媒介中心性(betweenness centreality)")
    st.write("""
             あるノードが他の全てのノードのペアの最短経路にどれだけ関与するかを指標としたものが媒介中心性である。
             
             最短経路に多く含まれるノードは媒介中心性が高いということになる。
             また、異なる連結成分を繋ぐ橋の役割を果たすノードは媒介中心性が大きくなる。
             
             例：異なる組織間の情報伝達を担う人物、交通ネットワークにおける主要な交差点。
             """)
    
    with st.container(border=True):
        st.subheader("媒介中心性$b_i$",divider=  "gray")
        st.latex(r'''
                 b_i = \sum_ {h\neq j \neq i } \frac{\sigma _ {hj(i)}}{\sigma _ {hj}}
                 \\　
                 \\
                  \tilde{b_{i}} = \frac{1}{
                    \begin{pmatrix}
                        N-1  \\
                        2 
                    \end{pmatrix}                         
                  } 
                 \sum_ {h\neq j \neq i } \frac{\sigma _ {hj(i)}}{\sigma _ {hj}} 
                 
                 =\sum_ {h\neq j \neq i } \frac{2 \sigma _ {2hj(i)}}{(N-1)(N-2)\sigma _{hj}}
                 ''')
        st.write(r"""
                 
                 $ \sigma_{hj } $ : $h$から$j$までの最短経路の総数
                 
                 $ \sigma_{hj(i)} $ : そのノードのなかでノード$i$を通る最短経路の本数
                 
                 $hj$の最短経路がノード$i$を通る場合 $ \sigma _{hj(i)} =1$、通らない場合 $ \sigma _{hj(i)} =0$
                 
                
                 
                 
                 """)
    
    st.code('nx.betweenness_centrality(G,node)',language='python')
    
def chapter2():
    st.header("2.ネットワークに対するアタック",divider=True)
    # 概要
    st.write("""
             システムの構成要素の一部が故障しても、その機能に影響がない場合、そのシステムは頑健であるという。
             ネットワークの頑健性はどのように定義できるだろうか？
             
             「システムの一部の故障」を「ノード１つの除去」と考えネットワークに帰着させることにする。  
             方法の１つはノードとそのリンクを除去したとき、そのネットワーク内での特徴量にどのような影響がでるかを調べることである。
             
             """)
    
    st.subheader("2.1 崩壊度の測定")
    
    st.write("""
             なにかしらの方法に従いネットワークからノードを除去していく過程で、ネットワークは崩壊していく。
             この崩壊はどうしたら測定できるだろうか。
             
             方法の１つとして、ネットワークの「連結性」に着目してネットワークの崩壊を測定してみる。
             
             「ネットワークが連結である」とはある任意のノードから別の任意のノードへ、そのネットワーク上で互いに到達可能であるということ。
             逆にネットワークが連結でないならば、連結成分が2つ以上ある状態で、異なる連結成分間の任意のノードでは互い到達可能ではない。
                          
            例えば各ノードが相互に通信を行うシステム（ネットワーク）があったとして、連結正が維持されていれば、ある程度は問題なくシステムは動作する。一方で、バラバラに切断されるということは
            システムの機能を損なう深刻なダメージを意味する。
                          
             
            
             """)
    with st.container(border=True):
        
        st.subheader("$崩壊度S$",divider="violet")
        st.write("ネットワークの崩壊度を、ネットワークの最大連結成分と攻撃前のネットワークのサイズの割合$S$として定義する。 ")
        st.latex(r'''
                
                S=\frac{C_{max}}{N} 
                
                ''')
        
        st.write("""
                
                $C_{max}$ : 最大連結成分のサイズ  
                $N$ : 初期状態のネットワークのサイズ
                
                """)
    st.write("""
             除去するノードの割合が１に近付くと、僅かに残ったノードは小さな連結成分に分散する可能性
             が高く、$S$の値は0に
             近付く。
             """)
        
    st.subheader("2.2.1 ネットワークへのアタック")
    st.write("""
             2.1ではネットワークの崩壊度を定義した。次に具体的なノードの除去戦略を紹介する。  
             
             ランダム障害(random failures) : ランダムにノードを１つ除去する。

             標的型攻撃(targeted attack) : 全てのノードの中心性を計算し、その降順にノードを除去する。
                        
             """)
    
    
    
    
    # このへんにサンプル画像    
    st.subheader("2.2.2 中心性再計算の必要性")
    st.write("""
             あるネットワーク内の各ノードの中心性は、適当なノードを１つ削除した後でも変化しないか？
             一番単純な次数中心性で考えてみる。
             
             あるノード$i$の隣接ノードを削除したとき、そのノードの次数は１下がる。つまり次数中心性$d_i$も正規化された値だけ減少する。
             
             他の中心性でも同じ議論が行える。
             
             以下は次数中心性に従いノードを除去する例。
             
             """)
    
    slide1=get_image_path("slide_2(3).png")
    slide2=get_image_path("slide_2(2).png")
    slide3=get_image_path("slide_2(1).png")
    st.image(slide2)
    st.image(slide1)
    st.image(slide3)
    st.write("""
             初期状態の次数中心性の大きさは$d_D$ > $d_A$ = $d_B$ = $d_C$ > $d_E$ > $d_G$        
             再計算を伴わない場合の削除の順序の例はD,A,B,F,C,E,G

             ノードを削除する度に中心性を再計算した場合の順序はD,F,E,A,B,C,G
             
             """)   
    
    #ここでスライド
    
    
    st.write("""
             近接中心性、媒介中心性でも同じことが言える。
             
             
             では再計算を行う場合と行わない場合で、ネットワークの崩壊の仕方は変わるだろうか？
             
             実際にpythonで再計算を行う場合と行わない場合の比較実験を、2種類のモデルに対して各中心性で行った。     
             """)
    
    st.subheader("_ランダムネットワークモデル_")
    tab1,tab2,tab3=st.tabs(["degree","closeness","betweenness"])
    
    with tab1:
        compare_d = get_image_path("degree_centrality_compare_in_random.png")
        st.image(compare_d)
    with tab2:    
        compare_c = get_image_path("degree_closeness_compare_in_random.png")
        st.image(compare_c)    
    with tab3:
        compare_b = get_image_path("degree_betweennesss_compare_in_random.png")
        st.image(compare_b)    
    
    st.subheader("_BAモデル_")
    tab1,tab2,tab3=st.tabs(["degree","closeness","betweenness"])
    
    with tab1:
        compare_d = get_image_path("degree_centrality_compare.png")
        st.image(compare_d)
    with tab2:    
        compare_c = get_image_path("degree_closeness_compare.png")
        st.image(compare_c)    
    with tab3:
        compare_b = get_image_path("degree_betweennesss_compare.png")
        st.image(compare_b)
        
    st.write("""
            初期状態の中心性に従いノードを除去するよりも、ノードを除去するごとに中心性を再計算したアタックの方が
            効率的に崩壊に引き起こしていることがわかる。
                """)
        
    st.write("""
             一方で、再計算を行う場合はループ処理で$N$回「全ノードの中心性を計算」を行うことになるので、
             計算コストはネットワークのサイズが大きいほど大きくなる。     
            （局所的な再計算は難しいらしい？）
             
             以上の実験を踏まえ、明言しない限り以降の標的型攻撃は中心性の再計算を行うものとする。
             """)

    
    # 再計算を伴う標的型攻撃と伴わない標的型攻撃を実際に比較し、それぞれ評価していく。
    st.subheader("2.2.3 pythonを用いたシュミレーション例")
    
    tab1, tab2, tab3,tab4 = st.tabs(["random network model", "watts-strogatz model", 
                                     "Barabasi-Albert model","random walk model"])

    with tab1:
        st.subheader("random network model(P=0.3)")
        image=get_image_path("rdmodel_attack_0530.png")
        st.image(image)
    with tab2:        
        st.subheader("watts-strogatz model(k=5,p=0.3)") 
        image=get_image_path("wsmodel_k5p3_attack.png")
        st.image(image)
    with tab3:
        st.subheader("Barabasi-Albert model(m=5)")    
        image=get_image_path("bamodel_m5_attack_0530.png")
        st.image(image)
    with tab4:
        st.subheader("random walk model(m=5,p=0.5)")     
        image=get_image_path("rwmodel_m5p5_attack.png")
        st.image(image)
        
    st.write("""
             リンクの張り方に特徴がないランダムネットワークモデルは、明らかに攻撃に耐性がある。
             
             それ以外のモデルでは
             betweenness、closeness、betweenness
             の順番で完全に崩壊している。
             
              
             パラメータや特徴量を考慮した実験は次回以降で。
             """)
    st.write("「ネットワーク保管個」→ 「Attack on network」で実験可。")
        
    
    # まともな実験は次回以降で！今回はお試し実験だけ！
    st.subheader("2.2.4 ロバストネス指標")
    
    st.write("""ここまで紹介してきた崩壊度$S$はどれくらい崩壊しているかの指標であり、
             そのネットワークの頑健性そのものを示す指標ではない。""")
    
    with st.container(border=True):
        st.subheader("ロバストネス(robustness)指標$R$",divider="violet")
        st.write("あるネットワークの頑健性(robustness)を以下のように定義する。")
        
        st.latex(r'''
        
        R=\frac{1}{N} \sum_{Q=1}^N S(Q)
        
        ''') 
        
        st.write("""
                 $S(Q)$ :$Q$番目のノードを除去した後の崩壊度  
                 $N$ : 初期状態のネットワークのサイズ
                 """)
        
    st.write("""
             つまり、頑健性$R$は各段階の崩壊度$S$の和をノード数$N$で正規化したものである。        
             （崩壊度曲線の曲線下面積と似てる）       
             $R$が大きければ攻撃耐性が高く、完全グラフに対して最大値$0.5$を取る。
             逆にスターグラフに対して、最小値$1/{N}$を取る。
             
             これにより、異なるネットワーク間で攻撃耐性を比較することができる。
             
             ロバストネス指標は「ネットワーク保管個」→ 「Attack on network」で実装済み。
             
             """)
    # わざわざノードが１つになるまで破壊しつくす必要はある？なにがわかればネットワークを破壊し終えた、と判断できる？
    st.subheader("次回以降の予定",divider=True)
    st.write("""
             - 頑健性に関するなにかしらの実験
             
             （以下はやりたいことリストだと思ってください。順不同）           
             
             - 直径による崩壊の評価
             - パーコレーション概要　→　モロイ・リード基準とその導出　→　臨界しきい値の導出
             - 連鎖破綻のモデリングと実験
             - 固有ベクトル中心性の導入
             - 次数相関に関する議論


             """)

