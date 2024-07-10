import turtle

t = turtle.Turtle()

# Total No. of sides of the polygon to be drawn  
side = 3
  
# Total Length of each side of the polygon to be drawn  
lngth = 55 
  
for j in range(side):  
  t.forward(lngth)  
  t.right(360/side)  



turtle.done()