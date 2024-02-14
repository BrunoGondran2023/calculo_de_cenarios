import math
import numpy as np
import statistics as st

def calcular_cenarios(vetor):
    """
    Calcula cenários otimistas e pessimistas com base nos dados fornecidos.

    Args:
        vetor (numpy.ndarray): Um vetor numpy contendo os dados financeiros.

    Returns:
        tuple: Uma tupla contendo os cenários otimistas e pessimistas.
    """
    if len(vetor) >= 2:
        retorno = (vetor[1:] - vetor[:-1]) / vetor[:-1]
    else:
        retorno = np.array([])

    if len(retorno) > 0:
        media = st.mean(retorno)
        desvio = st.pstdev(retorno)

        n = len(retorno)
        otimista = media + 2 * desvio / math.sqrt(n)
        pessimista = media - 2 * desvio / math.sqrt(n)

        return otimista, pessimista
    else:
        return None, None

if __name__ == "__main__":
    # Exemplo de uso
    vetor = np.array([1.31, 1.34, 1.42, 1.4, 1.42, 1.4, 1.47, 1.45, 1.48, 1.42,
                      1.34, 1.34, 1.35, 1.35, 1.36, 1.32, 1.24, 1.22, 1.27, 1.26])
    otimista, pessimista = calcular_cenarios(vetor)
    if otimista is not None:
        print(f'Cenário otimista: {round(otimista * 100, 1)}%\nCenário pessimista: {round(pessimista * 100, 1)}%')
    else:
        print("Não há dados suficientes para calcular os cenários.")
