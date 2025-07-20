from treasure_hunt import juego_busqueda_tesoro
from lottery import juego_loteria

def mostrar_menu():
    """Muestra el menú principal del juego"""
    print("\n" + "="*50)
    print("    BIENVENIDO A LA BIBLIOTECA DE JUEGOS")
    print("="*50)
    print("1. Búsqueda del Tesoro")
    print("2. Lotería Interactiva")
    print("3. Salir")
    print("-"*50)

def main():
    """Función principal del programa"""
    print("¡Bienvenido al Sistema de Juegos!")
    
    nombre = input("Por favor, ingresa tu nombre: ").strip()
    if not nombre:
        nombre = "Jugador"
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-3): "))
            
            if opcion == 1:
                juego_busqueda_tesoro(nombre)
            elif opcion == 2:
                juego_loteria(nombre)
            elif opcion == 3:
                print(f"\n¡Gracias por jugar, {nombre}! Hasta la próxima 👋")
                break
            else:
                print("Por favor, selecciona una opción válida (1-3)")
        except ValueError:
            print("Por favor, ingresa un número válido")

if __name__ == "__main__":
    main()