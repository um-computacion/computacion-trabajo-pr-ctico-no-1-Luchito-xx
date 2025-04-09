def decimal_to_roman(numero):
    if numero < 1 or numero > 3999:
        raise ValueError("Número fuera de rango (1-3999)")
 
    romano = ""

    valor = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
    
    simbolo = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"]
    
    i = 0

    while numero > 0:
        if numero >= valor[i]:
            numero = numero - valor[i]
            romano = romano + simbolo[i]
        else:
            i = i + 1

    return romano



if __name__ == "__main__":
    numero = int(input("Ingresa un numero entre 1 y 3999: "))
    resultado = decimal_to_roman(numero)
    print("Numero en romano:", resultado)