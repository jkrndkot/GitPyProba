print("Hello, World!")

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
window_size = (512, 512)
screen = pygame.display.set_mode(window_size)

# Заголовок окна
pygame.display.set_caption('Мой корги!')

# Загрузка изображения
image = pygame.image.load('logo.png')

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона белым цветом
    screen.fill((255, 255, 255))
    
    # Отображение картинки в центре окна
    rect = image.get_rect(center=(window_size[0]//2, window_size[1]//2))
    screen.blit(image, rect)
    
    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()
sys.exit()
