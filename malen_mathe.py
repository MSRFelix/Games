import turtle
import time
import os
import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# laden eines Spielstandes
def laden(dateiname, default):
    if os.path.exists(dateiname):
        with open(dateiname, 'r') as json_datei:
            return json.load(json_datei)
    else:
        return default


def speichern(liste, dateiname):
    with open(dateiname, 'w') as json_datei:
        json.dump(liste, json_datei)


def zurucksetzen(liste, index, default):
    liste[index] = default


def loschen(dateiname):
    if os.path.exists(dateiname):
        os.remove(dateiname)


# Globale Variablen für die Parameter
radius = 100
num_shapes = 20
paint_speed = 1
skalierern = 0
phasenverschiebung = 60
shape_mode = 7
form = "Ball"
anzeige_values = 1
spieler = laden('benutzernamen', "Spieler")
aktuelles_datum = datetime.now()



# Liste der Grundfarben
farben = ["red", "green", "blue", "yellow", "purple", "orange", "cyan"]
aktuelle_farbe_index = 6  # Index für die aktuelle Farbe

parameter = [radius, num_shapes, skalierern, phasenverschiebung,
             shape_mode, aktuelle_farbe_index, spieler["password"], aktuelles_datum.strftime("%d.%m.%Y")]


def show_info():
    info_text = "Willkommen zum Malen mit Mathe!\n\n" \
                "Steuere die Parameter mit den folgenden Tasten:\n" \
                "[1|2] - Radius ändern\n" \
                "[3|4] - Anzahl der Formen ändern\n" \
                "[5|6] - Skalierung ändern\n" \
                "[7|8] - Phasenverschiebung ändern\n" \
                "[9] - Form wechseln\n" \
                "[0] - Farben wechseln\n" \
                "[Leertaste] - Zeichnen Pausieren\n" \
                "[x] - Parameter anzeigen/verbergen\n" \
                "[Escape] - Programm beenden und speichern\n" \
                "[i] - Info anzeigen\n\n" \
                "Viel Spaß beim Kreieren!"

    # Tkinter-Dialog für die Anzeige
    root = tk.Tk()
    root.withdraw()  # Hauptfenster ausblenden
    messagebox.showinfo("Info", info_text)
    root.destroy()  # Schließe das Tkinter-Fenster


# Funktion zum Ändern des Radius
def change_radius(delta):
    global radius
    radius += delta
    if radius < 10:  # Minimum Radius
        radius = 10
    elif radius > 300:  # Maximum Radius
        radius = 300


# Funktion zum Ändern der Anzahl der Kreise
def change_num_shapes(delta):
    global num_shapes
    num_shapes += delta
    if num_shapes < 5:  # Minimum Anzahl der Formen
        num_shapes = 5
    elif num_shapes > 150:  # Maximum Anzahl der Formen
        num_shapes = 150


def change_paint_speed(delta):
    global paint_speed
    paint_speed += delta
    if paint_speed % 2 == 0:  # Minimum Anzahl der Umdrehungen
        paint_speed = 0
    elif paint_speed % 2 != 0:  # Maximum Anzahl der Umdrehungen
        paint_speed = 1
    turtle.tracer(paint_speed)


def change_skalierer(delta):
    global skalierern
    skalierern += delta


def change_phasenverschiebung(delta):
    global phasenverschiebung
    phasenverschiebung += delta


def change_shape_mode(delta):
    global shape_mode
    global form
    shape_mode += delta
    if shape_mode >= 8:
        shape_mode = 1
    if shape_mode == 1:
        form = "Kreis"
    elif shape_mode == 2:
        form = "Achteck"
    elif shape_mode == 3:
        form = "Sechseck"
    elif shape_mode == 4:
        form = "Viereck"
    elif shape_mode == 5:
        form = "Spirale"
    elif shape_mode == 6:
        form = "Stern"
    elif shape_mode == 7:
        form = "Ball"


def draw_spiral(step_length, angle, turns):
    for i in range(turns):
        turtle.forward(step_length + i * skalierern)  # Bewege die Turtle vorwärts
        turtle.right(angle)           # Drehe die Turtle um den angegebenen Winkel
        step_length += 5              # Erhöhe die Schrittgröße für die Spirale


def change_color():
    global aktuelle_farbe_index
    aktuelle_farbe_index = (aktuelle_farbe_index + 1) % len(farben)  # Nächste Farbe auswählen
    turtle.color(farben[aktuelle_farbe_index])  # Setze die Turtle-Farbe


def change_anzeigen_value(delta):
    global anzeige_values
    anzeige_values += delta
    if anzeige_values % 2 == 0:  # Anzeige aus
        anzeige_values = 0
    elif anzeige_values % 2 != 0:  # Anzeige an
        anzeige_values = 1


def exit_program():
    speichern(parameter, "parameter_liste")
    turtle.bye()  # Use bye() to close the Turtle graphics window


# Tasteneingaben zuweisen
def setup_keybindings():
    turtle.listen()
    turtle.onkey(lambda: change_radius(-10), "1")  # Verringere den Radius
    turtle.onkey(lambda: change_radius(10), "2")     # Erhöhe den Radius
    turtle.onkey(lambda: change_num_shapes(-1), "3")  # Verringere die Anzahl der Kreise
    turtle.onkey(lambda: change_num_shapes(1), "4")   # Erhöhe die Anzahl der Kreise
    turtle.onkey(lambda: change_paint_speed(1), "space")  # Pausiere mit der Leertaste
    turtle.onkey(lambda: change_skalierer(-1), "5")  # Verringere die Skalierung
    turtle.onkey(lambda: change_skalierer(1), "6")  # Erhöhe die Skalierung
    turtle.onkey(lambda: change_phasenverschiebung(-1), "7")  # Verringere die Phasenverschiebung
    turtle.onkey(lambda: change_phasenverschiebung(1), "8")  # Erhöhe die Phasenverschiebung
    turtle.onkey(lambda: change_shape_mode(1), "9")  # Wechsel zwischen Formen
    turtle.onkey(lambda: change_color(), "0")  # Farben wechseln mit der Taste 0
    turtle.onkey(lambda: show_info(), "i")  # Info-Fenster mit der Taste 'i' öffnen
    turtle.onkey(lambda: exit_program(), "Escape")  # programm speichern und verlassen
    turtle.onkey(lambda: change_anzeigen_value(1), "x")  # Anzeige An/Aus


# Funktion zum Zeichnen der Figur
def draw_shapes():
    turtle.speed(0)  # Schnellste Zeichengeschwindigkeit
    if shape_mode != 5:
        for i in range(num_shapes):
            if shape_mode == 1:
                turtle.circle(radius + i * skalierern)  # Zeichne einen Kreis
            elif shape_mode == 2:
                for _ in range(8):  # Zeichne ein Quadrat
                    turtle.forward(radius + i * skalierern)
                    turtle.right(45)
            elif shape_mode == 3:
                for _ in range(6):  # Zeichne ein Quadrat
                    turtle.forward(radius + i * skalierern)
                    turtle.right(60)
            elif shape_mode == 4:
                for _ in range(4):  # Zeichne ein Quadrat
                    turtle.forward(radius + i * skalierern)
                    turtle.right(90)
            elif shape_mode == 6:
                for _ in range(2):  # Zeichne ein Quadrat
                    turtle.forward(radius + i * skalierern)
                    turtle.right(10)
            elif shape_mode == 7:
                turtle.hideturtle()
                turtle.goto(0, 200)
                abi = 5
                bia = 6
                while bia <= num_shapes * 10:
                    turtle.forward(abi)
                    turtle.right(bia)
                    abi += 2
                    bia += 1
                turtle.penup()
            turtle.right(phasenverschiebung)  # Drehe für die nächste Form
        turtle.hideturtle()

    elif shape_mode == 5:
        draw_spiral(step_length=10, angle=phasenverschiebung, turns=num_shapes)
        turtle.hideturtle()


# Funktion zum Anzeigen der aktuellen Werte
def display_values():
    turtle.penup()
    turtle.goto(0, 380)  # Position für die Anzeige
    turtle.color("white")
    turtle.write("  [1|2]                 [3|4]                [5|6]       "
                 "         [7|8]                  [9]                 [0]            [i]            ",
                 align="center", font=("Arial", 16, "normal"))
    turtle.pendown()

    turtle.penup()
    turtle.goto(0, 350)  # Position für die Anzeige
    turtle.color("white")
    turtle.write(f"    Radius: {radius}       Anzahl: {num_shapes}"
                 f"        Skala: {skalierern}       Winkel: {phasenverschiebung}    "
                 f"Form: {form}    Farbe: {farben[aktuelle_farbe_index]}    Info-Fenster     ",
                 align="center", font=("Arial", 16, "normal"))
    turtle.pendown()


# Funktion zum Zurücksetzen und Zeichnen
def reset_and_draw():
    turtle.clear()  # Lösche das vorherige Bild
    if anzeige_values == 1:
        display_values()  # Werte anzeigen
    turtle.penup()  # Hebe den Stift
    if shape_mode != 6 and shape_mode != 7:
        turtle.goto(0, 0)  # Gehe zum Ursprung
    elif shape_mode == 7:
        turtle.goto(0, 200)
    else:
        turtle.goto(-100, 100)
    turtle.setheading(0)
    turtle.pendown()  # Senke den Stift

    turtle.color(farben[aktuelle_farbe_index])

    draw_shapes()  # Zeichne die Figur

    # Aktualisiere die Parameterliste
    parameter[0] = radius
    parameter[1] = num_shapes
    parameter[2] = skalierern
    parameter[3] = phasenverschiebung
    parameter[4] = shape_mode
    parameter[5] = aktuelle_farbe_index


# Fenster einrichten
turtle.bgcolor("black")  # Hintergrundfarbe
turtle.pensize(1)  # Stiftgröße
turtle.tracer(paint_speed)  # Deaktiviere die automatische Aktualisierung
setup_keybindings()


# Endlosschleife zum Zeichnen
def main_loop_turtle():
    while True:
        reset_and_draw()
        turtle.update()  # Aktualisiere das Fenster
        time.sleep(1)  # Warte 1 Sekunde, bevor neu gezeichnet wird


# Hauptausführung
main_loop_turtle()  # Starte die Hauptschleife
turtle.done()  # Beende das Programm
