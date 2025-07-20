import random
from utils import guardar_resultado

def juego_loteria(nombre_jugador):
    """Implementa el juego de Lotería Interactiva"""
    print(f"\n¡Hola {nombre_jugador}! Bienvenido a la Lotería Interactiva")
    
    # Cartas de la lotería (simplificado)
    cartas = [
        "🐶 Perro", "🐱 Gato", "🐭 Ratón", "🐹 Hámster", "🐰 Conejo", "🦊 Zorro",
        "🐻 Oso", "🐼 Panda", "🐨 Koala", "🐯 Tigre", "🦁 León", "🐮 Vaca",
        "🐷 Cerdo", "🐸 Rana", "🐵 Mono", "🐔 Gallina", "🐧 Pingüino", "🐦 Pájaro",
        "🦆 Pato", "🦅 Águila", "🦉 Búho", "🦇 Murciélago", "🐺 Lobo", "🐗 Jabalí",
        "🐴 Caballo", "🦄 Unicornio", "🐝 Abeja", "🐛 Gusano", "🦋 Mariposa", "🐌 Caracol",
        "🐞 Mariquita", "🐜 Hormiga", "🦗 Grillo", "🕷️ Araña", "🦂 Escorpión", "🦕 Dinosaurio",
        "🦖 T-Rex", "🐟 Pez", "🐠 Pez tropical", "🐡 Pez globo", "🦈 Tiburón", "🐙 Pulpo",
        "🦑 Calamar", "🦐 Camarón", "🦞 Langosta", "🦀 Cangrejo", "🐚 Caracol marino", "🐢 Tortuga",
        "🐊 Cocodrilo", "🦎 Lagarto", "🐍 Serpiente", "🐉 Dragón", "🦕 Dinosaurio", "🦖 T-Rex"
    ]
    
    # Generar tablero del jugador (4x4)
    tablero_jugador = random.sample(cartas, 16)
    tablero_marcado = [False] * 16
    
    # Barajar el mazo
    mazo = cartas.copy()
    random.shuffle(mazo)
    
    print("\nTu tablero de lotería:")
    for i in range(4):
        for j in range(4):
            idx = i * 4 + j
            marca = "✅" if tablero_marcado[idx] else "⬜"
            print(f"{marca} {tablero_jugador[idx]}", end=" | ")
        print()
    
    cartas_restantes = len(mazo)
    completado = False
    
    print(f"\nComenzamos! Tienes que completar tu tablero antes de que se acaben las cartas.")
    
    while cartas_restantes > 0 and not completado:
        carta_actual = mazo.pop()
        cartas_restantes -= 1
        
        print(f"\n{'='*50}")
        print(f"Carta sorteada: {carta_actual}")
        print(f"Cartas restantes en el mazo: {cartas_restantes}")
        
        # Mostrar tablero actual
        print("\nTu tablero:")
        for i in range(4):
            for j in range(4):
                idx = i * 4 + j
                marca = "✅" if tablero_marcado[idx] else "⬜"
                print(f"{marca} {tablero_jugador[idx]}", end=" | ")
            print()
        
        respuesta = input(f"¿Tienes esta carta en tu tablero? (s/n): ").lower().strip()
        
        if respuesta == 's':
            if carta_actual in tablero_jugador:
                idx = tablero_jugador.index(carta_actual)
                if not tablero_marcado[idx]:
                    tablero_marcado[idx] = True
                    print(f"¡Correcto! Marcando {carta_actual}")
                else:
                    print("¡Ya estaba marcada!")
            else:
                print("¡Esa carta no está en tu tablero!")
        
        # Verificar si completó el tablero
        if all(tablero_marcado):
            completado = True
            break
    
    # Mostrar resultado final
    print(f"\n{'='*50}")
    if completado:
        print("¡FELICIDADES! ¡Completaste tu tablero! 🎉")
        print(f"Te quedaban {cartas_restantes} cartas en el mazo")
        resultado = "ganó"
    else:
        print("¡Se acabaron las cartas del mazo!")
        print("No lograste completar tu tablero 😢")
        resultado = "perdió"
    
    # Mostrar tablero final
    print("\nTu tablero final:")
    for i in range(4):
        for j in range(4):
            idx = i * 4 + j
            marca = "✅" if tablero_marcado[idx] else "❌"
            print(f"{marca} {tablero_jugador[idx]}", end=" | ")
        print()
    
    guardar_resultado(nombre_jugador, "Lotería Interactiva", resultado)
    input("\nPresiona Enter para continuar...")