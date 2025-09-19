import pandas as pd
import plotly.express as px
import streamlit as st

# Lee los datos del archivo CSV.
# El archivo 'vehicles_us.csv' debe estar en el mismo directorio.
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encuentra en el directorio del proyecto.")
    st.stop()

# Encabezado principal de la aplicación
st.header('Análisis Exploratorio de Datos del Mercado de Autos Usados')

# Botón para construir un histograma
hist_button = st.button('Construir Histograma')

if hist_button:
    # Escribe un mensaje en la pantalla
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches.')
    
    # Crea el histograma de la distribución de precios
    fig = px.histogram(car_data, x="price", title='Distribución de Precios de Vehículos')
    
    # Muestra el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir Gráfico de Dispersión')

if scatter_button:
    # Escribe un mensaje en la pantalla
    st.write('Creando un gráfico de dispersión de precio vs. kilometraje.')

    # Crea el gráfico de dispersión de precio vs. kilometraje
    fig = px.scatter(car_data, x="odometer", y="price", title='Precio vs. Kilometraje')

    # Muestra el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

