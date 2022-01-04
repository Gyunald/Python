class Parent :
    def can_sing(self) :
        print("Sing a song~!")
father = Parent()
print(father.can_sing())

class LuckyChild(Parent) :
    pass
child = LuckyChild()
print(child.can_sing())

class LuckyChild2(Parent) :
    def can_dance(self) :
        print("Shuffle Dance")
child2 = LuckyChild2()
print(child2.can_sing())
print(child2.can_dance())