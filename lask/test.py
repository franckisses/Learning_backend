class Granade:
    def __init__(self, atk):
        self.atk = atk

    def explode(self, damage_target):
        # 如果传入的不是子类，则报错.
        if not isinstance(damage_target, Damageable):
            raise ValueError("不是Damageable的子类")

        print("爆炸")
        # 多态:
        # 调用父类代表(玩家/敌人.....)的可以受伤者.
        # 执类行子(具体玩家/敌人.....)
        damage_target.damage(self.atk)


class Damageable:
    """
        可以受伤
        继承:统一多个子类的概念，隔离变化。
    """

    def damage(self, value):
        # 如果子类不重写，则异常。
        raise NotImplementedError()


# ------------------------------
class Player(Damageable):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("玩家受伤啦")
        print("碎屏")


class Enemy(Damageable):
    def __init__(self, hp):
        self.hp = hp

    def damage2(self, value):
        self.hp -= value
        print("敌人受伤喽")
        print("头顶爆字")


g01 = Granade(100)
e01 = Enemy(200)
p01 = Player(300)
g01.explode(e01)