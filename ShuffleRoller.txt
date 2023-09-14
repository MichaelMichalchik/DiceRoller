# Importing the required libraries
import random
import tkinter as tk

# Global variable to store the shuffled deck and the current index
shuffled_deck = []
current_index = 0

# Function to shuffle a deck of numbers from 1 to 20
def shuffle_deck():
    global shuffled_deck
    global current_index
    shuffled_deck = list(range(1, 21))
    random.shuffle(shuffled_deck)
    current_index = 0
    deck_label.config(text="Deck has been shuffled.")

# Function to draw the next number from the shuffled deck
def draw_number():
    global shuffled_deck
    global current_index
    if current_index >= len(shuffled_deck):
        shuffle_deck()  # Refill the deck if empty
    drawn_number = shuffled_deck[current_index]
    current_index += 1
    
    existing_text = drawn_numbers_label.cget("text")
    existing_text_list=existing_text.split()
    current_index_3=current_index-3
    current_index_2=current_index-2
    new_text = f"{existing_text_list[current_index_3]} {existing_text_list[current_index_2]}{drawn_number}"
    drawn_numbers_label.config(text=new_text)

# Create the main application window and set its title
window = tk.Tk()
window.title("Shuffle Deck Die Roller")
window.geometry("620x300")  # Resize the window

# Create buttons to shuffle the deck and draw a number
shuffle_button = tk.Button(window, text="Shuffle Deck", command=shuffle_deck)
shuffle_button.pack(pady=20)

draw_button = tk.Button(window, text="Draw Number", command=draw_number)
draw_button.pack(pady=20)

# Create labels to display the deck status and drawn numbers
deck_label = tk.Label(window, text="Deck is empty.")
deck_label.pack(pady=10)

drawn_numbers_label = tk.Label(window, text="Drawn Numbers:")
drawn_numbers_label.pack(pady=10)

# Start the main GUI loop
window.mainloop()
