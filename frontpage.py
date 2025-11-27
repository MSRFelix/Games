def startseite():
    from pong import level_1
    import sys
    import pygame
    import flappy_bird
    import mathe_trainer
    import cars_lv1
    import snake
    import memory
    import lotto
    import os
    import json
    import multiplayer_lv2

    # laden eines Spielstandes
    def laden(dateiname, default):
        if os.path.exists(dateiname):
            with open(dateiname, 'r') as json_datei:
                return json.load(json_datei)
        else:
            return default

    pygame.init()

    screen_width = 1100
    screen_hight = 600

    spieler = laden('benutzernamen', "Spieler")

    screen = pygame.display.set_mode((screen_width, screen_hight), pygame.RESIZABLE)
    pygame.display.set_caption("Mathe Trainer")
    introduction = "Startseite"
    hallo = f"Hallo {spieler["password"]}"
    button_pong = "Pong"
    button_ratespiel = "Snake"
    button_tiles = "Squares"
    button_flappy = "Flappy Bird"
    button_mathe = "Mathe"
    button_cars = "Cars"
    button_lotto = "Lotto"
    button_memory = "Memory"
    button_0 = pygame.Rect(480, 120, 120, 25)
    button_1 = pygame.Rect(480, 200, 120, 25)
    button_2 = pygame.Rect(480, 280, 120, 25)
    button_3 = pygame.Rect(480, 360, 120, 25)
    button_4 = pygame.Rect(480, 440, 123, 25)
    button_5 = pygame.Rect(480, 520, 120, 25)
    button_8 = pygame.Rect(950, 450, 120, 25)
    button_9 = pygame.Rect(950, 400, 120, 25)

    run = True
    while run:
        screen.fill((0, 0, 0))
        click = False
        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (0, 150, 0), button_0, 0, 5)
        pygame.draw.rect(screen, (0, 150, 0), button_1, 0, 5)
        pygame.draw.rect(screen, (0, 150, 0), button_2, 0, 5)
        pygame.draw.rect(screen, (0, 150, 0), button_3, 0, 5)
        pygame.draw.rect(screen, (0, 150, 0), button_4, 0, 5)
        pygame.draw.rect(screen, (0, 150, 0), button_5, 0, 5)
        pygame.draw.rect(screen, (0, 150, 0), button_8, 0, 5)
        pygame.draw.rect(screen, (0, 150, 0), button_9, 0, 5)

        font = pygame.font.Font(None, 73)
        font_2 = pygame.font.Font(None, 33)
        titulo = font.render(str(introduction), True, (255, 255, 255))
        hallo_text = font_2.render(str(hallo), True, (0, 105, 255))

        button_0_text = font_2.render(str(button_mathe), True, (0, 0, 0))
        button_1_text = font_2.render(str(button_pong), True, (0, 0, 0))
        button_2_text = font_2.render(str(button_ratespiel), True, (0, 0, 0))
        button_3_text = font_2.render(str(button_tiles), True, (0, 0, 0))
        button_4_text = font_2.render(str(button_flappy), True, (0, 0, 0))
        button_5_text = font_2.render(str(button_cars), True, (0, 0, 0))
        button_8_text = font_2.render(str(button_lotto), True, (0, 0, 0))
        button_9_text = font_2.render(str(button_memory), True, (0, 0, 0))

        screen.blit(button_0_text, (508, 122))
        screen.blit(button_1_text, (512, 201))
        screen.blit(button_2_text, (507, 282))
        screen.blit(button_3_text, (500, 362))
        screen.blit(button_4_text, (480, 442))
        screen.blit(button_5_text, (515, 522))
        screen.blit(button_8_text, (979, 452))
        screen.blit(button_9_text, (965, 402))

        screen.blit(titulo, (425, 25))
        screen.blit(hallo_text, (475, 80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

            if button_0.collidepoint(mx, my) and click:
                mathe_trainer.mathe()
            if button_1.collidepoint(mx, my) and click:
                level_1()
            if button_2.collidepoint(mx, my) and click:
                snake.snake_game()
            if button_3.collidepoint(mx, my) and click:
                multiplayer_lv2.multiplayer_lv2()
            if button_4.collidepoint(mx, my) and click:
                flappy_bird.flappy()
            if button_5.collidepoint(mx, my) and click:
                cars_lv1.cars_lv1()
            if button_8.collidepoint(mx, my) and click:
                lotto.lotto()
            if button_9.collidepoint(mx, my) and click:
                memory.main()

        pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    startseite()
