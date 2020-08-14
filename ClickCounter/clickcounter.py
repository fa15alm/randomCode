import pygame
pygame.init()
win = pygame.display.set_mode((300, 250))
pygame.display.set_caption('Click Counter')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 32)
smallfont = pygame.font.Font('freesansbold.ttf', 15)
clickCount = 0
def reloadWindow(win):
    win.fill(BLACK)
    countText = font.render(f'Clicks: {clickCount}', 1, WHITE, True)
    win.blit(countText, (80, 100))
    resetText = smallfont.render('Press space to reset counter.', 1, WHITE)
    win.blit(resetText, (50, 150))
    pygame.display.update()
run = True
while run:
    reloadWindow(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickCount += 1
            reloadWindow(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            clickCount = 0
pygame.quit()
