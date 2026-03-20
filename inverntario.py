
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
    print ("1. ADD PRODUCT  ")
    print ("2. SHOW INVENTORY ")
    print ("3. CALCULATE STATISTICS")
    print ("4. Exit")

from validacion import *

def menu () :
    opcion = 0

    while opcion !=4:
        inicio()
        opcion = pedirNumero("ENTER THE OPTION NUMBER: ", "int")

        if opcion == 1:
          option1()
        elif opcion == 2:
          option2()

        elif opcion==3:
          option3() 

        elif opcion==4:
           print("Exit")     
           
        else:


          print("OPTION NO VALID")

        
        

        
menu()
        





            
