def flappy():
    import random
    import frontpage
    import pygame
    import sys
    import json
    import os

    pygame.init()

    pygame.mixer.music.load("src_mathe/star Wars - Cantina Song.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)

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

    screen_width = 1100
    screen_height = 600

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.image.load("src_mathe/weltraum.jpg").convert_alpha()
    background = pygame.transform.scale(background, (screen_width, screen_height))
    pygame.display.set_caption("Tile Runner")

    length = random.randint(100, 400)
    start = random.randint(300, 550)
    length_2 = random.randint(100, 400)
    start_2 = random.randint(300, 550)

    vogel_player = pygame.image.load("src_mathe/vogel.png").convert_alpha()
    vogel_player = pygame.transform.scale(vogel_player, (55, 55))
    player_1 = vogel_player.get_rect()
    player_1.topleft = int(screen_width / 2), int(screen_height / 2)

    player_speed_y = 2
    obstacle_speed_x = 2

    obstacle_1 = pygame.Rect(950, 0, 30, length)
    obstacle_2 = pygame.Rect(1200, start, 30, 700)
    obstacle_3 = pygame.Rect(1500, 0, 30, length_2)
    obstacle_4 = pygame.Rect(1800, start_2, 30, 700)

    button_info = "info"
    button_verstanden = "Verstanden"
    info = "Benutze die Leertaste, um nach oben zu fliegen."
    info_2 = "Fliege an 100 Hindernissen vorbei, um eine Prämie"
    info_3 = "zu erhalten. Drücke \'Enter\' um neu zu starten"
    info_4 = "und ESC um zum Menü zurückzukehren."
    info_liste = [info, info_2, info_3, info_4]

    button_1 = pygame.Rect(7, 55, 80, 30)
    button_2 = pygame.Rect(340, 270, 140, 30)

    spielstand = laden('highscore_flappy_bird', 0)
    highscore = spielstand
    punkte = 0

    click = False
    info_active = False

    run = True
    while run:

        mx, my = pygame.mouse.get_pos()

        if punkte > highscore:
            highscore = punkte
        screen.blit(background, (0, 0))

        new_height = random.randint(100, 400)
        start = random.randint(300, 550)

        screen.blit(vogel_player, player_1)
        pygame.draw.rect(screen, (250, 0, 0), obstacle_1)
        pygame.draw.rect(screen, (250, 0, 0), obstacle_2)
        pygame.draw.rect(screen, (250, 0, 0), obstacle_3)
        pygame.draw.rect(screen, (250, 0, 0), obstacle_4)
        font = pygame.font.Font(None, 74)
        font_2 = pygame.font.Font(None, 54)
        font_4 = pygame.font.Font(None, 34)

        font_highscore = pygame.font.Font(None, 44)
        highscore_text = font_highscore.render("Highscore: " + str(highscore), True, (255, 255, 255))
        screen.blit(highscore_text, (4, 9))

        button_1_text = font_4.render(str(button_info), True, (255, 255, 255))
        button_2_text = font_4.render(str(button_verstanden), True, (0, 0, 0))
        screen.blit(button_1_text, (24, 59))
        pygame.draw.rect(screen, (255, 255, 255), button_1, 3, 5)

        counter_text = font.render(str(punkte) + " / 100", True, (250, 250, 250))
        loose_text = font.render(str("game over"), True, (250, 250, 255))
        screen.blit(counter_text, (550, 20))

        player_1.y += player_speed_y
        obstacle_1.x -= obstacle_speed_x
        obstacle_2.x -= obstacle_speed_x
        obstacle_3.x -= obstacle_speed_x
        obstacle_4.x -= obstacle_speed_x

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            player_speed_y = -6
        else:
            player_speed_y = 2

        if player_1.y >= screen_height or player_1.y <= -25:
            pygame.mixer.music.stop()
            player_speed_y = 0
            obstacle_speed_x = 0
            screen.blit(loose_text, (425, 300))

        if button_1.collidepoint(mx, my) and click:
            info_active = True
        if info_active:
            info_text = pygame.rect.Rect(100, 100, 650, 210)
            pygame.draw.rect(screen, (255, 255, 255), info_text)
            for x in range(len(info_liste)):
                informations_text = font_4.render(str(info_liste[x]), True, (0, 0, 0))
                screen.blit(informations_text, (145, 165 + 40 * (x - 1)))
                pygame.draw.rect(screen, (0, 0, 0), button_2, 3, 5)
                screen.blit(button_2_text, (345, 275))
            if button_2.collidepoint(mx, my) and click:
                info_active = False
        click = False
        if obstacle_1.x <= 0:
            obstacle_1.topleft = (1100, 0)
            obstacle_1.height = new_height
        if obstacle_2.x <= 0:
            obstacle_2.topleft = (1100, start)
        if obstacle_3.x <= 0:
            obstacle_3.topleft = (1100, 0)
            obstacle_3.height = new_height
        if obstacle_4.x <= 0:
            obstacle_4.topleft = (1100, start)

        if player_1.x == obstacle_1.x or player_1.x == obstacle_2.x:
            punkte = punkte + 1

        if player_1.x == obstacle_3.x or player_1.x == obstacle_4.x:
            punkte = punkte + 1

        if player_1.colliderect(obstacle_1) or player_1.colliderect(obstacle_2):
            pygame.mixer.music.stop()
            player_speed_y = 0
            obstacle_speed_x = 0
            screen.blit(loose_text, (425, 300))

        if player_1.colliderect(obstacle_3) or player_1.colliderect(obstacle_4):
            pygame.mixer.music.stop()
            player_speed_y = 0
            obstacle_speed_x = 0
            screen.blit(loose_text, (425, 300))

        if 100 <= punkte <= 102:
            winner_text_belohnung = font_2.render("Good Job", True, (255,  255, 255))
            screen.blit(winner_text_belohnung, (180, 70))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                speichern(highscore, 'highscore_flappy_bird')
                pygame.mixer.music.stop()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if key[pygame.K_ESCAPE]:
            speichern(highscore, 'highscore_flappy_bird')
            pygame.mixer.music.stop()
            frontpage.startseite()

        if key[pygame.K_RETURN]:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.6)
            player_1.topleft = int(screen_width / 2), int(screen_height / 2)
            obstacle_speed_x = 2
            obstacle_1.topleft = (950, 0)
            obstacle_2.topleft = (1200, start)
            obstacle_3.topleft = (1500, 0)
            obstacle_4.topleft = (1800, start)
            punkte = 0

        pygame.display.update()
        clock.tick(300)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    flappy()
