# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *

Configurar_Pagina("Exemplo 1", 
                    "amplo", 
                    "auto", 
                    "https://docs.streamlit.io", 
                    "mailto:informacoes.actsp@gmail.com", 
                    "ACT - Soluções para Pessoas. Você pode usar formatação Markdown para adicionar informações neste espaço. Para mais informações acesse *https://www.markdownguide.org*",
                    "©️")

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Mariana, a princesa das amazonas")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("A mulher mais linda desse mundo")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Uma mulher guerreira que não teme a nada, tem a coragem de um leão, a sabedoria de uma coruja e o carinho de uma gatinha (toda dengosa)")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Em muitos momentos pode tirar a sua paciência, mas independente de qualquer situação sempre está do seu lado, não consigo imaginar como seria a vida sem ela. Dona de um sorriso tão lindo que ilumina toda a noite, deusa de um corpo tão gostoso que é impossivel não se apaixonar!! Te amo demais vidinha!!")

Divisor()
    
coluna1 = Colunas(3)
with coluna1[0]:
  Escrever("")
with coluna1[1]:
  Escrever("O que você mais gosta do Jorgera?", "titulo")
  nome = Ler(rotulo = "Passa a visão:", nmax=30, tipo="padrao", info="Inserção de Nome", autocompletar=None, na_mudanca=None, args=None, kwargs=None, placeholder="Jorgera é um gostoso", desabilitada="falso", visibilidade="visivel")
  if nome:     
    Escrever("Você tem razão, ele é sensacional!!")
with coluna1[2]:
  Escrever("")
