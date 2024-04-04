import datetime


def somar_horas(hora_entrada_1, hora_entrada_2):
    hora_1 = datetime.datetime.strptime(hora_entrada_1, "%H:%M")
    hora_2 = datetime.datetime.strptime(hora_entrada_2, "%H:%M")

    soma = hora_1 + datetime.timedelta(hours=hora_2.hour, minutes=hora_2.minute)

    return soma.strftime("%H:%M")


if __name__ == "__main__":
    hora1 = input("Digite a primeira hora (HH:MM): ")
    hora2 = input("Digite a segunda hora (HH:MM): ")

    soma = somar_horas(hora1, hora2)

    print(f"A soma das duas horas é {soma}.")
