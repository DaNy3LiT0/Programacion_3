"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante"""


abcd = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
abcd_sinx3 = []

for i in abcd:
    if ((abcd.index(i)+1)%3) != 0:
        abcd_sinx3.append(i)
        
print(f"El abecedario quedo asi: {abcd_sinx3}")