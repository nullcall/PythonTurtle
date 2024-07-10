#Python Program to draw a square filled with colour in Turtle  
import turtle   
ttl = turtle.Turtle()  
  
#Providing the color to be filled  
ttl.color("yellow")  
  
#Instructing to "begin" and "end" filling the "square"  
ttl.begin_fill()  
  
#for-loop to run 4 times to complete drawing each side of square  
for j in range(4):  
    ttl.forward(160)  
    ttl.right(90)  
ttl.end_fill()  
  
#hiding the turtle after completing the drawing  
ttl.hideturtle()  
turtle.done()  