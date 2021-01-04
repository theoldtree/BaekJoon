class Unit:
    def __init__(self):
        print("Unit Constructor")

class Flyable:
    def __init__(self):
        print("Flyable Constructor")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() => 다중 상속시 먼저 상속된 클래스 만 생성자가 실행됨
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()