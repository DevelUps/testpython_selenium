a=20
b=19
c=25

if(a>b):
    print("El mayor es a: " + str(a))
else:
    print("EL mayor es b: "+str(b))

nom="juan"
if (nom == "juan"):
    print("tu nombre es:  " + nom)

if (a<=b):
    print("{} igual que {}: " .format(a,b))
else:
    print("el menor es b: "+ str(b))

if (a!=b):
    print("{} es diferente que {}" .format(a,b))
else:
    print("{} es igual que {}".format(a, b))

if (a>b) and (a>b):
    print("El mayor es: "+str(a))
elif (a<b) and (a>c):
    print("el mayor es: " + str(b))
if (a>b or a>c):
    print("{} es menor que {} o {} es mayor que {}:  ".format(a,b,a,c))