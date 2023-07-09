import pygame as pg
import random
from settings import *

def show_word_status():
    screen_pos = 300
    for ix, val in enumerate(current_progress):
        if val == "-":
            pg.draw.line(screen, BLACK, (screen_pos + ix * 2, 280), (screen_pos + 24 + ix * 2, 280), 4)
        else:
            ltr = input_font.render(val, True, BLACK)
            screen.blit(ltr, (screen_pos + ix, 254))
            print(val)
        screen_pos += 36


def show_alpha_remaining():
    for row in range(2):
        x_pos = 62
        for column in range(13):
            if letters_guessed[row * 13 + column] == "":
                pg.draw.circle(screen, BLACK, (x_pos, 450 + (row * 60)), 23, 4)
                letter = input_font.render(alpha_list[row * 13 + column], True, BLACK)
                screen.blit(letter, (x_pos - 12, 434 + row * 60))
            x_pos += 56

def get_guess():
    if pg.mouse.get_pressed()[0]:
        pos_x, pos_y = pg.mouse.get_pos()
        if pos_y >= 427 and pos_y <= 473: row = 0
        elif pos_y >= 487 and pos_y <= 533: row = 1
        if pos_x >= 62 and pos_x <= 778:
            col = (pos_x - 56) // 56
        print(alpha_list[row * 13 + col])

# Initialization variables
pg.init()
pg.font.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hangman")
title_font = pg.font.Font(None, 80)
input_font = pg.font.Font(None, 50)
game_title = title_font.render("HANGMAN", True, BLACK)
clock = pg.time.Clock()
word_list = ["incredible","university",'abbreviate','digest','radius','fortnite']
alpha_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Initialize images
hangman_images = [
    "hangman0.png",
    "hangman1.png",
    "hangman2.png",
    "hangman3.png",
    "hangman4.png",
    "hangman5.png",
    "hangman6.png"
    ]
hangman_list = []
for img in hangman_images:
    hangman_list.append(pg.image.load(img))

# Game variables
guesses_remaining = 7
dead = False
letters_guessed = ["","","","","","","","","","","","","","","","","","","","","","","","","",""]
selected_word = random.choice(word_list)
current_progress = "-" * len(selected_word)
current_progress = "DEVE-OPERS"
#current_progress = "----------"
print(selected_word)
print(current_progress)

guessed = False

while not guessed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            guessed = True
    screen.fill(WHITE)
    screen.blit(game_title, (260, 30))
    screen.blit(hangman_list[7-guesses_remaining], (80, 150))
    show_word_status()
    show_alpha_remaining()
    get_guess()
    pg.display.update()

pg.quit()
