import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹发射定时器常量
PLANE_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    # 在重写初始化方法时，一定要先super()一下父类的__init__方法
    # 保证父类中实现的__init__代码能够被正常执行
    def __init__(self, image_name, speed=1, speeds=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speeds = speeds

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")

        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的实现方法
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，并指定图像
        super().__init__("./images/enemy1.png")

        # 2.设置敌机的随机初始速度
        self.speed = random.randint(1, 3)

        # 3.设置敌机的随机初始位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，让敌机在垂直方向移动
        super().update()

        # 判断是否飞出屏幕，如果飞出删除精灵
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Plane(GameSprite):

    def __init__(self):
        # 1.调用父类方法设置图片
        super().__init__("./images/me1.png", 0)

        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speeds

        # 控制飞机左右移动不能移出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

        # 控制飞机上下移动不能移除屏幕
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):

        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()

            # 2.设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):

        # 调用父类方法，让子弹在垂直方向移动
        super().update()

        # 判断是否飞出屏幕，如果飞出删除精灵
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()