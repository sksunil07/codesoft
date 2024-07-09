import tkinter as tk
import random

def determine_winner(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg='#2d2d2d')

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg='#2d2d2d', fg='aqua')
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Choose one:", font=("Arial", 15), bg='#2d2d2d', fg='pink')
instruction_label.pack(pady=5)

button_frame = tk.Frame(root, bg='#2d2d2d')
button_frame.pack(pady=10)

button_style = {
    "font": ("Arial", 15),
    "bg": "yellow",   
    "fg": "black",   
    "activebackground": "#81c784",
    "activeforeground": "#ffffff",  
    "width": 10,
    "bd": 0,
    "highlightthickness": 0,
    "relief": "flat"
}

rock_button = tk.Button(button_frame, text="Rock", **button_style, command=lambda: determine_winner('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", **button_style, command=lambda: determine_winner('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", **button_style, command=lambda: determine_winner('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

computer_choice_label = tk.Label(root, text="", font=("Arial", 15), bg='#2d2d2d', fg='#1e90ff') 
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 15, "bold"), bg='#2d2d2d', fg='#ff6347')  
result_label.pack(pady=10)

root.mainloop()
