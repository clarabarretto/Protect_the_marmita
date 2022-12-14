# Protect the Marmita.

  Protect The Marmita é um jogo top-down shooter desenvolvido usando Pygame baseado no minigame Journey of The Prairie King de Stardew Valley, de onde tiramos grande parte da jogabilidade e algumas sprites também. O jogador controla um atirador e deve matar hordas de ladrões de marmitas para coletar alguns itens especiais que vão te ajudar nessa jornada até que consiga vencer todos os inimigos que vierem tentar terminar com o jogo.
  O jogador começa a fase com 5 corações de vida, perdendo um de vida sempre que colide com um inimigo, a bota aumenta a velocidade do seu persoangem facilitando na hora de se movimentar pelo mapa e a arma é o item especial do jogo que faz com que as balas vão em todas as direções. Ambas são upgrades permanentes enquanto os corações são itens consumíveis, podendo ter mais de um na tela ao mesmo tempo. 
#
## Equipe:
>- Geydson Renan <grml>
>- Gabriel Aragão <gaca>
>- Antonio Henrique <ahsl>
>- Maria Beatriz Martins <mbmpg>
>- Rodrigo Barbosa <rbo3>
>- Maria Clara Barretto <mcfgb>

## Como Rodar o Jogo:
>- Basta Ter o Python e o Pygame instalados em sua Máquina.
>
> 
>- Clonar este repositório ou baixar o aquivo zip.
>
>- Rodar o arquivo main.py.

## Controles:
  |            Teclas              |          Descrição           |
  | ------------------------------ | -------------------------- |
  | **W-A-S-D** | movimento |
  | **setas** | atira |
  | **tecla de espaço** | colecta corações |
  
## Itens:
  |            Itens              |          Efeitos           |
  | ------------------------------ | -------------------------- |
  | **Boots of Swiftness** | aumento da velocidade do personagem por um tempo específico |
  | **Heart Pieces** | aumenta em uma unidade a vida máxima |
  | **Special Gun** | ativa tiros em todas as direções possíveis temporariamente |
  | **Fast Shots** | A cadência de tiros aumenta |
  | **Reaper** | Todos inimigos são derrotados de uma vez só |
#

## Divisão de tarefas:

|      Equipes      |     Tarefas (principal)     |
| ------------------- | ------------------- |
|  **gaca** e  **rbo3**|  Criação dos itens, Sistema de colisão com o personagem e Sistema de Musica|
|  **grml** e **mbmpg** |  Criação do Personagem juntamente com suas mecanicas e Criação do mapa |
|  **ahsl** e **mcfgb** |  Tela Inicial, Organização do código e Assistencia na lógica de códigos |

  
  
  
  #
  ## Bibliotecas e Ferramentas:
|      Biblioteca e ferramentas      |     Aplicação     |
| ------------------- | ------------------- |
|  PyGame  |  A biblioteca pygame é a principal de nosso projeto, uma vez que se trata de uma jogo, essa biblioteca é capaz de facilitar a criação de um jogo, tendo diversas funções específicas para cada parte de um projeto desses, como renderização de objetos e interação entre eles |
|  Random  |  Utilizamos essa biblitoteca, para gerar números aleatórios com randint, que escolhe um número aleatoriamente no intervalo que definimos. Isso foi aplicado em diversas partes do código, como na definição do drop e se o inimigo seguirá o player ou atacará a geladeira.|
|  Sys |  Da bibliotca Sys, utilizamos a função exit, que é capaz de parar o código sem ter que gerar um erro para isso. Utilizamos isso, nas situações em que precisavamos finalizar o jogo, no caso quando ele acabava ou exitia uma situação que o levava ao fim. |
| Piskel |  Essa é uma ferramenta que serve como editor de sprites, dela fizemos uso bem intenso, basicamene para formatar todas sprites usadas no jogo além de criar algumas. |
  
  
#
## Conceitos e Aplicação:
> A aplicação do que foi desenvolvido no decorrer da cadeira, pode ser visto por todo o código.  A utilização de laços de repetição é uma das que pode ser notada o mais facilmente, uma vez que o nosso jogo roda inteirmente dentro de um "while", e dentro dele temos diversos "for" que para cada tipo de resposta do sistema faz uma ação.
  As listas também são muito presentes, uma vez que são a base para nosso sistema de drop de powerUps, além de utilizarmos ela para organizarmos nossas sprites, o maior exemplod disso, é o mapa do próprio jogo, que é uma lista com diversas listas dentro, formando uma grande matriz e assim definindo diretamente onde cada sprite será renderizada. Ainda falando dessa definição estética do projeto, as tuplas também são muito usadas nela, uma vez que na biblioteca do pygame são muito usadas para definir posições e cores para objetos criados.
  Por fim os conceitos que acredito que tenham sido os mais utilizados na produção do jogo, foram o de condicionais e classe. As condicionaus estão prezentes em todo o código, servindo como direção para o compilador, assim como um jogo depende literamete da situação específica que esta acontecendo naquele loop do laço do jogo pricipal, as situações possiveis e suas respostas devem estar contidas neles, e são organizadas e indicadas pelas condicionais. As classes, são a base do jogo, responsáveis pela base da criação de inimigos, balas e objetos do nosso jogo, o que demosntra a grande participação desse conceito em todo nosso projeto e sua importância.  
  
#
## Organização do código:
>- Sounds: Uma pasta que contém todos os sons utilizados no jogo.
>- Sprites: Pasta que salva os arquivos de imagens utilizados no jogo, tanto em personagens, objetos e mapa.
>- drops.py: Módulo específico para as funcionalidade de drop de itens.
>- enemies.py: Módulo com as funções responsáveis pela criação e definição de ação dos inimigos.
>- mapa.py: Módulo específico para a criação e definição do mapa com as sprites sendo alocadas de acordo com a definição em matriz do mapa.
>- obstáculo.py: Módulo responsável pelas interações, contendo as funções necessárias para a ocorrência delas.
>- personagem.py: Módulo que define o personagem juntamente com suas funcionalidades.
>- projetil.py: Módulo que é responsável pela física e aplicabilidade dos projeteis utilizados mo jogo (as balas do personagem principal).
>- main.py: Onde o laço principal responsável pelo jogo é encontrado. Aqui também é o local onde todos os outros módulos são importados e colocados em uso no laço principal.
  
#
## Desafios/Experiência:

> Em relação a erros, no início do projeto tivemos ideias grandiosas demais, mas ainda não tínhamos contato nenhum com a biblioteca do pygame e nem com um projeto dessa escala. Por isso acabamos por perder um tempo no início do projeto com uma ideia que era muito fora do nosso alcance dado o tempo e experiência. Felizmente percebemos isso rápido e conseguimos mudar onosso objetivo e abordagem, fazendo assim, esse jogo que apresentamos agora, que não acaba por ser muito grandioso, porém gostamos muito do seu rsultado final.
>
> Coordenar o trabalho da equipe, quem vai fazer o que, como cada pessoa está fazendo sua parte, como juntar o que foi feito, assim como o uso do github, ferramenta que muitos dos membros do grupo não estavam familiarizados, foram alguns dos maiores problemas encontrados. Mas com o proceder do trabalho e estudo do gitHub principalmente, essas dificuldades acabaram sumindo bastante, já que as atividades de cada um ficaram bem definidas e o entendimento da ferramenta também e assim a criação dojogo acabou fluindo até melhor do que pensamos.
>
>Portanto, após a produção desse projeto, podemos olhar para trás e perceber o quão importanteé um planejamento e a organização de equipe, uma pequena equipe bem entrosada e definida consegue fazer algo muito mais bem feito do que uma gigante que não se ajuda. Assim fica a lição aprendida nesse trabalho é que nunca se sabe tudo, sempre alguém poderá ajudar naquilo que é preciso e que se deve ter humildde para aceitar essa ajuda.
  
#
## Organização do Código
>


#
#
## Imagens do jogo:
![image](https://user-images.githubusercontent.com/108024639/200386203-ab8e6eb7-bbd9-42a6-9439-8f92a58f2b20.png)
#
![image](https://user-images.githubusercontent.com/108024639/200386332-3ec6f3fc-b665-4a63-a67f-e55495908ee3.png)
#
![image](https://user-images.githubusercontent.com/108024639/200386365-aa0eee85-6513-4a8d-abeb-622993a3027f.png)
 #
![image](https://user-images.githubusercontent.com/108024639/200372800-947da521-2094-4fa2-b353-b7866ac4de6a.png)
#
![image](https://user-images.githubusercontent.com/108024639/200414194-2bd5b9d4-d16a-4938-8981-3e998f1e1cbe.png)





