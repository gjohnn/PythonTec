import time
def temporizador(tiempo_total):
    horas, minutos, segundos = tiempo_total.split(":")
    tiempo_total_segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)

    print(f"Temporizador configurado para {tiempo_total}")
    while tiempo_total_segundos > 0:
        horas_restantes, segundos_restantes = divmod(tiempo_total_segundos, 3600)
        minutos_restantes, segundos_restantes = divmod(segundos_restantes, 60)
        print(f"Tiempo restante: {horas_restantes:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}")
        time.sleep(0)
        tiempo_total_segundos -= 1

    print("¡Tiempo agotado!")


# ingresar tiempo
temporizador(input("Ingrese tiempo en formato hh:mm:ss : "))
