import frontpage


def multiplayer_lv2():
    import pygame
    import random

    pygame.init()
    sw = 1200
    sh = 850

    screen = pygame.display.set_mode((sw, sh))
    clock = pygame.time.Clock()

    startposition_1_x = 50
    startposition_2_x = 1150
    startposition_y = 400

    random_start = random.randint(100, 1000)
    random_start_2 = random.randint(50, 700)
    random_start_4 = random.randint(100, 1000)
    random_start_3 = random.randint(50, 700)
    random_start_5 = random.randint(100, 1000)
    random_start_6 = random.randint(50, 700)

    player = pygame.Rect(startposition_1_x, startposition_y, 20, 20)
    player_2 = pygame.Rect(startposition_2_x, startposition_y, 20, 20)
    goal = pygame.Rect(random_start, random_start_2, 20, 20)
    enemy_1 = pygame.Rect(100, 100, 35, 35)
    enemy_2 = pygame.Rect(random_start, random_start_2, 60, 60)
    enemy_3 = pygame.Rect(300, 200, 40, 40)
    enemy_4 = pygame.Rect(500, 300, 40, 40)
    enemy_5 = pygame.Rect(700, 400, 40, 40)
    enemy_6 = pygame.Rect(random_start_4, random_start_3, 60, 60)
    enemy_7 = pygame.Rect(random_start_5, random_start_6, 60, 60)

    teleport = pygame.Rect(100, 100, 30, 30)
    teleport_2 = pygame.Rect(1050, 650, 30, 30)

    ability_1 = pygame.Rect(800, 250, 15, 15)
    ability_2 = pygame.Rect(200, 500, 15, 15)

    punkte_player = 0
    punkte_player_2 = 0

    speed_x = 2
    speed_y = 2
    speed_2_y = 2
    start_x, start_y = 100, 100
    end_x, end_y = 600, 400

    start_x_2, start_y_2 = 300, 400
    end_x_2, end_y_2 = 300, 50

    start_x_3, start_y_3 = 500, 400
    end_x_3, end_y_3 = 500, 50

    start_x_4, start_y_4 = 700, 400
    end_x_4, end_y_4 = 700, 50

    run = True

    while run:

        screen.fill((0, 0, 0))

        random_a = random.randint(100, 1000)
        random_b = random.randint(50, 700)
        random_c = random.randint(100, 1000)
        random_d = random.randint(50, 700)
        random_e = random.randint(100, 1000)
        random_f = random.randint(50, 700)
        random_g = random.randint(100, 1000)
        random_h = random.randint(50, 700)
        random_i = random.randint(100, 1000)
        random_j = random.randint(50, 700)
        pygame.draw.rect(screen, (250, 0, 250), player)
        pygame.draw.rect(screen, (250, 250, 0), player_2)
        pygame.draw.rect(screen, (250, 250, 250), goal)

        pygame.draw.rect(screen, (250, 250, 250), teleport, 2)
        pygame.draw.rect(screen, (250, 250, 250), teleport_2, 2)
        font = pygame.font.Font(None, 74)

        counter_text = font.render(str(punkte_player), True, (250, 0, 250))
        counter_text_2 = font.render(str(punkte_player_2), True, (250, 250, 0))
        winner_text = font.render(str("Pink hat gewonnen"), True, (250, 0, 250))
        winner_text_2 = font.render(str("Gelb hat gewonnen"), True, (250, 250, 0))
        screen.blit(counter_text, (150, 20))
        screen.blit(counter_text_2, (1000, 20))
        pygame.draw.rect(screen, (250, 0, 0), enemy_1)
        pygame.draw.rect(screen, (250, 0, 250), ability_1, 2)
        pygame.draw.rect(screen, (250, 250, 0), ability_2, 2)

        enemy_1.x += speed_x
        enemy_1.y += speed_y
        if enemy_1.x >= end_x or enemy_1.x <= start_x:
            speed_x = -speed_x
        if enemy_1.y >= end_y or enemy_1.y <= start_y:
            speed_y = -speed_y

        enemy_3.y += speed_2_y
        if enemy_3.y >= end_y_2 or enemy_3.y <= start_y_2:
            speed_2_y = - speed_2_y

        enemy_4.y += speed_2_y
        if enemy_4.y <= end_y_3 or enemy_4.y >= start_y_3:
            speed_2_y = - speed_2_y

        enemy_5.y += - speed_2_y
        if enemy_5.y >= end_y_4 or enemy_5.y <= start_y_4:
            speed_2_y = - speed_2_y

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            run = False
            frontpage.startseite()
        if key[pygame.K_a]:
            player.move_ip(-1, 0)
        if key[pygame.K_d]:
            player.move_ip(1, 0)
        if key[pygame.K_w]:
            player.move_ip(0, -1)
        if key[pygame.K_s]:
            player.move_ip(0, 1)
        if key[pygame.K_v]:
            if key[pygame.K_a]:
                player.move_ip(-2, 0)
            if key[pygame.K_d]:
                player.move_ip(2, 0)
            if key[pygame.K_w]:
                player.move_ip(0, -2)
            if key[pygame.K_s]:
                player.move_ip(0, 2)

        if key[pygame.K_LEFT]:
            player_2.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
            player_2.move_ip(1, 0)
        if key[pygame.K_UP]:
            player_2.move_ip(0, -1)
        if key[pygame.K_DOWN]:
            player_2.move_ip(0, 1)
        if key[pygame.K_m]:
            if key[pygame.K_LEFT]:
                player_2.move_ip(-2, 0)
            if key[pygame.K_RIGHT]:
                player_2.move_ip(2, 0)
            if key[pygame.K_UP]:
                player_2.move_ip(0, -2)
            if key[pygame.K_DOWN]:
                player_2.move_ip(0, 2)

        pygame.draw.rect(screen, (255, 0, 0), enemy_2)
        pygame.draw.rect(screen, (255, 0, 0), enemy_3)
        pygame.draw.rect(screen, (255, 0, 0), enemy_4)
        pygame.draw.rect(screen, (255, 0, 0), enemy_5)
        pygame.draw.rect(screen, (255, 0, 0), enemy_6)
        pygame.draw.rect(screen, (255, 0, 0), enemy_7)

        if player.x >= 1200 or player.x <= 0:
            player.topleft = (startposition_1_x, startposition_y)
        if player.y >= 850 or player.y <= 0:
            player.topleft = (startposition_1_x, startposition_y)

        if player_2.x >= 1200 or player_2.x <= 0:
            player_2.topleft = (startposition_2_x, startposition_y)
        if player_2.y >= 850 or player_2.y <= 0:
            player_2.topleft = (startposition_2_x, startposition_y)

        if enemy_2.colliderect(goal):
            goal.topleft = (random_a, random_b)
        if enemy_6.colliderect(goal):
            goal.topleft = (random_a, random_b)

        if player.colliderect(teleport):
            player.topleft = (1000, 700)
        if player_2.colliderect(teleport):
            player_2.topleft = (1000, 700)
        if player.colliderect(ability_1):
            ability_1.topleft = (random_a, random_b)
            punkte_player += 1
        if player_2.colliderect(ability_2):
            ability_2.topleft = (random_e, random_f)
            punkte_player_2 += 1

        if ability_1.colliderect(enemy_2):
            ability_1.topleft = (random_a, random_b)
        if ability_1.colliderect(enemy_6):
            ability_1.topleft = (random_a, random_b)
        if ability_1.colliderect(enemy_7):
            ability_1.topleft = (random_a, random_b)
        if ability_2.colliderect(enemy_2):
            ability_2.topleft = (random_a, random_b)
        if ability_2.colliderect(enemy_6):
            ability_2.topleft = (random_a, random_b)
        if ability_2.colliderect(enemy_7):
            ability_2.topleft = (random_a, random_b)

        if player.colliderect(teleport_2):
            player.topleft = (200, 150)
        if player_2.colliderect(teleport_2):
            player_2.topleft = (200, 150)

        if player.colliderect(goal):
            goal.topleft = (random_a, random_b)
            punkte_player += 2
        if player_2.colliderect(goal):
            goal.topleft = (random_a, random_b)
            punkte_player_2 += 2
        if punkte_player >= 10:
            screen.blit(winner_text, (350, 20))
            player.topleft = (startposition_1_x, startposition_y)
            player_2.topleft = (startposition_2_x, startposition_y)
        if punkte_player_2 >= 10:
            screen.blit(winner_text_2, (350, 20))
            player.topleft = (startposition_1_x, startposition_y)
            player_2.topleft = (startposition_2_x, startposition_y)
        if player.colliderect(enemy_1):
            punkte_player -= 1
            player.topleft = (startposition_1_x, startposition_y)
        if player.colliderect(enemy_7):
            punkte_player -= 1
            player.topleft = (startposition_1_x, startposition_y)
        if player_2.colliderect(enemy_7):
            punkte_player_2 -= 1
            player_2.topleft = (startposition_2_x, startposition_y)
        if player.colliderect(enemy_2):
            punkte_player -= 1
            player.topleft = (startposition_1_x, startposition_y)
        if player.colliderect(enemy_3):
            punkte_player -= 1
            player.topleft = (startposition_1_x, startposition_y)
        if player.colliderect(enemy_4):
            punkte_player -= 1
            player.topleft = (startposition_1_x, startposition_y)
        if player.colliderect(enemy_5):
            punkte_player -= 1
            player.topleft = (startposition_1_x, startposition_y)
        if player.colliderect(enemy_6):
            punkte_player -= 1
            player.topleft = (startposition_1_x, startposition_y)
        if player_2.colliderect(enemy_1):
            punkte_player_2 -= 1
            player_2.topleft = (startposition_2_x, startposition_y)
        if player_2.colliderect(enemy_2):
            punkte_player_2 -= 1
            player_2.topleft = (startposition_2_x, startposition_y)
        if player_2.colliderect(enemy_3):
            punkte_player_2 -= 1
            player_2.topleft = (startposition_2_x, startposition_y)
        if player_2.colliderect(enemy_4):
            punkte_player_2 -= 1
            player_2.topleft = (startposition_2_x, startposition_y)
        if player_2.colliderect(enemy_5):
            punkte_player_2 -= 1
            player_2.topleft = (startposition_2_x, startposition_y)
        if player_2.colliderect(enemy_6):
            punkte_player_2 -= 1
            player_2.topleft = (startposition_2_x, startposition_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.topleft = (startposition_1_x, startposition_y)
                    player_2.topleft = (startposition_2_x, startposition_y)
                    goal.topleft = (random_a, random_b)
                    punkte_player = 0
                    punkte_player_2 = 0
                    enemy_6.topleft = (random_a, random_b)
                    enemy_2.topleft = (random_c, random_d)
                    enemy_7.topleft = (random_e, random_f)
                    ability_1.topleft = (random_g, random_h)
                    ability_2.topleft = (random_i, random_j)

        pygame.display.update()
        clock.tick(600)
    pygame.quit()


if __name__ == "__main__":
    multiplayer_lv2()
