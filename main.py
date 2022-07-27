import pygame
import random

#setup display
pygame.init()
WIDTH,HEIGHT = 500,400
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman")

#button variables
RADIUS = 12
GAP = 8
letters = []
startx = round((WIDTH-(RADIUS*2 + GAP) * 13) / 2)
starty = 250
A = 65

for i in range(26):
  x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i%13)
  y = starty + ((i//13) * (GAP + RADIUS * 2))
  letters.append([x,y, chr(A+i)])


#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 15)
LETTER_FONT_2 = pygame.font.SysFont('comicsans', 30)


#images
images = []
for i in range(7):
  image = pygame.image.load(f"hangman{i}.png")
  images.append(image)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

#game variables
hangman_status = 0

words = ["GALAXY", "PNEUMONIA", "WATERMELON", "DALMATION", "PENGUIN", "ELEPHANT", "XYLOPHONE", "JIGSAW", "ABRUPTLY", "NIGHTCLUB", "WRISTWATCH", "STRENGTHS"]
global word
word = words[random.randrange(len(words))]


#setup game
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
  win.fill(WHITE)

  # draw buttons
  for letter in letters:
    x,y,ltr= letter
    pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
    text = LETTER_FONT.render(ltr, True, BLACK)
    win.blit(text, (x-text.get_width()/2, y-text.get_width()/2))
  win.blit(images[hangman_status], (10,10))



global lines
lines = []
x = 230
y = 150
for i in range(len(word)):  
  lines.append([x,y, "_"])
  x+=25
  

  
def draw_line():
  for x,y,z in lines:
    text = LETTER_FONT_2.render(z, True, BLACK)
    win.blit(text,(x,y))

#game functions
def pick_letter(coord):
  x,y = coord
  for letter in letters:
    if x in range(letter[0]-RADIUS, letter[0]+RADIUS) and y in range(letter[1]-RADIUS, letter[1]+RADIUS):
      global guess
      guess = letter[2]
      letters.remove(letter)
      draw()
      break
    else:
      guess = str()
      draw()

  return guess

def add_to_word():
  if guess in word:
    for i in range(len(word)):
      if guess == word[i]:
        lines[i][-1] = guess
        draw_line()

  else:
    if ord(guess) in range(65,91):
      global hangman_status
      hangman_status += 1

def check_end():
  total = str()
  for x,y,z in lines:
    total += z
  while total == word:
    win.fill(GREEN)
    text = LETTER_FONT_2.render("Congratulations, you won!", True, BLACK)
    win.blit(text,(150,150))
    pygame.display.update()
    
    
  while hangman_status == 6:
    win.fill(RED)
    text = LETTER_FONT_2.render(f"Sorry, you lost! The word was {word}", True, BLACK)
    win.blit(text,(30,150))
    pygame.display.update()
    
#game loop
  
while run:
  clock.tick(FPS)

  draw()

  draw_line()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      pick_letter(pos)
      add_to_word()
      check_end()

  pygame.display.update()

pygame.quit()




  


  

