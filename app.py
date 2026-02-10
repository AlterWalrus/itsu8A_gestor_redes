import streamlit as st
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
            pass_input = center_container.text_input("", type="password", placeholder="Contraseña")
            
            if center_container.button("Iniciar Sesión", use_container_width=True):
                if db.verificar_usuario(user_input, pass_input):
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")
            
            center_container.button("¿Olvidaste tu contraseña?", use_container_width=True)
                    
        return False
    return True



if login():
    st.title("Admin")
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

    
    