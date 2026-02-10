import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.set_page_config(page_title="Inventario", layout="wide")

st.title("Inventario")

data = {
    
    "Dispositivo": ["PC1", "PC2", "Laptop", "Server"],
    "Owner": ["Admin", "JuanLol", "MariaLel", "Root"],
    "IP": ["soy la ip", "soy la ip 2", "soy la ip3", "soy la otra ip"],
    "Status": ["Completo", "COmpletyo", "NO iniciado", "Completo"],
    "Notes": ["Null", "Null", "Null", "Null"]
}

df = pd.DataFrame(data)

#Ver la tabla
st.data_editor(
    df,
    use_container_width=True,
    height=600,
    hide_index=True
)