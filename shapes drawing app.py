'''
Python Project: Shapes Drawing App 
Developed a graphical application using Python Turtle that draws multiple geometric shapes:
(square, circle, triangle, rectangle, hexagon, pentagon, star, decagon) along with a house shape.
'''

import turtle
#============================================================================

class Square:
    def __init__(self, side_length, fill_color, x, y):
        self.side_length = side_length
        self.fill_color = fill_color
        self.x = x
        self.y = y


    def __str__(self):
        return f"Square Shape: \n \t Length: {self.side_length} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"
    

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.fill_color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(self.side_length)
            turtle.right(90)
        turtle.end_fill()


square = Square(120, "red", -50, 50)
print(square)
square.draw()

#============================================================================

class Circle:
    def __init__(self, radius, fill_color, x, y):
        self.radius = radius
        self.fill_color = fill_color
        self.x = x
        self.y = y


    def __str__(self):
        print()
        return f"Circle Shape: \n \t Radius: {self.radius} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"
    

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.fill_color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()


circle = Circle (70, "purple", 260, -80)
print(circle)
circle.draw()

#============================================================================
   
class Triangle:
    def __init__(self, side_length, fill_color , x , y):
        self.side_length = side_length
        self.fill_color = fill_color
        self.x = x
        self.y = y


    def __str__(self):
        print()
        return f"Triangle Shape: \n \t Length: {self.side_length} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"


    def draw (self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color (self.fill_color)
        turtle.begin_fill()
        for i in range (3):
            turtle.forward(self.side_length)
            turtle.right(-120)
        turtle.end_fill()


triangle = Triangle (150, "green" , -315, -70)
print(triangle)
triangle.draw()

#============================================================================

class Rectangle:
    def __init__(self, width, height, fill_color , x , y):
        self.width = width
        self.height = height
        self.fill_color = fill_color
        self.x = x
        self.y = y


    def __str__(self):
        print()
        return f"Rectangle Shape: \n \t Width: {self.width} \n \t Height: {self.height} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"
    

    def draw (self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.fill_color)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)
        turtle.end_fill()


rectangle = Rectangle (250 , 100, "blue" , -110 , -120)
print(rectangle)
rectangle.draw()

#============================================================================

class Hexagon:
    def __init__(self, side_length, fill_color , x , y):
        self.side_length = side_length
        self.fill_color = fill_color
        self.x = x
        self.y = y

        
    def __str__(self):
        print()
        return f"Hexagon Shape: \n \t Length: {self.side_length} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"
    

    def draw (self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color (self.fill_color)
        turtle.begin_fill()
        for i in range(6):
            turtle.forward(self.side_length)
            turtle.right(60)
        turtle.end_fill()


hexagon = Hexagon (90, "orange" , -280, -130)
print(hexagon)
hexagon.draw()

#============================================================================

class Pentagon:
    def __init__(self, side_length, fill_color, x, y):
        self.side_length = side_length
        self.fill_color = fill_color
        self.x = x
        self.y = y


    def __str__(self):
        print()
        return f"Pentagon Shape: \n \t Length: {self.side_length} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"
    
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.fill_color)
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(self.side_length)
            turtle.left(72)
        turtle.end_fill()


pentagon = Pentagon(110, "pink", 210, -280)
print(pentagon)
pentagon.draw()

#============================================================================

class Star:
    def __init__(self, side_length, fill_color, x, y):
        self.side_length = side_length
        self.fill_color = fill_color
        self.x = x
        self.y = y


    def __str__(self):
        print ()
        return f"Star Shape: \n \t Side Length: {self.side_length} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"


    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.fill_color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(self.side_length)
            turtle.right(145)
        turtle.end_fill()


star = Star(150, "skyblue", -310, 200)
print(star)
star.draw()

#============================================================================

class Decagon:
    def __init__(self, side_length, fill_color, x, y):
        self.side_length = side_length
        self.fill_color = fill_color
        self.x = x
        self.y = y


    def __str__(self):
        print ()
        return f"Decagon Shape: \n \t Length: {self.side_length} \n \t Color: {self.fill_color} \n \t Position: ( x: {self.x} , y: {self.y} )"
    

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.fill_color)
        turtle.begin_fill()
        for i in range(10):  
            turtle.forward(self.side_length)
            turtle.left(36)  
        turtle.end_fill()


decagon = Decagon(45, "light green", 320, 220)
print(decagon)
decagon.draw()

#============================================================================

class House:
    def __init__(self, body_size, roof_size, body_color, roof_color, door_color, doorhandle_color, x, y):
        self.body_size = body_size
        self.roof_size = roof_size
        self.body_color = body_color
        self.roof_color = roof_color
        self.door_color = door_color
        self.doorhandle_color = doorhandle_color
        self.x = x
        self.y = y


    def __str__(self):
        print ()
        return f"House Shape: \n \t Body Size: {self.body_size} \n \t Roof Size: {self.roof_size} \n \t Body Color: {self.body_color} \n \t Roof Color: {self.roof_color} \n \t Door Color: {self.door_color} \n \t Door Handle Color: {self.doorhandle_color} \n \t Position: ( x: {self.x} , y: {self.y} )"


    def draw(self):

        # Body of the House
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.setheading(0)
        turtle.pendown()
        turtle.color(self.body_color)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.body_size)
            turtle.right(90)
            turtle.forward(self.body_size)
            turtle.right(90)
        turtle.end_fill()

        # Roof of the House
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.roof_color)
        turtle.begin_fill()
        turtle.forward(self.body_size)
        turtle.left(135)
        turtle.forward(self.roof_size)
        turtle.left(90)
        turtle.forward(self.roof_size)
        turtle.left(135)
        turtle.end_fill()

        # Door of the House
        turtle.penup()
        turtle.goto(self.x + 45, self.y - self.body_size)
        turtle.pendown()
        turtle.color(self.door_color)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.body_size / 4)
            turtle.left(90)
            turtle.forward(self.body_size / 2)
            turtle.left(90)
        turtle.end_fill()

        # Door Handle of the House
        turtle.penup()
        turtle.goto(self.x + 50, self.y - self.body_size + 30)
        turtle.pendown()
        turtle.color(self.doorhandle_color)
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()

house = House(120, 85, "gold", "saddlebrown", "saddlebrown", "white", -50, 205)
print(house)
house.draw()

#============================================================================
turtle.hideturtle()
turtle.done()