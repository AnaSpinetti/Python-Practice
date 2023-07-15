import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses_states = []

while len(guesses_states) < 50:

    answer_state = screen.textinput(title=f"{len(guesses_states)}/50 states correct", prompt="What's another state's name? R: ").title()
    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guesses_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)