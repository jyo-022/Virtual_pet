import time  # Import the time module to use for simulating time passing
import random  # Import the random module (not used in this version, but can be useful for future features)

class VirtualPet:
    def __init__(self, name):
        # Constructor to initialize the pet's name, happiness, and hunger levels
        self.name = name  # Set the pet's name
        self.happiness = 50  # Initialize happiness level to 50
        self.hunger = 50  # Initialize hunger level to 50

    def feed(self):
        # Method to feed the pet
        if self.hunger > 0:  # Check if the pet is hungry
            self.hunger -= 10  # Decrease hunger by 10
            self.happiness -= 5  # Decrease happiness by 5
            # Print the updated status after feeding
            print(f"You fed {self.name}. Hunger is now {self.hunger}. Happiness is now {self.happiness}.")
        else:
            # If the pet is not hungry, inform the user
            print(f"{self.name} is not hungry!")

    def play(self):
        # Method to play with the pet
        if self.happiness < 100:  # Check if the pet's happiness is less than 100
            self.happiness += 10  # Increase happiness by 10
            self.hunger += 5  # Increase hunger by 5
            # Print the updated status after playing
            print(f"You played with {self.name}. Happiness is now {self.happiness}. Hunger is now {self.hunger}.")
        else:
            # If the pet is already very happy, inform the user
            print(f"{self.name} is already very happy!")

    def check_status(self):
        # Method to check and display the pet's current status
        print(f"{self.name}'s Happiness: {self.happiness}, Hunger: {self.hunger}")

    def automatic_changes(self):
        # Method to simulate automatic changes over time
        self.hunger += 5  # Increase hunger by 5
        self.happiness -= 2  # Decrease happiness by 2
        # Ensure hunger does not exceed 100
        if self.hunger > 100:
            self.hunger = 100
        # Ensure happiness does not drop below 0
        if self.happiness < 0:
            self.happiness = 0

def main():
    # Main function to run the pet simulator
    name = input("What would you like to name your pet? ")  # Prompt user for pet's name
    pet = VirtualPet(name)  # Create a new VirtualPet instance with the given name

    while True:  # Start an infinite loop for the game
        pet.automatic_changes()  # Apply automatic changes to the pet's status
        pet.check_status()  # Display the current status of the pet

        # Check for game over conditions
        if pet.hunger >= 100:
            print(f"{pet.name} has become too hungry! Game Over.")  # Inform user of game over due to hunger
            break  # Exit the loop
        if pet.happiness <= 0:
            print(f"{pet.name} has become too sad! Game Over.")  # Inform user of game over due to sadness
            break  # Exit the loop

        # Display the menu options to the user
        print("\nMenu:")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Check pet's status")
        print("4. Quit")
        choice = input("Choose an action (1-4): ")  # Prompt user for their choice

        # Execute the corresponding action based on user choice
        if choice == '1':
            pet.feed()  # Call the feed method
        elif choice == '2':
            pet.play()  # Call the play method
        elif choice == '3':
            pet.check_status()  # Call the check_status method
        elif choice == '4':
            print("Thanks for playing!")  # Thank the user for playing
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

        time.sleep(1)  # Pause for 1 second to simulate time passing

if __name__ == "__main__":
    main()  # Call the main function to start the game






