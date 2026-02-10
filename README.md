# Trabalho_AVL_python
Trabalho Índice Remissivo usando AVL

Nomes: João Daniel Ramires Esteves e Théo Magalhaes

Relatório – Implementação de Índice Remissivo utilizando Árvore AVL

1 - Introdução

Este trabalho tem como objetivo o desenvolvimento de um índice remissivo a partir de um arquivo texto, utilizando como estrutura de dados uma Árvore AVL. O índice remissivo permite associar cada palavra distinta do texto às linhas em que ela aparece, garantindo ordenação alfabética e eficiência nas operações de busca, inserção e remoção.

A escolha da Árvore AVL justifica-se por ser uma árvore binária de busca auto-balanceada, assegurando que as operações fundamentais apresentem eficiência, mesmo para grandes volumes de dados.

2 - Estrutura de Dados Utilizada

Nó da Árvore: Cada nó da Árvore AVL armazena: Uma palavra do texto; Uma lista contendo os números das linhas em que a palavra aparece; Referências para os filhos esquerdo e direito; A altura do nó, utilizada para o balanceamento da árvore.

Essa estrutura permite representar eficientemente o índice remissivo, evitando a duplicação de palavras e mantendo o registro completo das linhas associadas a cada termo.

3 - Leitura e Processamento do Arquivo Texto

O arquivo de entrada no formato .txt é lido linha a linha. Durante esse processo:

Os símbolos de pontuação são utilizados apenas como delimitadores, não sendo incorporados às palavras;
Todas as palavras são convertidas para letras minúsculas, evitando duplicidade por diferença de capitalização;
Cada palavra encontrada é inserida na Árvore AVL juntamente com o número da linha correspondente.
Caso a palavra já exista na árvore, apenas a linha é adicionada à lista do nó, desde que ainda não esteja presente.

4 - Inserção na Árvore AVL

A operação de inserção segue as regras da Árvore Binária de Busca, utilizando a ordem lexicográfica das palavras. Após cada inserção:

A altura dos nós é atualizada;
O fator de balanceamento é verificado;
Se necessário, rotações simples ou duplas são executadas para restaurar o balanceamento da árvore.
Quando uma palavra já está presente, não é criado um novo nó. Apenas a linha correspondente é adicionada à lista associada à palavra.

5 - Busca de Palavras

A função de busca percorre a Árvore AVL comparando a palavra desejada com os valores armazenados nos nós, respeitando a ordem lexicográfica. Caso a palavra seja encontrada, o nó correspondente é retornado; caso contrário, o resultado indica que a palavra não existe no índice.

A decisão sobre a mensagem exibida ao usuário é realizada na função principal, separando a lógica da estrutura de dados da interface com o usuário.

6 - Remoção de Palavras e Linhas

A remoção foi implementada considerando duas situações:

Remoção de uma linha específica:
A linha indicada é removida da lista do nó correspondente à palavra.

Remoção do nó:

Caso, após a remoção da linha, a lista fique vazia, o nó inteiro é removido da árvore.
Após a remoção, a árvore tem suas alturas recalculadas e, se necessário, rotações são aplicadas para manter o balanceamento AVL.

7 - Busca Aproximada por Prefixo

Foi implementada uma função de busca aproximada que retorna todas as palavras da árvore que se iniciam com um determinado prefixo. Essa funcionalidade explora a ordenação natural da Árvore AVL, permitindo a recuperação das palavras em ordem alfabética.

Essa busca é útil para consultas parciais, como em mecanismos de autocompletar ou sugestões de termos.

8 - Medidor de Equilíbrio (ME)

Além das operações tradicionais, foi implementada uma função de busca que calcula o Medidor de Equilíbrio (ME) de um nó quando a palavra é encontrada. O ME é definido como a diferença entre o número de nós da subárvore esquerda e o número de nós da subárvore direita.

O comportamento da função é definido da seguinte forma:

Retorna -1 se a palavra não for encontrada;
Retorna 0 se a palavra for encontrada e o ME for igual a zero;
Retorna 1 se a palavra for encontrada e o ME for diferente de zero, imprimindo o valor do ME.

É importante destacar que o ME não representa o fator de balanceamento da AVL, pois considera a quantidade de nós, e não a altura das subárvores. Por esse motivo, é raro que o ME seja igual a zero em árvores grandes, mesmo que estejam perfeitamente balanceadas em termos de altura.

9 - Palavra Mais Frequente

Foi implementada uma função que percorre a Árvore AVL e identifica a palavra mais frequente, definida como aquela que aparece no maior número de linhas do documento.

O tempo dssa operação cresce na mesma proporção do número de elementos, pois é necessário visitar todos os nós da árvore para comparar o tamanho da lista de linhas associada a cada palavra.

10 - Geração do Índice Remissivo em Arquivo Texto

O índice remissivo completo é gerado em um arquivo .txt, contendo:

Todas as palavras em ordem alfabética, acompanhadas das linhas em que aparecem;
Estatísticas finais do processamento, incluindo:
Total de palavras lidas do texto;
Total de palavras distintas;
Total de palavras descartadas (repetidas);
Tempo de construção da árvore;
Total de rotações executadas durante o balanceamento.

O tempo de construção é medido utilizando funções de temporização, permitindo avaliar o desempenho da solução.

11 - Conclusão

Neste trabalho, foi possível desenvolver um índice remissivo eficiente utilizando uma Árvore AVL, garantindo ordenação alfabética e bom desempenho mesmo para grandes volumes de dados. As funcionalidades implementadas abrangem inserção, busca, remoção, buscas aproximadas e geração de relatórios estatísticos.

A utilização da Árvore AVL mostrou-se adequada para o problema proposto, oferecendo uma solução robusta e conceitualmente alinhada aos fundamentos de estruturas de dados avançadas.

Demonstrações de algumas operações feitas sobre a árvore AVL, com exemplos de código e com as saídas obtidas, podem ser encontrados no arquivo exemplos.py
