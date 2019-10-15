def euclidesExtendido(a, b):
    if (a > 0 and b == 0):
        return a, 1, 0
    if (a == 0 and b == 0):
        return False, False ,False
    residuo = -1

    xprevio = 1
    yprevio = 0

    x = 0
    y = 1
    while residuo != 0:
        q = int(a/b)
        residuo = a % b
        print(a,"=",q,"x",b ,"+",residuo)
        a = b
        b = residuo
        auxx = xprevio - q * x
        print(auxx,"=",xprevio,"-",q,"x",x)
        xprevio = x
        x = auxx
        auxy = yprevio - q * y
        print(auxy,"=",yprevio,"-",q,"x",y)
        yprevio = y
        y = auxy
    return a, xprevio, yprevio
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b
def expBinaria(x, exp, clase, printProcess):
    Expbase2 = "{0:b}".format(exp)
    if printProcess:
        print("");
        print(Expbase2);
        print("")
    Expbase2 = list(Expbase2)
    result = x; 
    expvariable = 2
    result = pow(result, 2, clase)
    if printProcess:
        print(x, "^", expvariable, "=", result, "mod", clase)
    lastpos = len(Expbase2) - 1
    for i in range(1, lastpos):
        if (Expbase2[i] == "1"):
            result = pow(result * x, 2, clase)
            expvariable = (expvariable + 1) * 2
            if printProcess:
            	print(x, "^", expvariable, "=", result, "mod", clase)
            else:
                result = pow(result, 2, clase)
                expvariable = expvariable * 2
                if printProcess:
                	print(x, "^", expvariable, "=", result, "mod", clase)
        if (Expbase2[lastpos] == "1"):
            result = (result * x) % clase
            expvariable += 1
            if printProcess:
            	print(x, "^", expvariable, "=", result, "mod", clase)
    return result

print("Elegir operacion:\n1. P=Q\n2. P=/Q\n3. Calcular K=(x0^3 - y0^2)(x0)^-1 mod p")
opc=int(input())
if(opc==1):
#q se pasa a base 2 de der a izq se duplica, de regreso se suma si hay un uno la posicion 2 a la n
# alpha + alpha P=Q
# lambda = (3x^2 + a)(2y)^-1  mod p
#x3= (lambda^2  -2x1 ) mod p
#y3= (lambda(x1 - x3) - y1 )mod p
    xp = int(input("Ingrese x1: "))
    yp= int(input("Ingrese y1: "))
    p=int(input("Ingrese p: "))
    k=int(input("Ingrese k: "))
    aux1=((3*(xp**2)) + k)  % p # NO OLVIDAR EL SIGNO
    print("3*x^2+a=",aux1)
    aux2=mulinv(2*yp,p)
    print("2*y^-1=",aux2)
    lam=(aux1* aux2 ) % p
    print("lambda=",lam)
    x3=(lam**2-2*xp) % p
    y3=((lam * (xp - x3)) - yp) % p
    #y3=(abs((lam * (xp - x3)) - yp)) % p
    print("x3=",x3,"\ty3=",y3)
elif (opc==2):
#alpha + n alpha P=/=Q
#lambda = (y2-y1)(x2-x1) mod p 
#x3=(lambda ^2 - x1 - x2)mod p
#y3=(lambda (x1 -x3) -y1 )mod p
    x1 = int(input("Ingrese x1: "))
    y1= int(input("Ingrese y1: "))
    x2 = int(input("Ingrese x2: "))
    y2= int(input("Ingrese y2: "))
    p=int(input("Ingrese p: "))
    k=int(input("Ingrese k: "))
    aux1=(y2-y1)  % p # NO OLVIDAR EL SIGNO
    print("y2-y1 mod p=",aux1)
    aux2=mulinv(x2-x1,p)
    print("x2-x1 mod p=",aux2)
    lam=(aux1* aux2 ) % p
    print("lambda=",lam)
    x3=(lam**2 - x1 - x2) % p
    y3=(abs((lam * (x1 - x3)) - y1)) % p
    print("x3=",x3,"\ty3=",y3)
elif (opc==3):
    #K=(x0^3 - y0^2)(x0)^-1 mod p
    #1<x0 && y0<p-1
    x0 = int(input("Ingrese x0: "))
    y0= int(input("Ingrese y0: "))
    p=int(input("Ingrese p: "))
    aux1=((x0**3)-y0**2) % p
    aux2=mulinv(x0,p)
    k=(aux1*aux2) % p
    print(aux1,"*",aux2,"=",k)
else:
    print("opcion no valida")
#inv=mulinv(a,b)
#print("Inverso Multiplicativo=",inv,"\n",inv,"*",a,"%",b,"==1")
#x = int(input("Ingrese x: "))
#exp = int(input("Ingrese Exp: "))
#clase = int(input("Ingrese la clase: "))
#print("")
#result = expBinaria(x, exp, clase, True)
#print("Resultado = ", result)
