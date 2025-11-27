import pygame
import random
import frontpage
import os
import json

# Initialisiere Pygame
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


def zurucksetzen(liste, index, default):
    liste[index] = default


def loschen(dateiname):
    if os.path.exists(dateiname):
        os.remove(dateiname)



# Konstanten
WIDTH, HEIGHT = 1400, 1000
CARD_WIDTH, CARD_HEIGHT = 150, 190
CARD_BACK_COLOR = (0, 100, 100)
FPS = 30

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 150, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)

# Schwierigkeitsgrade definieren
DIFFICULTY_LEVELS = {
    "Einfach": 4,  # 4 Paare (max. 8 Karten)
    "Mittel": 8,   # 8 Paare (max. 16 Karten)
    "Schwierig": 12  # 12 Paare (max. 24 Karten)
}


# Lade Bilder
def load_images(image_files):
    images = []
    for file in image_files:
        try:
            bild_verzeichnis = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mathe/Mädels')
            image = pygame.image.load(os.path.join(bild_verzeichnis, f"{file}.png")).convert_alpha()
            image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
            images.append(image)
        except pygame.error as e:
            print(f"Could not load image {file}: {e}")
    return images

# Funktion zur Auswahl von Bildern basierend auf der Schwierigkeit
def select_random_images(images, pairs):
    return random.sample(images, pairs)

# Spielklasse
class MemoryGame:
    def __init__(self, images, pairs):
        self.images = select_random_images(images, pairs) * 2  # Paare erstellen
        random.shuffle(self.images)
        self.grid_size = (4, (pairs * 2) // 4)  # Maximal 4 Reihen
        self.start_new_game()

    def start_new_game(self):
        random.shuffle(self.images)  # Mische die Bilder neu
        self.cards = [[self.images[i * self.grid_size[1] + j] for j in range(self.grid_size[1])]
                       for i in range(self.grid_size[0])]
        self.flipped = [[False] * self.grid_size[1] for _ in range(self.grid_size[0])]
        self.first_flip = None
        self.second_flip = None
        self.matched_pairs = 0

    def flip_card(self, row, col):
        if self.flipped[row][col] or self.second_flip is not None:
            return

        self.flipped[row][col] = True

        if self.first_flip is None:
            self.first_flip = (row, col)
        else:
            self.second_flip = (row, col)
            pygame.time.set_timer(pygame.USEREVENT, 1000)  # Timer für 1 Sekunde setzen

    def update(self):
        if self.second_flip is not None:
            # Versuche erhöhen, wenn die zweite Karte aufgedeckt wird
            if self.first_flip is not None:
                # Überprüfe, ob die Karten übereinstimmen
                if self.cards[self.first_flip[0]][self.first_flip[1]] != self.cards[self.second_flip[0]][self.second_flip[1]]:
                    # Karten nicht übereinstimmend, Karten nach 1 Sekunde umdrehen
                    pygame.time.delay(1000)
                    self.flipped[self.first_flip[0]][self.first_flip[1]] = False
                    self.flipped[self.second_flip[0]][self.second_flip[1]] = False
                else:
                    # Karten übereinstimmend
                    self.matched_pairs += 1

            self.first_flip = None
            self.second_flip = None
            pygame.time.set_timer(pygame.USEREVENT, 0)  # Stoppe den Timer

    def draw(self, screen):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                rect = pygame.Rect(j * (CARD_WIDTH + 10) + 50, i * (CARD_HEIGHT + 10) + 50, CARD_WIDTH, CARD_HEIGHT)
                if self.flipped[i][j]:
                    screen.blit(self.cards[i][j], rect.topleft)
                else:
                    pygame.draw.rect(screen, CARD_BACK_COLOR, rect)

# Hauptfunktion
def main():
    # Bilddateien hier einfügen
    bild_verzeichnis = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mathe/Mädels')
    bild_test = pygame.image.load(os.path.join(bild_verzeichnis, f"{bild_auswahl}.png")).convert_alpha()

    images = load_images(image_files)
    selected_difficulty = "Einfach"  # Standard-Schwierigkeitsgrad
    pairs = DIFFICULTY_LEVELS[selected_difficulty]

    game = MemoryGame(images, pairs)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Memory Spiel')
    clock = pygame.time.Clock()
    running = True

    difficulty_index = list(DIFFICULTY_LEVELS.keys()).index(selected_difficulty)
    attempt_counter = 0  # Zähler für die Versuche

    while running:
        screen.fill((0, 0, 0))
        game.draw(screen)

        # Button für neues Spiel
        button_rect = pygame.Rect(235, 900, 250, 50)
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

        font = pygame.font.Font(None, 36)
        text = font.render("Neues Spiel", True, WHITE)
        screen.blit(text, (button_rect.x + 50, button_rect.y + 10))

        # Button für Schwierigkeitsgrad
        difficulty_button_rect = pygame.Rect(500, 900, 210, 50)
        if difficulty_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, difficulty_button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, difficulty_button_rect)

        difficulty_text = font.render("Level: " + list(DIFFICULTY_LEVELS.keys())[difficulty_index], True, WHITE)
        screen.blit(difficulty_text, (difficulty_button_rect.x + 10, difficulty_button_rect.y + 10))

        # Versuchszähler anzeigen
        if list(DIFFICULTY_LEVELS.keys())[difficulty_index] == "Schwierig":
            attempt_text = font.render("Versuche: " + str(attempt_counter) + " / 24", True, WHITE)
            screen.blit(attempt_text, (WIDTH - 300, 50))

            bild_verzeichnis = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mathe/Mädels')
            bild_test = pygame.image.load(os.path.join(bild_verzeichnis, f"{bild_auswahl}.png"))
            bild_neu = pygame.transform.scale(bild_test, (30, 37))
            screen.blit(bild_neu, (1200, 150))
        else:
            attempt_text = font.render("Versuche: " + str(attempt_counter), True, WHITE)
            screen.blit(attempt_text, (WIDTH - 300, 50))

        # Game Over Nachricht
        if 2 * game.matched_pairs == len(game.images):
            font = pygame.font.Font(None, 48)
            game_over_text = font.render(f"Du hast alle Paare in {attempt_counter} Runden gefunden.", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT - 140))

        if 2 * game.matched_pairs == len(game.images) and attempt_counter < 25 and list(DIFFICULTY_LEVELS.keys())[difficulty_index] == "Schwierig":
            font_winner = pygame.font.Font(None, 48)
            winner_text_belohnung = font_winner.render("Du hast einen neuen Charakter freigeschaltet", True, (252, 18, 190))
            screen.blit(winner_text_belohnung, (WIDTH / 2 - 320, 10))
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if key[pygame.K_ESCAPE]:
                    frontpage.startseite()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pairs = DIFFICULTY_LEVELS[selected_difficulty]
                    images_for_game = select_random_images(images, pairs)  # Neue zufällige Bilder auswählen
                    game = MemoryGame(images_for_game, pairs)  # Neues Spiel starten
                    attempt_counter = 0  # Versuchszähler zurücksetzen
                elif difficulty_button_rect.collidepoint(event.pos):
                    # Schwierigkeit ändern
                    difficulty_index = (difficulty_index + 1) % len(DIFFICULTY_LEVELS)
                    selected_difficulty = list(DIFFICULTY_LEVELS.keys())[difficulty_index]
                    pairs = DIFFICULTY_LEVELS[selected_difficulty]
                    images_for_game = select_random_images(images, pairs)  # Neue zufällige Bilder auswählen
                    game = MemoryGame(images_for_game, pairs)  # Neues Spiel starten
                    attempt_counter = 0  # Versuchszähler zurücksetzen
                else:
                    x, y = event.pos
                    col = (x - 50) // (CARD_WIDTH + 10)
                    row = (y - 50) // (CARD_HEIGHT + 10)
                    if 0 <= row < game.grid_size[0] and 0 <= col < game.grid_size[1]:
                        game.flip_card(row, col)
            elif event.type == pygame.USEREVENT:
                if game.second_flip is not None:  # Versuche erhöhen, wenn die zweite Karte aufgedeckt wird
                    attempt_counter += 1
                game.update()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
