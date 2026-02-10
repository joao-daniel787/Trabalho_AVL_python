from no import No

class AVL:
    def __init__(self):
        self.rotacoes = 0

    def altura(self, no):
        return no.altura if no else 0

    def pegar_balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita) if no else 0

    def rotacao_direita(self, y):
        self.rotacoes += 1
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        self.rotacoes += 1
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def inserir(self, raiz, palavra, linha):
        if not raiz:
            return No(palavra, linha)

        if palavra == raiz.palavra:
            if linha not in raiz.linhas:
                raiz.linhas.append(linha)
            return raiz

        elif palavra < raiz.palavra:
            raiz.esquerda = self.inserir(raiz.esquerda, palavra, linha)
        else:
            raiz.direita = self.inserir(raiz.direita, palavra, linha)

        raiz.altura = 1 + max(self.altura(raiz.esquerda),
                          self.altura(raiz.direita))

        balanceamento = self.pegar_balanceamento(raiz)

        # Casos de rotação
        if balanceamento > 1 and palavra < raiz.esquerda.palavra:
            return self.rotacao_direita(raiz)

        if balanceamento < -1 and palavra > raiz.direita.palavra:
            return self.rotacao_esquerda(raiz)

        return raiz

    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(f"{raiz.palavra}: {raiz.linhas}")
            self.em_ordem(raiz.direita)

    def buscar(self, raiz, palavra):
        if not raiz or raiz.palavra == palavra:
            return raiz

        if palavra < raiz.palavra:
            return self.buscar(raiz.esquerda, palavra)
        else:
            return self.buscar(raiz.direita, palavra)
        
    def menor_valor(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual
    
    def remover(self, raiz, palavra, linha):
        if not raiz:
            return raiz

        if palavra < raiz.palavra:
            raiz.esquerda = self.remover(raiz.esquerda, palavra, linha)

        elif palavra > raiz.palavra:
            raiz.direita = self.remover(raiz.direita, palavra, linha)

        else:
            # Palavra encontrada
            if linha in raiz.linhas:
                raiz.linhas.remove(linha)

            # Se ainda restam linhas, NÃO remove o nó
            if len(raiz.linhas) > 0:
                return raiz

            # Remove o nó
            if not raiz.esquerda:
                return raiz.direita
            elif not raiz.direita:
                return raiz.esquerda

            # Nó com dois filhos
            temp = self.menor_valor(raiz.direita)
            raiz.palavra = temp.palavra
            raiz.linhas = temp.linhas.copy()
            raiz.direita = self.remover(raiz.direita, temp.palavra, temp.linhas[0])

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda),
                          self.altura(raiz.direita))

        balanceamento = self.pegar_balanceamento(raiz)

        if balanceamento > 1 and self.pegar_balanceamento(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)

        if balanceamento < -1 and self.pegar_balanceamento(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)

        return raiz
    
    def buscar_por_prefixo(self, raiz, prefixo):
        resultados = []
        self._buscar_prefixo(raiz, prefixo.lower(), resultados)
        return resultados
    
    def _buscar_prefixo(self, raiz, prefixo, resultados):
        if not raiz:
            return

        # Percorre esquerda
        self._buscar_prefixo(raiz.esquerda, prefixo, resultados)

        # Verifica prefixo
        if raiz.palavra.startswith(prefixo):
            resultados.append(raiz.palavra)

        # Percorre direita
        self._buscar_prefixo(raiz.direita, prefixo, resultados)

    def contar_nos(self, raiz):
        if not raiz:
            return 0
        return 1 + self.contar_nos(raiz.esquerda) + self.contar_nos(raiz.direita)

    def buscar_com_me(self, raiz, palavra):
        if not raiz:
            return -1

        if palavra < raiz.palavra:
            return self.buscar_com_me(raiz.esquerda, palavra)

        elif palavra > raiz.palavra:
            return self.buscar_com_me(raiz.direita, palavra)

        else:
            # Palavra encontrada
            qtd_esq = self.contar_nos(raiz.esquerda)
            qtd_dir = self.contar_nos(raiz.direita)

            me = qtd_esq - qtd_dir

            if me == 0:
                return 0
            else:
                print(f"\nMedidor de Equilíbrio (ME): {me}")
                return 1
            
    def palavra_mais_frequente(self, raiz):
        if not raiz:
            return None

        palavra = self._palavra_mais_frequente(raiz)
        return palavra

    def _palavra_mais_frequente(self, raiz):
        if not raiz:
            return None, 0

        # Frequência do nó atual
        freq_atual = len(raiz.linhas)

        # Frequência das subárvores
        palavra_esq, freq_esq = self._palavra_mais_frequente(raiz.esquerda)
        palavra_dir, freq_dir = self._palavra_mais_frequente(raiz.direita)

        # Determina o maior
        palavra_max = raiz.palavra
        freq_max = freq_atual

        if freq_esq > freq_max:
            palavra_max = palavra_esq
            freq_max = freq_esq

        if freq_dir > freq_max:
            palavra_max = palavra_dir
            freq_max = freq_dir

        return palavra_max, freq_max
    
    def contar_palavras_distintas(self, raiz):
        if not raiz:
            return 0
        return 1 + self.contar_palavras_distintas(raiz.esquerda) + self.contar_palavras_distintas(raiz.direita)

    def imprimir_indice(self, raiz, arquivo):
        if not raiz:
            return
        self.imprimir_indice(raiz.esquerda, arquivo)
        arquivo.write(f"{raiz.palavra}: {raiz.linhas}\n")
        self.imprimir_indice(raiz.direita, arquivo)

    def gerar_indice_remissivo_txt(arvore, raiz, nome_arquivo,
                               total_palavras,
                               tempo_construcao):
        with open(nome_arquivo, "w", encoding="utf-8") as arq:

            # Índice remissivo em ordem alfabética
            arvore.imprimir_indice(raiz, arq)

            arq.write("\n--- Estatísticas ---\n")

            total_distintas = arvore.contar_palavras_distintas(raiz)
            descartadas = total_palavras - total_distintas

            arq.write(f"Total de palavras: {total_palavras}\n")
            arq.write(f"Total de palavras distintas: {total_distintas}\n")
            arq.write(f"Total de palavras descartadas: {descartadas}\n")
            arq.write(f"Tempo de construção: {tempo_construcao:.3f} segundos\n")
            arq.write(f"Total de rotações executadas: {arvore.rotacoes}\n")