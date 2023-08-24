import streamlit as st
from PIL import Image

st.title("miau de pablitus03")

st.header ("aqui comienza mi historia")
st.write ("confio en que puuedo entender")
image = Image.open('nyan_cat.jpg')

st.image(image, caption= 'interfaces')

texto =st.text_input('eres libre de escribir','mia mie mii mio miu')
st.write( 'el texto es', texto)

st.subheader ("xX   .......... vienen 2 columnas ..........   Xx")

col1, col2 = st.columns(2)

with col1:
  st.subheader ("soy la primera")
  st.write("si soy la primera")
  resp = st.checkbox ('de acuerdo')
  if resp:
    st.write('sip')

with col2:
  st.subheader ("this is the remix")
  modo = st.radio ("tu interfaz es", ('visual','auditiva','touch'))
  if modo == 'visual':
    st.write (" menos mal, ya me preocuparia si escribieras sin ver")
    
  if modo == 'auditiva':
      st.write ("tenemos orejas que alegria")
    
  if modo == 'touch':
    st.write (" ve a abrasar un arbol, llevas mucho aqui sentado")

st.subheader ("NOOOOO,MIS BOTONES DE GOMITA")
if st.button ('press start'):
  st.write ('player n1, ready')

else:
  st.write ('exit?')

st.subheader("hoy quiero...")
in_mod = st.selectbox(
  " que llevas el dia de hoy",
  ("pizza","anvorguesa","niños con queso y tocineta"),
)

if in_mod == "pizza":
  set_mod = "en la michi pizzeria todo se amaza a patita"

elif in_mod == "anvorguesa":
  set_mod = " para pa pa paaaaa"

elif in_mod == "niños con queso y tocineta":
  set_mod = "sale un niño especialllll"

st.write (" 3, 2, 1", set_mod)

with st.sidebar:
  st.subheader ("configuara el termino")
  mod_radio = st.radio(
    "escoge tu color";
  ('rosadito', 'cafe','mejor pide un carbon')
  )
