
data_base= []

def pedirNumero(msg, tipo):
    terminate = 0
    while terminate == 0:
        try:
            if tipo == "int":
                pedir = int(input(msg))
            elif tipo == "float":
                pedir = float(input(msg))
            if pedir < 0:
                print("Colocar un numero positivo")
                continue
            return pedir
        except:
            print("Input invalido") 

def pedirPalabra(msg):
    terminate = 0
    while terminate == 0:
        try:
            pedir = str(input(msg))
            if pedir.isalpha() == False:
                print("Por favor colocar solo una palabra")
                continue
            return pedir
        except:
            print("Input invalido") 


def inicio ():
    print ("1. Agregar producto")
    print ("2.Ver productos agregados")
    print ("3.FInalizar compra")
    

def option1():
      producto= pedirPalabra("nombre del producto: ")
      precio= pedirNumero(f"agregar el precio unitario de {producto}: ", "float")
      cantidad= pedirNumero(f"cantidad de {producto}: ", "int")
      nueva_tupla =(producto, precio, cantidad)
      data_base.append(nueva_tupla)
  

def option2():
        
        for producto, precio, cantidad in data_base:
            print(f"NOMBRE DEL PRODUCTO: {producto}")
            print(f"PRECIO DEL PRODUCTO: {precio}")
            print(f"CANTIDAD DEL PRODUCTO: {cantidad}")
            print(f"Valor toral: {cantidad * precio}")
        
 
def option3():
        valorgeneral = 0

        for producto, precio, cantidad in data_base:

            print(f"NOMBRE DEL PRODUCTO: {producto}")
            print(f"PRECIO DEL PRODUCTO: {precio}")
            print(f"CANTIDAD DEL PRODUCTO: {cantidad}")
            print(f"Valor toral: {cantidad * precio}")
            valortotal = cantidad * precio
            valorgeneral += valortotal
            
        print(f"EL VALOR GENERAL ES {valorgeneral}")        
       

def pedirNumero2():

    seguir=True
    while seguir:
        try:
            numero=int(input())
            seguir=False
            return numero
        except ValueError:
            print("opcion invalida")


def menu():
    opcion = 0

    inicio()

    while opcion !=3:
        opcion = pedirNumero("DIgite el numero de la opcion: ", "int")

        if opcion == 1:
          option1()
        elif opcion == 2:
          option2()
        else:
          print("Opcion Invalida")

        option3()  

menu()

