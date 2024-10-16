#   Temporizador em Python
import time

def main():
    tempo = int(input("Digite quantos segundos quer esperar: "))
    for x in range(tempo):
        print(x + 1)
        if x + 1 == tempo:
            return "Acabou o tempo!"
        time.sleep(1)

print(main())