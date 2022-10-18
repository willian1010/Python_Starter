# Tabuada do valor especificado pelo usuario.
# Aqui é introdusido um novo metodo de preenchimento dos prints como informado na linha 8.
# Tambem introdusido o for como estrutura de repetição a funcao range (x,x) cria o inicio e o fim da contagem de i.
# (nota: o else intro dus o codigo apos o fim do for).

# num=X(input('Digite qual TABUADA deseja: '));
# dependendo do q é posto no lugar de X ele vai reagir de uma forma,
# caso deixe sem nada como no programa ele vai aceitar qual quer coisa e fazer a operação,
# (o q pode ser posto que eu sei no momento é float, int, acredito que char e ou doble(essas ultimas duas eu n tenho certeza)).

num=(input('Digite qual TABUADA deseja: '));

for i in range (1, 11):
    
    print('{:2} x {:2} = {:2}'.format(num,i,num*i));
else:
    print('-'*15);