import numpy as np
import matplotlib.pyplot as plt


# Graficar funciones discretas
def plot_discrete(n, X, xlabel="Número de muestras", ylabel="Amplitud", label="Señal"):
    plt.stem(n, X, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="upper right")
    plt.grid()


# Crear las funciones básicas
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


def delta(N=7, k=0, A=1, reflexed=False):
    n, X = init_function(N=N, k=k, reflexed=reflexed)

    # Asignar los valores característicos del delta
    X[np.where(n == (-1 if reflexed else 1) * k)] = A

    return n, X


def step(N=7, k=0, A=1, reflexed=False):
    n, X = init_function(N=N, k=k, reflexed=reflexed)

    # Asignar los valores característicos del escalón
    if reflexed:
        X[np.where(n <= (-1) * k)] = A
    else:
        X[np.where(n >= k)] = A

    return n, X


def ramp(N=7, k=0, A=1, reflexed=False):
    n, X = init_function(N=N, k=k, reflexed=reflexed)

    # Asignar los valores característicos del escalón
    if reflexed:
        X[np.where(n < (-1) * k)] = A
        X = np.array([-x * (n_i + k) for x, n_i in zip(X, n)])
    else:
        X[np.where(n > k)] = A
        X = np.array([x * (n_i - k) for x, n_i in zip(X, n)])
    # Multiplicar cada valor por el n - k para hacer la rampa

    return n, X


# Función para añadir ruido blanco
def noise(X: np.ndarray, snr: float):
    # Calcular la potencia en dB de la señal original
    X_avg_p = np.mean(np.power(X, 2))
    X_avg_db = 10 * np.log10(X_avg_p)

    # Calcular la potencia en dB del ruido
    noise_avg_db = X_avg_db - snr
    noise_avg_p = np.power(10, noise_avg_db / 10)

    # Crear el vector de ruido con distribución normal
    noise = np.random.normal(scale=np.sqrt(noise_avg_p), size=len(X))
    return X + noise
