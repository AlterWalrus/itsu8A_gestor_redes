import streamlit as st
import pandas as pd
import db


st.set_page_config(page_title="redes", layout="wide")
db.inicializar_db()


def login():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if not st.session_state.autenticado:
        st.markdown("""
            <style>
            h1, h2, label {
                color: white !important;
                text-align: center;
            }
            </style>
        """, unsafe_allow_html=True)
        
        col1, center, col3 = st.columns([1, 1, 1])
        center_container = center.container(border=True, height="stretch", vertical_alignment="center")
        
        with center:
            c1, c2, c3 = center_container.columns([1, 2, 1])
            with c2:
                c2.image("https://img.icons8.com/?size=132&id=0Z7Zn2Vvq88O&format=png&color=FFFFFF", width=132)

            center_container.markdown("## Bienvenido")
            
            user_input = "admin"
            pass_input = center_container.text_input("pswd", type="password", placeholder="Contraseña", label_visibility="hidden")
            
            if center_container.button("Iniciar Sesión", use_container_width=True):
                if db.verificar_usuario(user_input, pass_input):
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")
            
            center_container.button("¿Olvidaste tu contraseña?", use_container_width=True)
                    
        return False
    return True



#if login():
if True:
    #st.container(*, border=None, key=None, width="stretch", height="content", horizontal=False, horizontal_alignment="left", vertical_alignment="top", gap="small")
    with st.container(border=True, horizontal=True):
        #st.title("Admin")
        
        
        if st.button("Inventario"):
            print("inv")
        
        if st.button("Configuración"):
            print("config")
        
        if st.button("Planes"):
            print("planes")
        
        if st.button("Cerrar Sesión"):
            st.session_state.autenticado = False
            st.rerun()
    

    with st.container(horizontal=True):
        with st.container(border=True, horizontal=True):
            df = pd.DataFrame(
                {
                    "t": [1, 2, 3, 4, 5, 4, 3, 4, 2, 1, 12, 12, 2, 11, 2, 7, 6, 7, 8, 5, 4, 3]
                }
            )
            st.line_chart(df, color=(1.0, 0.0, 0.0))
                
            df = pd.DataFrame(
                {
                    "t": [1, 2, 3, 4, 5, 4, 3, 4, 2, 1, 12, 12, 2, 11, 2, 7, 6, 7, 8, 5, 4, 3]
                }
            )
            st.line_chart(df, color=(0.0, 1.0, 0.0))
        
    
        with st.container(border=True, horizontal_alignment="right"):
            st.text("Dispositivos")

            pass_input = st.text_input("Filtrar", type="default")
            
            with st.container(height=256):
                lst = ['192.168.12.12 - Device connected via blah blah'] * 12
                for i in lst:
                    st.markdown(i)
            
        
    