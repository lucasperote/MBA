from lib import download_dataset
from lib import preencher_matriz_contratos
from lib import imprimir_matriz
from lib import exportar_csv

def main():
    # Download do dataset
    link_txt = "https://drive.google.com/uc?id=1YFPo-k9yyzitXp6HTfCfbselD1DUSJ4K" 
    file_txt = 'entradagrande.txt'
    download_dataset(link_txt, file_txt)

    # Preenche a matriz de contratos
    m, n, t, matriz = preencher_matriz_contratos(file_txt)

    # Imprime os resultados
    print(f"Valores gerais: m={m}, n={n}, t={t}\n")
    imprimir_matriz(matriz)

    # Exporta os resultados para um arquivo CSV
    file_csv = "contratos.csv"
    exportar_csv(file_csv, matriz)

if __name__ == "__main__":
    main()