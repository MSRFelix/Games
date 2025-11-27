import random

import pygame
import sys

pygame.init()

pygame.mixer.music.load("Star Wars - Cantina Song.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)

sound = pygame.mixer.Sound("pew.mp3")
pygame.mixer.Sound.set_volume(sound, 0.2)

screen_width = 1100
screen_hight = 600

vogel_player = pygame.image.load("vogel.png")
vogel_player = pygame.transform.scale(vogel_player, (55, 55))
player_1 = vogel_player.get_rect()
player_1.center = screen_width/5, screen_hight/2

vogel_gegner = pygame.image.load("gegner.png")
vogel_gegner = pygame.transform.scale(vogel_gegner, (55, 55))
goal = vogel_gegner.get_rect()

zombie_gegner = pygame.image.load("zombie.png")
zombie_gegner = pygame.transform.scale(zombie_gegner, (55, 55))

zombie_2_gegner = pygame.image.load("zombie_2.png")
zombie_2_gegner = pygame.transform.scale(zombie_2_gegner, (55, 55))

goal_2 = zombie_gegner.get_rect()
goal_3 = zombie_2_gegner.get_rect()
goal_4 = vogel_gegner.get_rect()
goal_2.center = 850, 200
goal_3.center = 1050, 300
goal_4.center = 950, 250
goal.center = 1050, 450

background = pygame.image.load("C:\\Users\\Bwdlz\\Desktop\\mathe\\weltraum.jpg")
background = pygame.transform.scale(background, (screen_width, screen_hight))
screen = pygame.display.set_mode("Pew")

lenght = random.randint(100, 400)
start = random.randint(300, 550)
lenght_2 = random.randint(100, 400)
start_2 = random.randint(300, 550)

player_speed_y = 1
obstacle_speed_x = 1

obstacle_1 = pygame.Rect(950, 0, 30, lenght)
obstacle_2 = pygame.Rect(1200, start, 30, 700)
obstacle_3 = pygame.Rect(1500, 0, 30, lenght_2)
obstacle_4 = pygame.Rect(1800, start_2, 30, 700)

punkte = 0
schuss_speed = 2
schusse = []
schusse_aktiv = 0
for i in range(1000):
    schuss_1 = pygame.Rect(screen_width/5+12, player_1.y+12, 15, 5)
    schusse.append(schuss_1)
schuss_ok = False
run = True
vidas = 10
goal_speed = 2
goal_2_speed = 1
goal_3_speed = 3
goal_4_speed = 2

color_random_1 = random.randint(5, 255)
color_random_2 = random.randint(5, 255)
color_random_3 = random.randint(5, 255)
color_random_4 = random.randint(5, 255)


while run:
    screen.blit(background, (0, 0))

    new_hight = random.randint(100, 400)
    start = random.randint(300, 550)

    screen.blit(vogel_player, player_1)
    screen.blit(vogel_gegner, goal)
    screen.blit(zombie_gegner, goal_2)
    screen.blit(zombie_2_gegner, goal_3)
    screen.blit(vogel_gegner, goal_4)

    pygame.draw.rect(screen, (color_random_1, 0, 0), obstacle_1)
    pygame.draw.rect(screen, (250, color_random_2, 0), obstacle_2)
    pygame.draw.rect(screen, (250, 0, color_random_3), obstacle_3)
    pygame.draw.rect(screen, (color_random_1, color_random_3, color_random_4), obstacle_4)

    goal.x += goal_speed
    goal_2.x += goal_2_speed
    goal_3.x += goal_3_speed
    goal_4.x += goal_4_speed

    if goal.x >= 1000:
        goal_speed = -2
    if goal.x <= 100:
        goal_speed = 2

    if goal_2.x >= 1000:
        goal_2_speed = -1
    if goal_2.x <= 100:
        goal_2_speed = 1

    if goal_3.x >= 1000:
        goal_3_speed = -3
    if goal_3.x <= 100:
        goal_3_speed = 3

    if goal_4.x >= 800:
        goal_4_speed = -2
    if goal_4.x <= 100:
        goal_4_speed = 2

    if player_1.colliderect(goal):
        vidas -= 1
        goal.topleft = (random.randint(900, 1070), random.randint(200, 500))

    if player_1.colliderect(goal_2):
        vidas -= 1
        goal_2.topleft = (random.randint(900, 1070), random.randint(200, 500))

    if player_1.colliderect(goal_3):
        vidas -= 1
        goal_3.topleft = (random.randint(900, 1070), random.randint(200, 500))

    if player_1.colliderect(goal_4):
        vidas -= 1
        goal_4.topleft = (random.randint(900, 1070), random.randint(200, 500))

    font = pygame.font.Font(None, 74)
    counter_text = font.render(str(punkte), True, (250, 250, 250))
    vidas_text = font.render("Leben: " + str(vidas), True, (250, 250, 250))
    loose_text = font.render(str("game over"), True, (250, 250, 255))
    screen.blit(counter_text, (550, 20))
    screen.blit(vidas_text, (100, 20))

    player_1.y += player_speed_y
    obstacle_1.x -= obstacle_speed_x
    obstacle_2.x -= obstacle_speed_x
    obstacle_3.x -= obstacle_speed_x
    obstacle_4.x -= obstacle_speed_x

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        player_speed_y = -4
    else:
        player_speed_y = 1

    if key[pygame.K_s]:
        sound.play()
        schusse_aktiv += 0.1
        print(schusse_aktiv)
        for i in range(int(schusse_aktiv)):
            schusse[int(schusse_aktiv)].topleft = (screen_width/5+12, player_1.y+12)

    for i in range(int(schusse_aktiv)):
        pygame.draw.rect(screen, (20, 250, 20), schusse[i])
        schusse[i].x += schuss_speed
        if schusse[i].colliderect(goal):
            punkte += 1
            schusse.remove(schusse[i])
            goal.topleft = (random.randint(900, 1070), random.randint(200, 500))

        if schusse[i].colliderect(goal_2):
            punkte += 1
            vidas += 1
            schusse.remove(schusse[i])
            goal_2.topleft = (random.randint(900, 1070), random.randint(200, 350))

        if schusse[i].colliderect(goal_3):
            punkte += 1
            schusse.remove(schusse[i])
            goal_3.topleft = (random.randint(900, 1070), random.randint(200, 350))

        if schusse[i].colliderect(goal_4):
            punkte += 1
            vidas += 1
            schusse.remove(schusse[i])
            goal_4.topleft = (random.randint(900, 1070), random.randint(200, 350))

    if player_1.y >= screen_hight or player_1.y <= -25:
        player_speed_y = 0
        obstacle_speed_x = 0
        screen.blit(loose_text, (425, 100))
        punkte = punkte

    if obstacle_1.x <= 0:
        color_random_1 = random.randint(5, 255)
        color_random_2 = random.randint(5, 255)
        color_random_3 = random.randint(5, 255)
        color_random_4 = random.randint(5, 255)
        obstacle_1.topleft = (1100, 0)
        obstacle_1.height = new_hight
    if obstacle_2.x <= 0:
        color_random_1 = random.randint(5, 255)
        color_random_2 = random.randint(5, 255)
        color_random_3 = random.randint(5, 255)
        color_random_4 = random.randint(5, 255)
        obstacle_2.topleft = (1100, start)
    if obstacle_3.x <= 0:
        color_random_1 = random.randint(5, 255)
        color_random_2 = random.randint(5, 255)
        color_random_3 = random.randint(5, 255)
        color_random_4 = random.randint(5, 255)
        obstacle_3.topleft = (1100, 0)
        obstacle_3.height = new_hight
    if obstacle_4.x <= 0:
        color_random_1 = random.randint(5, 255)
        color_random_2 = random.randint(5, 255)
        color_random_3 = random.randint(5, 255)
        color_random_4 = random.randint(5, 255)
        obstacle_4.topleft = (1100, start)
        #><

    if key[pygame.K_TAB]:
        player_1.topleft = (screen_width/5, screen_hight/2)
        obstacle_speed_x = 1
        obstacle_1.topleft = (950, 0)
        obstacle_2.topleft = (1200, start)
        obstacle_3.topleft = (1500, 0)
        obstacle_4.topleft = (1800, start)
        punkte = 0
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)

    if player_1.x == obstacle_1.x or player_1.x == obstacle_2.x:
        punkte = punkte + 1

    if player_1.x == obstacle_3.x or player_1.x == obstacle_4.x:
        punkte = punkte + 1

    if player_1.colliderect(obstacle_1):
        vidas -= 1
        obstacle_1.topleft = (1100*1.5, 0)
        obstacle_1.height = new_hight

    if player_1.colliderect(obstacle_2):
        vidas -= 1
        obstacle_2.topleft = (1100*1.5, start)

    if player_1.colliderect(obstacle_3):
        vidas -= 1
        obstacle_3.topleft = (1100*1.5, 0)
        obstacle_3.height = new_hight
    if player_1.colliderect(obstacle_4):
        obstacle_4.topleft = (1100*1.5, start)
    if vidas == 0:
        player_speed_y = 0
        obstacle_speed_x = 0
        screen.blit(loose_text, (425, 100))
        punkte = punkte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if key[pygame.K_ESCAPE]:
        run = False

    pygame.display.update()
pygame.quit()
sys.exit()

