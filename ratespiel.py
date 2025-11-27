def adivinanza():
    import random

    numero = random.randint(1, 100)
    run = True
    print("Ich denke an eine Zahl von 1 bis 100 "
          "du hast 7 Versuche, die Zahl zu erraten. "
          "An welche Zahl denke ich gerade?")
    ronda = 0
    while run:
        ronda = ronda + 1
        intento = input()
        if int(intento) == numero:
            print("Richtig, Du  hast die Zahl erraten. Die Zahl ist " + str(numero) + ".")
            run = False
        if int(intento) > numero:
            print("DeineZahl ist zu groß.")
        if int(intento) < numero:
            print("Deine Zahl ist zu klein.")
        if ronda == 7:
            if numero == int(intento):
                run = False
            else:
                print("Leider hat du es nicht geschafft, die Zahl rechtzeitig zu erraten. Meine Zahl war die " + str(numero) + ".")
                run = False
    print("Das Spiel ist vorbei.")


if __name__ == "__main__":
    adivinanza()
