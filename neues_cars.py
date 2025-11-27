def cars():
    import frontpage
    import cars_lv1
    import pygame
    import sys
    import random
    import os
    import json

    pygame.init()

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

    pygame.mixer.init()
    clock = pygame.time.Clock()
    sw = 600
    sh = 600
    fps = 80
    screen = pygame.display.set_mode((sw, sh))
    pygame.display.set_caption("Cars")


    button_name = "Level 1"
    button_info = "info"
    button_verstanden = "Verstanden"
    info = "Benutze die Pfeiltasten LINKS und RECHTS,"
    info_2 = "um die anderen Autos zu überholen ohne"
    info_3 = "zu crashen. Drücke LEERTASTE zum neu starten"
    info_4 = "und ESC um zum Menü zurückzukehren."
    info_liste = [info, info_2, info_3, info_4]
    car_lanes = [179, 274, 369]
    car_lane_random = random.choice(car_lanes)

    car_player = pygame.image.load("car_players.png").convert_alpha()
    cars_player = pygame.transform.scale(car_player, (55, 95))
    black_car = pygame.image.load("car_blacks.png").convert_alpha()
    cars_black = pygame.transform.scale(black_car, (55, 95))
    new_car_black = cars_black.get_rect()
    new_car_black.center = car_lane_random, -300
    new_car_player = cars_player.get_rect()
    new_car_player.topleft = 264, 500
    red_car = pygame.image.load("carsss.png").convert_alpha()
    cars_red = pygame.transform.scale(red_car, (65, 95))
    new_car_red = cars_red.get_rect()
    new_car_red.topleft = car_lane_random, -600
    blue_car = pygame.image.load("car_blues.png").convert_alpha()
    cars_blue = pygame.transform.scale(blue_car, (55, 95))
    new_car_blue = cars_blue.get_rect()
    new_car_blue.topleft = car_lane_random, -900
    green_car = pygame.image.load("green_cars.png").convert_alpha()
    cars_green = pygame.transform.scale(green_car, (55, 95))
    black_truck = pygame.image.load("car.PNG").convert_alpha()
    trucks_black = pygame.transform.scale(black_truck, (55, 95))
    red_truck = pygame.image.load("car_red.PNG").convert_alpha()
    trucks_red = pygame.transform.scale(red_truck, (55, 95))
    yellow_car = pygame.image.load("car_yellows.PNG").convert_alpha()
    cars_yellow = pygame.transform.scale(yellow_car, (55, 95))
    stopp_schild = pygame.image.load("stopp_schild..jpg").convert_alpha()
    schild_stopps = pygame.transform.scale(stopp_schild, (85, 85))
    spielstrasse_schild = pygame.image.load("spielstrasse.PNG").convert_alpha()
    schild_spielstrasse = pygame.transform.scale(spielstrasse_schild, (100, 85))
    kinder_schild = pygame.image.load("schild_kinder.jpg").convert_alpha()
    schild_kinders = pygame.transform.scale(kinder_schild, (100, 85))
    new_stopp_schild = schild_stopps.get_rect()
    new_stopp_schild.topleft = (480, -960)
    police_car = pygame.image.load("car_black.PNG").convert_alpha()
    cars_police = pygame.transform.scale(police_car, (55, 95))
    crash_image = pygame.image.load("crash.png").convert_alpha()
    crash_new = pygame.transform.scale(crash_image, (300, 300))
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)

    liste_autos = [cars_blue, cars_red, cars_yellow, cars_green, trucks_black, trucks_red, cars_police]
    liste_schilder = [schild_stopps, schild_spielstrasse, schild_kinders]
    auswahl_schilder = random.choice(liste_schilder)
    auswahl_auto = random.choice(liste_autos)
    auswahl_auto_1 = random.choice(liste_autos)
    auswahl_auto_2 = random.choice(liste_autos)
    auswahl_auto_3 = random.choice(liste_autos)

    new_car_yellow = auswahl_auto.get_rect()
    new_car_yellow.topleft = car_lane_random, -300
    street = pygame.Rect(150, 0, 300, sh)
    street_end_left = pygame.Rect(150, 0, 15, sh)
    street_end_right = pygame.Rect(435, 0, 15, sh)

    lanes = []
    lanes_2 = []
    for x in range(6):
        lane = pygame.Rect(243, x * 108, 15, 60)
        lanes.append(pygame.draw.rect(screen, "white", lane))
        lane_2 = pygame.Rect(335, x * 108, 15, 60)
        lanes_2.append(pygame.draw.rect(screen, "white", lane_2))

    button_0 = pygame.Rect(20, 560, 80, 30)
    button_1 = pygame.Rect(7, 15, 80, 30)
    button_2 = pygame.Rect(230, 270, 140, 30)
    lane_speed_y = 12
    car_speed_y = 1

    spielstand = laden('highscore_neues_cars', 0)
    highscore = spielstand
    score = 0
    info_active = False
    run = True
    while run:
        screen.fill((0, 230, 0))
        click = False
        if score > highscore:
            highscore = score
        mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, "grey", street)
        pygame.draw.rect(screen, "yellow", street_end_left)
        pygame.draw.rect(screen, "yellow", street_end_right)
        font = pygame.font.Font(None, 64)
        counter_text = font.render(str(score) + " / 100", True, (0, 0, 0))
        screen.blit(counter_text, (5, 50))
        screen.blit(auswahl_auto_3, new_car_red)
        screen.blit(auswahl_auto_1, new_car_yellow)
        screen.blit(auswahl_auto_2, new_car_blue)
        screen.blit(cars_player, new_car_player)
        screen.blit(auswahl_schilder, new_stopp_schild)
        pygame.draw.rect(screen, (0, 0, 0), button_0, 3, 5)
        pygame.draw.rect(screen, (0, 0, 0), button_1, 3, 5)
        font_highscore = pygame.font.Font(None, 24)
        highscore_text = font_highscore.render("Highscore: " + str(highscore), True, (0, 0, 0))
        screen.blit(highscore_text, (4, 89))

        font_2 = pygame.font.Font(None, 33)
        font_3 = pygame.font.Font(None, 23)
        button_0_text = font_2.render(str(button_name), True, (0, 0, 0))
        button_1_text = font_2.render(str(button_info), True, (0, 0, 0))
        button_2_text = font_2.render(str(button_verstanden), True, (255, 255, 255))
        screen.blit(button_0_text, (24, 564))
        screen.blit(button_1_text, (24, 19))

        for x in range(6):
            pygame.draw.rect(screen, (255, 255, 255), lanes[x-1])
            pygame.draw.rect(screen, "white", lanes_2[x-1])

            lanes[x].y += lane_speed_y
            lanes_2[x].y += lane_speed_y
            new_car_red.y += car_speed_y
            new_car_yellow.y += car_speed_y
            new_car_blue.y += car_speed_y
            new_stopp_schild.y += car_speed_y

        collision = (new_car_player.colliderect(new_car_red) or new_car_player.colliderect(new_car_yellow) or
                     new_car_player.colliderect(new_car_blue))
        if collision:
            screen.blit(crash_new, (new_car_player.x-110, new_car_player.y - 85))
        if lanes[0].y == sh:
            lanes[0].topleft = (243, -60)
        if lanes[1].y == sh:
            lanes[1].topleft = (243, -60)
        if lanes[2].y == sh:
            lanes[2].topleft = (243, -60)
        if lanes[3].y == sh:
            lanes[3].topleft = (243, -60)
        if lanes[4].y == sh:
            lanes[4].topleft = (243, -60)
        if lanes[5].y == sh:
            lanes[5].topleft = (243, -60)
        if lanes_2[0].y == sh:
            lanes_2[0].topleft = (335, -60)
        if lanes_2[1].y == sh:
            lanes_2[1].topleft = (335, -60)
        if lanes_2[2].y == sh:
            lanes_2[2].topleft = (335, -60)
        if lanes_2[3].y == sh:
            lanes_2[3].topleft = (335, -60)
        if lanes_2[4].y == sh:
            lanes_2[4].topleft = (335, -60)
        if lanes_2[5].y == sh:
            lanes_2[5].topleft = (335, -60)

        if new_stopp_schild.y == sh:
            auswahl_schilder = random.choice(liste_schilder)
            new_stopp_schild.topleft = (480, -960)
        if new_car_red.y == sh:
            score = score + 1
            auswahl_auto_3 = random.choice(liste_autos)
            car_lane_random = random.choice(car_lanes)
            screen.blit(cars_blue, new_car_red)
            new_car_red.topleft = (car_lane_random, -60)
        if new_car_yellow.y == sh:
            auswahl_auto_1 = random.choice(liste_autos)
            score = score + 1
            car_lane_random = random.choice(car_lanes)
            new_car_yellow.topleft = (car_lane_random, -60)
        if new_car_blue.y == sh:
            auswahl_auto_2 = random.choice(liste_autos)
            score = score + 1
            car_lane_random = random.choice(car_lanes)
            new_car_blue.topleft = (car_lane_random, -60)
        if new_car_red.colliderect(new_car_blue) or new_car_red.colliderect(new_car_yellow):
            car_lane_random = random.choice(car_lanes)
            new_car_red.topleft = car_lane_random, -60
        if new_car_yellow.colliderect(new_car_blue):
            car_lane_random = random.choice(car_lanes)
            new_car_yellow.topleft = (car_lane_random, -60)

        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                speichern(highscore, 'highscore_neues_cars')
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.KEYUP:
                if key[pygame.K_LEFT] and new_car_player.x == 264 and not collision:
                    new_car_player.topleft = (169, 500)
                if key[pygame.K_LEFT] and new_car_player.x == 359 and not collision:
                    new_car_player.topleft = (264, 500)
                if key[pygame.K_RIGHT] and new_car_player.x == 264 and not collision:
                    new_car_player.topleft = (359, 500)
                if key[pygame.K_RIGHT] and new_car_player.x == 169 and not collision:
                    new_car_player.topleft = (264, 500)
                if key[pygame.K_ESCAPE]:
                    speichern(highscore, 'highscore_neues_cars')
                    pygame.mixer.music.stop()
                    frontpage.startseite()
                if key[pygame.K_SPACE]:
                    lane_speed_y = 12
                    car_speed_y = 1
                    score = 0
                    new_car_player.topleft = (264, 500)
                    new_car_red.topleft = (car_lane_random, -600)
                    new_car_yellow.topleft = (car_lane_random, -300)
                    new_car_blue.topleft = (car_lane_random, -900)
                    new_stopp_schild.topleft = (480, -960)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(-1)
        if (new_car_player.colliderect(new_car_red) or new_car_player.colliderect(new_car_yellow) or
                new_car_player.colliderect(new_car_blue)):
            loose_text = font.render(str("Game Over"), True, (0, 0, 0))
            screen.blit(loose_text, (180, 100))
            lane_speed_y = 0
            car_speed_y = 0
            pygame.mixer.music.stop()
        if button_0.collidepoint(mx, my) and click:
            cars_lv1.cars_lv1()
        if button_1.collidepoint(mx, my) and click:
            info_active = True
        if info_active:
            info_text = pygame.rect.Rect(100, 100, 450, 210)
            pygame.draw.rect(screen, (0, 0, 0), info_text)
            for x in range(len(info_liste)):
                informations_text = font_3.render(str(info_liste[x]), True, (255, 255, 255))
                screen.blit(informations_text, (145, 165 + 40*(x-1)))
                pygame.draw.rect(screen, (255, 255, 255), button_2, 3, 5)
                screen.blit(button_2_text, (235, 275))
            if button_2.collidepoint(mx, my) and click:
                info_active = False

        if 50 <= score <= 99:
            winner_text = font_3.render("Du schaffst das!!", True, (0, 0, 0))
            screen.blit(winner_text, (16, 150))
        if score >= 100:
            winner_text = font_3.render("Du bist unglaublich", True, (0, 0, 0))
            screen.blit(winner_text, (12, 150))
            if 100 <= score <= 104:
                winner_text_belohnung = font_2.render("Nice Job", True,
                                                      (100, 100, 240))
                screen.blit(winner_text_belohnung, (80, 250))

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    cars()
