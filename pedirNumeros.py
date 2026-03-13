
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




def pedirNumero2():

    seguir=True
    while seguir:
        try:
            numero=int(input())
            seguir=False
            return numero
        except ValueError:
            print("opcion invalida")
