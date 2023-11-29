import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#Page config
st.set_page_config(page_title="My Portfolio", page_icon=":ringed_planet:", layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#Load Assets

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_ass_0 = load_lottieurl("https://lottie.host/57952b23-870c-4297-accd-a969263b9fad/s16hw389Xz.json")
lottie_ass_1 = load_lottieurl("https://lottie.host/0c0c5913-ab48-4741-8096-8726d2f1d08d/KG4iQ673Ot.json")


#Header Section
with st.container():
    st.subheader("Hi, I'm Kevin!")
    st.title("I am an Attorney and aspiring Developer:rocket:")
    st.write("I use Python:snake: & Rust:crab: to save me from my day job where I eat cheese from the government.")
    

with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)

    with left_col:
        st.header("What I do...")
        st.write("##")
        st.write("* build and test trading Systems: develop and assess trading systems for financial markets, incorporating algorithmic strategies. Utilize coding skills to backtest and optimize algorithms.")
        st.write("* algorithmic trading: apply expertise in algorithmic trading to implement and fine-tune strategies for automated financial trading.")
        st.write("* data analysis with python")
        st.write("* front-end development")
        st.write("* building large language models")

    with right_col:
        st.lottie(lottie_ass_0, height=600, key="coding")


#Projects Section

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    text_col, image_col = st.columns(2)

    with text_col:
        st.subheader("Backtest and Optimise trading strategies with Python")
        st.write("* I debunk all the trading junk you see on youtube by backtesting and optimising trading strategies!")
        st.write("* I use Python and Pandas to pull Cryptocurrency price data and construct a trading strategy!")
        st.write("* After backtesting and verifying the strategy works I then optimise the trading strategy.")
    with image_col:
        st.video("https://www.youtube.com/watch?v=dFJ1Md6GCXQ&t=27s")


#Header Section
with st.container():
    st.write("---")
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.markdown("[Github](https://github.com/KevinHancke)")
        st.markdown("[X | Twitter](https://twitter.com/HanckeKevin)")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/kevin-hancke/)")
