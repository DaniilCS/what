import pygame

window = pygame.display.set_mode((570, 380))

pygame.display.set_caption("GLADIKO")

run = True
x, y = 50, 50 # текущие координаты танка, которые потом будут изменяться(коорд берется с правого верхнего угла)
width, height = 80, 100 #размеры танка(надо доработать)
speed = 15 # СПИД))))))))
tank_down = pygame.image.load('танчик_вниз.jpg') #картинка, где танк едет вниз(нужно создать остальные картинки и возм взять с инета другие танки(других цветов))
clock = pygame.time.Clock()
bg = pygame.image.load('default-1sjz.jpg')
def draw():
    window.blit(bg, (0,0)) #рисуем сначала заставку
    window.blit(tank_down, (x, y)) #затем танк с его текущими коордами
    pygame.display.update #очищаем окно
while run:
    
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.event.QUIT:# выход из прилож
            run = False

    keys = pygame.key.get_pressed()#берем массив с кнопками с клавы
    if keys[pygame.K_UP] or keys[pygame.K_w] and y >= 5:#если мы нажали W или прямо и также мы не пределами карты, то меняем коорд, то есть двигаемся
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and y <= 380:
        y += speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and x <= 570:
        x += speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and x > 0:
        x -= speed
    draw()
pygame.quit()
    