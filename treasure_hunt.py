import random
from utils import guardar_resultado

def juego_busqueda_tesoro(nombre_jugador):
    """Implementa el juego de Búsqueda del Tesoro"""
    print(f"\n¡Hola {nombre_jugador}! Bienvenido a la Búsqueda del Tesoro")
    
    # Niveles de dificultad
    niveles = {
        1: {"nombre": "Fácil", "tamaño": 4, "intentos": 12, "trampas": 0, "penalizacion": 0},
        2: {"nombre": "Intermedio", "tamaño": 5, "intentos": 15, "trampas": 2, "penalizacion": 1},
        3: {"nombre": "Difícil", "tamaño": 6, "intentos": 20, "trampas": 3, "penalizacion": 1},
        4: {"nombre": "Legendario", "tamaño": 8, "intentos": 25, "trampas": 10, "penalizacion": 2}
    }
    
    print("\nNiveles disponibles:")
    for nivel, info in niveles.items():
        print(f"{nivel}. {info['nombre']} - Tablero {info['tamaño']}x{info['tamaño']} - {info['intentos']} intentos")
    
    while True:
        try:
            nivel_elegido = int(input("\nSelecciona un nivel (1-4): "))
            if nivel_elegido in niveles:
                break
            else:
                print("Por favor, selecciona un nivel válido (1-4)")
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    nivel = niveles[nivel_elegido]
    tamaño = nivel["tamaño"]
    intentos_max = nivel["intentos"]
    num_trampas = nivel["trampas"]
    penalizacion = nivel["penalizacion"]
    
    # Generar tablero
    tablero = [["🟦" for _ in range(tamaño)] for _ in range(tamaño)]
    
    # Colocar tesoro
    tesoro_fila = random.randint(0, tamaño-1)
    tesoro_col = random.randint(0, tamaño-1)
    
    # Colocar trampas
    trampas = []
    for _ in range(num_trampas):
        while True:
            trampa_fila = random.randint(0, tamaño-1)
            trampa_col = random.randint(0, tamaño-1)
            if (trampa_fila, trampa_col) != (tesoro_fila, tesoro_col) and (trampa_fila, trampa_col) not in trampas:
                trampas.append((trampa_fila, trampa_col))
                break
    
    intentos = 0
    encontrado = False
    
    print(f"\n¡Comienza la búsqueda! Tienes {intentos_max} intentos")
    print(f"Tablero {tamaño}x{tamaño}")
    
    while intentos < intentos_max and not encontrado:
        # Mostrar tablero
        print("\n  ", end="")
        for i in range(tamaño):
            print(f" {i}", end="")
        print()
        
        for i, fila in enumerate(tablero):
            print(f"{i} ", end="")
            for celda in fila:
                print(f"{celda}", end=" ")
            print()
        
        print(f"\nIntentos restantes: {intentos_max - intentos}")
        
        # Pedir coordenadas
        while True:
            try:
                fila = int(input(f"Ingresa la fila (0-{tamaño-1}): "))
                col = int(input(f"Ingresa la columna (0-{tamaño-1}): "))
                
                if 0 <= fila < tamaño and 0 <= col < tamaño:
                    if tablero[fila][col] == "🟦":
                        break
                    else:
                        print("Ya excavaste en esa posición. Intenta otra.")
                else:
                    print("Coordenadas fuera del rango. Intenta de nuevo.")
            except ValueError:
                print("Por favor, ingresa números válidos")
        
        # Verificar resultado
        if fila == tesoro_fila and col == tesoro_col:
            tablero[fila][col] = "💰"
            encontrado = True
            print("\n¡FELICIDADES! ¡Encontraste el tesoro! 🎉")
        elif (fila, col) in trampas:
            tablero[fila][col] = "💣"
            intentos += penalizacion
            print(f"¡TRAMPA! Pierdes {penalizacion} intento(s) 💥")
        else:
            tablero[fila][col] = "❌"
            
            # Calcular distancia
            distancia = abs(fila - tesoro_fila) + abs(col - tesoro_col)
            distancia_max = (tamaño - 1) * 2
            
            if distancia <= 2:
                print("¡MUY CALIENTE! 🔥")
            elif distancia <= distancia_max // 3:
                print("¡CALIENTE! 🌡️")
            elif distancia <= distancia_max // 2:
                print("¡TIBIO! 🌤️")
            else:
                print("¡FRÍO! ❄️")
        
        intentos += 1
    
    if not encontrado:
        print(f"\n¡Se acabaron los intentos! El tesoro estaba en ({tesoro_fila}, {tesoro_col})")
        tablero[tesoro_fila][tesoro_col] = "💰"
    
    # Mostrar tablero final
    print("\nTablero final:")
    print("  ", end="")
    for i in range(tamaño):
        print(f" {i}", end="")
    print()
    
    for i, fila in enumerate(tablero):
        print(f"{i} ", end="")
        for celda in fila:
            print(f"{celda}", end=" ")
        print()
    
    resultado = "ganó" if encontrado else "perdió"
    guardar_resultado(nombre_jugador, "Búsqueda del Tesoro", resultado)
    
    input("\nPresiona Enter para continuar...")