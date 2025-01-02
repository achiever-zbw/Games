import pygame
import random

# 初始化 Pygame
pygame.init()

# 屏幕大小
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("吃星星游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 玩家属性
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# 星星属性
star_size = 30
star_x = random.randint(0, SCREEN_WIDTH - star_size)
star_y = random.randint(0, SCREEN_HEIGHT - star_size)

# 分数
score = 0
font = pygame.font.Font(None, 36)

# 游戏主循环标志
running = True
clock = pygame.time.Clock()

while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
        player_y += player_speed

    # 检测碰撞
    if (player_x < star_x + star_size and
        player_x + player_size > star_x and
        player_y < star_y + star_size and
        player_y + player_size > star_y):
        score += 1
        star_x = random.randint(0, SCREEN_WIDTH - star_size)
        star_y = random.randint(0, SCREEN_HEIGHT - star_size)

    # 绘制游戏元素
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))  # 玩家
    pygame.draw.rect(screen, YELLOW, (star_x, star_y, star_size, star_size))  # 星星

    # 显示分数
    score_text = font.render(f"分数: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 更新屏幕
    pygame.display.flip()
    clock.tick(100)  # 控制帧率

# 退出游戏
pygame.quit()
