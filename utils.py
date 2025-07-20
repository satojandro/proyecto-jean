import json
from datetime import datetime

def guardar_resultado(nombre_jugador, juego, resultado):
    """Guarda el resultado del juego en un archivo JSON"""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = {
        "jugador": nombre_jugador,
        "juego": juego,
        "resultado": resultado,
        "fecha": fecha
    }
    
    try:
        with open("resultados_juegos.json", "a") as f:
            f.write(json.dumps(registro) + "\n")
    except:
        pass