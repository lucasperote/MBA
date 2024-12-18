import csv
from gdown import download

# Definir a função download_from_drive
def download_dataset(link, filename):
    download(link, filename, quiet=False)

    return None

# Função para inicializar a matriz de contratos
def inicializar_matriz(n, m):
    contratos = [[[float('inf')] * (m + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    return contratos

# Função para preencher a matriz com os contratos
def preencher_matriz(contratos, fornecedores, m):
    for contrato in fornecedores:
        fornecedor, inicio, fim, valor = contrato
        contratos[fornecedor][inicio][fim] = min(contratos[fornecedor][inicio][fim], valor)

# Função para processar os dados de entrada e preencher a matriz de contratos
def preencher_matriz_contratos(nome_arquivo: str):
    # Processa os dados de entrada
    with open(nome_arquivo, 'r') as f:
        m, n, t = map(float, f.readline().split())
        m, n = int(m), int(n)

        fornecedores = []
        for linha in f:
            fornecedor, inicio, fim, valor = map(float, linha.split())
            fornecedor, inicio, fim = int(fornecedor), int(inicio), int(fim)
            fornecedores.append((fornecedor, inicio, fim, valor))

    # Inicializa e preenche a matriz
    contratos = inicializar_matriz(n, m)
    preencher_matriz(contratos, fornecedores, m)

    return m, n, t, contratos

# Função para imprimir a matriz de contratos
def imprimir_matriz(matriz, k=None):
    for fornecedor in range(1, len(matriz)):
        print(f'Fornecedor {fornecedor}:')
        for i in range(1, len(matriz[0])):
            print(matriz[fornecedor][i][1:])
        print()
    return None

# Função para exportar a matriz para um arquivo CSV
def exportar_csv(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Fornecedor', 'Inicio', 'Fim', 'Valor'])
        for fornecedor in range(1, len(matriz)):
            for i in range(1, len(matriz[fornecedor])):
                for j in range(1, len(matriz[fornecedor][i])):
                    valor = matriz[fornecedor][i][j]
                    if valor != float('inf'):
                        writer.writerow([fornecedor, i, j, valor])
    return None