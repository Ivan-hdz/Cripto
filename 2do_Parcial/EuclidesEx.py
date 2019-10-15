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
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
print("")
#mcd, x, y = euclidesExtendido(a, b)
mcd, x, y= xgcd(a,b)
print("MCD(", a, ",", b, ") = ", mcd, " = ", a, "(", x, ") + ", b, "(", y, ")")
inv=mulinv(a,b)
print("Inverso Multiplicativo=",inv,"\n",inv,"*",a,"%",b,"==1")
#Condiciones Curva Eliptica
#p mod 4 == 1           a + b mod4==1
#q=(p+1+2a)/4
#K=(x0^3-y0^3)(x0)^-1 mod p
#K^(p-1)/2  mod p ==1
#K^(p-1)/4  mod p =/=1

#condicion de no singul   4(-K)^3 mod p=/0
#condicion de no singul q mod p=/=1
#no sea traza uno q=/p

#cifrar y decifrar el gammal
#y1=alpha^k  mod p*
#y2=xBeta^k mod p*
#dk=y1^(p-a-1) y2   modp*