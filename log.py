import streamlit as st
import db

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
        center_container = center.container(border=True)
        
        with center_container:
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                st.image("https://img.icons8.com/?size=132&id=0Z7Zn2Vvq88O&format=png&color=FFFFFF", width=132)

            st.markdown("## Bienvenido")
            
            with st.form("login_form", border=False):
                user_input = "admin"
                pass_input = st.text_input(
                    "pswd", 
                    type="password", 
                    placeholder="Contraseña", 
                    label_visibility="hidden"
                )

                submit_button = st.form_submit_button(
                    "Iniciar Sesión", 
                    icon=":material/login:", 
                    use_container_width=True, 
                    type="primary"
                )
            
            if submit_button:
                if db.verificar_usuario(user_input, pass_input):
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")
            
            if st.button("¿Olvidaste tu contraseña?", use_container_width=True):
                st.info("aun por hacer xD")
                    
        return False
    return True
