def mathe():
    import pygame
    import sys
    import random
    import frontpage
    import json
    import os

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

    def display_text_animation(ort, text, position, font, colour, delay=30):
        """Zeigt den Text Buchstabe für Buchstabe an."""
        for char in text:
            text_feld = font.render(char, True, colour)
            ort.blit(text_feld, position)
            pygame.display.update()
            pygame.time.delay(delay)
            position[0] += 20


    spieler = laden('benutzernamen', "Spieler")

    screen_width = 1200
    screen_height = 850
    base_font = pygame.font.Font(None, 30)
    user_text = ''
    fps = 300
    color_active = (0, 0, 0)
    color_passive = (150, 150, 150)
    color_in_use = color_passive
    color = False
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Mathe Trainer")
    title = "Mathetrainer"
    clock = pygame.time.Clock()
    winner_speeches = [f"\'Gut gemacht, {spieler["password"]}!\'", "\'Wow, ich bin beeindruckt\'", "\'Sehr gut\'"]
    looser_speeches = ["\'Ich bin enttäuscht\'", "\'Das geht aber besser.\'",
                       "\'Leider falsch\'"]
    winner = random.choice(winner_speeches)
    looser = random.choice(looser_speeches)
    input_field = pygame.Rect(550, 500, 125, 25)

    zahl_1_multi = random.randint(0, 10)
    zahl_2_multi = random.randint(3, 20)
    zahl_1_add = random.randint(0, 100)
    zahl_2_add = random.randint(30, 100)
    zahl_1_sub = random.randint(30, 100)
    zahl_2_sub = random.randint(1, 30)

    spielstand = laden('highscore_mathe_trainer', 0)
    highscore = spielstand

    richtig_beantwortet: int = 0
    falsch_beantwortet: int = 0
    keine_zahl: int = 0
    no_number = "Das ist keine Zahl!!!"

    white = (255, 255, 255)

    background = pygame.image.load("src_mathe/mathe_bg.PNG").convert_alpha()
    background = pygame.transform.scale(background, (screen_width, screen_height-100))
    background_papier = pygame.image.load("src_mathe/kariertes_papier.PNG").convert_alpha()
    background_papier = pygame.transform.scale(background_papier, (340, 400))

    aufgabe_art_random = random.randint(1, 3)

    active = False
    run = True
    while run:
        if richtig_beantwortet > highscore:
            highscore = richtig_beantwortet
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(background_papier, (450, 300))

        text_richtig_in_folge = f"richtige Antworten in Folge: {richtig_beantwortet} / 10"

        task_text_add = "Was ergibt: " + str(zahl_1_add) + "+" + str(zahl_2_add)
        correct_answer_add = zahl_1_add + zahl_2_add

        task_text_multi = "Was ergibt: " + str(zahl_1_multi) + "*" + str(zahl_2_multi)
        correct_answer_multi = zahl_1_multi * zahl_2_multi

        task_text_sub = "Was ergibt: " + str(zahl_1_sub) + "-" + str(zahl_2_sub)
        correct_answer_sub = zahl_1_sub - zahl_2_sub

        korrekte_antworten = [correct_answer_multi, correct_answer_add, correct_answer_sub]

        pygame.draw.rect(screen, color_in_use, input_field, 2, 4)
        text_surface = base_font.render(user_text, True, color_in_use)
        font_2 = pygame.font.Font(None, 73)
        font_3 = pygame.font.Font(None, 53)
        font_4 = pygame.font.Font(None, 43)
        screen.blit(text_surface, (input_field.x + 5, input_field.y + 3))
        font_highscore = pygame.font.Font(None, 44)
        highscore_text = font_highscore.render("Highscore: " + str(highscore), True, (0, 0, 0))
        screen.blit(highscore_text, (550, 266))

        title_text = font_2.render(str(title), True, (255, 255, 255))
        richtig_text = font_3.render(str(text_richtig_in_folge), True, (10, 80, 10))
        screen.blit(richtig_text, (350, 230))
        font_4.set_italic(True)
        input_field.w = max(125, text_surface.get_width() + 10)
        screen.blit(title_text, (450, 22))
        if aufgabe_art_random == 1:
            task_text = font_3.render(str(task_text_multi), True, (0, 0, 0))
            screen.blit(task_text, (470, 322))
        elif aufgabe_art_random == 2:
            task_text = font_3.render(str(task_text_add), True, (0, 0, 0))
            screen.blit(task_text, (470, 322))
        elif aufgabe_art_random == 3:
            task_text = font_3.render(str(task_text_sub), True, (0, 0, 0))
            screen.blit(task_text, (470, 322))

        if color:
            color_in_use = color_active
        else:
            color_in_use = color_passive
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                speichern(highscore, 'highscore_mathe_trainer')
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_field.collidepoint(event.pos):
                    active = True
                    color = True
                else:
                    active = False
                    color = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        looser = random.choice(looser_speeches)
                        if not user_text.isdigit():
                            keine_zahl += 1
                            richtig_beantwortet = 0
                            falsch_beantwortet = 0
                        elif int(user_text) == korrekte_antworten[aufgabe_art_random-1]:
                            zahl_1_multi = random.randint(0, 10)
                            zahl_2_multi = random.randint(3, 20)
                            zahl_1_add = random.randint(0, 100)
                            zahl_2_add = random.randint(30, 100)
                            zahl_1_sub = random.randint(30, 100)
                            zahl_2_sub = random.randint(1, 30)
                            aufgabe_art_random = random.randint(1, 3)
                            keine_zahl = 0
                            richtig_beantwortet += 1
                            falsch_beantwortet = 0
                            winner = random.choice(winner_speeches)
                            user_text = ''

                        elif int(user_text) != correct_answer_multi:
                            keine_zahl = 0
                            falsch_beantwortet += 1
                            richtig_beantwortet = 0
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        if falsch_beantwortet >= 1:
            looser_text = font_4.render(str(looser), True, (255, 50, 50))
            screen.blit(looser_text, (480, 630))

        if keine_zahl >= 1:
            keine_zahl_text = font_4.render(str(no_number), True, (255, 0, 0))
            screen.blit(keine_zahl_text, (480, 630))
        if 1 <= richtig_beantwortet < 4:
            winner_text = font_4.render(winner, True, white)
            screen.blit(winner_text, (350, 760))

        if 4 <= richtig_beantwortet <= 6:
            winner_text = font_4.render(winner, True, white)
            screen.blit(winner_text, (350, 760))

        if 7 <= richtig_beantwortet <= 9:
            winner_text = font_4.render(winner, True, white)
            screen.blit(winner_text, (350, 760))

        if richtig_beantwortet >= 10:
            winner_text = font_4.render(winner, True, white)
            screen.blit(winner_text, (350, 760))

        if key[pygame.K_ESCAPE]:
            speichern(highscore, 'highscore_mathe_trainer')
            frontpage.startseite()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    mathe()
