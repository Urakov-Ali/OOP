class Wizzard:
    def __init__(self, name, power):
        self. name = name
        self.power = power
     
    def attack(self):
        print(f'Wizzard {self.name} attacks with power of {self.power}')

class Archer:
    def __init__(self, name, arrow):
        self. name = name
        self.arrow = arrow
    
    def shot(self):
        print(f'Archer {self.name} shots, he left {self.arrow}')

class Hybrid(Wizzard, Archer):
    def __init__(self, name, power, arrow):
        Wizzard.__init__(self, name, power)
        Archer.__init__(self, name, arrow)

hyb1 = Hybrid('ROG', 100, 50)

print(hyb1.attack())
