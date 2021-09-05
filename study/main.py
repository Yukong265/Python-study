class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def status(self):
        print("health : " + str(self.health))
        print("mana : " + str(self.mana))
        print("armor : " + str(self.armor))

    def slash(self):
        print("베기?")


x = Knight(health=542.4, mana=210.3, armor=38)
x.slash()
x.status()
# 여기 노래방 아닌데