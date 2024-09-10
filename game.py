import random
import os
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = 10
        self.heal_power = 15
        self.points = 0

    def attack(self, enemy):
        damage = random.randint(5, self.attack_power)
        enemy.hp -= damage
        os.system('cls')
        print(f"\nYou attacked {enemy.name} for {damage} damage!")

    def heal(self):
        heal_amount = random.randint(10, self.heal_power)
        self.hp += heal_amount
        self.hp = min(self.hp, 100)
        os.system('cls')
        print(f"\nYou healed yourself for {heal_amount} HP!")

    def add_points(self, amount):
        self.points += amount
        print(f"\nYou earned {amount} points! Total points: {self.points}")

    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"HP: {self.hp}")
        print(f"Points: {self.points}")

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, player):
        damage = random.randint(5, 12)
        player.hp -= damage
        os.system('cls')
        print(f"\n{self.name} attacked you for {damage} damage!")

def random_event(player):
    os.system('cls')
    print("You venture further into the cave...")
    time.sleep(1)
    event_type = random.choice(['enemy', 'treasure'])
    
    if event_type == 'enemy':
        creature_encounter(player)
    elif event_type == 'treasure':
        find_treasure(player)

def cave_exploration(player):
    while player.hp > 0:
        print("\nWhat will you do next?")
        choice = input("Choose an action: (1) Move forward, (2) Rest, (3) View Stats, (4) Exit the cave: ")

        if choice == '1':
            random_event(player)
        elif choice == '2':
            os.system('cls')
            print("\nYou take a brief rest and recover some health.")
            player.heal()
        elif choice == '3':
            os.system('cls')
            player.show_stats()
        elif choice == '4':
            print("\nYou decide to exit the cave and end your adventure.")
            break
        else:
            print("\nInvalid choice! Let's try that again.")
            time.sleep(1)
            os.system('cls')
    
    os.system('cls')
    print("\nYour adventure has ended.")
    print(f"Final Stats: {player.name} - HP: {player.hp}, Points: {player.points}")

def creature_encounter(player):
    print("\nA wild cave creature appears!")
    creature = Enemy("Cave Creature", 50)
    while creature.hp > 0 and player.hp > 0:
        print(f"\nYour HP: {player.hp} | Cave Creature HP: {creature.hp}")
        action = input("Choose an action: (1) Attack, (2) Heal: ")

        if action == '1':
            player.attack(creature)
        elif action == '2':
            player.heal()
        else:
            print("Invalid action!")
            continue

        if creature.hp > 0:
            creature.attack(player)
        time.sleep(1)
    
    if player.hp > 0:
        print("\nYou defeated the cave creature!")
        player.add_points(10)
        time.sleep(1)
        os.system('cls')
    else:
        print("\nThe cave creature defeated you...")
        time.sleep(1)

def find_treasure(player):
    treasure_points = random.randint(5, 20)
    print(f"\nYou found a hidden treasure chest! You gain {treasure_points} points.")
    player.add_points(treasure_points)
    time.sleep(1)
    os.system('cls')

def start_game():
    os.system('cls')
    print("Welcome to the Cave Exploration Adventure!")
    name = input("Enter your character's name: ")
    player = Player(name)
    
    os.system('cls')
    print(f"Welcome, {player.name}. Your adventure begins in the dark and mysterious cave.")
    time.sleep(2)
    os.system('cls')
    cave_exploration(player)

if __name__ == "__main__":
    start_game()
