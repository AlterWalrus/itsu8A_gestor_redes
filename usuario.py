import streamlit as st

@st.dialog("Configuración de usuario")
def configurar_usuario():
    usuario = st.text_input("Nombre de Usuario", placeholder="Usuario", value="Oscar")
    correo = st.text_input("Correo electrónico", placeholder="ejemplo@gmail.com")

    st.divider()

    with st.expander("Cambiar contraseña"):
        contra = st.text_input("Nueva contraseña", type="password", placeholder="****")
    
    with st.container(horizontal=True):
        if st.button("Confirmar", icon=":material/check_circle:", type="primary"):
            st.rerun()
        
        if st.button("Celebrar", icon=":material/celebration:"):
            st.balloons()
    
    