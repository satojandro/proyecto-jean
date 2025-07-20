# 🎰 lottery.py - Explicación Línea por Línea

## **Líneas 1-2: Importaciones**
```python
import random
from utils import guardar_resultado
```
- **Línea 1**: Importa el módulo `random` para generar números aleatorios
- **Línea 2**: Importa la función para guardar resultados

## **Líneas 4-6: Función principal**
```python
def juego_loteria(nombre_jugador):
    """Implementa el juego de Lotería Interactiva"""
    print(f"\n¡Hola {nombre_jugador}! Bienvenido a la Lotería Interactiva")
```
- **Línea 4**: Define la función principal del juego
- **Línea 5**: Documentación
- **Línea 6**: Mensaje de bienvenida personalizado

## **Líneas 8-15: Definición de cartas**
```python
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
```
- **Líneas 8-15**: Lista con todas las cartas de la lotería (54 cartas con emojis)

## **Líneas 17-20: Generación del tablero**
```python
    tablero_jugador = random.sample(cartas, 16)
    tablero_marcado = [False] * 16
```
- **Línea 17**: Selecciona 16 cartas aleatorias para el tablero del jugador
- **Línea 18**: Crea una lista de 16 valores `False` para marcar cartas encontradas

## **Líneas 22-24: Preparación del mazo**
```python
    mazo = cartas.copy()
    random.shuffle(mazo)
```
- **Línea 22**: Copia todas las cartas para crear el mazo
- **Línea 23**: Mezcla aleatoriamente el mazo

## **Líneas 25-31: Mostrar tablero inicial**
```python
    print("\nTu tablero de lotería:")
    for i in range(4):
        for j in range(4):
            idx = i * 4 + j
            marca = "✅" if tablero_marcado[idx] else "⬜"
            print(f"{marca} {tablero_jugador[idx]}", end=" | ")
        print()
```
- **Línea 25**: Título del tablero
- **Líneas 26-31**: Bucle anidado para mostrar el tablero 4x4
- **Línea 27**: Bucle para filas (0-3)
- **Línea 28**: Bucle para columnas (0-3)
- **Línea 29**: Calcula el índice en la lista unidimensional
- **Línea 30**: Determina si mostrar ✅ (marcada) o ⬜ (sin marcar)
- **Línea 31**: Imprime la carta con su marca
- **Línea 32**: Salto de línea al final de cada fila

## **Líneas 33-35: Variables de control**
```python
    cartas_restantes = len(mazo)
    completado = False
```
- **Línea 33**: Cuenta cuántas cartas quedan en el mazo
- **Línea 34**: Variable para saber si completó el tablero

## **Líneas 37-38: Instrucciones**
```python
    print(f"\nComenzamos! Tienes que completar tu tablero antes de que se acaben las cartas.")
```
- Explica las reglas del juego

## **Líneas 40-42: Bucle principal del juego**
```python
    while cartas_restantes > 0 and not completado:
        carta_actual = mazo.pop()
        cartas_restantes -= 1
```
- **Línea 40**: Continúa mientras haya cartas y no haya completado
- **Línea 41**: Toma una carta del mazo (la elimina)
- **Línea 42**: Reduce el contador de cartas restantes

## **Líneas 44-47: Mostrar información del turno**
```python
        print(f"\n{'='*50}")
        print(f"Carta sorteada: {carta_actual}")
        print(f"Cartas restantes en el mazo: {cartas_restantes}")
```
- Muestra la carta actual y cuántas quedan

## **Líneas 49-56: Mostrar tablero actual**
```python
        print("\nTu tablero:")
        for i in range(4):
            for j in range(4):
                idx = i * 4 + j
                marca = "✅" if tablero_marcado[idx] else "⬜"
                print(f"{marca} {tablero_jugador[idx]}", end=" | ")
            print()
```
- Similar al código anterior, muestra el tablero actualizado

## **Líneas 58-59: Obtener respuesta del jugador**
```python
        respuesta = input(f"¿Tienes esta carta en tu tablero? (s/n): ").lower().strip()
```
- Pregunta al jugador y normaliza la respuesta

## **Líneas 61-70: Verificar respuesta**
```python
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
```
- **Línea 61**: Si el jugador dice que sí tiene la carta
- **Línea 62**: Verifica si la carta está en su tablero
- **Línea 63**: Encuentra la posición de la carta
- **Líneas 64-66**: Si no estaba marcada, la marca y confirma
- **Líneas 67-68**: Si ya estaba marcada, avisa
- **Líneas 69-70**: Si no tiene la carta, avisa

## **Líneas 72-75: Verificar victoria**
```python
        if all(tablero_marcado):
            completado = True
            break
```
- **Línea 72**: Si todas las cartas están marcadas
- **Línea 73**: Marca como completado
- **Línea 74**: Sale del bucle

## **Líneas 77-87: Mostrar resultado final**
```python
    print(f"\n{'='*50}")
    if completado:
        print("¡FELICIDADES! ¡Completaste tu tablero! 🎉")
        print(f"Te quedaban {cartas_restantes} cartas en el mazo")
        resultado = "ganó"
    else:
        print("¡Se acabaron las cartas del mazo!")
        print("No lograste completar tu tablero 😢")
        resultado = "perdió"
```
- Determina si ganó o perdió y muestra el mensaje correspondiente

## **Líneas 89-96: Mostrar tablero final**
```python
    print("\nTu tablero final:")
    for i in range(4):
        for j in range(4):
            idx = i * 4 + j
            marca = "✅" if tablero_marcado[idx] else "❌"
            print(f"{marca} {tablero_jugador[idx]}", end=" | ")
        print()
```
- Muestra el tablero final con ✅ para completadas y ❌ para incompletas

## **Líneas 98-99: Guardar resultado y pausa**
```python
    guardar_resultado(nombre_jugador, "Lotería Interactiva", resultado)
    input("\nPresiona Enter para continuar...")
```
- Guarda el resultado y espera que el usuario presione Enter

## **Conceptos Clave:**

### **1. Listas y Arrays**
- **random.sample()**: Selecciona elementos aleatorios sin repetir
- **random.shuffle()**: Mezcla aleatoriamente una lista
- **.copy()**: Crea una copia de la lista
- **.pop()**: Extrae y elimina el último elemento

### **2. Bucles Anidados**
- **for i in range(4)**: Bucle para filas
- **for j in range(4)**: Bucle para columnas
- **idx = i * 4 + j**: Convierte coordenadas 2D a índice 1D

### **3. Condicionales**
- **if respuesta == 's'**: Verifica respuesta del usuario
- **if carta_actual in tablero_jugador**: Verifica si elemento está en lista
- **if not tablero_marcado[idx]**: Verifica si no está marcado

### **4. Listas Booleanas**
- **[False] * 16**: Crea lista de 16 valores False
- **all(tablero_marcado)**: Verifica si todos son True

### **5. Manipulación de Strings**
- **.lower()**: Convierte a minúsculas
- **.strip()**: Elimina espacios
- **f-string**: Formato con variables

### **6. Control de Flujo**
- **while**: Bucle mientras se cumpla condición
- **break**: Sale del bucle
- **continue**: Salta a la siguiente iteración

## **Algoritmo del Juego:**
1. Generar tablero aleatorio de 16 cartas
2. Crear mazo mezclado con todas las cartas
3. Mostrar tablero inicial
4. Repetir hasta completar o acabar cartas:
   - Tomar carta del mazo
   - Mostrar carta al jugador
   - Preguntar si tiene la carta
   - Verificar respuesta y marcar si es correcta
   - Verificar si completó el tablero
5. Mostrar resultado final
6. Guardar resultado
