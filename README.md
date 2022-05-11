# projetoIP - Equipe 5

# Título do projeto e membros da equipe

Abacaxiland

Iasmym Mendes (ilmf);
Nathaniel Rocha (nrs3);
Pedro Baptista (phab);
Rafaela Pitanga (raap);
Rubens Lima (rnl2).

# Link para repositório git

https://github.com/rubdelima/projetoIP


# Como funciona?

Bem vindo à Abacaxiland, você tem 1 minuto para colotar as frutas que vão caindo, mas tenha cuidado, nessa ilha houve ha muito tempo uma guerra que deixou bombas perigosas no seu caminho, esas bombas vão vazer você perder o seu precioso tempo e perderá 10 pontos. As frutas e suas pontuações respectivas são: Abacaxi, a mais deliciosa fruta da ilha lhe dá 10 pontos, a bela pitango lhe dará 9 pontos, e as bananas dão 7 pontos. Consiga pontuar mais e fazer uma deliciosa salada de frutas.

# Requerimentos do jogo e como instalar

Para rodar o jogo é necessário ter instalado na máquina o python, onde pode ser obtido de form oficial no site: https://www.python.org/, ou em bibliotecas próprias do seu Sistema Operacional, para Linux basta digitar no terminal "sudo apt install python3". A pós o Python instalado, você irá precisar instaar o pygame. Para instalar o pygame em SO que possuem bash (como MacOS e Linux) você ira digitar o comando no terminal com "pip3 install pygame", e no windowns você entrará no cmd e digitar "python3 -m pip install pygame", clonar este repositório e colocar para executar no arquivo main.py

# A organização do código

O código foi dividido em 4 arquivos, no qual no arquivo principal (Main.py) importamos as bibliotecas utilizadas e realizamos as configurações do jogo como um todo (criação da tela, player, variáveis, background, etc.), essas associadas ao código do ambiente, jogador e objetos do jogo, o qual dividimos em outros 3 arquivos (ambiente.py, objetos.py e player.py). Também registramos todas as referências de imagens, além de organizá-las em pastas separadas das fontes e músicas/efeitos sonoros utilizados no projeto.

# Ferramentas, bibliotecas, frameworks utilizados

O código foi desenvolvido com a linguagem de Python, através do Visual Studio Code, e contou com algumas alterações no próprio Github, principalmente porque a maioria dos integrantes do grupo já utilizava essa ferramenta e possuia maior familiaridade. 
Quanto ao uso de bibliotecas, adicionamos ao nosso código o Pygame, para implementar gráficos e operações para a base do jogo, e também Random, o qual usamos para escolher de forma aleatória a posição linear e a classe dos objetos coletados.

# A divisão do trabalho dentro do grupo

A parte de desenvolvimento e lógica do código foi mais trabalhada por Nathaniel, Pedro e Rubens. Já a parte gráfica teve maior participação de Iasmym e Rafaela. Em questão de ideias para o desenvolvimento geral do projeto, todos participaram e trabalharam juntos, sempre testando e discutindo o que seria feito.

# Conceitos que foram apresentados durante a disciplina e utilizados no projeto

No nosso código, fizemos uso das condições, laços de repetição e funções.
As condições foram usadas, principalmente, dentro das funções do main.py e objetos.py, como por exemplo para gerar a queda aleatória das frutas, e ainda dentro dos laços de repetição do arquivo principal para rodar o jogo (abrir e fechar a janela).
As funções também foram amplamente utilizadas ao longo do código, definindo comandos de movimento do jogador, aparição da pontuação, aparição de objetos (frutas, bombas) junto às condições, além de conter informações das cores, imagens e ambientes.


# Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?

O maior erro cometido pela nossa equipe foi na divisão de tarefas, principalmente por a gente não saber exatamente, de início, como tudo seria feito. Isso talvez tenha ficado um pouco desequilibrado, mas a gente entendia e sempre tentava se encontrar de forma presencial, ou por meio de chamadas online com o Discord para conversar sobre o que cada um estava fazendo e poder alinhar tudo da melhor forma e com a participação de todos.

# Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?

Manipular o código em diferentes arquivos, para alguns estudantes, pois não foi abordado anteriormente na disciplina; adminstrar melhor o tempo com outras cadeiras do curso. O primeiro item foi resolvido com uma explicação de alguns integrantes mais experientes na linguagem que facilitaram o entendimento do sistema, bem como acompanhamento presencial. Já o segundo item, nós lidamos por meio de uma divisão equitativa de acordo com a dispoiblidade de tempo de cada um, e os integrantes que possuíam uma carga de trabalho e estudo menor, ficavam com mais funções e auxiliavam os demais.

# Quais as lições aprendidas durante o projeto?

Uma das principais lições que aprendemos com o projeto foi a importância de escrever e manter o código o mais limpo possível, principalmente pela facilidade que isso traz de editar e até o entender melhor posteriormente, ainda mais trabalhando em equipe. Também trouxe uma experiência nova (para alguns) em relação a trabalho em grupo por meio do GitHub, e na utilidade e importância que essa ferramenta possui para a realização de projetos desse tipo, além de termos treinado bastante seu uso.
