import random

# Function to randomly remove two options from the given list
def remove_two_options(options, correct_answer):
    # Create a list of incorrect options by excluding the correct answer
    incorrect_options = [option for option in options if not option.startswith(correct_answer)]
    
    # Randomly select 2 incorrect options to remove
    options_to_remove = random.sample(incorrect_options, 2)
    
    # Remove the selected options from the original list
    remaining_options = [option for option in options if option not in options_to_remove]
    
    return remaining_options

def ask_friend():
    pass

# Welcome message and rules
welcome_note = "Welcome To Kaun Banega Crorepati (KBC):"
print(welcome_note.center(55))
kbc_rules = [
    "The game consists of 5 questions.",
    "Each question has four multiple-choice options (A, B, C, D).",
    "The player inputs their answer by typing 'A', 'B', 'C', or 'D'.",
    "Each correct answer awards 10 points.",
    "No negative marking for incorrect answers.",
    "The player has two lifelines: 50-50 and Ask a Friend.",
    "50-50: Removes two incorrect options.",
    "Ask a Friend: The system suggests an answer (random and may not always be correct).",
    "Each lifeline can be used only once during the game.",
    "The player can use lifelines before answering any question.",
    "After each question, the player has the option to continue or quit.",
    "If the player chooses to quit, their current score is saved, and the game ends.",
    "The game ends when: the player answers all questions, decides to quit, or answers incorrectly and has no lifelines left.",
    "At the end of the game, the final score is displayed."
]
for rules in kbc_rules:
    print(rules)

# Questions with correct answers
questions = [
    [
        "What is the capital of France?", 
        ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "C"  # Correct answer
    ],
    [
        "Which planet is known as the Red Planet?", 
        ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "B"  # Correct answer
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?", 
        ["A) William Shakespeare", "B) Charles Dickens", "C) Leo Tolstoy", "D) Mark Twain"],
        "A"  # Correct answer
    ],
    [
        "Which is the largest ocean in the world?", 
        ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "D"  # Correct answer
    ],
    [
        "What is the square root of 64?", 
        ["A) 6", "B) 7", "C) 8", "D) 9"],
        "C"  # Correct answer
    ],
    [
        "In which year did the Titanic sink?", 
        ["A) 1910", "B) 1912", "C) 1914", "D) 1916"],
        "B"  # Correct answer
    ],
    [
        "Which is the smallest continent by land area?", 
        ["A) Africa", "B) Australia", "C) Europe", "D) Antarctica"],
        "B"  # Correct answer
    ],
    [
        "Which gas do plants absorb from the atmosphere during photosynthesis?", 
        ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
        "C"  # Correct answer
    ]
]

score = 0
lifeline_used = False  # Track if the 50-50 lifeline has been used

# Game loop
for i in questions:
    question, options, correct_answer = i  # Unpack the question, options, and correct answer
    
    print("\n", question)
    for option in options:
        print(option)

    # Check if player wants to use 50-50 lifeline
    if not lifeline_used:
        use_lifeline = input("Do you want to use the 50-50 lifeline? (Yes/No): ")
        if use_lifeline.lower() == "yes":
            # Call the function to remove two options
            options = remove_two_options(options, correct_answer)
            print("Options after 50-50 lifeline:")
            for option in options:
                print(option)
            lifeline_used = True  # Mark lifeline as used
    
    ask_user = input("Which Option is correct? (A, B, C, D): ")
    
    if ask_user == correct_answer:
        score += 10
        print("The Provided option is correct!")
    else:
        print("The Provided option is wrong!")
    
    # Ask if player wants to continue or quit
    ask_user = input("Do you want to quit the game? (Yes/No): ")
    if ask_user.lower() == "yes":
        print(f"Thanks for participating! Your final score is: {score}")
        break

print(f"Your final score is: {score}")





