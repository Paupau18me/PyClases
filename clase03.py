#FUNCIONES DE CASTEO
'''
int(var) -> convierte a entero
float(var) -> convierte a num con decimales
str(var) -> convierte a texto
bool(var) -> convierte a booleano // 1 ó cualquier oro numero=True 0=False
'''
num = 10
num2 = '20'
cad = str(num)
print(num + int(num2))
print(type(cad))

x= -2
v_bool = bool(x)
print(v_bool)

#ENTRADA

#nom = input('Ingrese su nombre: ')
#print(nom)

#IF
'''
if condition:
    exe code
else:
    exe this code
'''
age_juan = 30
age_ariel = 15
if age_juan>=18 :
    print('Ingresa a la fiesta :)')
else:
    print('No entra a la fiesta :(')
# elif -> if: else

#for
'''
for valor in range:
    code to exe
'''
#Range
rango = range(0,10,4)
print(rango, type(rango))
for valor in rango:
    print(valor)
list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#check
for number in list_nums:
    print(f'{number}\tEs par' if number%2 == 0  else f'{number} \tno es par')
cadX = 'Hola a todo el mundo'
for letra in cadX:
    if letra is 'a' or letra is 'e' or letra is 'i' or letra is 'o' or letra is 'u':
        print(f'{letra}\t es vocal')
#TAREA
#1.INgresae un nun ej,1234 y devolver 4321
#2.Generar los primeros n numeros primos