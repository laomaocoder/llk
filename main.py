import pygame
import random

pygame.init()

# 游戏窗口大小
WINDOW_SIZE = (600, 600)

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# 图标和标题
#ICON_IMAGE = pygame.image.load('icon.png')
BACKGROUND_IMAGE = pygame.image.load('background.jpg')
#pygame.display.set_icon(ICON_IMAGE)
pygame.display.set_caption('连连看')

# 创建游戏窗口
screen = pygame.display.set_mode(WINDOW_SIZE)

# 加载图片素材
animal_images = []
for i in range(1, 9):
    animal_images.append(pygame.image.load(f'animal_{i}.png'))

# 网格大小为10x10
GRID_SIZE = 10
CELL_SIZE = 50

# 创建网格二维数组
grid = [[0 for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

# 随机生成格子上的动物
for i in range(1, 5):
    for j in range(1, 9):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        while grid[x][y] != 0:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
        grid[x][y] = i

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = int(pos[0] / CELL_SIZE)
            y = int(pos[1] / CELL_SIZE)
            print(f'Clicked on cell ({x}, {y})')
    # 绘制界面
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            animal_id = grid[x][y]
            if animal_id != 0:
                image = animal_images[animal_id - 1]
                screen.blit(image, (x * CELL_SIZE, y * CELL_SIZE))
    # 绘制网格线
    for i in range(GRID_SIZE):
        pygame.draw.line(screen, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, GRID_SIZE * CELL_SIZE))
        pygame.draw.line(screen, GRAY, (0, i * CELL_SIZE), (GRID_SIZE * CELL_SIZE, i * CELL_SIZE))
    # 刷新屏幕
    pygame.display.flip()

pygame.quit()
