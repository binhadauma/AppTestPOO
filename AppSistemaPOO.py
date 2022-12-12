#Universidade Estadual Norte Fluminense Darcy Ribeiro
#Disciplina: Programação Orientada a Objeto
#Professora: Annabell Tamariz
#Aluna: Binha Ferraz Dauma
#Descrição do Projeto: Implementação de um sistema de cadastro d eatividades extracurriculares.

#------------------------------------------------------------------------------------------------

import streamlit as st

#Gestão de Banco de Dados
import sqlite3 #Importando Módulo
conn = sqlite3.connect('dataPOO.db') #Conectando Banco de Dados
c = conn.cursor() #acessar Banco

def create_usertable(): #Criar Tabela
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

def add_userdata(username, password): #Adicionar Dados
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))

def login_user(username,password): #Adicionar Dados de Login
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))

def login_user(username,password): #Executar a Chamada dos Dados
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data

def view_all_users(): #Visualizar os Dados
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

conn.commit()  #Salvar no Banco de Dados

#Título Página

st.title("Sistema de Cadastro de Atividades Extracurriculares - CCT - UENF")

#Programa Principal

def main():
    "Login Webpage de Cadastro de Atividades"

    st.header("Cadastro de Atividades Extracurriculares - CCT - UENF")

    menu = ["Inicio", "Entrar", "Cadastro"] #Criação Menu
    choice = st.sidebar.selectbox("Menu", menu)

#Seleção de Páginas

    if choice == "Inicio":
      st.subheader("Pagina Inicial")

    elif choice == "Entrar":
      st.subheader("Entrar")

      username = st.sidebar.text_input("E-mail") #Formulário E-mail
      password = st.sidebar.text_input("Senha", type= 'password') #Formulário Senha
      if st.sidebar.button("Entrar"):
        #create_usertable() #Código para Autenticar o Login
        #result = login_user(username,password)
        #if result:

            st.subheader("Logado como {}".format(username))

            task1, task2, task3 = st.tabs(["Sobre","Cadastrar Atividade", "Atividades Cadastradas"]) #Cria Subpáginas Internas
           #Conteúdo das Subpáginas
            with task1:
                  st.subheader("Sobre o Sistema CAE")
                  st.video("https://www.youtube.com/watch?v=q-26leP5DcE", format="video/mp4" )
                  st.write("O Sistema CAE - Sistema de Cadastro de Atividades Curriculares, pertence ao Centro de Ciância e Tecnologia (CCT) da UENF e tem como objetivo cadastrar as disciplinas das atividades extensionistas requeridas pelo curso.")
                  st.image("https://cc.uenf.br/_next/image?url=%2Fassets%2Flogo-cc.png&w=640&q=75")
            with task2:
                  st.subheader("Cadastre suas Atividades")
                  name = st.text_input("Nome da Atividade")
                  hours_options =st.selectbox("Tempo da atividade em horas",[5,10,20,30,40,50,100,150,200])
                  text = st.text_area("Descrição Breve da Atividade")
                  data = st.file_uploader("Faça o upload do seu certificado")
                  if st.button("Enviar"):
                    create_usertable()
                    add_userdata(new_user,new_password)

            with task3:
             
                  st.subheader("Veja Suas Atividades Cadastradas")

        #else: 
          #st.warning("Senha ou login errado.")
#Criar Página de Cadastro
    elif choice == "Cadastro":
      st.subheader("Página de Cadastro")
      new_user = st.text_input("E-mail")
      new_password = st.text_input("Senha", type='password')
#Interligar os Dados de Cadastro ao Banco
      if st.button("Cadastrar"):
          create_usertable()
          add_userdata(new_user,new_password)
          st.subheader("Você conseguiu criar a conta!")
          st.subheader("Vá para a página de login!")

if __name__ == '__main__':
  main()
