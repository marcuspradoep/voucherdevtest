import streamlit as st
nome=st.text_input("digite seu nome: ")
st.write(f"bem vindo: {nome}")

a= st.number_input("Etanol")
b= st.number_input("Gasolina")
if a>=b*0.70:
    st.write("Compensa Gasolina")
else:
    st.write("Compensa Etanol")
