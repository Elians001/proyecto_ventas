# Análisis de Ventas de Productos

import pandas as pd  # Para manejar los datos
import matplotlib.pyplot as plt  # Para generar gráficos

# Cargar los datos desde el archivo CSV
datos = pd.read_csv("ventas_productos.csv", encoding="utf-8")

# Calcular el precio total por producto (Cantidad * Precio)
datos["Total"] = datos["Cantidad"] * datos["Precio"]

# Mostrar los datos con la nueva columna "Total"
print(" Datos de Ventas:")
print(datos)

# Crear un gráfico de barras para visualizar los ingresos por producto
plt.figure(figsize=(8,5))  # Tamaño del gráfico
plt.bar(datos["Producto"], datos["Total"], color="skyblue")  # Crear el gráfico
plt.xlabel("Producto")  # Etiqueta del eje X
plt.ylabel("Total de Ventas ($)")  # Etiqueta del eje Y
plt.title("Total de Ventas por Producto")  # Título del gráfico
plt.xticks(rotation=45)  # Rotar nombres de productos
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Agregar líneas de guía
plt.savefig("ventas_grafico.png")  # Guardar la imagen como PNG
plt.show()  # Mostrar el gráfico
