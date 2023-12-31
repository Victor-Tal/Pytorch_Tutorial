#-----------------------------------------------
# Cordero Correa Victor Hugo

#-----------------------------------------------
import torch

# Todo en pytorch se basa en operaciones de Tensor.
# Un tensor puede tener diferentes dimensiones
# Así que puede ser 1D, 2D o incluso 3D y superior

# escalar, vector, matriz, tensor

# torch.empty(size)
x = torch.empty(1) # escalar
print(x)
x = torch.empty(3) # vector, 1D
print(x)
#----------------------------------------
#Tensor en R2XR3
#-----------------------------------------

x = torch.empty(2,3) # matrix, 2D
print(x)
#-------------------------------------
#Torch.rand(size):número aleatorio[0,1]
x = torch.empty(2,2,3) # tensor, 3 dimensions
#x = torch.empty(2,2,2,3) # tensor, 4 dimensions
print(x)

# torch.rand(size): numeros de[0, 1]
x = torch.rand(5, 3)
print(x)

# Tensor de R5XR3 lleno de ceros
x = torch.zeros(5, 3)
print(x)

# Checar tamaño del vector
#---------------------------------
print(x.size())

# chacar tipo de datos(defaul float32)
#------------------------------
print(x.dtype)

# Especificando tipo de datos
#-------------------------------------
x = torch.zeros(5, 3, dtype=torch.float16)
print(x)
print(x.dtype)

# Construir vectores con datos
#----------------------------------
x = torch.tensor([5.5, 3])
print(x.size())

# requires_grad argumento
# Esto le dirá a pytorch que necesitará calcular los gradientes para este tensor
# más adelante en sus pasos de optimización
# es decir, esta es una variable en su modelo que desea optimizar


#
#Vector optimizable(requiere gradiente)
#----------------------------------------
x = torch.tensor([5.5, 3], requires_grad=True)

# Suma de tensores(componente a componente)
y = torch.rand(2, 2)
x = torch.rand(2, 2)

# elementos adicionales
z = x + y

# Además de lugar, todo con un guión bajo final es una operación en el lugar
# es decir, modificará la variable
# y.add_(x)

# Resta de tensores
#--------------------------
z = x - y
z = torch.sub(x, y)
#---------------------------------
# multiplicación de vectores
#---------------------------------
z = x * y
z = torch.mul(x,y)

#---------------------
# division
#--------------------
z = x / y
z = torch.div(x,y)

# ------------------------
#Rebanadas de tensores 
#-------------------------
x = torch.rand(5,3)
print(x)
print(x[:, 0]) # todos los renglones, columna 0
print(x[1, :]) # renglon1, todas las columnas
print(x[1,1]) # elemento  1, 1

# Valor del elemento
print(x[1,1].item())

# Cambia formas con torch.view()
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # -1: se infiere de las otras dimenciones
print(x.size(), y.size(), z.size())

# Numpy
# Convertir un tensor de antorcha en una matriz NumPy y viceversa es muy fácil
a = torch.ones(5)
print(a)

# torch a numpy con .numpy()
b = a.numpy()
print(b)
print(type(b))

# Carful: Si el Tensor está en la CPU (no en la GPU),
# Ambos objetos compartirán la misma ubicación de memoria, por lo que cambiar uno
# también cambiará el otro
a.add_(1)
print(a)
print(b)

# De numpy a torch with .from_numpy(x)
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
print(a)
print(b)

#----------------------------------------
# le suma 1 a todas las entradas de A
#----------------------------------------
a += 1
print(a)
print(b)

# por defecto todos los tensores se crean en la CPU,
# pero también puedes moverlos a la GPU (solo si está disponible)
#----------------
#DE CPU A GPU
#----------------
if torch.cuda.is_available():
    device = torch.device("cuda")          # Tarjeta de video
    y = torch.ones_like(x, device=device)  # crar tensor en el GPU
    x = x.to(device)                       # Copiar a GPU y usar ``.to("cuda")``
    z = x + y
    # z = z.numpy() # no es posible porque numpy no puede manejar tenores de GPU
    # mover a la CPU de nuevo
    #DE VUELTA AL CPU
    z.to("cpu")    
    # z = z.numpy()