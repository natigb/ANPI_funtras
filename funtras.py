
pi = 3.141592653589793
tol = 10**-8
iterMax = 2500
eps = 2.2204*(10**-16)

def fact(n):
    """
    Toma un numero entero y retorna el factorial de ese numero
    
    :param n: numero entero
    :return: factorial del numero
    """
    n= int(n)
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
  
   
def div_t(x):
    """
    calcula la inversa de un numero, es decir 1/x o x^-1
    
    :param x: numero
    :return: inverso de x
    """
    if x==0:
        return "err"
    if x>0:
        return div_t_v(x)
    if x<0:
        return -1*div_t_v(abs(x))
def div_t_v(x):
    if fact(80)< x < fact(100):
        return div_t_aux(x, eps**15)
    if fact(60)< x <= fact(80):
        return div_t_aux(x, eps**11)
    if fact(40)< x <= fact(60):
        return div_t_aux(x, eps**8)
    if fact(20)< x <= fact(40):
        return div_t_aux(x, eps**4)
    if 0 < x <= fact(20):
        return div_t_aux(x, eps**2)
    if x >= fact(100):
        return 0
    return "err"
def div_t_aux(x, x0):
    xk = x0*(2-x*x0)
    for n in range (1,iterMax):
        xk1=xk*(2-(x*xk))
        if abs(xk1-xk)< tol*abs(xk1):
            return xk1
        xk=xk1
    return xk1

def power_t(x,y):
    """
    calcula la potencia de un numero, es decir x^y
    
    :param x: numero
    :param y: exponente
    :return: numero elevado al exponente
    """
    if y == round(y):
        if y >=0:
            return x**y
        else:
            return div_t(x**abs(y))
    return x**y

def sin_t(x):
    """
    calcula el seno de un numero en radianes
    
    :param x: numero
    :return: seno de x
    """
    xk=x
    for n in range (1,iterMax):
        var = (2*n)+1
        xk1 = xk + ( power_t(-1,n) * (power_t(x,var) *div_t(fact(var))) )
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return xk1
    print("break no err")
    return xk1


def sinh_t(x):
    """
    calcula el seno hiperbolico de un numero en radianes
    
    :param x: numero
    :return: seno hiperbolico de x
    """
    xk=x
    for n in range (1,iterMax):
        var = (2*n)+1
        xk1 = xk + (power_t(x,var) *div_t(fact(var))) 
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return xk1
    print("break no err")
    return xk1


def tanh_t(x):
    """
    calcula la tangente hiperbolica de un numero en radianes
    
    :param x: numero
    :return: tangente hiperbolica de x
    """
    print("tanh(x) not implemented")
    return "err"

def root_t(x,y):
    """
    calcula la raiz de un numero 
    
    :param x: numero
    :param y: indice
    :return: raiz de x segun el indice y
    """
    print("y/(x) not implemented")
    return "err"

def atan_t(x):
    """
    calcula el arco tangente de un numero en radianes
    
    :param x: numero
    :return: arco tangente de x
    """
    if -1 <= x <= 1:
        return atan_t_aux(x)
    if x>1:
        return atan_t_aux2(x,pi*div_t(2))
    if x<1:
        return atan_t_aux2(x,-1*pi*div_t(2))
def atan_t_aux(x):
    xk=x
    for n in range (1,iterMax):
        var = (2*n)+1
        xk1 = xk + ( power_t(-1,n) * (power_t(x,var) *div_t(var)) )
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return xk1
    print("break no err")
    return xk1
def atan_t_aux2(x, const):
    xk= div_t(x)
    for n in range (1,iterMax):
        xk1 = xk + ( power_t(-1,n) * div_t((2*n+1) * power_t(x, 2*n+1)) )
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return const-xk1
    print("break no err")
    return const-xk1
    

def exp_t(x):
    """
    calcula la funcion exponencial de un numero con base e
    
    :param x: numero
    :return: e elevado a x
    """
    xk= 1
    for n in range (1,iterMax):
        xk1=xk+power_t(x,n)*div_t(fact(n))
        error = abs(xk1-xk)
        if error<tol:
            return xk1
        xk=xk1
    
    return xk1

def cos_t(x):
    """
    calcula el coseno de un numero en radianes
    
    :param x: numero
    :return: coseno de x
    """
    xk=1
    for n in range (1,iterMax):
        var = 2*n
        xk1 = xk + ( power_t(-1,n) * (power_t(x,var) *div_t(fact(var))) )
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return xk1
    print("break no err")
    return xk1


def sec_t(x):
    """
    calcula el secante de un numero en radianes
    
    :param x: numero
    :return: secante de x
    """
    return div_t(cos_t(x))


def tan_t(x):
    """
    calcula la tangente de un numero en radianes
    
    :param x: numero
    :return: tangente de x
    """
    return sin_t(x)* div_t(cos_t(x))


#no se puede con negativos
def ln_t(x):
    """
    calcula el logaritmo natural de un numero en radianes
    
    :param x: numero
    :return: logaritmo natural de x
    """
    xk=1
    const = (2*(x-1)) * div_t(x+1)
    for n in range (1,iterMax):
        xk1 = xk + ( div_t(2*n+1) * (power_t((x-1) * div_t(x+1), 2*n) ))
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return xk1 * const
    print("break no err")
    return xk1 * const


#no funciona con negativos
def log_t(x, y):
    """
    calcula el logaritmo de un numero
    
    :param x: argumento
    :param y: base
    :return: logaritmo base y de x
    """
    return ln_t(x)* div_t(ln_t(y))


def cosh_t(x):
    """
    calcula el coseno hiperbolico de un numero en radianes
    
    :param x: numero
    :return: coseno hiperbolico de x
    """
    xk=1
    for n in range (1,iterMax):
        var = 2*n
        xk1 = xk + (power_t(x,var) *div_t(fact(var)))
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return xk1
    print("break no err")
    return xk1


def sqrt_t(x):
    """
    calcula la raiz cuadrada de un numero
    
    :param x: numero
    :return: raiz cuadrada de x
    """
    print("sqrt(x) not implemented")
    return "err"

def asin_t(x):
    """
    calcula el arco seno de un numero en radianes
    
    :param x: numero
    :return: arco seno de x
    """
    if -1 <= x <= 1:
        return asin_t_aux(x)
    return "err"   
def asin_t_aux(x):
    xk=x
    for n in range (1,iterMax):
        xk1 = xk + ( fact(2*n) * div_t(power_t(4,n) * power_t(fact(n), 2) * (2*n+1)) * power_t(x,2*n+1))
        error = abs(xk1-xk)
        xk=xk1
        if error<tol:
            return xk1
    print("break no err")
    return xk1



def csc_t(x):
    """
    calcula el cosecante de un numero en radianes
    
    :param x: numero
    :return: cosecante de x
    """
    return div_t(sin_t(x))


def cot_t(x):
    """
    calcula el cotangente de un numero en radianes
    
    :param x: numero
    :return: cotangente de x
    """
    return div_t(tan_t(x))

def acos_t(x):
    """
    calcula el arco coseno de un numero en radianes
    
    :param x: numero
    :return: arco coseno de x
    """
    return pi*div_t(2) - asin_t(x)


"""print(div_t(0.15))
print(sin_t(5.2))
print(tan_t(0.9))
print(log_t(10,5))
print(sinh_t(5.2))
print(tanh_t(5))#
print(root_t(5,7))#
print(atan_t(-0.9))
print(sec_t(-0.9))
print(exp_t(0))
print(cos_t(1))
print(ln_t(970))
print(power_t(5,-3))
print(cosh_t(1))
print(sqrt_t(51))#
print(asin_t(0.56))
print(csc_t(-1))
print(cot_t(0.56))

print(acos_t(-0.56))"""