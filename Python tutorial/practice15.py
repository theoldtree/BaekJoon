### 클래스
class Unit:
    def __init__(self,name,hp,damage):
        self.name = name # self 는 멤버 변수를 정의하는 것임
        self.hp = hp
        self.damage = damage
        print("{0} unit was produced".format(name))
        print("hp : {0}, damage : {1}".format(hp, damage))
        print()

marine1 = Unit("marine",40,5)
tank = Unit("tank",150,35)

marine2 = Unit("upgrade marine",40,5)
marine2.steampack = True # 파이썬은 외부에서 클래스 내부의 멤버 변수를 만드는 것을 허용함
if marine2.steampack == True:
    print("steampack is ready")
print()


class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location):
        print("{0}: attack at {1} for damage {2}".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0}: {1} damgaed".format(self.name,damage))
        self.hp -= damage
        print("{0}: remaing hp is {1}".format(self.name,self.hp))
        if self.hp <= 0:
            print("unit was dead")
            print()

class FlyableUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0}: fly towards at {1} speed {2}".format(name, location, self.flying_speed))

class ColckingAttackUnit(AttackUnit): # 상속
    def __init__(self, name, hp, damage, clocking):
        AttackUnit.__init__(self,name,hp,damage)
        print("{0} unit was produced".format(name))
        print("hp : {0}, damage : {1}".format(hp, damage))
        self.clocking = clocking
        if clocking == True:
            print("clocking is ready")

class FlyableAttackUnit(FlyableUnit, AttackUnit): # 다중상속
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        FlyableUnit.__init__(self,flying_speed)
    
    def attack(self, location, direction): # 메소드 오버로딩
        self.fly(self.name,location) # 상속받은 메소드를 이용할 수 있다.
        print("{0}".format(direction))

def game_start():
    print("game start")

def game_over():
    pass # pass 키워드는 아무것도 안하고 넘어감

game_start()
firebat1 = AttackUnit("firebat",40,16)
firebat1.attack("5")
firebat1.damaged(25)
firebat1.damaged(25)
wraith = ColckingAttackUnit("wraith",150,8,True)
valkyrie = FlyableAttackUnit("valkyrie",200,6,5)
valkyrie.fly(valkyrie.name,3)
valkyrie.attack(6,"sky")
game_over()