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
    letters_guessed = [True] * 26
    show_word_status()
def show_alpha_remaining():
    for row in range(2):
        x_pos = 62
        for column in range(13):
            if letters_guessed[row * 13 + column] == False:
                pg.draw.circle(screen, BLACK, (x_pos, 450 + (row * 60)), 23, 4)
                letter = input_font.render(alpha_list[row * 13 + column], True, BLACK)
                screen.blit(letter, (x_pos - letter.get_width() /2, 450 + row * 60 - letter.get_height() / 2))
            x_pos += 56

def get_guess():
    global guesses, letters_guessed
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
                guesses += 1
    return guess

def show_game_result(message):
    text = input_font.render(message, True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 90))
    pg.display.update()
    delay(2000)

def delay(pause):
    pg.time.delay(pause)

# Initialization variables
pg.init()
pg.font.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hangman")
title_font = pg.font.Font(None, 80)
input_font = pg.font.Font(None, 50)
game_title = title_font.render("HANGMAN", True, BLACK)
clock = pg.time.Clock()

words = open("wordlist.txt", "r")
word_list = words.read().splitlines()
words.close()
print(word_list)
alpha_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Initialize images
hangman_list = []
for img in range(7):
    hangman_list.append(pg.image.load("hangman" + str(img) + ".png"))

def main():
    global selected_word, letters_guessed, guesses
    # Game variables
    guessed = False
    guesses = 0
    letters_guessed = [False] * 26
    selected_word = random.choice(word_list)
    while not guessed:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                guessed = True
        screen.fill(WHITE)
        screen.blit(game_title, (WIDTH/2-game_title.get_width()/2, 30))
        screen.blit(hangman_list[guesses], (80, 150))
        if show_word_status() == len(selected_word):
            show_game_result("YOU WIN!!")
            guessed = True
        if guesses == 6:
            show_game_result(f"YOU LOSE -- The word was {selected_word}")
            guessed = True
        show_alpha_remaining()
        key = get_guess()
        pg.display.update()
        clock.tick(FPS)

first_entry = play_again = True
while play_again:
    if first_entry:
        first_entry = False
        main()
    screen.fill(WHITE)
    playAgain_text = input_font.render("Play again? (Y/N)", True, BLACK)
    screen.blit(playAgain_text, (WIDTH/2 - playAgain_text.get_width()/2, 90))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_y:
                play_again = True
                main()
            if event.key == pg.K_n:
                play_again = False

pg.quit()