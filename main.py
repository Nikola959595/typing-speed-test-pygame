import pygame
import sys
import random
from words import words

words_list = random.sample(words, 150)
words_to_type = " ".join(words_list)
letters_to_type = list(words_to_type)
print(letters_to_type)
typed_letters = []

pygame.init()
screen = pygame.display.set_mode((900, 500))
text_font = pygame.font.SysFont("Arial", 50)
pygame.display.set_caption("Typing Speed Test")
bg = pygame.image.load('background.png')
clock = pygame.time.Clock()
running = True

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    return img.get_width()
    

start_text_display = True

letter_pos_x = 350
letter_pos_y = 250
letter_color = (0, 0, 0)
letter_color_correct = (0, 255, 0)
letter_color_incorrect = (255, 0, 0)



while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    screen.blit(bg, (0,0))
    if start_text_display:
        start_text = draw_text("Press any key to start!", text_font, letter_color, 225,0)
    else:
        current_x = letter_pos_x
        for i, letter in enumerate(letters_to_type):
            if i < len(typed_letters):
                if typed_letters[i] == letter:
                    color = letter_color_correct
                else:
                    color = letter_color_incorrect
            else:
                color = letter_color
            letter_width = draw_text(letter, text_font, color, current_x, letter_pos_y)
            current_x += letter_width
          
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if start_text_display:
                start_text_display = False
            else:
                if event.key == pygame.K_BACKSPACE:
                    if typed_letters:
                        last_letter_width = draw_text(typed_letters.pop(), text_font, letter_color, 0, 0)
                        letter_pos_x += last_letter_width
                elif len(typed_letters) < len(letters_to_type):
                    typed_letter = event.unicode
                    typed_letters.append(typed_letter)
                    last_letter_width = draw_text(typed_letter, text_font, letter_color, 0, 0)
                    letter_pos_x -= last_letter_width           
    
    pygame.display.update()        

       
