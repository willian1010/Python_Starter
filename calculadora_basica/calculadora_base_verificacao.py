#Inicio do estudo da linguagem python
#Programa para calcular numeros inteiros e/ou float operacoes + - / *.


numero1= float (input ('primeiro numero')) #imprime e guarda o valor emformado
a = input('qual a operação')#imprime e guarda a operacao emformado
numero2= float (input('segundo numero'))
x=True
while x==True :
    if a == '+' or a == '-'or a == '/'or a == '*':
        x==False
        if a == '+': # caso a variavel tiver o mesmo valor da opracao ela é feita
            print (numero1+numero2)#apresenta a soma
            break
        if a == '-':# caso a variavel tiver o mesmo valor da opracao ela é feita
            print (numero1-numero2)#apresenta a subitracao
            break
        if a == '/':# caso a variavel tiver o mesmo valor da opracao ela é feita
            print (numero1/numero2)#apresenta a divisao
            break
        if a == '*':# caso a variavel tiver o mesmo valor da opracao ela é feita
            print (numero1*numero2)#apresenta a multiplicacao
            break
        
        

    else:
      x==True  
      print ('Digite uma Operacao Valida')
      a = input('qual a operação')#imprime e guarda a operacao emformado


#dapra fazer com match case ficaria assim : (fica mais bonito e otimisado))
#match a: #qual a vriavel vai ser analisada
#    case '+':
#        print (numero1+numero2) #apresenta a soma
#    case '-':
#        print (numero1-numero2) #apresenta a subtracao
#    case '/':
#        print (numero1/numero2) #apresenta a divisao
#    case '*':
#        print (numero1*numero2) #apresenta a mulltiplicacao