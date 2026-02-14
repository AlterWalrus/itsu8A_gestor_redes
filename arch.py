import streamlit as st
from pathlib import Path
import base64


def mostrar_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


@st.dialog("Vista previa", width="medium")
def modal_preview(archivo_path):
    st.write(f"**Archivo:** {archivo_path.name}")
    extension = archivo_path.suffix.lower()

    if extension == ".pdf":
        mostrar_pdf(archivo_path)
    elif extension in [".txt", ".cfg", ".conf", ".log", ".ini"]:
        try:
            contenido = archivo_path.read_text(encoding="utf-8")
            st.code(contenido, language="bash")
        except Exception as e:
            st.error(f"No se pudo leer el archivo de texto: {e}")
    else:
        st.warning("La previsualización no está disponible para este tipo de archivo")


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

            st.success("Archivo subido correctamente", icon=":material/check:")

    with col2:
        st.space("small")
        upload_path = Path(tipo_archivo + "es")
        upload_path.mkdir(exist_ok=True)
        archivos = list(upload_path.iterdir())

        c = st.container(height=400, horizontal_alignment="center")

        if not archivos:
            c.image("https://img.icons8.com/?size=100&id=45967&format=png&color=FFFFFF")
            c.markdown("<p style='text-align: center;'>Sin archivos subidos</p>", unsafe_allow_html=True)
        else:
            for archivo in archivos:
                cont = c.container(horizontal=True, border=True)
                with cont:
                    st.write(f"{archivo.name}")

                    if st.button("", key=f"view_{archivo.name}", icon=":material/visibility:"):
                        modal_preview(archivo)

                    st.download_button(
                        "",
                        archivo.read_bytes(),
                        file_name=archivo.name,
                        key=f"down_{archivo.name}",
                        icon=":material/download:"
                    )

                    if st.button("", key=f"del_{archivo.name}", icon=":material/delete:",):
                        archivo.unlink()
                        st.rerun()
