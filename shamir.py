import random
from sympy import mod_inverse, nextprime

# Proporcionando el secreto, la cantidad de partes a dividir y el grado del polinomio
secreto = 500
cantidadPartes = 20
maxPolinomio = 6

# Iniciar las listas que almacenan los coeficientes de la funcion y las partes en las que se divide el polinomio
coeficientes = []
partes = []


def generar_polinomio():
    coeficientes.append(secreto)
    for i in range(1, maxPolinomio):
        coeficiente = random.randint(0, 100)
        coeficientes.append(coeficiente)


def dividir_secreto():
    for parteSecreto in range(1, cantidadPartes + 1):
        y = evaluar_polinomio(parteSecreto)
        partes.append(str(parteSecreto) + ", " + str(y))


def evaluar_polinomio(parte_secreto):
    y = 0.0
    for i in range(len(coeficientes)):
        y += coeficientes[i] * (parte_secreto ** i)
    return y


def recuperar_secreto(partes, num_a_determinar):
    secret = 0
    primo = 0
    for i in range(len(partes)):
        split = partes[i].split(", ")
        max_y = max(split, key=lambda x: split[0])
        primo = nextprime(max_y)
        x_i = float(split[0])
        y_i = float(split[1])
        term = y_i
        for j in range(len(partes)):
            if i != j:
                split_j = partes[j].split(", ")
                x_j = float(split_j[0])
                term = term * (num_a_determinar - x_j) * mod_inverse(x_i - x_j,primo)
        secret += term
    return round(secret)


# Crear el polinomio y dividir el secreto
generar_polinomio()
dividir_secreto()

for i in range(len(partes)):
    print(partes[i])

print("Clave recuperada: "+ str(recuperar_secreto(partes, 0)))
