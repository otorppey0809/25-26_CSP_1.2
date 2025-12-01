import turtle as trtl
james = trtl.Turtle()



def drawsquare():
    for sides in range(4):
        james.forward(100)
        james.right(90)

drawsquare()
james.forward(100)
drawsquare()

wn = trtl.Screen
wn.mainloop()