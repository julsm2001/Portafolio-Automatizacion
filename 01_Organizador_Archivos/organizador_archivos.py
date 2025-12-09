import os
import shutil

def organizar_archivos():
    base_path = input("Ingresa la ruta de la carpeta a ordenar: ").strip()

    if not os.path.exists(base_path):
        print(f"Error: La ruta '{base_path}' no existe.")
        return

    archivos = os.listdir(base_path)
    conteo = 0

    print(f"Procesando carpeta: {base_path}...")

    for archivo in archivos:
        ruta_origen = os.path.join(base_path, archivo)

        if not os.path.isfile(ruta_origen):
            continue

        ext = os.path.splitext(archivo)[1].lower()
        carpeta_destino = None

        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            carpeta_destino = "Imagenes"
        elif ext in ['.pdf', '.doc', '.docx', '.xlsx', '.pptx']:
            carpeta_destino = "Documentos"
        elif ext in ['.txt', '.log', '.md']:
            carpeta_destino = "Texto"
        elif ext in ['.exe', '.msi', '.zip', '.rar']:
            carpeta_destino = "Instaladores_Zip"

        if carpeta_destino:
            ruta_destino = os.path.join(base_path, carpeta_destino)
            os.makedirs(ruta_destino, exist_ok=True)
            
            shutil.move(ruta_origen, os.path.join(ruta_destino, archivo))
            print(f"Movido: {archivo} -> {carpeta_destino}")
            conteo += 1

    print(f"Proceso finalizado. Total archivos movidos: {conteo}")

if __name__ == "__main__":
    organizar_archivos()
