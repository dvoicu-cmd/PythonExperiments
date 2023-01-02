from math import pi

class Canvas:
    def __init__(self,length,height):
        self.rows = length
        self.cols = height
        self.dataPoints = []
        for i in range(self.rows):
            currentRow = []
            for j in range(self.cols):
                currentRow.append(0)
            self.dataPoints.append(currentRow)

    def toString(self):
        outputStr = ''
        for i in range(self.rows):
            strRow = ''
            for j in range(self.cols):
                strRow = strRow + str(self.dataPoints[i][j])
            outputStr = outputStr + strRow + '\n'
        print(outputStr)

    def drawSquare(self,size):
        square = Rectangle(size,size)


    def drawCircle(self,radius):
        circle = Circle(radius)

    def getCanvasMid(self):
        x = int((self.rows)/2)
        y = int((self.cols)/2)
        mid = (x,y)
        return mid


class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.area = (pi * radius) ** 2
        self.perimeter = 2 * pi * radius

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = (length ** 2) + (width ** 2)



def tester():
    testCanvas = Canvas(25,25)
    testCanvas.toString()
tester()