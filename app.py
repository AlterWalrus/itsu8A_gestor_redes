import streamlit as st
import db
import log
import usuario
import inicio
import inve
import arch

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
        
        header {
            visibility: hidden;
            height: 0px;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="redes", layout="wide")
db.inicializar_db()

if "page" not in st.session_state:
    st.session_state.page = "inicio"

if log.login():
    with st.container(border=True, horizontal=True):
        if st.button("Inicio", icon=":material/home:"):
            st.session_state.page = "inicio"

        if st.button("Inventario", icon=":material/dataset:"):
            st.session_state.page = "invent"
        
        if st.button("Configuraciones", icon=":material/settings:"):
            st.session_state.page = "config"
        
        if st.button("Planes", icon=":material/task:"):
            st.session_state.page = "planes"

        st.space("stretch")

        if st.button("Perfil", icon=":material/account_circle:"):
            usuario.configurar_usuario()

        if st.button("", icon=":material/logout:", help="Cerrar sesión"):
            st.session_state.autenticado = False
            st.rerun()
    

    if st.session_state.page == "inicio":
        inicio.show()
    elif st.session_state.page == "invent":
        inve.show()
    elif st.session_state.page == "config":
        arch.show("Configuracion")
    elif st.session_state.page == "planes":
        arch.show("Plan")