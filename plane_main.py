from 飞机大战.plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化！")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法完成精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置定时器事件创建实践1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(PLANE_FIRE_EVENT, 500)

    def start_game(self):
        print("游戏开始！")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 添加敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建飞机的精灵和精灵组
        self.plane = Plane()
        self.plane_group = pygame.sprite.Group(self.plane)

    def __event_handler(self):
        # 判断是否退出游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == PLANE_FIRE_EVENT:
                self.plane.fire()

        # 使用pygame.key.get_pressed()返回所有按键元组
        # 通过键盘常量，判断元组中某一个键是否被按下 如果被按下，对应数值为1
        keys_pressed = pygame.key.get_pressed()
        # 判断是否按下了方向键
        if keys_pressed[pygame.K_RIGHT]:
            self.plane.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.plane.speed = -3
        elif keys_pressed[pygame.K_UP]:
            self.plane.speeds = -3
        elif keys_pressed[pygame.K_DOWN]:
            self.plane.speeds = 3
        else:
            self.plane.speed = 0
            self.plane.speeds = 0

    def __check_collide(self):
        # 1.子弹摧毁敌机 groupcollide()两个精灵组所有精灵组的碰撞
        pygame.sprite.groupcollide(self.plane.bullets, self.enemy_group, True, True)

        # 2. 飞机碰到敌机
        enemies = pygame.sprite.groupcollide(self.plane_group, self.enemy_group, True, True)
        if len(enemies) > 0:
            # 让英雄牺牲
            self.plane.kill()
            # 结束游戏
            PlaneGame.game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.plane_group.update()
        self.plane_group.draw(self.screen)

        self.plane.bullets.update()
        self.plane.bullets.draw(self.screen)

    @staticmethod
    def game_over():
        print("游戏结束！")
        pygame.quit()
        exit()


Play = PlaneGame()
Play.start_game()