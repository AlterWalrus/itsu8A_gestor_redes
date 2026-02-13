import streamlit as st
from pathlib import Path

def show(tipo_archivo):
    st.write("### " + tipo_archivo + "es")

    col1, col2 = st.columns([1, 1.3])

    with col1:
        archivo = st.file_uploader("file", label_visibility='hidden', )

        if archivo and st.button("Subir archivo"):
            upload_path = Path(tipo_archivo + "es")
            upload_path.mkdir(exist_ok=True)

            with open(upload_path / archivo.name, "wb") as f:
                f.write(archivo.getbuffer())

            st.success("Archivo subido correctamente")
            st.rerun()

    with col2:
        st.space("small")
        upload_path = Path(tipo_archivo + "es")
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
                        "",
                        archivo.read_bytes(),
                        file_name=archivo.name,
                        key=f"down_{archivo.name}",
                        icon=":material/download:"
                    )

                with col_delete:
                    if st.button("", key=f"del_{archivo.name}", icon=":material/delete:",):
                        archivo.unlink()
                        st.rerun()
