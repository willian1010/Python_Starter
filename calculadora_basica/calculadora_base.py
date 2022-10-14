#Inicio do estudo da linguagem python
#Programa para calcular numeros inteiros e/ou float operacoes + - / *.


numero1= float (input ('primeiro numero')) #imprime e guarda o valor emformado
a = input('qual a operação')#imprime e guarda a operacao emformado
numero2= float (input('segundo numero'))
if a == '+': # caso a variavel tiver o mesmo valor da opracao ela é feita
    print (numero1+numero2)#apresenta a soma
if a == '-':# caso a variavel tiver o mesmo valor da opracao ela é feita
    print (numero1-numero2)#apresenta a subitracao
if a == '/':# caso a variavel tiver o mesmo valor da opracao ela é feita
    print (numero1/numero2)#apresenta a divisao
if a == '*':# caso a variavel tiver o mesmo valor da opracao ela é feita
    print (numero1*numero2)#apresenta a multiplicacao


#dapra fazer com match case ficaria assim :
#match a: #qual a vriavel vai ser analisada
#    case '+':
#        print (numero1+numero2) #apresenta a soma
#    case '-':
#        print (numero1-numero2) #apresenta a subtracao
#    case '/':
#        print (numero1/numero2) #apresenta a divisao
#    case '*':
#        print (numero1*numero2) #apresenta a mulltiplicacao