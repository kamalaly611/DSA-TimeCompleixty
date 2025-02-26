
welcome_note="---Welcome To Kaun Banega Crorepati (KBC)---"
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

questions = [
    [
        "What is the capital of France?", 
        ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"]
    ],
    [
        "Which planet is known as the Red Planet?", 
        ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"]
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?", 
        ["A) William Shakespeare", "B) Charles Dickens", "C) Leo Tolstoy", "D) Mark Twain"]
    ],
    [
        "Which is the largest ocean in the world?", 
        ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"]
    ],
    [
        "What is the square root of 64?", 
        ["A) 6", "B) 7", "C) 8", "D) 9"]
    ],
    [
        "In which year did the Titanic sink?", 
        ["A) 1910", "B) 1912", "C) 1914", "D) 1916"]
    ],
    [
        "Which is the smallest continent by land area?", 
        ["A) Africa", "B) Australia", "C) Europe", "D) Antarctica"]
    ],
    [
        "Which gas do plants absorb from the atmosphere during photosynthesis?", 
        ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"]
    ]
]
score=0
for i in questions[0:8]:
    if i==questions[0]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="A":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break

        else:
            print("The Provided options is Wrong: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
    elif i==questions[1]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="B":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
    elif i==questions[2]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="C":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
    elif i==questions[3]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="D":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
    elif i==questions[4]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="A":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
    elif i==questions[5]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="C":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
    elif i==questions[6]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="A":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
    elif i==questions[7]:
        print(i)
        ask_user=input("which Option is correct: ")
        if ask_user=="D":
            score+=10
            print("The Provided options is correct: ")
            ask_user=input("Do You want to quit the game:")
            if ask_user=="No":
                print("Now move to Next Question: ")
            else:
                print(f"Thanks for Participating \n Your final score is: {score}")
                break
print(f"The Final Amount That You Won is: {score}")