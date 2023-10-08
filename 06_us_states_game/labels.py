from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Label:
    def __init__(self):
        self.correct_states = []

    def new_state(self, x, y, state_name):
        new_state = Turtle()
        new_state.color('black')
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x, y)
        new_state.write(state_name, align='center', font=FONT)
        self.correct_states.append(state_name)
