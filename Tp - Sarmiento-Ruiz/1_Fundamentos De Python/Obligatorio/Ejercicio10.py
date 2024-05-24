### Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel ##
'''
Imagina que vendes pan a 400 pesos el kilo. El pan que no es del día tiene un 
descuento del 60%. Escribe un programa que comience leyendo los kilos de pan 
vendidos que no son del día, el precio del pan del día, el descuento que se hace por 
no serlo y el monto total del pan vendido que no es fresco. 
'''


import os

def ventas():
    venta_PanViejo = 0
    venta_PanNuevo = 0
    
    menu_venta = """
    1 - Pan Nuevo
    2 - Pan Viejo
    3 - Fin de Venta
    """
    opcion_venta = ""
    
    while opcion_venta != '3':
        os.system('cls')
        print(menu_venta)
        opcion_venta = input("Seleccione un tipo de venta >>> ")
        print("")
        if opcion_venta == '1':
            peso_pn = float(input("Ingrese el peso del pan >>> "))
            print("")
            venta_PanNuevo = peso_pn*400
            
        elif opcion_venta == '2':
            peso_pv = float(input("Ingrese el peso del pan >>> "))
            print("")
            venta_PanViejo = (peso_pv*400)*0.6
            
        else:
            Monto_venta = venta_PanNuevo + venta_PanViejo
            if venta_PanNuevo > 0 and venta_PanViejo == 0:
                print(f"La suma total de la venta es ${Monto_venta}")
            elif venta_PanViejo > 0 and venta_PanNuevo == 0:
                print(f"La suma total de la venta es ${Monto_venta}")
            else:
                print(f"Subtotal_1 ${venta_PanNuevo}")
                print(f"Subtotal_2 es de ${venta_PanViejo}")
                print(f"La suma total de la venta es ${Monto_venta}")
            
            TotalVenta_PN = venta_PanNuevo        
            TotalVenta_PV = venta_PanViejo
            input("presione ENTER para continuar")
            return TotalVenta_PN, TotalVenta_PV

def informe(TotalVenta_PN,TotalVenta_PV):
    
    print(f"El total de ventas de Pan del Día es de ${TotalVenta_PN}")
    print("")
    print(f"El total de ventas de Pan con Descuento es de ${TotalVenta_PV}")
    return



### Menu Principal ##

menu = """

*** Menú ***
1 - Ingresar Venta
2 - Informe de Ventas
3 - Salir
"""
opcion = ""

#### Estructura Principal ###
TotalVenta_PN = 0
TotalVenta_PV = 0
while opcion != '3':
    os.system('cls')
    print(menu)
    opcion = input("Elija una Opción >>> ")
    if opcion == '1':
        TotalVenta_PN, TotalVenta_PV = ventas()
    elif opcion == '2':
        informe(TotalVenta_PN,TotalVenta_PV)
        input("ENTER para continuar")
    elif opcion == '3':
        print('¡Hasta Mañana!')
    else:   
        print('¡Opcion invalida!')
        input('ENTER para continuar')
