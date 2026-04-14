import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

#STEP 4: USE A LOOP TO ALLOW THE USER TO KEEP GUESSING
guesses = []
# STEP 6: KEEP TRACK OF THE SCORE

while len(guesses) < 50:

    #STEP 1: CONVERT THE GUESS TO TITLE CASE
    answer_state = screen.textinput(title=f"{len(guesses)}/50 States Correct",
                                    prompt="What's Another State's Name?").title()

    # if answer_state == "Exit":
    #     # STATES TO LEARN CSV
    #     states_to_learn = []
    #     for state in states.state:
    #         if state not in guesses:
    #             states_to_learn.append(state)
    #     missing_states_df = pd.DataFrame(states_to_learn)
    #     missing_states_df.to_csv("Missing_States.csv")
    #     break

    if answer_state == "Exit":
        # STATES TO LEARN - DAY 26 SHORTENING LINES 22-30 THROUGH LIST COMPREHENSION
        states_to_learn = [state for state in states.state if state not in guesses]
        missing_states_df = pd.DataFrame(states_to_learn)
        missing_states_df.to_csv("Missing_States.csv")
        break


    #STEP 2: CHECK IF THE GUESS IS AMONG THE 50 STATES
    states = pd.read_csv("50_states.csv")
    for state in states.state:
        if answer_state == state:
            print("")
            # STEP 5: RECORD THE CORRECT GUESSES IN A LIST
            guesses.append(answer_state)

    # if answer_state not in states.state:
    #     answer_state = screen.textinput(title=f"{len(guesses)}/50 States Correct",
    #                                     prompt="What's Another State's Name?").title()
    #
    #STEP 3: WRITE CORRECT GUESSES ONTO THE MAP
    state_row = (states[states.state == answer_state])
    co_ordinates = (state_row.x.item(), state_row.y.item())
    ##OR WHAT I DID INITIALLY:
    #co_ordinates = (int(states_row.x), int(states_row.y))
    turtle.ht()
    turtle.up()
    turtle.goto(co_ordinates)
    turtle.write(f"{answer_state}")
