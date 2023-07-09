import pygame as pg
import random
from settings import *

def show_word_status():
    screen_pos = 300
    position = input_font.render("---", True, BLACK)
    for _ in range(len(selected_word)):
        screen.blit(position, (screen_pos, 260))
        screen_pos += 48


def show_alpha_remaining():
    for row in range(2):
        x_pos = 62
        for column in range(13):
            if letters_guessed[row * 13 + column] == " ":
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
word_list = ["incredible","constitution",'abbreviate']
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
selected_word = random.choice(word_list)
letters_guessed = ["a","b", "c","d"," ", "f"," "," ", "i", " "," ", "l", "m", " "," ", "p", " ", " ", "s", "t", " ", " ", "w", " ", " "," "]

print(selected_word)

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
