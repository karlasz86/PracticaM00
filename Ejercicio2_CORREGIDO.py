def Esnumero(n):
    try:
        float(n)
        return True
    except:
        return False
def EsEntero(n):
    try:
        int(n)
        return True
    except:
        return False
    

_UNIDADES = 1
_PRECIO = 0

cadenaPrecio = input("Introducir el precio del producto ")

while not Esnumero(cadenaPrecio):
    print("Debes introducir un valor numérico, intenta de nuevo")
    cadenaPrecio = input("Introducir el precio del producto ")
precio = float(cadenaPrecio)

cadenaUnidades = input("Introducir el número de productos ")

while not EsEntero(cadenaUnidades):
    print("Debes introducir un valor entero, intenta de nuevo")
    cadenaUnidades = input("Introducir el número de productos ")

precio = float(cadenaPrecio)
unidades = float(cadenaUnidades)


totalItems = 0
precioTotal = 0
listaFactura = []

while precio > 0 and unidades > 0:
    
    totalUnidad = precio * unidades
    
    item = []
    
    item.append(precio)
    item.append(unidades)
    
    listaFactura.append(item)
    
    totalItems += unidades
    precioTotal += totalUnidad
    
       
    cadenaPrecio = input("Introducir el precio del producto ")
    while not Esnumero(cadenaPrecio):
        print("Debes introducir un valor numérico, intenta de nuevo")
        cadenaPrecio = input("Introducir el precio del producto ")
        
    precio = float(cadenaPrecio)
               
    cadenaUnidades = input("Introducir el número de productos ")
    while not EsEntero(cadenaUnidades):
        print("Debes introducir un valor entero, intenta de nuevo")
        cadenaUnidades = input("Introducir el número de productos ")
    unidades = float(cadenaUnidades)
    
    if precio == 0:
        break
    if unidades == 0:
        break
    
 
for item in listaFactura:
    preciofinal= '{:.2f}'.format(item[_PRECIO]*item[_UNIDADES])
    print(item[_PRECIO], "€ - ", item[_UNIDADES], "unidades - ", preciofinal, "€")

print("-------------------")
print("Total:", '{:.2f}'.format(precioTotal),"€")
print("Unidades:", totalItems)
