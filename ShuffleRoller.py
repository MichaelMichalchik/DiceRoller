# Importing the required libraries
import random
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

# Global variable to store the shuffled deck and the current index
shuffled_deck = []
current_index = 0
last_20=[]
# Global variable to store the count of each number drawn
number_counts = [0] * 20  # A list of 20 zeros

# Create the main application window and set its title
window = tk.Tk()
window.title("Shuffle Deck Die Roller")
window.geometry("620x300")  # Resize the window
#Number of draws text box
draws_label = tk.Label(window, text="Enter number of draws:")
draws_label.pack(pady=5)
draws_entry = tk.Entry(window)
draws_entry.pack(pady=5)
reshuffle_label = tk.Label(window, text="Enter number of draws before reshuffle:")
reshuffle_label.pack(pady=5)
reshuffle_entry = tk.Entry(window)
reshuffle_entry.pack(pady=5)
# Create labels to display the deck status and drawn numbers
deck_label = tk.Label(window, text="Deck is empty.")
deck_label.pack(pady=10)


# Matplotlib Figure and Canvas Setup
fig, ax = plt.subplots(figsize=(5, 3))  # This will hold our plot
histogram_canvas = FigureCanvasTkAgg(fig, master=window)  # This creates the Tkinter canvas containing the Matplotlib figure
histogram_canvas_widget = histogram_canvas.get_tk_widget()  # This gets the Tkinter widget that will display the Matplotlib figure
histogram_canvas_widget.pack()  # Pack the Matplotlib canvas onto the Tkinter window

# Function to update the histogram
def update_histogram():
    ax.clear()  # Clear the previous histogram
    ax.bar(range(1, 21), number_counts, tick_label=range(1, 21))
    # Create a bar chart with numbers 1 to 20 on the x-axis and their corresponding counts on the y-axis
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Drawn Numbers')
    histogram_canvas.draw_idle()  # Redraw the histogram canvas

# Insert this function just before defining the `shuffle_deck` function


# Function to shuffle a deck of numbers from 1 to 20
def shuffle_deck():
    global shuffled_deck
    global current_index
    global last_20
    shuffled_deck = list(range(1, 21))
    random.shuffle(shuffled_deck)
    current_index = 0
    deck_label.config(text="Deck has been shuffled.")
    update_histogram() 

# Function to draw the next number from the shuffled deck
def draw_number():
    global shuffled_deck
    global current_index
    global last_20
    global number_counts
    
    if current_index >= len(shuffled_deck):  # This should ideally never happen
        shuffle_deck()
    drawn_number = shuffled_deck[current_index]
    number_counts[drawn_number - 1] += 1
    last_20.append(drawn_number)
    if len(last_20) > 20:
        last_20.pop(0)
    current_index += 1

def clear_program():
    global shuffled_deck, current_index, last_20, number_counts

    # Reinitialize the variables
    shuffled_deck = list(range(1, 21))
    current_index = 0
    last_20 = []
    number_counts = [0] * 20

    # Reset the text entries
    # draws_entry.delete(0, tk.END)
    # reshuffle_entry.delete(0, tk.END)
    # Clear the histogram
    update_histogram()

    # Reset labels
    deck_label.config(text="Deck is empty.")
    drawn_numbers_label.config(text="Drawn Numbers:")

def start_draw_reshuffle():
    global current_index
    global shuffled_deck
    
    try:
        total_draws = int(draws_entry.get())
        draws_before_reshuffle = int(reshuffle_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for total draws and draws before reshuffle.")
        return
    
    current_index = 0  # Reset the index
    shuffle_deck()  # Start by shuffling once
    
    for i in range(total_draws):
        if i > 0 and i % draws_before_reshuffle == 0:  # Reshuffle logic
            shuffle_deck()
        draw_number()  # Draw a number from the deck
    
    update_histogram()  # Update the histogram after all draws
    drawn_numbers_label.config(text=' '.join(map(str, last_20)))  # Update the label with the last drawn numbers


# Create buttons to shuffle the deck, draw a number, and clear the program
shuffle_button = tk.Button(window, text="Shuffle Deck", command=shuffle_deck)
shuffle_button.pack(pady=20)

draw_button = tk.Button(window, text="Start Draw", command=start_draw_reshuffle)
draw_button.pack(pady=20)

clear_button = tk.Button(window, text="Clear", command=clear_program)
clear_button.pack(pady=20)


# Create label to display the drawn numbers
drawn_numbers_label = tk.Label(window, text="Drawn Numbers:")
drawn_numbers_label.pack(pady=10)

# Start the main GUI loop
window.mainloop()