# 🗺️ treasure_hunt.py - Explicación Línea por Línea

## **Líneas 1-2: Importaciones**
```python
import random
from utils import guardar_resultado
```
- **Línea 1**: Importa el módulo `random` para generar números aleatorios
- **Línea 2**: Importa la función para guardar resultados

## **Líneas 4-6: Función principal**
```python
def juego_busqueda_tesoro(nombre_jugador):
    """Implementa el juego de Búsqueda del Tesoro"""
    print(f"\n¡Hola {nombre_jugador}! Bienvenido a la Búsqueda del Tesoro")
```
- **Línea 4**: Define la función principal del juego
- **Línea 5**: Documentación
- **Línea 6**: Mensaje de bienvenida personalizado

## **Líneas 8-14: Definición de niveles**
```python
    niveles = {
        1: {"nombre": "Fácil", "tamaño": 4, "intentos": 12, "trampas": 0, "penalizacion": 0},
        2: {"nombre": "Intermedio", "tamaño": 5, "intentos": 15, "trampas": 2, "penalizacion": 1},
        3: {"nombre": "Difícil", "tamaño": 6, "intentos": 20, "trampas": 3, "penalizacion": 1},
        4: {"nombre": "Legendario", "tamaño": 8, "intentos": 25, "trampas": 10, "penalizacion": 2}
    }
```
- Diccionario con configuración de cada nivel
- Cada nivel tiene: nombre, tamaño del tablero, intentos máximos, número de trampas y penalización

## **Líneas 16-20: Mostrar niveles disponibles**
```python
    print("\nNiveles disponibles:")
    for nivel, info in niveles.items():
        print(f"{nivel}. {info['nombre']} - Tablero {info['tamaño']}x{info['tamaño']} - {info['intentos']} intentos")
```
- Muestra todas las opciones de nivel disponibles

## **Líneas 22-30: Selección de nivel**
```python
    while True:
        try:
            nivel_elegido = int(input("\nSelecciona un nivel (1-4): "))
            if nivel_elegido in niveles:
                break
            else:
                print("Por favor, selecciona un nivel válido (1-4)")
        except ValueError:
            print("Por favor, ingresa un número válido")
```
- Bucle para obtener una selección válida del usuario
- Maneja errores si el usuario ingresa texto en lugar de números

## **Líneas 32-37: Configuración del nivel**
```python
    nivel = niveles[nivel_elegido]
    tamaño = nivel["tamaño"]
    intentos_max = nivel["intentos"]
    num_trampas = nivel["trampas"]
    penalizacion = nivel["penalizacion"]
```
- Extrae la configuración del nivel seleccionado

## **Línea 39: Crear tablero**
```python
    tablero = [["🟦" for _ in range(tamaño)] for _ in range(tamaño)]
```
- Crea una matriz cuadrada llena de cuadros azules (🟦)

## **Líneas 41-43: Colocar tesoro**
```python
    tesoro_fila = random.randint(0, tamaño-1)
    tesoro_col = random.randint(0, tamaño-1)
```
- Genera coordenadas aleatorias para el tesoro

## **Líneas 45-52: Colocar trampas**
```python
    trampas = []
    for _ in range(num_trampas):
        while True:
            trampa_fila = random.randint(0, tamaño-1)
            trampa_col = random.randint(0, tamaño-1)
            if (trampa_fila, trampa_col) != (tesoro_fila, tesoro_col) and (trampa_fila, trampa_col) not in trampas:
                trampas.append((trampa_fila, trampa_col))
                break
```
- **Línea 45**: Lista vacía para almacenar coordenadas de trampas
- **Línea 46**: Bucle para crear el número de trampas del nivel
- **Líneas 47-52**: Bucle interno para encontrar posición válida para cada trampa
- **Líneas 48-49**: Genera coordenadas aleatorias
- **Línea 50**: Verifica que no esté donde el tesoro y no esté repetida
- **Líneas 51-52**: Añade la trampa y sale del bucle interno

## **Líneas 54-56: Variables de control**
```python
    intentos = 0
    encontrado = False
```
- Contador de intentos y flag para saber si encontró el tesoro

## **Líneas 58-60: Mensaje inicial**
```python
    print(f"\n¡Comienza la búsqueda! Tienes {intentos_max} intentos")
    print(f"Tablero {tamaño}x{tamaño}")
```
- Información inicial del juego

## **Líneas 62-63: Bucle principal**
```python
    while intentos < intentos_max and not encontrado:
```
- Continúa mientras tenga intentos y no haya encontrado el tesoro

## **Líneas 64-72: Mostrar tablero**
```python
        print("\n  ", end="")
        for i in range(tamaño):
            print(f" {i}", end="")
        print()
        
        for i, fila in enumerate(tablero):
            print(f"{i} ", end="")
            for celda in fila:
                print(f"{celda}", end=" ")
            print()
```
- **Líneas 64-67**: Imprime los números de columnas (0, 1, 2, ...)
- **Líneas 69-72**: Imprime cada fila con su número y las celdas

## **Línea 74: Mostrar intentos restantes**
```python
        print(f"\nIntentos restantes: {intentos_max - intentos}")
```

## **Líneas 76-89: Obtener coordenadas del jugador**
```python
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
```
- Bucle para obtener coordenadas válidas
- Verifica que estén en el rango y que no haya sido excavada antes

## **Líneas 91-93: Verificar si encontró el tesoro**
```python
        if fila == tesoro_fila and col == tesoro_col:
            tablero[fila][col] = "💰"
            encontrado = True
            print("\n¡FELICIDADES! ¡Encontraste el tesoro! 🎉")
```
- Si las coordenadas coinciden con el tesoro, marca con 💰 y gana

## **Líneas 94-98: Verificar si cayó en trampa**
```python
        elif (fila, col) in trampas:
            tablero[fila][col] = "💣"
            intentos += penalizacion
            print(f"¡TRAMPA! Pierdes {penalizacion} intento(s) 💥")
```
- Si las coordenadas coinciden con una trampa, marca con 💣 y penaliza

## **Líneas 99-115: Calcular pista de distancia**
```python
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
```
- **Línea 99**: Marca la celda como excavada (❌)
- **Línea 102**: Calcula la distancia Manhattan al tesoro
- **Línea 103**: Calcula la distancia máxima posible
- **Líneas 105-113**: Da pistas según la distancia (muy caliente, caliente, tibio, frío)

## **Línea 115: Incrementar intentos**
```python
        intentos += 1
```

## **Líneas 117-121: Verificar derrota**
```python
    if not encontrado:
        print(f"\n¡Se acabaron los intentos! El tesoro estaba en ({tesoro_fila}, {tesoro_col})")
        tablero[tesoro_fila][tesoro_col] = "💰"
```
- Si se acabaron los intentos, muestra dónde estaba el tesoro

## **Líneas 123-133: Mostrar tablero final**
```python
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
```
- Similar al código anterior, muestra el tablero final completo

## **Líneas 135-137: Guardar resultado y pausa**
```python
    resultado = "ganó" if encontrado else "perdió"
    guardar_resultado(nombre_jugador, "Búsqueda del Tesoro", resultado)
    
    input("\nPresiona Enter para continuar...")
```
- Determina el resultado y lo guarda

## **Conceptos Clave:**

### **1. Diccionarios**
- **niveles = {}**: Estructura de datos clave-valor
- **nivel["tamaño"]**: Acceso a valores del diccionario
- **niveles.items()**: Itera sobre clave y valor

### **2. List Comprehension**
- **["🟦" for _ in range(tamaño)]**: Crea lista con elementos repetidos
- **[[...] for _ in range(tamaño)]**: Crea matriz 2D

### **3. Tuplas**
- **(fila, col)**: Par ordenado de coordenadas
- **in trampas**: Verifica si tupla está en lista

### **4. Matemáticas**
- **abs()**: Valor absoluto
- **//**: División entera
- **random.randint()**: Número aleatorio en rango

### **5. Control de Flujo**
- **while True**: Bucle infinito
- **break**: Sale del bucle
- **continue**: Salta iteración

### **6. Manejo de Errores**
- **try/except**: Captura errores
- **ValueError**: Error de conversión de tipo

### **7. Enumeración**
- **enumerate()**: Itera con índice y valor
- **range()**: Genera secuencia de números

## **Algoritmo del Juego:**
1. Mostrar niveles disponibles
2. Obtener selección del usuario
3. Configurar parámetros del nivel
4. Generar tablero vacío
5. Colocar tesoro aleatoriamente
6. Colocar trampas aleatoriamente
7. Repetir hasta encontrar tesoro o agotar intentos:
   - Mostrar tablero actual
   - Obtener coordenadas del jugador
   - Verificar si encontró tesoro
   - Verificar si cayó en trampa
   - Calcular y mostrar pista de distancia
   - Incrementar contador de intentos
8. Mostrar resultado final
9. Guardar resultado
