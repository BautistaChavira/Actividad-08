import math

def distanciaEuclidiana(x1, y1, x2, y2):
    diferenciaX = pow((x2 - x1), 2)
    diferenciaY = pow((y2 - y1), 2)
    resultado = math.sqrt(diferenciaX + diferenciaY)
    return (resultado)