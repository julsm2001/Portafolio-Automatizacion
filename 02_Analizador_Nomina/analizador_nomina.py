#Leer archivo .csv
ruta_archivo = r"C:\Users\Julia\Desktop\empleados.csv"

total_sueldos = 0

with open(ruta_archivo, "r") as archivo_abierto:
   
    for linea in archivo_abierto:
        linea = linea.strip()
        datos = linea.split(",")
        nombre = datos[0]
        departamento = datos[1]
        salario = int(datos[2])

        if departamento == "Ventas":
            total_sueldos += salario
print(f"Total gastado en Ventas: {total_sueldos}")