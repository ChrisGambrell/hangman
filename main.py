import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game!')

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images
images = []
for i in range(0, 7):
    image = pygame.image.load('images/hangman' + str(i) + '.png')
    images.append(image)


def get_words():
    words = []
    f = open('words.txt', 'r')

    print('[ INFO ] Fetching word bank...')
    for line in f:
        words.append(line[0:len(line) - 1])

    print('[ SUCCESS ] Got word bank')

    return words


# game variables
hangman_status = 0
# word has to be <= 22 chars
words = get_words()
word = random.choice(words)
guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# setup game loop
FPS = 60
clock = pygame.time.Clock()


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render('DEVELOPER HANGMAN', 1, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

    # draw word
    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '

    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (30, 325))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() //
                            2, y - text.get_height() // 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)

    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() //
                    2, HEIGHT // 2 - text.get_height() // 2))

    text = WORD_FONT.render('Your word was... ' + word, 1, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() //
                    2, HEIGHT // 2 - text.get_height() // 2 + 50))

    pygame.display.update()
    pygame.time.delay(3000)


def start():
    global hangman_status
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message('You WON!')
            break

        if hangman_status == 6:
            display_message('You lost :(')
            break

    pygame.quit()


start()
