#Ingresar un número ej. 1234 y devolver 4321 (Usar un solo for)

x = input('Ingrese un numero x:  ')
print('x al reves: ',end='')
for n in range(len(x),0,-1):
    print(x[n-1],end='')

numero=input()
a=numero[::-1]
print(a)


#Generar los primero 'n' números primos 2, 3, 5, 7, 9, 11, 13, 17... (for for if)
n = int(input('Ingresa n: '))
m = 2
j = 1
while j<=n :
    c=1
    for i in range(1,m):
        if m%i == 0:
            c+=1
    if c==2 :
        print(m, end=' ')
        j+= 1
    m = m+1
