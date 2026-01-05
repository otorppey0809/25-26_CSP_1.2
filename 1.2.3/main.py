#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

drawer = trtl.Turtle()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold"))

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.
wn.onkeypress(draw_an_A, "a")

import turtle as trtl

drawer1 = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()

wn = trtl.Screen()

wn.tracer(False)

drawer1.setheading(45)
drawer1.forward(200)

wn.tracer(True)

drawer2.setheading(315)
drawer2.forward(200)

wn.tracer(False)

drawer3.setheading(135)
drawer3.forward(200)

wn.listen()


wn.mainloop()

#-----function calls-----

draw_apple(apple)

wn.mainloop()