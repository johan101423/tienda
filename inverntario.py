
data_base =  []

from pedirNumeros import *
from opciones import *

def pedriNombre (msg):
    try:
        pedriNombre=str(input(msg))

        
        if pedriNombre.isalpha() == False:
                print("Por favor colocar solo una palabra")

                return pedriNombre
    except :
     print ("solo palabras")


def inicio ():
    print ("1. ADD PRODUCT NAME ")
    print ("2. SEE PRODUCTS")
    print ("3. TOTAL FOR THE DAY")

from validacion import *

def menu () :
    opcion = 0
    inicio ()

    while opcion !=3:
        opcion = pedirNumero("ENTER THE OPTION NUMBER: ", "int")

        if opcion == 1:
          option1()
        elif opcion == 2:
          option2()
        else:
          print("OPTION NO VALID")

        option3()  

menu()
        





            
