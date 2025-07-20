# 🛠️ utils.py - Explicación Línea por Línea

## **Líneas 1-2: Importaciones**
```python
import json
from datetime import datetime
```
- **Línea 1**: Importa el módulo `json` para trabajar con archivos JSON
- **Línea 2**: Importa la clase `datetime` para manejar fechas y horas

## **Líneas 4-18: Función guardar_resultado()**
```python
def guardar_resultado(nombre_jugador, juego, resultado):
    """Guarda el resultado del juego en un archivo JSON"""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = {
        "jugador": nombre_jugador,
        "juego": juego,
        "resultado": resultado,
        "fecha": fecha
    }
```
- **Línea 4**: Define la función que recibe 3 parámetros
- **Línea 5**: Documentación de la función
- **Línea 6**: Obtiene la fecha y hora actual en formato específico
- **Líneas 7-12**: Crea un diccionario con la información del resultado

```python
    try:
        with open("resultados_juegos.json", "a") as f:
            f.write(json.dumps(registro) + "\n")
    except:
        pass
```
- **Línea 14**: Bloque `try-except` para manejar errores de archivo
- **Línea 15**: Abre el archivo en modo "append" (añadir al final)
- **Línea 16**: Convierte el diccionario a JSON y lo escribe en el archivo
- **Líneas 17-18**: Si hay error, no hace nada (manejo silencioso)

## **Conceptos Clave:**

### **1. Módulos Importados**
- **json**: Para trabajar con formato JSON
- **datetime**: Para manejar fechas y horas

### **2. Funciones de Fecha**
- **datetime.now()**: Obtiene fecha y hora actual
- **.strftime()**: Formatea fecha en string específico
- **"%Y-%m-%d %H:%M:%S"**: Formato año-mes-día hora:minuto:segundo

### **3. Diccionarios**
- **{}**: Estructura de datos clave-valor
- **"clave": valor**: Define pares clave-valor
- **registro["jugador"]**: Accede a valor por clave

### **4. Manejo de Archivos**
- **with open()**: Abre archivo de forma segura
- **"a"**: Modo append (añadir al final)
- **as f**: Alias para el archivo
- **f.write()**: Escribe en el archivo

### **5. JSON**
- **json.dumps()**: Convierte diccionario a string JSON
- **+ "\n"**: Añade salto de línea

### **6. Manejo de Errores**
- **try/except**: Captura errores
- **pass**: No hace nada (manejo silencioso)

### **7. Parámetros de Función**
- **def guardar_resultado(nombre_jugador, juego, resultado)**:
  - `nombre_jugador`: String con el nombre del jugador
  - `juego`: String con el nombre del juego
  - `resultado`: String con el resultado ("ganó" o "perdió")

## **Estructura del Archivo JSON:**
```json
{"jugador": "Juan", "juego": "Lotería Interactiva", "resultado": "ganó", "fecha": "2024-07-20 16:30:45"}
{"jugador": "María", "juego": "Búsqueda del Tesoro", "resultado": "perdió", "fecha": "2024-07-20 16:35:12"}
```

## **Flujo de la Función:**
1. Recibe parámetros (jugador, juego, resultado)
2. Obtiene fecha y hora actual
3. Crea diccionario con toda la información
4. Abre archivo en modo append
5. Convierte diccionario a JSON
6. Escribe línea en archivo
7. Cierra archivo automáticamente (with)
8. Si hay error, no hace nada

## **Ventajas de esta Implementación:**
- **Persistencia**: Los resultados se guardan permanentemente
- **Formato JSON**: Fácil de leer y procesar
- **Manejo de errores**: No falla si hay problemas de archivo
- **Append**: No sobrescribe resultados anteriores
- **Timestamp**: Cada resultado tiene fecha y hora

## **Uso en el Proyecto:**
- Se llama desde `lottery.py` y `treasure_hunt.py`
- Guarda automáticamente cada resultado de juego
- Permite análisis posterior de estadísticas
- Mantiene historial de partidas 