import time
from avl import AVL
from leitor import inserir_arquivo_em_avl

arvore = AVL()
inicio = time.time()

raiz, total_palavras = inserir_arquivo_em_avl("texto_origem.txt", arvore)

fim = time.time()
tempo = fim - inicio

arvore.gerar_indice_remissivo_txt(raiz,"indice_remissivo.txt",total_palavras,tempo)