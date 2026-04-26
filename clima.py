import requests
import json

respuesta = requests.get("https://wttr.in/CDMX?format=j1")
data = respuesta.json()

clima = data['weather'][0]
print(json.dumps(data["weather"][0], indent=4))



fecha = "2024-01-15"
print("=== Clima en CDMX ===")
print("Fecha: ", clima["date"])
print("Temperatura promedio: ", clima["avgtempC"], "C")
print("Máxima:", clima['maxtempC'], "°C")
print("Mínima:", clima['mintempC'], "°C")
print("Indice UV: ", clima["uvIndex"])

