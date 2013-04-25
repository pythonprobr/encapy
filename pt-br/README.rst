==================================
Benchmark simples dos exemplos
==================================

Criando 100 000 instâncias em cada passo.

----- ----- ------------
passo tempo instancias/s
----- ----- ------------
  1   0.072     1388152
  2   0.104      962937
  3   0.175      572846
  4   1.338       74756
  5   0.179      557603
 5d   0.183      546265
  6   0.185      539266
 6d   0.189      529871
----- ----- ------------

As versões de 3 a 6 são equivalentes em funcionalidade: a validação é feita nos atributos ``peso`` e ``preco``. Na versão 2 apenas o ``peso`` é validado e na versão 1 não há validação.

Este benchmark é limitado pois a única operação feita é instanciação. Em um programa real, uma vez instanciados os objetos sofrem outras operações, o que significa que o custo da instanciação é mais diluído. Em outras palavras, este benchmark não garante que um programa sem validação será 3x mais rápido que um que usa validação de atributos por descriptors.
