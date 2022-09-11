
pi = 3.141592653589793
tol = 10**-8
iterMax = 2500
eps = 2.2204*(10**-16)

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
  

def div_t(x):
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
##print(div_t(-1.5648))    
##print(div_t(0))

"""
print(div_t(0))
print(div_t(0.15))
print(div_t(fact(101)))
print(div_t(fact(99)))
"""
def power_t(x,y):
    if y == round(y):
        if y >=0:
            return x**y
        else:
            return div_t(x**abs(y))
    return x**y
    ##print("x^y not implemented")
"""print(power_t(5,15)) 
print(power_t(5,-3))
print(power_t(5,6.2))"""

def sin_t(x):
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
"""print(sin_t(19))
print(sin_t(5.2))
print(sin_t(1))
print(sin_t(0))"""

def sinh_t(x):
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
"""print(sinh_t(19))
print(sinh_t(5.2))
print(sinh_t(1))
print(sinh_t(0))"""

def tanh_t(x):
    print("tanh(x) not implemented")
    return "err"

def root_t(x,y):
    print("y/(x) not implemented")
    return "err"

def atan_t(x):
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
    
"""print(atan_t(50000))
print(atan_t(0.9))
print(atan_t(-0.9))
print(atan_t(-2))"""

def exp_t(x):
    xk= 1
    for n in range (1,iterMax):
        xk1=xk+power_t(x,n)*div_t(fact(n))
        error = abs(xk1-xk)
        if error<tol:
            return xk1
        xk=xk1
    
    return xk1

"""
print(exp_t(19))
print(exp_t(0))
print(exp_t(1))
"""
def cos_t(x):
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
"""print(cos_t(19))
print(cos_t(5.2))
print(cos_t(1))
print(cos_t(0))
print(cos_t(38))"""

def sec_t(x):
    return div_t(cos_t(x))
"""print(sec_t(30))
print(sec_t(-30))
print(sec_t(7.8))
print(sec_t(0))"""

def tan_t(x):
    return sin_t(x)* div_t(cos_t(x))
"""print(tan_t(30))
print(tan_t(0.9))
print(tan_t(-0.9))
print(tan_t(-2))"""

#no se puede con negativos
def ln_t(x):
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

"""print(ln_t(2))
print(ln_t(970))
print(ln_t(1565464))"""

#no funciona con negativos
def log_t(x, y):
    return ln_t(x)* div_t(ln_t(y))
"""print(log_t(7,454542))
print(log_t(10,5))
print(log_t(10.5656,5.2))
print(log_t(1,0))#deberia dar error creo
print(log_t(0,5.2))#deberia dar error creo"""

def cosh_t(x):
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
"""print(cosh_t(19))
print(cosh_t(5.2))
print(cosh_t(1))
print(cosh_t(0))
print(cosh_t(50))"""

def sqrt_t(x):
    print("sqrt(x) not implemented")
    return "err"

def asin_t(x):
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

"""print(asin_t(0))
print(asin_t(0.22))
print(asin_t(0.56))
print(asin_t(-1))
print(asin_t(2))"""

def csc_t(x):
    return div_t(sin_t(x))
"""print(csc_t(0))
print(csc_t(0.22))
print(csc_t(0.56))
print(csc_t(-1))
print(csc_t(2))"""

def cot_t(x):
    return div_t(tan_t(x))

"""print(cot_t(0))
print(cot_t(0.22))
print(cot_t(0.56))
print(cot_t(-1))
print(cot_t(2))"""

def acos_t(x):
    return pi*div_t(2) - asin_t(x)

"""print(acos_t(0.56))
print(acos_t(-0.56))"""

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