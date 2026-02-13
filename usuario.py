import streamlit as st

@st.dialog("Configuración de usuario")
def configurar_usuario():
    usuario = st.text_input("usr", label_visibility="hidden", placeholder="Usuario")
    contra = st.text_input("pswd", label_visibility="hidden", placeholder="Nueva contraseña")
    correo = st.text_input("mail", label_visibility="hidden", placeholder="ejemplo@gmail.com")
    
    if st.button("Confirmar"):
        st.rerun()
    
    