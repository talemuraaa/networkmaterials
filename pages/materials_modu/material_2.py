import streamlit as st
from pages.materials_modu.chapter import no2_chapter

def material20255030():

    #ページ頭

    no2_chapter.intro()
    #サイドバー頭

    page=st.sidebar.radio("Chapter",["Chapter0","Chapter1","Chapter2"])
    
    if page == "Chapter0":
        no2_chapter.chapter0()    
    
    elif page == "Chapter1":
        no2_chapter.chapter1()
        
    elif page =="Chapter2":
        no2_chapter.chapter2()
    