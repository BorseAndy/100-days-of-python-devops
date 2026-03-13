import turtle
import pandas
from score import Score

# --- CONFIGURATION ---
DATA_FILE = "50_states.csv"
IMAGE_FILE = "blank_states_img.gif"
TOTAL_STATES = 50

# --- SETUP ---
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_FILE)
turtle.shape(IMAGE_FILE)

# Load data once at startup
data = pandas.read_csv(DATA_FILE)
all_states = data.state.to_list()

# Initialize managers and utilities
score_manager = Score()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guessed_states = []

# --- MAIN GAME LOOP ---
while len(guessed_states) < TOTAL_STATES:
    # Prompt user for input
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{TOTAL_STATES} States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    )

    # Handle cancellation (Esc or Cancel button)
    if answer_state is None:
        break
    
    answer_state = answer_state.title()

    # Exit sequence: Save missing states to CSV for learning
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state is not guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    # Validate guess and prevent duplicates
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        
        # Extract coordinates using Pandas .item()
        state_row = data[data.state == answer_state]
        x_pos = int(state_row.x.item())
        y_pos = int(state_row.y.item())
        
        # Display state name on map
        writer.goto(x_pos, y_pos)
        writer.write(answer_state, align="center")
        
        # Update scoreboard
        score_manager.increase_score()

# Exit on click if the loop finishes or 'Exit' is called
screen.exitonclick()
