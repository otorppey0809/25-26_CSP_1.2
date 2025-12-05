import turtle as trtl
james = trtl.Turtle()



def drawsquare(length):
    for sides in range(4):
        james.forward(length)
        james.right(90)


drawsquare(62)
james.forward(100)
drawsquare(47)





wn = trtl.Screen
wn.mainloop()