import pygame
from 飞机大战.plane_sprites import *

# 初始化pygame方法
pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像数据
background = pygame.image.load("./images/background.png")
# 2.blit绘制图像
screen.blit(background, (0, 0))
# 3.update更新屏幕显示
# pygame.display.update()

# 绘制飞机图像
plane = pygame.image.load("./images/me1.png")
screen.blit(plane, (200, 500))

# 可以在所有绘制工作完成之后，统一调用update方法
# pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义飞机的初始位置
plane_rect = pygame.Rect(200, 500, 102, 126)

# 创建敌机的精灵
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy2.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)

# 创建一个游戏循环
while True:
    # 可以指定循环体内部代码的执行频率
    clock.tick(60)

    # 修改飞机的位置
    plane_rect.y -= 1

    # 如果移出屏幕，将飞机的顶部移动到屏幕的底部
    if plane_rect.y <= -126:
        plane_rect.y = 700

    # 调用blit方法绘制图像
    screen.blit(background, (0, 0))
    screen.blit(plane, plane_rect)

    # 让精灵组调用的两个方法
    # update 让组中所有精灵更新位置
    enemy_group.update()
    # draw 在screen上绘制所有精灵
    enemy_group.draw(screen)

    # 调用updata方法更新显示
    pygame.display.update()

    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            # quit卸载所有模块
            pygame.quit()
            # exit() 直接终止当前正在执行的程序
            exit()