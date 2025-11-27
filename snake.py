def snake_game():
    import pygame
    import sys
    import random
    import frontpage
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

    screen_width = 700
    screen_height = 800
    block_size = 50
    fps = 70
    rund = 100
    eckig = 0
    top_left_radius = eckig
    top_right_radius = rund
    bottom_left_radius = eckig
    bottom_right_radius = rund
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()

    # Goal platzieren
    random_x = random.randint(0, screen_width // block_size - 1)
    random_y = random.randint(0, screen_height // block_size - 1)

    gold = pygame.Rect((random_x * block_size), (random_y * block_size), block_size, block_size)
    up = False
    right = True
    left = False
    down = False
    game_over = False

    spielstand = laden('highscore_snake', 0)
    highscore = spielstand
    count = 0
    nicht_vorhanden = False
    player_1 = pygame.Rect(screen_width / 2, screen_height / 2, block_size, block_size)
    grenze_rot = pygame.Rect(0, 1, screen_width, screen_height)
    body = []
    bereits_gespawned = []
    shade = 255
    runde_timer = 0
    ende_runde = 8
    grenzen_an = 0
    info = 0
    bunt_an = 0
    rot = (255, 0, 0)
    grun = (15, 200, 20)
    blau = (20, 30, 140)
    mix = (50, 0, 200)
    mix_2 = (0, 180, 90)
    mix_3 = (200, 100, 0)
    mix_4 = (230, 30, 200)
    colors = (rot, grun, blau, mix, mix_2, mix_3, mix_4)
    random_color = random.choice(colors)
    info_texte = ["Drücke \"b\", um BUNT zu aktivieren", "Drücke \"g\", um Grenzen zu aktivieren",
                  "Drücke LEERTASTE für einen Neustart", "Drücke ESC, um das Spiel zu verlassen"]
    random_text = random.choice(info_texte)
    farbhistorie = [(0, 255, 0)]
    hintergrund_liste = []

    run = True
    while run:

        screen.fill((0,0,0))
        if info == 0:
            runde_timer += 1
        if shade > 0 and count < highscore:
            shade -= 1
        elif count == highscore:
            shade = 255

        font_highscore = pygame.font.Font(None, 44)

        if count > highscore:
            highscore = count

        for part in hintergrund_liste:
            test = pygame.rect.Rect(part)
            pygame.draw.rect(screen, (0, 0, 0), test, 0, 2)
        highscore_text = font_highscore.render("Highscore: " + str(highscore), True, (shade, shade, shade))
        font = pygame.font.Font(None, 53)
        font_game_over = pygame.font.Font(None, 73)
        font_leertaste = pygame.font.Font(None, 33)
        count_text = font.render(str(count) + " / 50", True, (255, 255, 255))
        easter_egg_text = font.render("Hier gibt's nix zu sehen", True, (255, 255, 255))

        pygame.draw.rect(screen, (25, 255, 25), player_1, 0, 0,
                         top_left_radius, top_right_radius, bottom_left_radius, bottom_right_radius)
        if grenzen_an:
            pygame.draw.rect(screen, (255, 25, 25), grenze_rot, 2)
        font_winner = pygame.font.Font(None, 53)
        font_winner.set_italic(True)

        # Goal platzieren
        def check_goal_position(goal, tail):
            for part in tail:
                if goal.collidepoint(part):
                    return False
                if goal.collidepoint(player_1.x, player_1.y):
                    return False
            return True

        # bereits_gespawned checken
        def check_bereits_gespawned_position(goal, tail):
            for part in tail:
                if goal.collidepoint(part):
                    return False
            return True

        def spawn_goal():
            while True:
                random_xx = random.randint(0, screen_width // block_size - 1)
                random_yy = random.randint(0, screen_height // block_size - 1)
                gold.topleft = (random_xx * block_size, random_yy * block_size)
                if (gold.x, gold.y) not in bereits_gespawned:
                    random_xx = random.randint(0, screen_width // block_size - 1)
                    random_yy = random.randint(0, screen_height // block_size - 1)
                    gold.topleft = (random_xx * block_size, random_yy * block_size)
                if check_bereits_gespawned_position(gold, bereits_gespawned) or check_goal_position(gold, body):
                    bereits_gespawned.append((gold.x, gold.y))
                    pass
                if check_goal_position(gold, body):
                    break

        # Kollision mit Gold
        if player_1.colliderect(gold) and runde_timer == 9 and info != 1:
            farbhistorie.append(random_color)
            count = count + 1
            spawn_goal()
            random_color = random.choice(colors)
        elif player_1.x == gold.x and player_1.y == gold.y and info != 1:
            count = count + 1
            spawn_goal()
            random_color = random.choice(colors)
        elif not player_1.colliderect(gold) and runde_timer == 9 and info != 1:
            body.remove(body[0])

        # Gewinnanzeige
        if 50 <= count <= 51 and nicht_vorhanden:
            winner_text_belohnung = font_winner.render("Good Job", True, (180, 0, 130))
            screen.blit(winner_text_belohnung, (screen_width/2 - screen_width/5, 50))
        if runde_timer == ende_runde + 2:
            runde_timer = 0
        if runde_timer == 8:
            body.append((player_1.x, player_1.y))

        for parts in range(len(body)):
            if bunt_an == 1:
                body_0 = pygame.rect.Rect(body[parts][0], body[parts][1], block_size, block_size)
                pygame.draw.rect(screen, farbhistorie[-parts-1], body_0, 10, 5)
            elif bunt_an == 0:
                body_0 = pygame.rect.Rect(body[parts][0], body[parts][1], block_size, block_size)
                pygame.draw.rect(screen, (0, 255, 0), body_0, 10, 5)

        # goal neu spawnen
        if bunt_an == 1:
            random_x = random.randint(0, screen_width // block_size - 1)
            random_y = random.randint(0, screen_height // block_size - 1)
            pygame.draw.rect(screen, random_color, gold, 0, 0)
            if check_bereits_gespawned_position(gold, bereits_gespawned) or check_goal_position(gold, body):
                bereits_gespawned.append((gold.x, gold.y))
                for part in hintergrund_liste:
                    if (gold.x, gold.y) == (part[0], part[1]):
                        hintergrund_liste.remove(part)
        elif bunt_an == 0:
            random_x = random.randint(0, screen_width // block_size - 1)
            random_y = random.randint(0, screen_height // block_size - 1)
            pygame.draw.rect(screen, (255, 0, 0), gold, 0, 0)
            if check_bereits_gespawned_position(gold, bereits_gespawned) or check_goal_position(gold, body):
                bereits_gespawned.append((gold.x, gold.y))
                for part in hintergrund_liste:
                    if (gold.x, gold.y) == (part[0], part[1]):
                        hintergrund_liste.remove(part)

        # Kollision mit dem Bildschirmrand
        if grenzen_an == 1:
            if player_1.y >= screen_height or player_1.y <= - block_size:
                count = 0
                player_1.topleft = (screen_width/2, screen_height/2)
                body.clear()
                bereits_gespawned.clear()
                farbhistorie = [(0, 255, 0)]
                game_over = True
            if player_1.x >= screen_width or player_1.x <= - block_size:
                count = 0
                player_1.topleft = (screen_width / 2, screen_height / 2)
                body.clear()
                bereits_gespawned.clear()
                farbhistorie = [(0, 255, 0)]
                game_over = True
        if grenzen_an == 0:
            if player_1.y >= screen_height:
                runde_timer = 9
                player_1.y = 0
            if player_1.y <= - block_size:
                runde_timer = 9
                player_1.y = screen_height - 50
            if player_1.x >= screen_width:
                runde_timer = 9
                player_1.x = 0
            if player_1.x <= - block_size:
                runde_timer = 9
                player_1.x = screen_width - block_size

        # Kollision mit body
        for parts in body[0:-1]:
            if player_1.collidepoint(parts):
                count = 0
                player_1.topleft = (screen_width / 2, screen_height / 2)
                body.clear()
                bereits_gespawned.clear()
                farbhistorie = [(0, 255, 0)]
                game_over = True

        if runde_timer == ende_runde and up and info == 0:
            player_1.move_ip(0, -block_size)
        if down and runde_timer == ende_runde and info == 0:
            player_1.move_ip(0, block_size)
        if right and runde_timer == ende_runde and info == 0:
            player_1.move_ip(block_size, 0)
        if left and runde_timer == ende_runde and info == 0:
            player_1.move_ip(-block_size, 0)

        if game_over:
            game_over_text = font_game_over.render("GAME OVER", True, (255, 255, 255))
            leertaste_text = font_leertaste.render("drücke LEERTASTE zum Starten", True, (255, 255, 255))
            info_text = font_leertaste.render("drücke \"t\" für Tipps", True, (255, 255, 255))
            screen.blit(game_over_text, (screen_width / 2 - 130, (screen_height/2) - 60))
            screen.blit(leertaste_text, (screen_width / 2 - 150, (screen_height/2) + 60))
            screen.blit(info_text, (screen_width / 2 - 80, (screen_height / 2) + 110))
            runde_timer = 0
            up = False
            right = False
            left = False
            down = False

        # Info-Text
        if info == 1:
            runde_timer = runde_timer
            shade = 255
            fenster_breite = 150
            info_fenster = pygame.Rect(0, screen_height - fenster_breite, screen_width, fenster_breite)
            pygame.draw.rect(screen, (255, 255, 255), info_fenster, 0, 0)
            font_info_text = pygame.font.Font(None, 44)
            font_info_text.set_italic(True)
            info_text = font_info_text.render(random_text, True, (180, 0, 130))
            screen.blit(info_text, (screen_width/2.3 - (len(random_text)*6.6), screen_height - fenster_breite/2 - 15))

        elif info == 0:
            random_text = random.choice(info_texte)
        if shade > 39:
            screen.blit(highscore_text, (9, 16))

        # Neustart
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                shade = 255
            if event.type == pygame.KEYUP:

                if key[pygame.K_UP]:
                    if count == 0:
                        right = False
                        left = False
                        down = False
                        up = True
                        top_right_radius = top_left_radius = rund
                        bottom_left_radius = bottom_right_radius = eckig
                    if not down and count < 3:
                        right = False
                        left = False
                        up = True
                        top_right_radius = top_left_radius = rund
                        bottom_left_radius = bottom_right_radius = eckig
                    if not down and count > 2 and body[-1][1] == player_1.y:
                        right = False
                        left = False
                        up = True
                        top_right_radius = top_left_radius = rund
                        bottom_left_radius = bottom_right_radius = eckig

                if key[pygame.K_DOWN]:
                    if count == 0:
                        right = False
                        left = False
                        up = False
                        down = True
                        top_right_radius = top_left_radius = eckig
                        bottom_left_radius = bottom_right_radius = rund
                    if not up and count < 3:
                        right = False
                        left = False
                        down = True
                        top_right_radius = top_left_radius = eckig
                        bottom_left_radius = bottom_right_radius = rund
                    if not up and count > 2 and body[-1][1] == player_1.y:
                        right = False
                        left = False
                        down = True
                        top_right_radius = top_left_radius = eckig
                        bottom_left_radius = bottom_right_radius = rund

                if key[pygame.K_LEFT]:
                    if count == 0:
                        up = False
                        down = False
                        right = False
                        left = True
                        top_right_radius = bottom_right_radius = eckig
                        bottom_left_radius = top_left_radius = rund
                    if not right and count < 3:
                        up = False
                        down = False
                        left = True
                        top_right_radius = bottom_right_radius = eckig
                        bottom_left_radius = top_left_radius = rund
                    if not right and count > 2 and body[-1][0] == player_1.x:
                        up = False
                        down = False
                        left = True
                        top_right_radius = bottom_right_radius = eckig
                        bottom_left_radius = top_left_radius = rund

                if key[pygame.K_RIGHT]:
                    if count == 0:
                        up = False
                        down = False
                        left = False
                        right = True
                        top_right_radius = bottom_right_radius = rund
                        bottom_left_radius = top_left_radius = eckig
                    if not left and count < 3:
                        up = False
                        down = False
                        right = True
                        top_right_radius = bottom_right_radius = rund
                        bottom_left_radius = top_left_radius = eckig
                    if not left and count > 2 and body[-1][0] == player_1.x:
                        up = False
                        down = False
                        right = True
                        top_right_radius = bottom_right_radius = rund
                        bottom_left_radius = top_left_radius = eckig
                if key[pygame.K_g]:
                    if grenzen_an == 1:
                        grenzen_an = 0
                    elif grenzen_an == 0:
                        grenzen_an = 1
                if key[pygame.K_t]:
                    if info == 0:
                        info = 1
                    elif info == 1:
                        info = 0
                if key[pygame.K_b]:
                    if bunt_an == 0:
                        bunt_an = 1
                    elif bunt_an == 1:
                        bunt_an = 0

            if event.type == pygame.KEYUP:
                if key[pygame.K_SPACE] and info == 0:
                    body.clear()
                    gold.topleft = (random_x * block_size, random_y * block_size)
                    farbhistorie = [(0, 255, 0)]
                    player_1.topleft = (screen_width / 2, screen_height / 2)
                    runde_timer = 0
                    count = 0
                    shade = 255
                    left = False
                    up = False
                    down = False
                    right = True
                    game_over = False
                    top_right_radius = bottom_right_radius = rund
                    bottom_left_radius = top_left_radius = eckig

        screen.blit(count_text, (screen_width / 2, 10))
        screen.blit(easter_egg_text, (screen_width * 1.2, screen_height * 1.1))

        if key[pygame.K_ESCAPE]:
            speichern(highscore, 'highscore_snake')
            frontpage.startseite()
        pygame.display.update()
        clock.tick(fps)
    speichern(highscore, 'highscore_snake')
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    snake_game()
