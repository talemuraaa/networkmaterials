import streamlit as st


#サイドバーのページタイトルを日本語で表示する

def sideber_title(): 
    with st.sidebar:
        st.page_link("app.py",label="HOME",icon="🏠")
        st.page_link("pages/experiment.py",label="実験場",icon="🚀")
        st.page_link("pages/programs.py",label="ネットワーク保管庫",icon="🔨")
        st.page_link("pages/MATERIALS.py",label="発表資料",icon="📖")        
        st.page_link("pages/RECORD.py",label="アーカイブ",icon="📚")
    
    st.sidebar.divider()
