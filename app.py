import streamlit as st
import pandas as pd
import log
import db

st.set_page_config(page_title="redes", layout="wide")
db.inicializar_db()

if log.login():
    with st.container(border=True, horizontal=True):
        if st.button("Inventario", icon=":material/dataset:"):
            print("inv")
        
        if st.button("Configuración", icon=":material/settings:"):
            print("config")
        
        if st.button("Planes", icon=":material/task:"):
            print("planes")
        
        if st.button("Cerrar Sesión", icon=":material/logout:"):
            st.session_state.autenticado = False
            st.rerun()
    

    with st.container(horizontal=True):
        with st.container(border=True, horizontal=True):
            df = pd.DataFrame({
                    "t": [1, 2, 4, 3, 4, 3, 4, 5, 2, 1, 12, 12, 2, 11, 2, 7, 6, 7, 8, 5, 4, 3, 1, 2, 4, 3, 4, 3, 4, 5, 2, 1, 12, 12, 2, 11, 2, 7, 6, 7, 8, 5, 4, 3]
                })
            st.line_chart(df, color=(1.0, 0.0, 0.0))
                
            df = pd.DataFrame({
                    "t": [1, 2, 4, 3, 4, 3, 4, 5, 2, 1, 12, 12, 2, 11, 2, 7, 6, 7, 8, 5, 4, 3, 1, 2, 4, 3, 4, 3, 4, 5, 2, 1, 12, 12, 2, 11, 2, 7, 6, 7, 8, 5, 4, 3]
                })
            st.line_chart(df, color=(0.0, 1.0, 0.0))
        
    
        with st.container(border=True, horizontal_alignment="right"):
            st.info("Dispositivos conectados", icon=":material/devices:")
            pass_input = st.text_input("Filtrar", type="default", label_visibility="hidden")
            
            with st.container(height=190):
                lst = ['192.168.12.12 - Device connected via blah blah'] * 12
                for i in lst:
                    st.markdown(i)