"""Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el
monto de la cuenta.

El programa debe:
Pedir al usuario el monto total de la cuenta.
Calcular la propina sugerida al 10%.Calcular la propina sugerida al 15%.
Calcular el total a pagar en ambos casos (cuenta + propina).
Mostrar todos los resultados en pantalla."""

#Ingreso el monto total de la cuenta
monto_total = float(input("Ingrese el monto total de la cuenta: "))
print(f"El monto total de la cuenta es {monto_total}")

#Calculo la propina al 10% y 15%
propina_al_10 = monto_total * 0.10
propina_al_15 = monto_total * 0.15

#Sumo la propina al monto total de la cuenta para obtener el monto final en cada caso
monto_final_10 = monto_total + propina_al_10
monto_final_15 = monto_total + propina_al_15

#Imprimo el monto sugerido de la propina y el monto final sumando monto_total y _propina_al_10
print(f"Con propina sugerida al 10% el monto es {propina_al_10}")
print(f"El monto total con propina al 10% es {monto_final_10}")

#Imprimo el monto sugerido de la propina y el monto final sumando monto_total y _propina_al_15
print(f"Con propina sugerida al 15% el monto es {propina_al_15}")
print(f"El monto total con propina al 10% es {monto_final_15}")







