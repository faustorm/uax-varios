frase = input("Pon tu frase: ")
frase_invertida = ""

relacion = {
    "a": 4,
    "e": 3,
    "i": 1,
    "o": 0,
    "u": 5 
}

for letra in frase:    
    letra = letra.lower()
    print(f"estamos en {letra}")
    if letra in relacion:
        print(letra)
        letra = relacion[letra]
    
    frase_invertida = str(letra) + frase_invertida
    print(frase_invertida)

print(frase, frase_invertida)