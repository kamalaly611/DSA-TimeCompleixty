import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For background image

# Function to determine the winner
def check(comp, user):
    if comp == user:
        return 0  # Draw
    if (comp == "Snake" and user == "Water") or \
       (comp == "Water" and user == "Gun") or \
       (comp == "Gun" and user == "Snake"):
        return -1  # User loses
    return 1  # User wins

# Function to play the game
def play_game(user_choice):
    global user_score, comp_score
    
    choices = ["Snake", "Water", "Gun"]
    comp_choice = random.choice(choices)
    
    result = check(comp_choice, user_choice)
    
    # Update scores
    if result == 0:
        result_text = "It's a draw!"
    elif result == -1:
        result_text = "You lose!"
        comp_score += 1
    else:
        result_text = "You win!"
        user_score += 1

    # Update the score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    comp_score_label.config(text=f"Computer Score: {comp_score}")
    
    # Show result
    messagebox.showinfo("Game Result", f"Your choice: {user_choice}\n"
                                       f"Computer's choice: {comp_choice}\n"
                                       f"{result_text}")

# Function to restart the game
def restart_game():
    global user_score, comp_score
    user_score, comp_score = 0, 0
    user_score_label.config(text="Your Score: 0")
    comp_score_label.config(text="Computer Score: 0")
    messagebox.showinfo("Game Restarted", "The game has been reset!")

# Initialize the main window
root = tk.Tk()
root.title("Snake-Water-Gun Game")
root.geometry("600x500")

# Add Canvas to set the background image
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack(fill="both", expand=True)

# Add background image
bg_image = Image.open("bg.jpeg")  # Add your own image file
bg_image = bg_image.resize((1500, 750), Image.Resampling.LANCZOS)  # Resize image to fit window
bg_photo = ImageTk.PhotoImage(bg_image)

# Display background image on canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Initialize scores
user_score = 0
comp_score = 0

# Add title label (centered)
title_label = tk.Label(root, text="Snake-Water-Gun Game", font=("Arial", 24, "bold"), fg="white", bg="#4B0082")
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Add score labels (centered)
user_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 16), fg="white", bg="#4B0082")
user_score_label.place(relx=0.2, rely=0.2, anchor="center")

comp_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 16), fg="white", bg="#4B0082")
comp_score_label.place(relx=0.8, rely=0.2, anchor="center")

# Add buttons for user choices (centered)
button_snake = tk.Button(root, text="Snake", font=("Arial", 14), command=lambda: play_game("Snake"), bg="#00CED1", fg="black")
button_snake.place(relx=0.2, rely=0.4, anchor="center")

button_water = tk.Button(root, text="Water", font=("Arial", 14), command=lambda: play_game("Water"), bg="#00CED1", fg="black")
button_water.place(relx=0.5, rely=0.4, anchor="center")

button_gun = tk.Button(root, text="Gun", font=("Arial", 14), command=lambda: play_game("Gun"), bg="#00CED1", fg="black")
button_gun.place(relx=0.8, rely=0.4, anchor="center")

# Add restart button (centered)
restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=restart_game, bg="#FF6347", fg="white")
restart_button.place(relx=0.5, rely=0.8, anchor="center")

# Run the GUI event loop
root.mainloop()
