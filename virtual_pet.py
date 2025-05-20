import time
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness -= 5
            print(f"You fed {self.name}. Hunger is now {self.hunger}. Happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.hunger += 5
            print(f"You played with {self.name}. Happiness is now {self.happiness}. Hunger is now {self.hunger}.")
        else:
            print(f"{self.name} is already very happy!")

    def check_status(self):
        print(f"{self.name}'s Happiness: {self.happiness}, Hunger: {self.hunger}")

    def automatic_changes(self):
        self.hunger += 5
        self.happiness -= 2
        if self.hunger > 100:
            self.hunger = 100
        if self.happiness < 0:
            self.happiness = 0

def main():
    name = input("What would you like to name your pet? ")
    pet = VirtualPet(name)

    while True:
        pet.automatic_changes()
        pet.check_status()

        if pet.hunger >= 100:
            print(f"{pet.name} has become too hungry! Game Over.")
            break
        if pet.happiness <= 0:
            print(f"{pet.name} has become too sad! Game Over.")
            break

        print("\nMenu:")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Check pet's status")
        print("4. Quit")
        choice = input("Choose an action (1-4): ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.check_status()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(1)  # Simulate time passing

if __name__ == "__main__":
    main()
