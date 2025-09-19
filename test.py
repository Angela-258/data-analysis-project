import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV
data = pd.read_csv('vehicles_us.csv')

# Imprimir las primeras 5 filas del DataFrame para verificar
print(data.head())

# Muestra un resumen de los tipos de datos y los valores no nulos
data.info()