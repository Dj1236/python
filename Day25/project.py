import pandas
import turtle

screen = turtle.Screen()
screen.title("State Name Finder -Harsh")
image = "./Day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./Day25/50_states.csv")
all_states = data.state.to_list()



# If answer_state is one of the states in all the states of the 50_states.csv:
    #If they got it right: 
        #create a turtle to write the name of the state at state's x and y cordinates.
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct.",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./Day25/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) 













