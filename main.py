import pygame as pg
import random
from settings import *

def show_word_status():
    screen_pos = 300
    found = 0
    for ix, val in enumerate(selected_word):
        alpha_pos = alpha_list.find(val.upper())
        if letters_guessed[alpha_pos] == False:
            pg.draw.line(screen, BLACK, (screen_pos + ix * 2, 280), (screen_pos + 24 + ix * 2, 280), 4)
        else:
            ltr = input_font.render(val.upper(), True, BLACK)
            screen.blit(ltr, (screen_pos + ix, 254))
            found += 1
        screen_pos += 36
    return found

def show_word():
    global letters_guessed
    letters_guessed = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    show_word_status()
def show_alpha_remaining():
    for row in range(2):
        x_pos = 62
        for column in range(13):
            if letters_guessed[row * 13 + column] == False:
                pg.draw.circle(screen, BLACK, (x_pos, 450 + (row * 60)), 23, 4)
                letter = input_font.render(alpha_list[row * 13 + column], True, BLACK)
                screen.blit(letter, (x_pos - 12, 434 + row * 60))
            x_pos += 56

def get_guess():
    global guesses_remaining, letters_guessed
    guess = row = col = -1
    if pg.mouse.get_pressed()[0]:
        pos_x, pos_y = pg.mouse.get_pos()
        if pos_y >= 427 and pos_y <= 473: row = 0
        elif pos_y >= 487 and pos_y <= 533: row = 1
        if pos_x >= 62 and pos_x <= 778: col = (pos_x - 56) // 56
        guess = alpha_list[row * 13 + col]
        if letters_guessed[row * 13 + col] == False:
            letters_guessed[row * 13 + col] = True
            if guess.lower() not in selected_word:
                guesses_remaining -= 1
    return guess

# Initialization variables
pg.init()
pg.font.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hangman")
title_font = pg.font.Font(None, 80)
input_font = pg.font.Font(None, 50)
game_title = title_font.render("HANGMAN", True, BLACK)
clock = pg.time.Clock()
word_list = ["incredible","university",'abbreviate','digest','radius','fortnite', 'constitution','express','soluble']
alpha_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Initialize images
hangman_list = []
for img in range(7):
    hangman_list.append(pg.image.load("hangman" + str(img) + ".png"))

# Game variables
guesses_remaining = 7
dead = False
letters_guessed = [False, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False,False, False,]
selected_word = random.choice(word_list)

guessed = False

while not guessed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            guessed = True
    screen.fill(WHITE)
    screen.blit(game_title, (260, 30))
    screen.blit(hangman_list[7-guesses_remaining], (80, 150))
    if show_word_status() == len(selected_word):
        win = input_font.render("YOU WIN!", False, (255, 0, 0))
        screen.blit(win, (330, 90))
    show_alpha_remaining()
    key = get_guess()
    if guesses_remaining == 0:
        show_word()
    pg.display.update()
    clock.tick(FPS)

pg.quit()