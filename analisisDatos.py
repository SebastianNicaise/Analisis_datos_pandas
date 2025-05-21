import pandas as pd #Libreria para analizar datos
import plotly.express as px #Libreria para visualizar los datos y hacerlos interactivos

data= pd.read_excel("ventas.xlsx") 

#Revisión de datos correctos del archivo
print(f"""Datos superiores:
      {data.head()}""")

print(f"""Registros inferiores:
      {data.tail()}""")

print(f"""Cantidad de filas y columnas
      {data.shape}""")


#Visualizar columnas
#print(list(data.columns))

#Crear gráficos en html de la siguiente lista
lista_columnas=["tienda", "Ciudad", "País", "tamaño", "local_consumo"]

for columna in lista_columnas:
    grafico=px.histogram(data, x=columna,
                         y="precio", 
                         text_auto=True,
                         title="Facturación",
                         color="forma_pago")
    
    grafico.show()
    grafico.write_html(f"Facturación_{columna}.html")



