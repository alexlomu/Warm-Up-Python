#TAREA 1
# Write your python code here
print("Roses are #ff0000 Violets are #0000ff why my code's working I haven't a clue")

#TAREA 2
#This is an example code
print("Hello World")
print("\033[92mHello World\033]0m")

#TAREA 3
print(21+43)
print(142-52)
print(10*342)
print(5**2)

#TAREA 4
altura = 200
altura = altura+50
print(altura)

#TAREA 5
dinero = 2000
precio_helado = 100
satisfaccion = 34
if satisfaccion < 85 and dinero >= precio_helado: #Comprobamos que satisfaccion es inferior a 35 además de que tenemos suiciente dinero para pagar el helado
    dinero = dinero - precio_helado
    satisfaccion = satisfaccion + 10 #Por cada helado que comamos sumaremos una satisfaccion de un 10%
    precio_helado = precio_helado * 1.2 #El precio del helado incrementa un 120% cada vez
    print("No estas lleno todavía, te has comido un helado y tu satisfacción ahora es de un", str(satisfaccion) + "%")
    print("Dinero restante:" , str(dinero) + "$")
elif satisfaccion >= 85 or satisfaccion <= 100: #Satisfaccion se encuentra entre los valores acordes a no tener hambre
    print("Ya no tienes hambre!")
    print("Tu dinero actual es:" + str(dinero), "%")
elif dinero < precio_helado: #El caso de no tener suficiente dinero para pagar un helado
    print("Vaya, no te queda suficiente dinero para comprar un helado")
else: #En el caso que el valor de satisfacción introducido sea erroneo recibiremos un mensaje de error
    print("Algo ha salido mal :(")

#TAREA 7
for i in range(51):
    print(i)

#TAREA 9
f = open("flag.txt", "r") #Al estar el documento flag.txt vacío no se obtiene nada

#TAREA 10
import datetime
current_time = datetime.datetime.now()
print(current_time) #Obtenemos la fecha actual junto con la hora(hora, minutos, segundos y milisegundos)
