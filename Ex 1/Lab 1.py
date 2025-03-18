class Hero:
    def __init__(self, name, health, attack):
        # ініціалізація героя
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        #герой отримує шкоду
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} загинув!")
        else:
            print(f"{self.name} отримав {damage} шкоди. Залишилось {self.health} HP.")

    def attack_enemy(self, enemy):
        #герой атакує ворога
        print(f"{self.name} атакує {enemy.name} на {self.attack} шкоди!")
        enemy.take_damage(self.attack)


class Enemy:
    def __init__(self, name, health, attack):
        #ініціалізація ворога
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        #ворог отримує шкоду
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} загинув!")
        else:
            print(f"{self.name} отримав {damage} шкоди. Залишилось {self.health} HP.")

    def attack_hero(self, hero):
        #ворог атакує героя
        print(f"{self.name} атакує {hero.name} на {self.attack} шкоди!")
        hero.take_damage(self.attack)


# характеристики героя і ворога
hero = Hero("Лицар", 100, 20)
enemy = Enemy("Ворог", 80, 15)

# вивід
print(f"{hero.name} - HP: {hero.health}, Атака: {hero.attack}")
print(f"{enemy.name} - HP: {enemy.health}, Атака: {enemy.attack}")

# бій
hero.attack_enemy(enemy)  # Лицар атакує Ворога
enemy.attack_hero(hero)   # Ворог атакує Лицаря
