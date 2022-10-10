from random import *

class Unit: #부모
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛이 생성되었습니다.")

    def move(self, location):
        print("지상 유닛 이동")
        print(f"{self.name} : {location} 방향으로 이동. 속도 {self.speed}")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다")
        self.hp -= damage
        if self.hp > 0 :
            print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        else:
            print(f"{self.name} : 파괴되었습니다.")


# marine1 = Unit("마린", 50, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print(f"{wraith2.name}는 클로킹 상태입니다.")

class AttackUnit(Unit): #자식
    def __init__(self, name, hp, speed, dagame):
        Unit.__init__(self, name, hp, speed)
        # self.name = name
        # self.hp = hp
        # self.speed = speed
        self.damage = dagame
     
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 공격. 공격력 {self.damage}")

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 이동. 속도 : {self.flying_speed}")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp >10 :
            self.hp -= 10
            print(f"{self.name} 스팀팩 사용 (hp 10 감소)")
        else:
            print(f"{self.name} 체력부족. 스팀팩 사용 불가.")

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False :
            print(f"{self.name} 시즈모드 전환.")
            self.damage *= 2
            self.set_seize_mode = True
        else:
            print(f"{self.name} 시즈모드 해제.")
            self.damage /= 2
            self.set_seize_mode = False
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True :
            print(f"{self.name} : 클로킹 모드 해제")
            self.clocked  = False
        else:
            print(f"{self.name} : 클로킹 모드 실행")
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_end():
    print("Player : gg")
    print("[Player] 퇴장.")

# firebat = AttackUnit("파이어뱃", 50, 16, 5)
# firebat.attack("5시")

# firebat.damaged(25)
# firebat.damaged(25)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "5시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         Unit.__init__(self, name, hp, 0)
#         # super().__init__(name, hp) # self 안씀. 다중 상속 시 맨앞 클래스만 호출.
#         self.location = location

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


game_start()

m1 = Marine()
t1 = Tank()
w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(t1)
attack_units.append(w1)

for unit in attack_units :
    unit.move("11시")
    
Tank.seize_developed = True
print("[알림] 시즈모드 개발 완료.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:    
    unit.damaged(randint(5,200))

game_end()