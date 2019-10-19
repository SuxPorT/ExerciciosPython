# DESAFIO DE INDEXAÇÃO

## Instruções:

1. Ao iniciar o programa, o software deverá pedir ao usuário o nome do arquivo a ser indexado.

2. Durante a indexação, o arquivo deverá ser quebrado em linhas. Para encontrar o término de linha, assuma um ponto final
(“.”) ou uma quebra de linha computacional (“\n”).

3. O software deverá ignorar acentos e a diferença entre letras maiúsculas e minúsculas.

4. O software deverá requisitar ao usuário uma palavra a ser buscada, até que o comando seja digitado (assuma que este
comando será digitado com os comparadores de menor (<) e maior (>)).

5. Com cada palavra informada ao software, todas as frases do documento indexado deverão ser apresentadas.

6. Dica: a indexação do arquivo deverá ocorrer apenas uma vez, isto é, quando o software é inicializado. Isso significa que
a cada palavra informada pelo usuário, deverá ocorrer apenas a listagem das frases, e o arquivo original não deverá ser
percorrido.

Vejam um exemplo de proposta de interação com um software, onde as linhas iniciadas com > denotam conteúdo digitado pelo
usuário:

********************************

********* INDEXADOR *********

********************************

Digite o nome do arquivo a ser indexado:

> biblia.txt

Indexando… (esse processo pode demorar…)

OK! Foram indexadas X linhas.

Digite uma palavra para buscar:

> mentira

Buscando…

Ok! Encontrei as seguintes linhas:

 - Disse, pois, Dalila a Sansão: Eis que zombaste de mim, e me disseste mentiras; declara-me agora com que poderia ser a
 amarrado.

 - Disse Dalila a Sansão: Até agora zombaste de mim, e me disseste mentiras; declara-me pois, agora, com que poderia ser
 amarrado. E ele lhe disse: Se teceres as sete tranças da minha cabeça com os liços da teia.

 - …

Digite uma palavra para buscar:

> infiel

Buscando…

OK! Encontrei as seguintes linhas:

 - Dos seus próprios caminhos se fartará o infiel de coração, como também o homem bom se contentará dos seus.

 - E não fez ele somente um, ainda que lhe sobejava espírito? E por que somente um? Não é que buscava descendência piedosa?
 Portanto guardai-vos em vosso espírito, e que ninguém seja infiel para com a mulher da sua mocidade.

Digite uma palavra para buscar:


(software termina)
