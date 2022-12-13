import turtle
import pandas
from labels import Label

image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States Games")
screen.addshape(image)
turtle.shape(image)
label = Label()

# Getting the coordinates of each State, but they're already in the csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv('50_states.csv')
states_list = data.state.to_list()

while len(label.correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(label.correct_states)}/50 States Correct",
                                    prompt="What's the next State's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in label.correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in states_list and answer_state not in label.correct_states:
        answer_state_xcoor = int(data[data.state == answer_state].x)
        answer_state_ycoor = int(data[data.state == answer_state].y)
        label.new_state(answer_state_xcoor, answer_state_ycoor, answer_state)
