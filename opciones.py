
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
                print("PLACE A NUMBER POSITIVE ")
                continue
            return pedir
        except:
            print("OPTIONS NOT VALID") 

def pedirPalabra(msg):
    terminate = 0
    while terminate == 0:
        try:
            pedir = str(input(msg))
            if pedir.isalpha() == False:
                print("please just words")
                continue
            return pedir
        except :
            print ("option not valid")


def option1():
      producto= pedirPalabra(" PRODUCT NAME : ")
      precio= pedirNumero(f" ADD PRICE {producto}: ", "float")
      cantidad= pedirNumero(f"AMOUNT OF  {producto}: ", "int")
      nueva_tupla =(producto, precio, cantidad)
      data_base.append(nueva_tupla)
  

def option2():
        
        for producto, precio, cantidad in data_base:
            print(f"PRODUCT NAME : {producto}")
            print(f"PRODUCT PRICE: {precio}")
            print(f"PRODUCT AMOUNT : {cantidad}")
            print(f"total: {cantidad * precio}")
        
 
def option3():
        valorgeneral = 0

        for producto, precio, cantidad in data_base:

            print (f"PRODUCT NAME : {producto}")
            print ("--------------------------------")
            print (f"PRODUCT PRICE: {precio}")
            print ("------------------------------------")
            print (f" PRODUCT AMOUNT: {cantidad}")
            print ("---------------------------------")
            print (f"Valor toral: {cantidad * precio}")
            valortotal = cantidad * precio
            valorgeneral += valortotal
            
        print(f"GENERAL VALUE {valorgeneral}")        
       
def option4 () :
     print("Exit")