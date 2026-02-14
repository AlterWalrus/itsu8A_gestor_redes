import streamlit as st
import pandas as pd
import db

def show():
    st.write("### Inicio")
    
    dispositivos = []#db.obtener_todos_dispositivos()
    fallas_activas = []#db.obtener_fallas_abiertas()

    col_1, col_2 = st.columns([1.5, 1])

    with col_1:
        tab1, tab2 = st.tabs(["Latencia (ms)", "Histórico de Fallas"])
        
        
        with tab1:
            data_latencia = pd.DataFrame({
                'Minutos': range(20),
                'Router Principal': [10, 12, 11, 15, 40, 12, 11, 10, 9, 11, 12, 13, 11, 10, 15, 12, 11, 10, 11, 12]
            })
            st.line_chart(data_latencia, x='Minutos', y='Router Principal', color="#00ff00")
        

        with tab2:
            t21, t22 = st.columns([1, 1])
            with t21:
                st.info("TODO: grafico de fallas por días")
            
            with t22:
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
            online = len([d for d in dispositivos if d['estado'] == 'Online'])
            st.metric("En Línea", online, delta=f"{online} activos", delta_color="normal")
        with col_m3:
            offline = len(dispositivos) - online
            st.metric("Fuera de Línea", offline, delta=f"-{offline}", delta_color="inverse")
        with col_m4:
            st.metric("Fallas Críticas", len(fallas_activas), delta_color="inverse")

        search = st.text_input("...", placeholder="Ej: 192.168...", label_visibility="hidden")
        


        with st.container(height=240, horizontal_alignment="center", border=True):
            if not dispositivos:
                st.image("https://img.icons8.com/?size=100&id=45967&format=png&color=FFFFFF")
                st.markdown("<p style='text-align: center;'>Dispositivos no encontrados</p>", unsafe_allow_html=True)
            else:
                for d in dispositivos:
                    if search.lower() in d['ip'].lower() or search.lower() in d['nombre'].lower():
                        status_color = "green" if d['estado'] == 'Online' else "red"
                        st.markdown(f"""
                        **{d['nombre']}** `{d['ip']}` | {d['tipo']} | <span style='color:{status_color}'>● {d['estado']}</span>  
                        *Ubicación: {d['ubicacion']}*
                        ---
                        """, unsafe_allow_html=True)
    