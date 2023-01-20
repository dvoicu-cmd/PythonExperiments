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

    def drawRectangle(self,length,height):
        rectangle = Rectangle(length,height)
        
        midPoint = self.getCanvasMid()
        halfLength = int((rectangle.length/2))
        halfHeight = int((rectangle.height/2))

        topLeftCorner = [midPoint[0] - halfLength, midPoint[1] + halfHeight]
        topRightCorner = [midPoint[0] + halfLength, midPoint[1] + halfHeight]
        bottomRightCorner = [midPoint[0] + halfLength, midPoint[1] - halfHeight]
        bottomLeftCorner = [midPoint[0] - halfLength, midPoint[1] - halfHeight]

        #Variable to store the point to draw
        drawPoint = [0,0]

        #Draw top line
        drawPoint[0] = int(topLeftCorner[0]) # x axis
        drawPoint[1] = int(topLeftCorner[1]) # y axis
        while (drawPoint[0] < rectangle.length):
            self.dataPoints[drawPoint[0]][drawPoint[0]] = 1
            drawPoint[0] = drawPoint[0] + 1


        # for i in range(rectangle.length):
        #     for j in range(rectangle.height):
        #         self.dataPoints[i][j] 
        #     drawPoint[0] = drawPoint[0] + 1 #next x point


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
    def __init__(self,length,height):
        self.length = length
        self.height = height
        self.area = length * height
        self.perimeter = (length ** 2) + (height ** 2)



def tester():
    testCanvas = Canvas(20,10)
    testCanvas.toString()
    testCanvas.drawRectangle(10,10)
    testCanvas.toString()
tester()