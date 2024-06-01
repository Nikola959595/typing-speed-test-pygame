import pygame
import sys
import random
from words import words


# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Typing Speed Test")
clock = pygame.time.Clock()

# Fonts and colors
text_font = pygame.font.SysFont("Arial", 50)
letter_color = (0, 0, 0)
letter_color_correct = (0, 255, 0)
letter_color_incorrect = (255, 0, 0)

# Load background image
try:
    bg = pygame.image.load('background.png')
except pygame.error as e:
    print(f"Unable to load background image: {e}")
    sys.exit()

# Words setup
def get_letters():
    words_list = random.sample(words, 150)
    words_to_type = " ".join(words_list).lower()
    letters_to_type = list(words_to_type)
    return letters_to_type

letters = get_letters()
typed_letters = []

# Initial variables
letter_pos_x = 350
letter_pos_y = 250
start_text_display = True
counter, timer_text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Function to draw text on the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    return img.get_width()

#Performance tracking variables
correct_chars = 0
total_chars = 0
wpm = 0
accuracy = 0

waiting = False
wait_timer = 3

while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))

    if start_text_display:
        draw_text("Press any key to start!", text_font, letter_color, 225, 0)
        if wpm > 0:
            draw_text(f"WPM: {wpm:.2f}", text_font, letter_color, 50, 400)
        if accuracy > 0:   
            draw_text(f"Accuracy: {accuracy:.2f}%", text_font, letter_color, 450, 400)
    else:
        current_x = letter_pos_x
        correct_chars = 0
        total_chars = len(typed_letters)
        for i, letter in enumerate(letters):
            if i < len(typed_letters):
                if typed_letters[i] == letter:
                    color = letter_color_correct
                    correct_chars += 1
                else:
                    color = letter_color_incorrect
            else:
                color = letter_color
            letter_width = draw_text(letter, text_font, color, current_x, letter_pos_y)
            current_x += letter_width

        elapsed_time = 60 - counter
        if elapsed_time > 0:
            wpm = (correct_chars / 5) * (60 / (60 - counter))
        else:
            wpm = 0

        accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0

        draw_text(f"WPM: {wpm:.2f}", text_font, letter_color, 50, 400)
        draw_text(f"Accuracy: {accuracy:.2f}%", text_font, letter_color, 450, 400)
        draw_text(timer_text, text_font, letter_color, 400, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if start_text_display:
                start_text_display = False
                typed_letters = []
                letters = get_letters()
                letter_pos_x = 350
                correct_chars = 0
                total_chars = 0
            else:
                if event.key == pygame.K_BACKSPACE:
                    if typed_letters:
                        typed_letters.pop()
                        letter_pos_x += 18
                elif counter > 0:
                    typed_letters.append(event.unicode)
                    letter_pos_x -= 18
        if event.type == pygame.USEREVENT:
            if not waiting:
                counter -= 1
                timer_text = str(counter).rjust(3) if counter > 0 else "Time's up!"
                if counter <= 0:
                    waiting = True
            else:
                wait_timer -= 1
                if wait_timer <= 0:
                    start_text_display = True
                    waiting = False
                    counter = 60
                    wait_timer = 3 
                
    pygame.display.update()   

       
