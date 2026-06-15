#Evidencia evauluacion 3 Bastian Saez

#los "#" son para organizarme yo mismo

#ejercicio 1
#1. registro de velocidades
a = int(input("ingrese la primera velocidad registrada en km/h: "))
b = int(input("ingrese la segunda velocidad registrada en km/h: "))
c = int(input("ingrese la tercera velocidad registrada en km/h: "))
d = int(input("ingrese la cuarta velocidad registrada en km/h: "))
e = int(input("ingrese la quinta velocidad registrada en km/h: "))
#2. guardado en lista :)
lista = [a, b, c, d, e]

todos_limite = True
#3.calcular promedio y velocidad max
prom_lista = sum(lista) / 5
print(f"el promedio de velocidades fue de {prom_lista} km/h y la velocidad maxima registrada fue de {max(lista)} km/h")
#4.verificar velocidades
for indice, fila in enumerate(lista):
    if (fila >= 60) and (fila <= 120):
        print(f"la velocidades de {indice + 1} estan dentro del limite. {fila} km/h")
    elif (fila > 140) or (fila < 20):
        todos_limite = False
#5.verificar peligro en el limite
if todos_limite == True:
    print("Todos estan dentro del limite")
else:
    print("Advertencia, no todos los vehiculos estan dentro del limite establecido")

#ejercicio 2

vendedor_1 = [40000, 50000, 90000]
vendedor_2 = [55000, 10000, 20000]
vendedor_3 = [1000, 24000, 700]

matriz = [
    vendedor_1,
    vendedor_2,
    vendedor_3
]
#1.matriz lista
mej_vendedor = 0
may_venta = -1
#2.Suma total lista
for indice, fila in enumerate(matriz):
    suma_vendedores = sum(fila)
    if suma_vendedores > may_venta: #3. identifica la mayor venta
        may_venta = suma_vendedores
        mej_vendedor = indice + 1
    print(f"el vendedor {indice + 1} obtuvo una venta total de {suma_vendedores}")
if suma_vendedores < 30000: #4. alerta de venta menor
    print(f"el vendedor {indice + 1} obtuvo un total de venta menor de {suma_vendedores}")
else:
    print("ningun vendedor tuvo una venta menor a 30000")

print(f"el vendedor {mej_vendedor} obtuvo la mayor venta total de {may_venta}")

#ejercicio 3
#1.solicitar edad, tarjeta y total
edad = int(input("coloque su edad: "))
tarjeta = input("posee tarjeta socio? 's' para si y 'n' para no: ")
total = int(input("Coloque el monto total: "))
#2.verificar si cumple o no
if (edad >= 60 or tarjeta == "s") and (total > 10000):
    print(f"Califica para el descuento. su total de {total} baja a {total * 0.85}")
else:
    print(f"no califica para el descuento. su total sigue siendo {total}")
#3.Mensaje de si obtuvo o no el descuento