import streamlit as st
import pandas as pd
import net
import db

def show():
    st.write("### Inicio")
    
    dispositivos = db.cargar_tabla_dispositivos()
    fallas_activas = [] #TODO: db.cargar_fallas()

    col_1, col_2 = st.columns([1.5, 1])

    with col_1:
        tab1, tab2 = st.tabs(["Latencia", "Historial de Fallas"])
        
        with tab1:
            data_latencia = pd.DataFrame({
                'Minutos': range(20),
                'Latencia (ms)': [10, 12, 11, 15, 40, 12, 11, 10, 9, 11, 12, 13, 11, 10, 15, 12, 11, 10, 11, 12]
            })
            st.line_chart(data_latencia, x='Minutos', y='Latencia (ms)', color="#00ff00")
        

        with tab2:
            t = st.columns([1, 1])
            with t[0]:
                datos = [
                    [5, 2, 0],
                    [4, 1, 0],
                    [6, 3, 1],
                    [5, 1, 0],
                    [4, 2, 1],
                    [6, 2, 0],
                    [7, 3, 0]
                ]

                df = pd.DataFrame(datos, columns=["Baja", "Media", "Alta"])
                st.bar_chart(df, color=["yellow", "orange", "red"])
            
            with t[1]:
                st.write("**Fallas Recientes**")
                if not fallas_activas:
                    st.success("No hay fallas reportadas actualmente")
                else:
                    df_fallas = pd.DataFrame(fallas_activas)
                    st.dataframe(df_fallas, use_container_width=True, hide_index=True)
    

    with col_2:
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        with col_m1:
            st.metric("Total Equipos", len(dispositivos))
        with col_m2:
            online = len([d for d in dispositivos if d['estado'] == 'ONLINE'])
            st.metric("En Línea", online, delta=f"{online} activos", delta_color="normal")
        with col_m3:
            offline = len(dispositivos) - online
            st.metric("Fuera de Línea", offline, delta=f"-{offline}", delta_color="inverse")
        with col_m4:
            st.metric("Fallas Críticas", len(fallas_activas), delta_color="inverse")


        with st.container(horizontal=True):
            search = st.text_input("...", placeholder="Ej: 192.168...", label_visibility="collapsed")

            if st.button("", icon=":material/radar:", help="Escanear red"):
                s = net.obtener_segmento()
                d = net.escanear_red(s)
                db.actualizar_tabla_dispositivos(d)
                print(f"Se encontraron {len(d)} dispositivos")


        with st.container(height=240, horizontal_alignment="center", border=False):
            if not dispositivos:
                st.image("https://img.icons8.com/?size=100&id=45967&format=png&color=FFFFFF")
                st.markdown("<p style='text-align: center;'>Dispositivos no encontrados</p>", unsafe_allow_html=True)
            else:
                dispositivos_filtrados = [
                    d for d in dispositivos 
                    if search.lower() in d['ip'].lower() or search.lower() in d['nombre'].lower()
                ]

                datos_tabla = []
                for d in dispositivos_filtrados:
                    datos_tabla.append({
                        "Nombre": d['nombre'],
                        "IP": d['ip'],
                        "MAC": d['mac'],
                        "Estado": d['estado']
                    })

                if datos_tabla:
                    df = pd.DataFrame(datos_tabla)
                    st.dataframe(df.style.applymap(color_estado, subset=["Estado"]))


def color_estado(e):
    color = "color: #4CFF50" if e == "ONLINE" else "color: #5A5A5A"
    return f"font-weight: bold; {color}"