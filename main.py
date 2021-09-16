from ejercicio1 import Texto

texto = "This is a line\nAnd this is other"

print(f"Palabras : {len(Texto.limpiar(texto))}")
print(f"Frecuencia : {Texto.contadorFrecuencia(texto)}")
print(f"Top-5 : {Texto.top5(texto, 5)}")

