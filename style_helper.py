import streamlit as st

def remover_espacio():
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