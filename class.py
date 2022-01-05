# 일반 유닛
class Unit :
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location) :
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")
# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed) # self.name = name (상속)
         # self.hp = hp (상속)
        self.damage = damage

    def attack(self, location) :
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage) :
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다")
        if self.hp <= 0 :
            print(f"{self.name} : 파괴되었습니다.")

# 날 수 있는 기능을 가진 클래스        
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
    def fly(self, name, location) :
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable) :
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)
    def move(self, location) :
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)
# # 레이스 : 공중 유닛, 비행기, 클로킹(투명)
# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (뺏기)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True :
#     print(f"{wraith2.name} 는 현재 클로킹 상태입니다.")

# 벌쳐 : 지상 유닛, 기동성 좋음
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# 배틀크루저 : 공중 공격 유닛
# 드랍쉽 : 공중 유닛, 수송기. 공격 기능 없음
# 메딕 : 의무병 
# 파이어뱃 : 공격 유닛, 화염방사기
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) 
valkyrie.fly(valkyrie.name, "3시")
firebat1 = AttackUnit("파이어뱃", 50, 2, 16)
firebat1.attack("5시")
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

