from graphics import *
import math

def main():
    print("""------------------Simple Transformation Demonstration--------------------
    Notes for proper images:
    The program makes a plane from (-10,-10) to (10,10)
    It draws a shape based on your input in blue, and then a matrix transformed
    shape in green.
    Enter your points in the order that you wish lines to be drawn, 
    the last point connects back to the first.
    Transformations must be typed exactly as shown with no leading or
    trailing whitespace or special characters, otherwise the program will crash :)
    Supported transformations:
    scalex = scale the x axis of your shape by a factor.
    scaley = scale the y axis of your shape by a factor.
    scalar = scale your shape by a factor.
    squeezeh = squeeze image horizontally by a factor.
    squeezev = squeeze image vertically by a factor.
    rotateR = theta clockwise rotation about the origin.
    rotateL = theta counterclockwise rotation about the origin.
    reflectx = reflect over the x-axis.
    reflecty = reflect over the y-axis.
    """)

    win = GraphWin("My Circle", 500, 500)
    XLOW = -10
    YLOW = -10
    XHIGH = +10
    YHIGH = +10
    win.setCoords(XLOW, YLOW, XHIGH, YHIGH)
    # ratio = (wx- -10)/(20)
    # px = ratio * 500

    # Draw the axes
    line = Line(Point(XLOW, 0), Point(XHIGH, 0))
    line.setOutline("red")
    line.setWidth(3)
    line.draw(win)

    line2 = Line(Point(0,YLOW), Point(0,YHIGH))
    line2.setOutline("red")
    line2.setWidth(3)
    line2.draw(win)

    for i in range(-10,11):
        xMark = Line(Point(i,0.5),Point(i,-0.5))
        xMark.setOutline("red")
        xMark.setWidth(3)
        xMark.draw(win)

        yMark = Line(Point(-0.5,i), Point(0.5,i))
        yMark.setOutline("red")
        yMark.setWidth(3)
        yMark.draw(win)


    # Gather the x and y points and lines
    xpoints = []
    ypoints = []
    lines = []

    numPoints = int(input("Please enter the desired number of points: "))
    
    for i in range(numPoints):
        xpoints.append(float(input("Please enter x"+str(i+1)+": ")))
        ypoints.append(float(input("Please enter y"+str(i+1)+": ")))
    
    # Draw the original x and y points
    for i in range(len(xpoints)):
        if i == len(xpoints)-1:
            p1 = Point(xpoints[i], ypoints[i])
            p2 = Point(xpoints[0], ypoints[0])
        else:
            p1 = Point(xpoints[i], ypoints[i])
            p2 = Point(xpoints[i + 1], ypoints[i + 1])
        line = Line(p1, p2)
        line.setWidth(2)
        line.setOutline("blue")
        line.draw(win)

    #time to apply a transformation
    transformation = str(input("Please enter the desired transformation: "))

    if transformation == "scalar":
        scalar = float(input("What number would you like to scale by?: "))
        # "function" representation:        [ x ]     [ s*x ]
        #   T = sv                 scalar * [ y ]  =  [ s*y ]
        for i in range(len(xpoints)):
            xpoints[i] = xpoints[i] * scalar
        for i in range(len(ypoints)):
            ypoints[i] = ypoints[i] * scalar
    if transformation == "scalex":
        scalar = int(input("What number would you like to scale x by?: "))
        for i in range(len(xpoints)):
            xpoints[i] = xpoints[i] * scalar
    if transformation == "scaley":
        scalar = int(input("What number would you like to scale y by?: "))
        for i in range(len(ypoints)):
            ypoints[i] = ypoints[i] * scalar
    if transformation == "squeezeh":
        k = float(input("What factor do you want to squeeze by?: "))
        for i in range(len(xpoints)):   #  ax + by   cx + dy
            newX = xpoints[i]*k
            newY = ypoints[i]*(1/k)
            xpoints[i] = newX
            ypoints[i] = newY
    if transformation == "squeezev":
        k = float(input("What factor do you want to squeeze by?: "))
        for i in range(len(xpoints)):   #  ax + by   cx + dy
            newX = xpoints[i]*(1/k)
            newY = ypoints[i]*k
            xpoints[i] = newX
            ypoints[i] = newY
    if transformation == "rotateR":
        theta = float(input("Please enter angle theta in radians: "))
        for i in range(len(xpoints)):   #  ax + by   cx + dy
            newX = math.cos(theta)*(xpoints[i]) + math.sin(theta)*(ypoints[i])
            newY = -1*math.sin(theta)*(xpoints[i]) + math.cos(theta)*(ypoints[i])
            xpoints[i] = newX
            ypoints[i] = newY
    if transformation == "rotateL":
        theta = float(input("Please enter angle theta in radians: "))
        for i in range(len(xpoints)):   #  ax + by   cx + dy
            newX = math.cos(theta)*(xpoints[i]) + -1*math.sin(theta)*(ypoints[i])
            newY = math.sin(theta)*(xpoints[i]) + math.cos(theta)*(ypoints[i])
            xpoints[i] = newX
            ypoints[i] = newY
    if transformation == "reflectx":
        for i in range(len(ypoints)):   #  ax + by   cx + dy
            newY = ypoints[i] * -1
            ypoints[i] = newY
    if transformation == "reflecty":
        for i in range(len(ypoints)):   #  ax + by   cx + dy
            newX = xpoints[i] * -1
            xpoints[i] = newX

    # Draw the transformed x and y points
    for i in range(len(xpoints)):
        if i == len(xpoints)-1:
            p1 = Point(xpoints[i], ypoints[i])
            p2 = Point(xpoints[0], ypoints[0])
        else:
            p1 = Point(xpoints[i], ypoints[i])
            p2 = Point(xpoints[i + 1], ypoints[i + 1])
        line = Line(p1, p2)
        line.setWidth(2)
        line.setOutline("green")
        line.draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done

main()