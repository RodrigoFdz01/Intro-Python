'''
def conversor(tipo_pesos, valor_dolar):
    pesos = input ("cuantos pesos "+ tipo_pesos+" tienes? ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares= str (dolares)
    print ("Tienes $" + dolares+ " dolares")

menu = """
BIenvenido al conversor
1-Pesos colombianos
2-Pesos arg
3-Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos" ,3875)
elif opcion == 2:
    conversor("arg",65)
elif opcion == 3:
     conversor("mexicanos", 24)
else:
    print("ingresa una correcta")



2------------------



def Calcular_IMC():
    print('Prueba')

Calcular_IMC()


peso = int(input('ingresa tu peso '))
altura = int(input('ingresa tu altura '))
altura_metros = altura/100
imc = peso / (altura_metros*altura_metros)
print (imc)

if imc < 20:
    print ('eres delgado')
if imc >=20 and imc < 26:
    print ('Peso Normal')
if imc >= 26 and imc < 30:
    print ('Sobrepeso')
if imc >= 30:
    print ('OBESIDAD')

3---------------------
edad = int(input ("edad? "))
mensaje = "mayor de edad" if edad >= 18 else "menor de edad"
print(mensaje)


4-------------------------

palabra = ''
while palabra != 'salir':
    palabra = input(">")
    print (f'la palabra es {palabra}')


5------funciones lambda

productos= [
    ('producto 1',10),
    ('producto 2',20),
    ('producto 3',30),
    ('producto 4',40),
]

precios = list(map(lambda prodcuto: prodcuto[1], productos))
print (precios)

6-----------------------------------
numbers = {"a":2, "b":"juan", "c":5}

for i in numbers:
    print(i)

def suma (a,b) :
    print('se suman dos numeros')
    resulado = a+b
    return resultado

sumatoria = suma(1,4)
print (sumatoria)
numero = int(input('elige un numero impar '))

numero2 = int(input('elige un numero par '))
resultado = numero + numero2
print('este es ' + str(resultado))

7-------------------------------

productos= ["1","2","3","4"] 
productos= (1,2,3,4,5)

for num in productos:
    preciofinal = list(num * 3)
    print(preciofinal)


productos = [
    ('producto 1',10),
    ('producto 2',20),
    ('producto 3',30),
    ('producto 4',240),
]

productos2 = (1,2,3,5,6)
precio = list(map(lambda element : element[1]* 2,productos))
precio = list(map(lambda element : element * 2,productos2))
precio3 = [item[0] for item in productos]

print (precio3)
 



# Recorriendo una list con indice y valor...
mylist = ["perro","gato","loro","pajaro"]
for i in (mylist):
    #print(i) 
    print("soy un " (i) + " y soy el numero" + mylist(i+1))



# conexion con Mysql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
 database="prueba",
 auth_plugin='mysql_native_password' 
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuarios")

myresult = mycursor.fetchall()

print(myresult)

class Humano:
    def __init__(self):
        print("soy un nuevo obejto")
    def hablar(self,mensaje):
        print (mensaje)
pedro = Humano()
raul = Humano()
pedro.hablar("soy Pedro")
raul.hablar("hola Pedro")
'''

def conversor(tipo_pesos, valor_dolar):
    pesos = input("cauntos pesos tenes "+ tipo_pesos+ "tenes?")
    pesos= float(pesos)
    dolares = pesos/valor_dolar
    dolares = str (dolares)
    print ("tenes $" + dolares+ " dolares")

menu = """
BIenvenido al conversor
1-Pesos colombianos
2-Pesos arg
3-Pesos mexicanos

Elige una opcion: """


opcion = int(input(menu))

if opcion == 1:
    conversor("colom", 3875)
elif opcion == 2:
    conversor("arg",290)
elif opcion == 3:
        conversor("mexi", 24)
else:
            print("ingrsa una opcion correcta") 