def criba_eratostenes(limite):
    """
    Implementa la criba de Eratóstenes para encontrar todos los primos hasta el límite
    """
    if limite < 2:
        return [False] * (limite + 1)
    
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    
    i = 2
    while i * i <= limite:
        if es_primo[i]:
            # Marcar múltiplos de i como no primos
            j = i * i
            while j <= limite:
                es_primo[j] = False
                j += i
        i += 1
    
    return es_primo

def precalcular_primos_hasta(limite):
    """
    Precalcula cuántos primos hay desde 1 hasta cada número k
    """
    es_primo = criba_eratostenes(limite)
    primos_hasta = [0] * (limite + 1)
    
    # Construir arreglo de suma acumulativa
    for i in range(1, limite + 1):
        primos_hasta[i] = primos_hasta[i-1] + (1 if es_primo[i] else 0)
    
    return primos_hasta

def contar_primos_intervalos(intervalos):
    """
    Función principal que resuelve el problema de Isaac
    """
    if not intervalos:
        return []
    
    # Encontrar el máximo valor de b en todos los intervalos
    max_b = max(b for _, b in intervalos)
    
    # Precalcular el arreglo de primos hasta el máximo necesario
    primos_hasta = precalcular_primos_hasta(max_b)
    
    # Procesar cada consulta en tiempo constante
    resultados = []
    for a, b in intervalos:
        if a == 0:
            # Si a es 0, ajustar para evitar índice negativo
            primos_en_rango = primos_hasta[b] - primos_hasta[0]
        else:
            primos_en_rango = primos_hasta[b] - primos_hasta[a-1]
        resultados.append(primos_en_rango)
    
    return resultados

# --- EJEMPLO DE USO ---
def main():
    # Simular entrada (en competencia, esto vendría de input())
    intervalos = [
        (1, 10),
        (20, 30),
        (100, 150),
        (1, 1000000)  # ¡Incluso para un millón responde instantáneamente!
    ]
    
    print("Isaac y los intervalos mágicos")
    print("=" * 40)
    
    resultados = contar_primos_intervalos(intervalos)
    
    for i, ((a, b), count) in enumerate(zip(intervalos, resultados)):
        print(f"Intervalo [{a}, {b}]: {count} números primos")
    

if __name__ == "__main__":
    main()
