import streamlit as st
from PIL import Image

st.title("miau de pablitus03")

st.header ("aqui comienza mi historia")
st.write ("confio en que puuedo entender")
image = Image.open('nyan_cat.jpg')

st.image(image, caption= 'interfaces')

texto =st.text_imput('pa pe pi po pu','mia mie mii mio miu')
st.write( 'el texto es', texto)
