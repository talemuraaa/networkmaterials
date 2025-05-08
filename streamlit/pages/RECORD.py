import streamlit as st

st.set_page_config(
    page_title="archive"
    ,layout="centered"
)

with st.sidebar:
    st.page_link("app.py",label="HOME",icon="🏠")
    st.page_link("pages/MATERIALS.py",label="発表資料",icon="📖")
    st.page_link("pages/programs.py",label="ネットワーク保管庫",icon="🔨")
    st.page_link("pages/RECORD.py",label="アーカイブ",icon="📚")

st.markdown("# 📚発表資料アーカイブ")
st.write("随時追加予定")
st.divider()

def page1():
    st.title("第１回")

def page2():
    st.title("第２回")

page_id=st.selectbox(
    '日付けを選択',
    ['第１回(5/9)'])

if page_id == "第１回":
    page1()
