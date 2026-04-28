import os
import shutil

origen = "C:/Users/jorge/Downloads"
destino = "C:/Users/jorge/Documents/chompi"

if not os.path.exists(destino):
        os.makedirs(destino)
        print("Carpeta creada")
        
for archivo in os.listdir(origen):
        if archivo.endswith("webp"):
                shutil.move(origen + "/" + archivo, destino)
