


import streamlit as st


st.header('CALCULADORA de IMC')


n1  = st.number_input('Peso' , value=0.0)
n2  = st.number_input('Altura ')



if st.button('Calcular'):
   Dividir =  n1 / n2 ** 2
   st.header(round(Dividir,2))

