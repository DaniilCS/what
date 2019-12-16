import pygame
pygame.init()

window = pygame.display.set_mode((1000, 487))
clock = pygame.time.Clock()
pygame.display.set_caption("MARIO")
mario_x, mario_y = 150, 350
mario = pygame.image.load('mario.png')
run = True
isJump = True
jumpCount = 10
speed = 10
dupe_x = 1000
dupe_y = 400
dupe_height = 150
def draw():
    window.fill((0, 191, 255))
    window.blit(mario, (mario_x, mario_y))
    if dupe_x > 0:
        pygame.draw.rect(window, (200,200,200), (dupe_x, dupe_y, dupe_x - 40, dupe_y - dupe_height))
        dupe_x -= speed
    else:
        dupe_x = 1280
        pygame.draw.rect(window, (200,200,200), (dupe_x, dupe_y, dupe_x - 40, dupe_y - dupe_height))
    pygame.display.update()

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                y -= (jump_count ** 2) / 3
            else:
                y += (jump_count ** 2) / 3
            jump_count -= 1
        else:
            isJump = False
            jump_count = 10
    draw()

pygame.quit()
    