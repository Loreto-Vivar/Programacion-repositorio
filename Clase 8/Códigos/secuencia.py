def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia
numero = int(input("Ingrese la cantidad de términos de Fibonacci: "))
resultado = fibonacci(numero)
print("Secuencia de Fibonacci:" , resultado)