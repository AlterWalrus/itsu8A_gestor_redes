import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Administrador", layout="wide")

col1, col2 = st.columns([1, 1.3])

with col1:
    st.subheader("Subir archivo")

    archivo = st.file_uploader("file", label_visibility='hidden')

    if archivo and st.button("Subir archivo"):
        upload_path = Path("uploads")
        upload_path.mkdir(exist_ok=True)

        with open(upload_path / archivo.name, "wb") as f:
            f.write(archivo.getbuffer())

        st.success("Archivo subido correctamente")
        st.rerun()

with col2:
    st.subheader("Archivos disponibles")

    upload_path = Path("uploads")
    upload_path.mkdir(exist_ok=True)
    archivos = list(upload_path.iterdir())

    if not archivos:
        st.info("No hay archivos subidos")
    else:
        for archivo in archivos:
            col_file, col_download, col_delete = st.columns([6, 1, 1])

            with col_file:
                st.write(f"{archivo.name}")

            with col_download:
                st.download_button(
                    "⬇",
                    archivo.read_bytes(),
                    file_name=archivo.name,
                    key=f"down_{archivo.name}"
                )

            with col_delete:
                if st.button("x", key=f"del_{archivo.name}"):
                    archivo.unlink()
                    st.rerun()
