# Parciales — Análisis de Algoritmos (193502)

Universidad Francisco de Paula Santander Ocaña  
Programa: Ingeniería de Sistemas  
Semestre: V  
Créditos: 3  
Asignatura: **Análisis de Algoritmos** 

---

## Instrucciones generales

- Tiempo máximo: **60 minutos**  
- Cada parcial tiene **4 puntos (25 pts c/u)**  
- Usa Python o pseudocódigo claro.  
- Para comparar funciones, basta con un **`for` + `if`** y reportar el menor `n` que verifica la desigualdad.  
- Justifica con fórmulas y razonamiento.  

---
# Parcial — Versión B

### Punto 1 (25 pts) — Ordena por complejidad
Ordena de menor a mayor las siguientes funciones (asintóticamente).  
Si dos son del mismo orden, indícalo.


![Logo](https://lh3.googleusercontent.com/pw/AP1GczOKbm4PRxvPmIk6xzWEndiZu8Rshw7xbFWnNI3rltL041tyTLuAEoS_afx5V8mtGSJr9FWorLJj02v-8Ga3JJ6YDmsSpBgSFL8ruWN_1OLTVyTerg_9zIomuoPte5JNZIQ_yNwoxVdjH8460tgjJaPO=w128-h290-s-no?authuser=0)

---

R// log2n < n < sqrtnlog2n < nlog2n < n^0.999 < n^3/2 < n^2 < n^2/log2n < (2^n/2) * n <  3^n 


### Punto 2 (25 pts) — Identifica y confronta
Asocia cada \(T(n)\) con un algoritmo plausible. Luego compara **dos pares** y encuentra el umbral de `n` con un `for` + `if`.

- T1(n) = 5n^2 + 10n 
- T2(n) = 6n\log2(n) + 300
- T3(n) = 0.01n^3
- T4(n) = 1.5^n 

Algoritmos posibles:  
- Selection/Insertion  
- Mergesort/Heapsort  
- Multiplicación de matrices cúbica  
- Backtracking con poda leve  


T3(n) = 0.01n^3 / Multiplicación de matrices cúbica 
T4(n) = 1.5^n / Backtracking con poda leve
T2(n) = 6n\log2(n) + 300 / Mergesort/Heapsort
T1(n) = 5n^2 + 10n / Selection/Insertion

Al comparar el Multiplicación de matrices cúbica vs Backtracking con poda leve, de la forma 0.01n^3 < 1.5^n , podemos evidenciar que el umbral en este caso es para todos los n>= a 1 , lo que quiere decir que su tiempo de ejecucion y consumo en memoria es mas optimo usar un Backtracking con poda leve que un Multiplicación de matrices cúbica a partir de n>=1

Al comparar el Mergesort/Heapsort vs Selection/Insertion, de la forma 6n\log2(n) + 300 < 5n^2 + 10n , podemos evidenciar que el umbral en este caso es para todos los n>=7, lo que quiere decir que su tiempo de ejecucion y consumo en memoria es mas optimo usar un Selection/Insertion a partir de n>=7 que un Mergesort/Heapsort
---

### Punto 3 (25 pts) — Ejercicio lógico
#### Isaac y los intervalos mágicos

Isaac, convencido de que tiene un talento especial para los números, asegura que puede contar al instante cuántos primos existen en cualquier rango que le propongan sus amigos. Para comprobarlo, ellos le entregan una lista con N pares de números (a,b), y él debe responder de inmediato cuántos números primos hay en cada intervalo. A partir de esta historia, elabora el análisis necesario para resolver el problema y define claramente qué se recibe como entrada, qué se debe producir como salida y qué lógica se requiere para verificar la afirmación de Isaac. 

---

### Punto 4 (25 pts) — Cuestionario

[![Click here!!](https://cf.quizizz.com/img/wayground/brand/plans/logo-basic.png)](https://wayground.com/join?gc=846438)




