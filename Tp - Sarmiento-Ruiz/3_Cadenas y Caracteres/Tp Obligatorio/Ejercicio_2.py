"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con 
dominio gob.ar"""

##### Programa Principal #####

email = input("Por favor ingrese su correo electorico: ")

while '@' not in email:
    email = input("Por favor ingrese su correo electrónico correcto: ")
        
div_email = email.split("@")
nuevo_email = div_email[0]+"@gob.ar"

print("Su nuevo e-mail es: ",nuevo_email)