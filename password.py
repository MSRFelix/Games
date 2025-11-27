benutzernamen = {}


def password():
    import pygame
    import sys
    import frontpage
    import os
    import json

    pygame.init()

    # Daten laden
    def laden(dateiname, default):
        if os.path.exists(dateiname):
            with open(dateiname, 'r') as json_datei:
                return json.load(json_datei)
        else:
            return default

    def speichern(liste, dateiname):
        with open(dateiname, 'w') as json_datei:
            json.dump(liste, json_datei)

    sw = 300
    sh = 260
    base_font = pygame.font.Font(None, 30)
    user_text = ''
    benutzer_text = ''
    color_active = (0, 0, 0)
    color_passive = (150, 150, 150)
    color_in_use = color_passive
    color_in_use_benutzer = color_passive

    color = False
    color_benutzer = False

    input_field = pygame.Rect(80, 190, 125, 25)
    input_field_benutzer = pygame.Rect(80, 100, 125, 25)
    title = "Kennwort eingeben"
    title_benutzer = "Benutzer eingeben"

    screen = pygame.display.set_mode((sw, sh))
    pygame.display.set_caption("Mathetrainer")
    fps = 60
    clock = pygame.time.Clock()
    run = True
    active = False
    active_benutzer = False

    falsches_passwort_eingegeben = False

    while run:

        clock.tick(fps)
        screen.fill((250, 250, 250))

        pygame.draw.rect(screen, color_in_use, input_field, 2, 4)
        pygame.draw.rect(screen, color_in_use_benutzer, input_field_benutzer, 2, 4)

        displayed_text = '*' * len(user_text)
        text_surface = base_font.render(displayed_text, True, color_in_use)
        displayed_text_benutzer = benutzer_text
        text_surface_benutzer = base_font.render(displayed_text_benutzer, True, color_in_use_benutzer)

        font_2 = pygame.font.Font(None, 30)
        font_4 = pygame.font.Font(None, 23)
        screen.blit(text_surface, (input_field.x + 5, input_field.y + 3))
        screen.blit(text_surface_benutzer, (input_field_benutzer.x + 5, input_field_benutzer.y + 3))

        title_text = font_2.render(str(title), True, (0, 0, 0))
        title_text_benutzer = font_2.render(str(title_benutzer), True, (0, 0, 0))

        falsches_passwort_text = font_2.render("falsches Passwort", True, (255, 0, 0))

        font_4.set_italic(True)
        input_field.w = max(125, text_surface.get_width() + 10)
        input_field_benutzer.w = max(125, text_surface_benutzer.get_width() + 10)

        screen.blit(title_text, (56, 142))
        screen.blit(title_text_benutzer, (56, 52))

        if color:
            color_in_use = color_active
        else:
            color_in_use = color_passive

        if color_benutzer:
            color_in_use_benutzer = color_active
        else:
            color_in_use_benutzer = color_passive

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_field.collidepoint(event.pos):
                    active = True
                    color = True
                else:
                    active = False
                    color = False
                if input_field_benutzer.collidepoint(event.pos):
                    active_benutzer = True
                    color_benutzer = True
                else:
                    active_benutzer = False
                    color_benutzer = False
                falsches_passwort_eingegeben = False
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if user_text == "password":
                        benutzernamen[user_text] = benutzer_text
                        speichern(benutzernamen, 'benutzernamen')
                        frontpage.startseite()
                    else:
                        user_text = ''
                        falsches_passwort_eingegeben = True
                else:
                    user_text += event.unicode
            if event.type == pygame.KEYDOWN and active_benutzer:
                if event.key == pygame.K_BACKSPACE:
                    benutzer_text = benutzer_text[:-1]
                elif event.key == pygame.K_RETURN:
                    active = True
                    color = True
                    active_benutzer = False
                    color_benutzer = False
                else:
                    benutzer_text += event.unicode
        if falsches_passwort_eingegeben:
            screen.blit(falsches_passwort_text, (50, 230))

        pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    password()
