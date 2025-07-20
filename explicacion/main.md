# 📁 main.py - Explicación Línea por Línea

## **Líneas 1-2: Importaciones**
```python
from treasure_hunt import juego_busqueda_tesoro
from lottery import juego_loteria
```
- **Línea 1**: Importa la función `juego_busqueda_tesoro` del archivo `treasure_hunt.py`
- **Línea 2**: Importa la función `juego_loteria` del archivo `lottery.py`
- Estas importaciones nos permiten usar las funciones de los otros archivos

## **Líneas 4-11: Función mostrar_menu()**
```python
def mostrar_menu():
    """Muestra el menú principal del juego"""
    print("\n" + "="*50)
    print("    BIENVENIDO A LA BIBLIOTECA DE JUEGOS")
    print("="*50)
    print("1. Búsqueda del Tesoro")
    print("2. Lotería Interactiva")
    print("3. Salir")
    print("-"*50)
```
- **Línea 4**: Define la función `mostrar_menu()` que no recibe parámetros
- **Línea 5**: Documentación de la función (docstring)
- **Líneas 6-11**: Imprime un menú visual con opciones para el usuario
- **Línea 6**: Crea una línea de 50 signos igual
- **Líneas 7-8**: Título del programa
- **Líneas 9-11**: Opciones disponibles para el usuario

## **Líneas 13-41: Función main()**
```python
def main():
    """Función principal del programa"""
    print("¡Bienvenido al Sistema de Juegos!")
    
    nombre = input("Por favor, ingresa tu nombre: ").strip()
    if not nombre:
        nombre = "Jugador"
```
- **Línea 13**: Define la función principal `main()`
- **Línea 14**: Documentación de la función
- **Línea 16**: Mensaje de bienvenida
- **Línea 18**: Solicita el nombre del jugador y elimina espacios extra con `.strip()`
- **Líneas 19-20**: Si no se ingresa nombre, asigna "Jugador" por defecto

```python
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
```
- **Línea 22**: Bucle infinito que mantiene el programa corriendo
- **Línea 23**: Llama a la función para mostrar el menú
- **Línea 25**: Bloque `try-except` para manejar errores de entrada
- **Línea 26**: Convierte la entrada del usuario a entero
- **Líneas 28-29**: Si opción es 1, ejecuta el juego de búsqueda del tesoro
- **Líneas 30-31**: Si opción es 2, ejecuta el juego de lotería
- **Líneas 32-34**: Si opción es 3, muestra mensaje de despedida y sale del bucle
- **Líneas 35-36**: Si la opción no es válida, muestra error
- **Líneas 37-38**: Si hay error al convertir a número, muestra mensaje de error

```python
if __name__ == "__main__":
    main()
```
- **Líneas 40-41**: Ejecuta la función `main()` solo si el archivo se ejecuta directamente

## **Conceptos Clave:**

### **1. Importaciones**
- **from**: Importa funciones específicas de otros módulos
- **import**: Importa módulos completos

### **2. Funciones**
- **def**: Define una nueva función
- **docstring**: Documentación de la función entre comillas triples
- **parámetros**: Variables que recibe la función

### **3. Control de Flujo**
- **while True**: Bucle infinito
- **if/elif/else**: Condicionales
- **break**: Sale del bucle
- **try/except**: Manejo de errores

### **4. Entrada/Salida**
- **input()**: Solicita entrada del usuario
- **print()**: Muestra texto en pantalla
- **.strip()**: Elimina espacios al inicio y final
- **f-string**: Formato de cadena con variables

### **5. Conversión de Tipos**
- **int()**: Convierte texto a número entero
- **str()**: Convierte número a texto

### **6. Estructura del Programa**
- **main()**: Función principal que controla el flujo
- **if __name__ == "__main__"**: Solo ejecuta si es el archivo principal
- **modularización**: Cada juego en su propio archivo

## **Flujo del Programa:**
1. Usuario ingresa nombre
2. Se muestra menú principal
3. Usuario selecciona juego
4. Se ejecuta el juego seleccionado
5. Se regresa al menú principal
6. Se repite hasta que el usuario elija salir
