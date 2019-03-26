# PracticasSeguridad
Creo que el título es bastante descriptivo no creen

Repositorio en el que meteré todas las movidas estas chungas de seguridad tu sabes.

Spoiler: movidas chungas == prácticas de seguridad

## Práctica 1
Dado el siguiente código Python, que implementa el cifrado Cesar (+3) para el
alfabeto inglés en Mayúsculas (C: M → M + 3 (mod. 26)) 
```python
def cifradoCesarAlfabetoInglesMAY(cadena):
     resultado = ''
     i = 0
     while i < len(cadena):
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
     if (ordenClaro >= 65 and ordenClaro <= 90):
        ordenCifrado = (((ordenClaro - 65) + 3) % 26) + 65
     resultado = resultado + chr(ordenCifrado)
     i = i + 1
     return resultado
```

se pide implementar la siguiente funcionalidad:

a) (4 puntos) Implementar la función de descifrado Cesar para alfabeto inglés en
mayúsculas, la cual descifre los textos cifrados creados por el código anterior.


b) (2 puntos) Modificar las funciones de cifrado y descifrado, para que soporten tanto
letras en mayúsculas (A..Z) como letras en minúsculas (a..z) en el alfabeto Inglés.


c) (2 puntos) Modificar las funciones de cifrado y descifrado, para que soporten el
cifrado Cesar generalizado (C: M → M + i (mod. 26))

## Práctica 2
1. El	código	Python	descrito	en	el	apéndice (`Cifrado_Descifrado_Basico.py`)	muestra	como	se	cifra	y	
se	descifra	un	texto	utilizando	para	ello	DES	en	modo	ECB,	CBC y	CTR.	Utilizando	como	base	ese	
código,	crear	 una	clase	llamada	DES_CIPHER

2. Se	 pide	 crear	 una	 clase	 AES_CIPHER,	 la	 cual	 tenga	 los	mismos	
métodos	 que	 la	 clase	 DES_CIPHER,	 pero	 que	 utilice	 el	 algoritmo	 AES	 para	 cifrar	 y	 descifrar.	
Para	este	ejercicio,	es	necesario	tener en	cuenta	tanto	el	tamaño	de	claves	como	el	tamaño	de	
bloques	del	algoritmo	AES.