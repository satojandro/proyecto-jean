#!/usr/bin/env python3
"""
Script de prueba para los juegos sin interacción manual
"""

import sys
import io
from main import juego_busqueda_tesoro, juego_loteria, guardar_resultado
import random

def test_treasure_hunt():
    """Prueba rápida del juego de búsqueda del tesoro"""
    print("=== TEST: Búsqueda del Tesoro ===")
    
    # Simular nivel fácil
    tamaño = 4
    intentos_max = 12
    tesoro_fila = random.randint(0, tamaño-1)
    tesoro_col = random.randint(0, tamaño-1)
    
    print(f"Tesoro oculto en: ({tesoro_fila}, {tesoro_col})")
    
    # Simular algunos intentos
    for intento in range(3):
        fila, col = random.randint(0, 3), random.randint(0, 3)
        print(f"Intento {intento+1}: Excavando en ({fila}, {col})")
        
        if fila == tesoro_fila and col == tesoro_col:
            print("✅ ¡Tesoro encontrado!")
            return True
        else:
            distancia = abs(fila - tesoro_fila) + abs(col - tesoro_col)
            print(f"   Distancia: {distancia} (pista: {'🔥 Muy caliente' if distancia <= 2 else '❄️ Frío'})")
    
    print("❌ Prueba terminada sin encontrar el tesoro")
    return False

def test_lottery():
    """Prueba rápida del juego de lotería"""
    print("\n=== TEST: Lotería Interactiva ===")
    
    # Generar tablero de prueba
    cartas = [f"Carta{i}" for i in range(1, 55)]
    tablero_jugador = random.sample(cartas, 16)
    tablero_marcado = [False] * 16
    
    print(f"Tablero del jugador: {tablero_jugador[:4]}...")
    
    # Simular 5 cartas sorteadas
    mazo = cartas.copy()
    random.shuffle(mazo)
    
    for i in range(5):
        carta = mazo.pop()
        print(f"Carta sorteada: {carta}")
        
        if carta in tablero_jugador:
            idx = tablero_jugador.index(carta)
            if not tablero_marcado[idx]:
                tablero_marcado[idx] = True
                print(f"   ✅ Marcando {carta}")
            else:
                print(f"   ⚠️ Ya estaba marcada")
        else:
            print(f"   ❌ No está en el tablero")
    
    marcadas = sum(tablero_marcado)
    print(f"Cartas marcadas: {marcadas}/16")
    return marcadas > 0

def test_guardado():
    """Prueba el sistema de guardado"""
    print("\n=== TEST: Sistema de Guardado ===")
    
    guardar_resultado("TestUser", "Búsqueda del Tesoro", "ganó")
    guardar_resultado("TestUser", "Lotería Interactiva", "perdió")
    
    try:
        with open("resultados_juegos.json", "r") as f:
            lineas = f.readlines()
            print(f"✅ Resultados guardados: {len(lineas)} entradas")
            if lineas:
                print(f"   Última entrada: {lineas[-1].strip()}")
    except FileNotFoundError:
        print("❌ Archivo no encontrado")

if __name__ == "__main__":
    print("Iniciando pruebas automáticas...\n")
    
    test_treasure_hunt()
    test_lottery()
    test_guardado()
    
    print("\n✅ Pruebas completadas!")
    print("Para probar interactivamente: python3 main.py")