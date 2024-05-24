'''
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
Por ejemplo, “Hola,tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función
'''


def convertirEspaciado(text1):
    text2 = ' '.join(text1)
    return text2


texto= input('Ingrese un texto: ')

print(convertirEspaciado(texto))

