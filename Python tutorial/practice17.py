from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} unit was produced".format(name))

    def move(self, location):
        print("{0} : move towards {1} at speed {2}".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : damaged {1}".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : unit was extinguished".format(self.name))

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : attack towards {1} for damage {2}".format(self.name, location, self.damage))
    
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"marine",40,1,5)

    def stimpack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : using stimpack(hp -10)".format(self.name))
        else: 
            print("{0} : can't use stimpack (lack of hp)".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"tank",150,1,35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print("{0} : set to the seize mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else:
            print("{0} : reset to the normal mode".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : fly towards to {1} at speed {2}".format(name,location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self,location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"wraith",80,20,5)
        self.clocked = False 
    
    def set_clocking(self):
        if self.clocked == True:
            print("{0} : clocking mode reset".format(self.name))
            self.clocked == False
        else:
            print("{0} : clocking mode set".format(self.name))
            self.clocked == True

def game_start():
    print("new game is started")

def game_over():
    print("player : gg")
    print("player left game")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move(1)

Tank.seize_developed = True
print("tank seize mode was developed")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.set_clocking() 

for unit in attack_units:
    unit.attack(1)

for unit in attack_units:
    unit.damaged(randint(5,21)) 

game_over()