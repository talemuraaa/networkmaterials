import streamlit as st
from module.page_modu.chapter import no1_chapter

def material20250509():


    st.sidebar.divider()    

    #ページ頭

    no1_chapter.intro()
    #サイドバー頭

    page=st.sidebar.radio("Chapter",["Chapter1","Chapter2"])

    if page == "Chapter1":
        no1_chapter.chapter1()
        
    elif page =="Chapter2":
        no1_chapter.chapter2()
