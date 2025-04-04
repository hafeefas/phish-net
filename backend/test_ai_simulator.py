# Import the AI simulator class and random module for scenario selection
from app.ai_simulator import AIPhoneCallSimulator
import random

def main():
    """Main function to run the AI Phone Call Scam Simulator"""
    # Create an instance of the simulator
    simulator = AIPhoneCallSimulator()
    
    # Display welcome message and instructions
    print("Welcome to the AI-Powered Phone Call Scam Simulator!")
    print("This tool helps seniors learn about common phone scams using AI.")
    print("\nAvailable scenarios:")
    
    # Get and display all available scam personas
    personas = simulator.get_personas()
    for i, persona in enumerate(personas):
        print(f"{i + 1}. {persona.replace('_', ' ').title()}")
    
    # Main program loop
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Run a random scenario")
        print("2. Choose a specific scenario")
        print("3. Exit")
        
        # Get user's choice
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            # Run a random scenario
            persona = random.choice(personas)
            simulator.simulate_call(persona)
        elif choice == "2":
            # Let user choose a specific scenario
            persona_num = int(input("Enter scenario number (1-3): ")) - 1
            if 0 <= persona_num < len(personas):
                simulator.simulate_call(personas[persona_num])
            else:
                print("Invalid scenario number!")
        elif choice == "3":
            # Exit the program
            print("Thank you for using the AI Phone Call Scam Simulator!")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")

# Run the main function if this script is run directly
if __name__ == "__main__":
    main() 