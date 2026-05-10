import schedule
import time

def tarea():
    print("Ejecutando tarea...")

schedule.every(1).minutes.do(tarea)

while True:
    schedule.run_pending()
    time.sleep(1)