import requests
import json

respuesta = requests.get("https://wttr.in/CDMX?format=j1")
data = respuesta.json()

clima = data['weather'][0]



fecha = "2024-01-15"
print("=== Clima en CDMX ===")
print("Fecha: ", clima["date"])
print("Temperatura promedio: ", clima["avgtempC"], "C")
print("Máxima:", clima['maxtempC'], "°C")
print("Mínima:", clima['mintempC'], "°C")
print("Indice UV: ", clima["uvIndex"])

with open("clima.txt", "w") as f:
    f.write("=== Clima en CDMX ===\n")
    f.write("Fecha: " + clima["date"] + "\n")
    f.write("Temperatura promedio: " + clima["avgtempC"] + "C" + "\n")
    f.write("Máxima:" + clima['maxtempC'] + "°C" + "\n")
    f.write("Mínima:" + clima['mintempC'] + "°C" + "\n")
    f.write("Indice UV: " + clima["uvIndex"] + "\n")






