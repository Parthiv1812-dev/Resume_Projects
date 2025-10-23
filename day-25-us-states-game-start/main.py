import turtle
import  pandas
from pandas import DataFrame
from turtle import Turtle

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score  = 0
game_over = False
correct_guesses = []
all_states = data.state.to_list()

answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Guess any state's name").title()
if answer_state in data["state"].values and answer_state not in correct_guesses:
    score += 1
    correct_guesses.append(answer_state)
    t = Turtle()
    t.hideturtle()
    t.penup()
    state_data  = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(answer_state)

else:
    game_over = True


while not game_over:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
    if answer_state in data["state"].values and answer_state not in correct_guesses:
        score += 1
        correct_guesses.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

    elif answer_state == "Exit":
        break

    else:
        game_over = True






# for s in all_states:
#     if s not in correct_guesses:
#         missing_states.append(s)

#Using list comprehension we can do the for loop above in one line
missing_states = [state for state in all_states if state not in correct_guesses]

missing_states_dict = {
    "states missing": missing_states
}

final_data = DataFrame(missing_states_dict)
final_data.to_csv("missing_states.csv")




