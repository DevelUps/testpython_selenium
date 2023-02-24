a = 10
b = 20
c = 9

# a>b and a<c

print("a es < que b 7 a es mayor que c ?  " + str(a>b and a<c))
print("a es < que b 7 a es mayor que c ?  " + str(a>b or a<b))

a= int(input("ingrese el primer valor :"))
b= int(input("ingrese el segundo valor valor: "))
suma = a + b
resta = a-b
divicion = a//b
multiplicacion = a*b
suma2= (a+b) + (a-b) + (a/b) + (a+b)



print("La suma de {} + la resta es : {} la divicion es es : {} la multiplicacion es : {} " .format(a, b,suma, resta, multiplicacion,divicion))
print(" el total es : ", str(suma2))