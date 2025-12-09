import os       # Tu herramienta para manejar el Sistema Operativo
import shutil   # Tu herramienta para mover cosas

# 1. VARIABLES (Nivel 1)
# Definimos dónde va a trabajar el script
# La 'r' al principio es importante en Windows para que lea bien las barras "\"
carpeta_a_ordenar = r"C:\Users\Julia\Desktop\Prueba_Organizador"

# 2. LISTAS (Nivel 4)
# Creamos una lista con todos los nombres de archivos en esa carpeta
archivos = os.listdir(carpeta_a_ordenar)

# 3. BUCLE (Nivel 5)
# "Para cada archivo en la lista de archivos..."
for archivo in archivos:
    
    # Obtenemos la ruta completa (ej: C:\Users\...\foto.jpg)
    ruta_completa = os.path.join(carpeta_a_ordenar, archivo)
    
    # Verificamos que sea un archivo y no una carpeta (para no mover carpetas)
    if os.path.isfile(ruta_completa):
        
        # 4. DECISIONES (Nivel 3)
        # Aquí definimos a dónde va cada cosa
        carpeta_destino = "" # Empezamos con la variable vacía

        if archivo.endswith(".jpg"):
            carpeta_destino = "Imagenes"
        elif archivo.endswith(".pdf"):
            carpeta_destino = "Documentos"
        elif archivo.endswith(".txt"):
            carpeta_destino = "Texto"
        else:
            # Si es otro tipo de archivo, no hacemos nada y pasamos al siguiente
            continue 
        
        # 5. CREAR CARPETA
        # Calculamos la ruta de la carpeta destino (ej: ...\Prueba\Imagenes)
        ruta_carpeta_nueva = os.path.join(carpeta_a_ordenar, carpeta_destino)
        
        # Si la carpeta no existe, la creamos (exist_ok=True evita errores si ya existe)
        os.makedirs(ruta_carpeta_nueva, exist_ok=True)
        
        # 6. FUNCIONES (Nivel 7)
        # Usamos la función move() para trasladar el archivo
        shutil.move(ruta_completa, ruta_carpeta_nueva)
        
        # Feedback para el usuario
        print(f"Movido: {archivo} --> {carpeta_destino}")

print("--------------------------------")
print(f"¡Listo! Se organizaron los archivos en: {carpeta_a_ordenar}")