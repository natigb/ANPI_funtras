# Función para probar la libreria funtras.
import funtras as f

a= f.sin_t(3*f.div_t(7)) + f.ln_t(2)
b= f.sinh_t(f.sqrt_t(2))
c= f.atan_t(f.exp_t(-1))
result = (f.root_t(a,3)* f.div_t(b)) + c
print(result)