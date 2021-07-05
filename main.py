import turtle
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("50_states.csv")
writer = turtle.Turtle()
writer.penup()
writer.shape("circle")
writer.shapesize(stretch_wid=0.2, stretch_len=0.2)
game_is_on = True

correct = 0
while game_is_on:
    screen.title(f"{correct}/{len(states)} States guessing game")
    answer_state = screen.textinput(title="Guess the State", prompt="Enter the state: ").title()


    for state in states["state"]:
        if answer_state == state:
            the_state = states[states["state"] == state]
            writer.goto(float(the_state["x"]), float(the_state["y"]))
            writer.write(the_state["state"].to_list()[0])
            correct += 1

turtle.mainloop()
