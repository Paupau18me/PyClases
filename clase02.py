from builtins import print

print('Holis Mundo Uwuw')
print('Salsas')
print('Tomate')
print('Carne')
print('Lechuga')
print('pan')

#Variabke
nom_var = 10        #numerico
nom_var2 = 'Holis'  #String
nom_var3 = True     #bool

#Numeros enteros
num1 = 10
num2 = 3

#Numeros con decimal
decimal1 = 2.5
decimal2 = -0.3
#type()-> indica el tipo de dato
print(type(num1))
#suma
sum = num1 + num2
print('La suma es: ')
print(sum)
#resta
res = num1 - num2
print('La resta es: ')
print(res)
#producto
prod = num1 * num2
print('El producto es: ')
print(prod)
#division float
div1 = num1/num2
print('La division float es: ')
print(div1)
#division entera
div2 = num1//num2
print('La div entera es: ')
print(div2)
#modulo
mod = num1%num2
print('El residuo es: ',mod)
#potencia
elev = num1**num2
print('El numero: ',num1,' elevado al ',num2,' es ',elev)

#Strings
cad1 = 'Hola'
cad2 = 'Mundo'
cad3 = cad1 +' '+ cad2
print(cad3*2)
print('La longitud es: ',len(cad3))
#subStrings
subcad = cad3[0:4]
#Tarea
a = 'Paulo'
b = 'Tintaya'
c = 'Conde'
nom = a +' '+b+' '+c
print(nom[14:19])

#Encontrar cadenas
print(cad3.find('Mundo'))
#UpperCAse
print(cad3.upper())
#LOwer
print('HOLIS'.lower())
#caracteres PROHIBIDOS
print('Las comillas simoles (\' \')')
#PArrafos
print('''Aqui voy a escribir un parrafo
en python para no escribir saltos
inncesarios de linea''')
#TAB
print('Hola\tmundo')

#BOOleanos

juego_pokemon = True
juego_digimon = False

#multipleAsignacionDeVariables
cad1,cad2,cad3 ='Hola',10,True
print(type(cad1), type(cad2), type(cad3))