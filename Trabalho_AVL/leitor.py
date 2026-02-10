import re

def inserir_arquivo_em_avl(nome_arquivo, arvore):
    raiz = None
    total_palavras = 0

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for num_linha, linha in enumerate(arquivo, start=1):

            # Remove pontuação e transforma em minúsculas
            palavras = re.findall(r'\b\w+\b', linha.lower())

            for palavra in palavras:
                total_palavras += 1
                raiz = arvore.inserir(raiz, palavra, num_linha)

    return raiz, total_palavras