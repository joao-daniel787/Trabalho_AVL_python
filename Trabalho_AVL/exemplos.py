from avl import AVL
from leitor import inserir_arquivo_em_avl

arvore = AVL()
raiz, total_palavras = inserir_arquivo_em_avl("texto_origem.txt", arvore)

print("Índice remissivo:\n")
arvore.em_ordem(raiz)

# Exemplo função buscar
lista = [arvore.buscar(raiz, "joao"), arvore.buscar(raiz, "rei")]
for i in lista:
    resultado = i

    if resultado:
        print("\nPalavra encontrada.")
        print(f"Linhas: {resultado.linhas}")
    else:
        print("\nPalavra não encontrada.")

# Exemplo função buscar por prefixo
resultado_prefx = arvore.buscar_por_prefixo(raiz, "al")
print("\nBusca com prefixo al", resultado_prefx, "\n")

# Exemplo função inserção e remoção em uma arvore separada
arvore2 = AVL()
raiz2 = None

raiz2 = arvore2.inserir(raiz2, "teste", 1)
raiz2 = arvore2.inserir(raiz2, "joao", 2)
raiz2 = arvore2.inserir(raiz2, "abacaxi", 3)

print("Antes da remoção:")
arvore2.em_ordem(raiz2)

raiz2 = arvore2.remover(raiz2, "joao", 2)

print("\nApós remover linha 2:")
arvore2.em_ordem(raiz2)

# Exemplo função medidor de equilibrio
resultado_me = arvore.buscar_com_me(raiz, "a")

if resultado_me == -1:
    print("\nPalavra não encontrada na árvore.")
elif resultado_me == 0:
    print("Palavra encontrada e a subárvore está perfeitamente equilibrada.")
else:
    print("Palavra encontrada e a subárvore NÃO está equilibrada.")

# Exemplo função palavra mais frequente
palavra = arvore.palavra_mais_frequente(raiz)

if palavra != None:
    print(f"\nPalavra mais frequente (em número de linhas): {palavra}")
else:
    print("\nA árvore está vazia.")