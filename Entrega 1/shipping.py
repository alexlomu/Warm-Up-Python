#TAREA 6
customer_basket_cost = 101
customer_basket_weight = 44
precio_envio = 1*2
if customer_basket_cost > 0 and customer_basket_cost < 100:
    precio_envio = precio_envio * customer_basket_weight
    customer_basket_cost = customer_basket_cost + precio_envio
    print("Como la compra no supera los 100%, el coste total junto con los gastos de envío será:" , str(customer_basket_cost) + "$") #Cuando la compra es inferior a 100 tenemos que sumar a la compra los gastos de envío
elif customer_basket_cost >= 100:
    print("El envío lo tiene gratuito, tendrá que pagar:" , str(customer_basket_cost) + "$") #Si la compra supera los 100, los gastos de envío son gratuitos
elif customer_basket_cost == 0:
    print("Aún no has comprado nada, a qué esperas?") #Aún no se ha comprado nada
else:
    print("Ups, algo ha ido mal :(") #En el caso de que se introduzca un valor negativo como precio obtendremos un mensaje de error

#Respuesta uno: Cuando ha habido compra(>0) y es menor que 100 se ejecuta el primer if en el cual se multiplicará el precio de envío de cada kilo por la cantidad total de kilos a enviar para luego sumar esta cantidad al precio de la compra
#Respuesta dos: Si cambiamos el valor de la compra a uno superior a 100 entonces al no tener que sumar gastos de envío nos dirá directamente el precio total de la compra