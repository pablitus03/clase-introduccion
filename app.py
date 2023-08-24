import streamlit as st
from PIL import Image

st.title("miau de pablitus03")

st.header ("aqui comienza mi historia")
st.write ("confio en que puuedo entender")
image = Image.open('nyan_cat.jpg')

st.image(image, caption= 'interfaces')

texto =st.text_input('eres libre de escribir','mia mie mii mio miu')
st.write( 'el texto es', texto)

st.subheader ("vienen 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader ("soy la primera")
  st.write("si soy la primera")
  resp = st.checkbox ('de acuerdo')
  if resp:
    st.write('sip')
