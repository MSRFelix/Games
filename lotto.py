def lotto():
    import pygame
    import sys
    import random
    import frontpage
    import json
    import os

    pygame.init()

    # laden wines Spielstandes
    def laden(dateiname, default):
        if os.path.exists(dateiname):
            with open(dateiname, 'r') as json_datei:
                return json.load(json_datei)
        else:
            return default

    # Spielstand speichern

    def speichern(liste, dateiname):
        with open(dateiname, 'w') as json_datei:
            json.dump(liste, json_datei)

    def loschen(dateiname):
        if os.path.exists(dateiname):
            os.remove(dateiname)

    screen_width = 1200
    screen_height = 860
    fps = 30

    button_info = "info"
    button_verstanden = "Verstanden"
    info = "Spieleinsatz: 0,50€"
    info_2 = "Eine Richtige: 1€ Gewinn"
    info_3 = "2 Richtige: 4€ Gewinn"
    info_4 = "3 Richtige: 10€ Gewinn"
    info_5 = "4 Richtige: 100€ Gewinn"
    info_6 = "5 Richtige: 10.000€ Gewinn"
    info_7 = "6 Richtige: 1.000.000€ Gewinn"
    info_8 = "Ab einem Kontostand von 200€ gibt es Prämien"
    info_9 = "Mit \'x\' kannst du den Kontostand zurücksetzen"
    info_10 = "Mit 'ESC' zurück zum Hauptmenü"
    info_liste = [info, info_2, info_3, info_4, info_5, info_6, info_7, info_8, info_9, info_10]
    button_1 = pygame.Rect(1100, 10, 80, 30)
    button_2 = pygame.Rect(500, 530, 140, 30)
    info_active = False

    geld = (laden('guthaben_lotto', 10))
    lottokugeln = []
    lottokugeln_ziehung = []
    wahl = []
    letze_ziehungen_liste = []
    for i in range(1, 50):
        lottokugeln.append(i)
        lottokugeln_ziehung.append(i)
    ziehung_final = []
    for i in range(1, 7):
        zahl = random.choice(lottokugeln_ziehung)
        ziehung_final.append(zahl)
        lottokugeln_ziehung.remove(zahl)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Lotto")
    clock = pygame.time.Clock()

    background = pygame.image.load("lotto_bg.jpg").convert_alpha()
    titel = pygame.transform.scale(background, (400, 140))

    schein = pygame.image.load("lotto_schein.jpg").convert_alpha()
    lotto_schein = pygame.transform.scale(schein, (600, 600))
    naechste_runde = "Neue Runde"
    los = "Starten"
    button_neue_runde = pygame.rect.Rect(25, 120, 160, 28)
    button_go = pygame.rect.Rect(25, 70, 120, 28)
    gewinn = 0
    gewinn_nochmal = 0
    richtig_beantwortet = 0
    buttons = []
    schwarz = 10, 10, 10
    gewinn_text_timer = 101
    gewaehlt = 0
    runde_vorbei = False
    click = False
    run = True
    while run:
        gewinn_text_timer += 1
        winner = f"Die Lottozahlen sind {ziehung_final}. Du hast {richtig_beantwortet} richtig geraten"
        if geld >= 0.5 and runde_vorbei:
            color_active = 0, 150, 0
        else:
            color_active = 150, 150, 150
        if len(wahl) == 6 and runde_vorbei == False:
            color_active_go = 0, 150, 0
        else:
            color_active_go = 150, 150, 150

        screen.fill((231, 231, 20))
        screen.blit(titel, (420, -10))
        screen.blit(lotto_schein, (320, 220))
        font_3 = pygame.font.Font(None, 53)
        font_4 = pygame.font.Font(None, 33)
        geld_text = font_4.render("Kontostand: " + str(geld) + " €", True, (0, 0, 0))
        screen.blit(geld_text, (10, 22))
        pygame.draw.rect(screen, color_active, button_neue_runde, 0, 5)
        pygame.draw.rect(screen, color_active_go, button_go, 0, 5)
        button_neue_runde_text = font_4.render(str(naechste_runde), True, (0, 0, 0))
        los_text = font_4.render(str(los), True, (0, 0, 0))
        letze_ziehungen_text = font_4.render("Letzte Ziehungen:", True, (0, 0, 0))
        screen.blit(button_neue_runde_text, (37, 125))
        screen.blit(los_text, (45, 73))
        screen.blit(letze_ziehungen_text, (20, 400))

        button_1_text = font_4.render(str(button_info), True, (0, 0, 0))
        button_2_text = font_4.render(str(button_verstanden), True, (255, 255, 255))
        screen.blit(button_1_text, (1120, 15))
        pygame.draw.rect(screen, (0, 0, 0), button_1, 3, 5)

        mx, my = pygame.mouse.get_pos()

        for i in range(7):
            for j in range(7):
                button = pygame.rect.Rect(321 + (j*85), 220 + (i * 85), 88, 85)
                buttons.append(button)
                if button.collidepoint(mx, my):
                    if len(wahl) <= 5:
                        pygame.draw.rect(screen, schwarz, button, 5)

                    if button.collidepoint(mx, my) and click:
                        if button not in wahl and len(wahl) <= 5:
                            wahl.append(button)
                            gewaehlt += 1
                        elif button in wahl and len(wahl) <= 6 and runde_vorbei == False:
                            wahl.remove(button)
                            gewaehlt -= 1
                        else:
                            pass
                if gewaehlt == 0:
                    pass
                if gewaehlt == 1:
                    pygame.draw.rect(screen, schwarz, wahl[0], 5)
                if gewaehlt == 2:
                    pygame.draw.rect(screen, schwarz, wahl[0], 5)
                    pygame.draw.rect(screen, schwarz, wahl[1], 5)
                if gewaehlt == 3:
                    pygame.draw.rect(screen, schwarz, wahl[0], 5)
                    pygame.draw.rect(screen, schwarz, wahl[1], 5)
                    pygame.draw.rect(screen, schwarz, wahl[2], 5)
                if gewaehlt == 4:
                    pygame.draw.rect(screen, schwarz, wahl[0], 5)
                    pygame.draw.rect(screen, schwarz, wahl[1], 5)
                    pygame.draw.rect(screen, schwarz, wahl[2], 5)
                    pygame.draw.rect(screen, schwarz, wahl[3], 5)
                if gewaehlt == 5:
                    pygame.draw.rect(screen, schwarz, wahl[0], 5)
                    pygame.draw.rect(screen, schwarz, wahl[1], 5)
                    pygame.draw.rect(screen, schwarz, wahl[2], 5)
                    pygame.draw.rect(screen, schwarz, wahl[3], 5)
                    pygame.draw.rect(screen, schwarz, wahl[4], 5)
                if gewaehlt == 6:
                    pygame.draw.rect(screen, schwarz, wahl[0], 5)
                    pygame.draw.rect(screen, schwarz, wahl[1], 5)
                    pygame.draw.rect(screen, schwarz, wahl[2], 5)
                    pygame.draw.rect(screen, schwarz, wahl[3], 5)
                    pygame.draw.rect(screen, schwarz, wahl[4], 5)
                    pygame.draw.rect(screen, schwarz, wahl[5], 5)

        if len(wahl) == 6 and button_go.collidepoint(mx, my) and click and geld >= 0.5 and runde_vorbei == False:
            zahl_1 = (buttons.index(wahl[0]) + 1)
            zahl_2 = (buttons.index(wahl[1]) + 1)
            zahl_3 = (buttons.index(wahl[2]) + 1)
            zahl_4 = (buttons.index(wahl[3]) + 1)
            zahl_5 = (buttons.index(wahl[4]) + 1)
            zahl_6 = (buttons.index(wahl[5]) + 1)
            letze_ziehungen_liste.append(ziehung_final.copy())
            if zahl_1 in ziehung_final:
                richtig_beantwortet += 1
            if zahl_2 in ziehung_final:
                richtig_beantwortet += 1
            if zahl_3 in ziehung_final:
                richtig_beantwortet += 1
            if zahl_4 in ziehung_final:
                richtig_beantwortet += 1
            if zahl_5 in ziehung_final:
                richtig_beantwortet += 1
            if zahl_6 in ziehung_final:
                richtig_beantwortet += 1
            runde_vorbei = True
            gewinn_text_timer = 0

            if richtig_beantwortet == 0 and runde_vorbei:
                gewinn = 0
                gewinn_nochmal = 0
            if richtig_beantwortet == 1:
                gewinn = 1
                gewinn_nochmal = 1
            if richtig_beantwortet == 2:
                gewinn = 4
                gewinn_nochmal = 4
            if richtig_beantwortet == 3:
                gewinn = 10
                gewinn_nochmal = 10
            if richtig_beantwortet == 4:
                gewinn = 100
                gewinn_nochmal = 100
            if richtig_beantwortet == 5:
                gewinn = 10000
                gewinn_nochmal = 10000
            if richtig_beantwortet == 6:
                gewinn = 1000000
                gewinn_nochmal = 1000000
            geld += gewinn_nochmal
        if gewinn_text_timer <= 100:
            gewinn_text = font_4.render("+ " + str(gewinn) + " €€", True, (0, 0, 255))
            screen.blit(gewinn_text, (155, 42))

        if geld >= 200:
            speichern(galerie.liste_bilder_gewonnen, 'bilder_gewonnen')

        # Info_Fenster
        if button_1.collidepoint(mx, my) and click:
            info_active = True
        if info_active:
            info_text = pygame.rect.Rect(100, 100, 900, 510)
            pygame.draw.rect(screen, (0, 0, 0), info_text)
            for x in range(len(info_liste)):
                informations_text = font_3.render(str(info_liste[x]), True, (255, 255, 255))
                screen.blit(informations_text, (145, 165 + 40*(x-1)))
                pygame.draw.rect(screen, (255, 255, 255), button_2, 3, 5)
                screen.blit(button_2_text, (505, 535))
            if button_2.collidepoint(mx, my) and click:
                info_active = False

        click = False

        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                speichern(geld, 'guthaben_lotto')
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

# Neue Runde
        if button_neue_runde.collidepoint(mx, my) and click and gewaehlt == 6 and geld >= 0.5 and runde_vorbei:
            geld -= 0.5
            runde_vorbei = False
            wahl.clear()
            ziehung_final.clear()
            lottokugeln.clear()
            lottokugeln_ziehung.clear()
            richtig_beantwortet = 0
            gewaehlt = 0
            gewinn = 0
            gewinn_nochmal = 0
            for i in range(1, 50):
                lottokugeln.append(i)
                lottokugeln_ziehung.append(i)
            for i in range(1, 7):
                zahl = random.choice(lottokugeln_ziehung)
                ziehung_final.append(zahl)
                lottokugeln_ziehung.remove(zahl)

# Textausgabe Lottozahlen
        if richtig_beantwortet == 0 and runde_vorbei:
            winner_text = font_3.render(str(winner), True, (0, 0, 0))
            screen.blit(winner_text, (2, 160))
        if richtig_beantwortet == 1:
            winner_text = font_3.render(str(winner), True, (0, 0, 0))
            screen.blit(winner_text, (2, 160))
        if richtig_beantwortet == 2:
            winner_text = font_3.render(str(winner), True, (0, 0, 0))
            screen.blit(winner_text, (2, 160))
        if richtig_beantwortet == 3:
            winner_text = font_3.render(str(winner), True, (0, 0, 0))
            screen.blit(winner_text, (2, 160))
        if richtig_beantwortet == 4:
            winner_text = font_3.render(str(winner), True, (0, 0, 0))
            screen.blit(winner_text, (2, 160))
        if richtig_beantwortet == 5:
            winner_text = font_3.render(str(winner), True, (0, 0, 0))
            screen.blit(winner_text, (2, 160))
        if richtig_beantwortet == 6:
            winner_text = font_3.render(str(winner), True, (0, 0, 0))
            screen.blit(winner_text, (5, 160))

        # Letzte Ziehungen anzeigen
        for i in range(len(letze_ziehungen_liste)):
            letze_ziehungen_liste_text = font_4.render(str(letze_ziehungen_liste[i - 1]), True, (0, 0, 0))
            screen.blit(letze_ziehungen_liste_text, (15, i * 30 + 460))
        # Spiel verlassen
        if key[pygame.K_ESCAPE]:
            speichern(geld, 'guthaben_lotto')
            frontpage.startseite()

        if key[pygame.K_x]:
            loschen('guthaben_lotto')
            frontpage.startseite()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    lotto()
