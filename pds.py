import numpy as np
import matplotlib.pyplot as plt


# Graficar funciones discretas
def plot_discrete(n, X, 
                  xlabel = "Número de muestras",
                  ylabel = "Amplitud"):
    plt.stem(n, X)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()


# Inicializar vectores de funciones fundamentales
def init_function(N=7, k=0, reflexed=False):
    # Calcular el origen basado en el desplazamiento
    origin = k

    # Vector de muestras
    n = np.array(range(origin - N // 2, origin + N // 2 + (1 if N % 2 == 1 else 0)))

    # Aplicar la reflexión en caso de ser solicitado
    n = -n if reflexed else n

    # Vector de valores
    X = np.zeros(N)

    return n, X


# Delta de Kronecker
def delta(N=7, k=0, A=1, reflexed=False):
    n, X = init_function(N=N, k=k, reflexed=reflexed)

    # Asignar los valores característicos del delta
    X[np.where(n == (-1 if reflexed else 1) * k)] = A

    return n, X


# Función escalón unitario
def step(N=7, k=0, A=1, reflexed=False):
    n, X = init_function(N=N, k=k, reflexed=reflexed)

    # Asignar los valores característicos del escalón
    X[np.where(n >= (-1 if reflexed else 1) * k)] = A

    return n, X


# Función rampa
def ramp(N=7, k=0, A=1, reflexed=False):
    n, X = init_function(N=N, k=k, reflexed=reflexed)

    # Asignar los valores característicos del escalón
    X[np.where(n >= (-1 if reflexed else 1) * k)] = A
    # Multiplicar cada valor por el n - k para hacer la rampa
    X = np.array([x * (n_i - k + 1) for x, n_i in zip(X, n)])

    return n, X
