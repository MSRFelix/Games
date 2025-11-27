def level_1():

    import pygame
    import sys
    import frontpage

    pygame.init()
    sw = 1200
    sh = 850

    fps = 300

    screen = pygame.display.set_mode((sw, sh))
    clock = pygame.time.Clock()

    button_info = "info"
    button_verstanden = "Verstanden"
    info = 'Bewegt die Blöcke am Rand hoch und runter,'
    info_2 = "sodass die Kugel nicht außerhalb des Spilefelds gelangt."
    info_3 = "Spieler 1 benutzt die Tasten \'w\' und \'s\'."
    info_4 = "Spieler 2 die Pfeiltasten HOCH und RUNTER."
    info_5 = "Drücke ESC um zum Hauptmenü zu gelangen"
    info_6 = "und LEERTASTE um neu zu starten."
    info_liste = [info, info_2, info_3, info_4, info_5, info_6]

    player_1 = pygame.Rect(0, 400, 15, 85)
    player_2 = pygame.Rect(1184, 400, 15, 85)
    ball_radius = 15
    ball_speed_x = 1
    ball_speed_y = 1
    pos_x = sw / 2
    pos_y = sh / 2

    punkte_player_1 = 0
    punkte_player_2 = 0

    sieg = 10

    button_1 = pygame.Rect(277, 15, 80, 30)
    button_2 = pygame.Rect(530, 325, 140, 30)
    info_active = False
    run = True
    while run:
        screen.fill((0, 0, 0))
        click = False

        mx, my = pygame.mouse.get_pos()

        font_2 = pygame.font.Font(None, 28)
        button_1_text = font_2.render(str(button_info), True, (255, 255, 255))
        button_2_text = font_2.render(str(button_verstanden), True, (0, 0, 0))
        screen.blit(button_1_text, (298, 21))
        pygame.draw.rect(screen, (255, 255, 255), button_1, 2, 5)

        level = 1
        block_player_1 = -1
        block_2_player_2 = 1
        block_player_2 = -1
        block_2_player_1 = 1

        abs_speed_ball_x = abs(ball_speed_x)
        if abs_speed_ball_x <= 1.5 and punkte_player_1 < sieg and punkte_player_2 < sieg:
            pygame.draw.circle(screen, (255, 255, 255), (pos_x, pos_y), ball_radius)
        pygame.draw.rect(screen, (255, 255, 255), player_1)
        pygame.draw.rect(screen, (255, 255, 255), player_2)

        font = pygame.font.Font(None, 74)
        counter_text = font.render(str(punkte_player_1) + " / 10", True, (255, 255, 255))
        counter_text_2 = font.render(str(punkte_player_2) + " / 10", True, (255, 255, 255))
        counter_level = font.render(str("Level: " + str(level)), True, (255, 255, 255))
        screen.blit(counter_text, (130, 20))
        screen.blit(counter_text_2, (1000, 20))
        screen.blit(counter_level, (490, 20))

        pos_x += ball_speed_x
        pos_y += ball_speed_y
        if pos_y >= 850 or pos_y <= 0:
            ball_speed_y = - ball_speed_y

        if pos_x >= 1186:
            pos_x = 200
            pos_y = sh / 2
            punkte_player_1 += 1

        if pos_x <= 14:
            pos_x = 1000
            pos_y = sh / 2
            punkte_player_2 += 1

        if player_1.collidepoint(pos_x - 13, pos_y):
            ball_speed_x *= -1.01
            ball_speed_y = ball_speed_y * 1.01

        if player_2.collidepoint(pos_x + 13, pos_y):
            ball_speed_x *= -1.01
            ball_speed_y = ball_speed_y * 1.01

        if player_1.collidepoint(0, 0):
            block_player_1 = 0
        if player_2.collidepoint(sw - 15, 0):
            block_player_2 = 0
        if player_1.collidepoint(0, sh):
            block_2_player_1 = 0
        if player_2.collidepoint(sw - 15, sh):
            block_2_player_2 = 0

        if abs_speed_ball_x >= 1.5 and punkte_player_1 < sieg and punkte_player_2 < sieg:
            pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), ball_radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            player_1.move_ip(0, block_player_1)
        if key[pygame.K_s]:
            player_1.move_ip(0, block_2_player_1)
        if key[pygame.K_UP]:
            player_2.move_ip(0, block_player_2)
        if key[pygame.K_DOWN]:
            player_2.move_ip(0, block_2_player_2)
        if key[pygame.K_SPACE]:
            punkte_player_2 = 0
            punkte_player_1 = 0
            pos_x = 200
            pos_y = sh / 2
            ball_speed_x = 1
            ball_speed_y = 1

        if key[pygame.K_ESCAPE]:
            frontpage.startseite()

        if punkte_player_1 >= sieg:
            pygame.draw.circle(screen, (255, 255, 255), (sw / 2, sh / 2), ball_radius)
            player_1.topleft = 0, 400
            player_2.topleft = 1184, 400
            ball_speed_x = 0
            ball_speed_y = 0

            looser_text = font.render(str("Nächstes Mal wird's besser"), True, (250, 0, 0))
            winner_text = font.render(str("Super"), True, (250, 0, 0))

            screen.blit(looser_text, (850, 425))
            screen.blit(winner_text, (200, 490))

        if punkte_player_2 >= sieg:
            pygame.draw.circle(screen, (255, 255, 255), (sw / 2, sh / 2), ball_radius)
            player_1.topleft = 0, 400
            player_2.topleft = 1184, 400
            ball_speed_x = 0
            ball_speed_y = 0
            looser_text = font.render(str("Nächstes Mal wird's besser"), True, (250, 0, 0))
            winner_text = font.render(str("Sehr gut"), True, (250, 0, 0))
            screen.blit(looser_text, (130, 425))
            screen.blit(winner_text, (830, 450))

        if button_1.collidepoint(mx, my) and click:
            info_active = True
        if info_active:
            info_text = pygame.rect.Rect(270, 150, 650, 210)
            pygame.draw.rect(screen, (255, 255, 255), info_text)
            for x in range(len(info_liste)):
                informations_text = font_2.render(str(info_liste[x]), True, (0, 0, 0))
                screen.blit(informations_text, (275, 185 + 30*(x-1)))
                pygame.draw.rect(screen, (0, 0, 0), button_2, 3, 5)
                screen.blit(button_2_text, (543, 330))
            if button_2.collidepoint(mx, my) and click:
                info_active = False

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    level_1()
