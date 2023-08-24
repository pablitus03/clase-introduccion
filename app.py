import streamlit as st
from PIL import image

st.title("miau de pablitus03")

st.header ("aqui comienza mi historia")
st.write ("confio en que puuedo entender")
image = image.open("nyan_cat.jpg")

st.image(image, caption="interfaces")
