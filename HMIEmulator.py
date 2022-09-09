from PixelFont import *
from Pixel import Pixel

class HMIEmulator:
    def __init__(self, width : int, height : int, backgroundColor : Pixel) -> None:
        self._width = width
        self._height = height
        self._pixelMatrix = self._drawBackground(backgroundColor)
    
    def _drawBackground(self, color : Pixel) -> list[list[Pixel]]:
        assert self._width > 0, "Value is out of range"
        assert self._height > 0, "Value is out of range"

        pixelMatrix = []
        for h in range(self._height):
            pixelMatrix.append([color] * self._width)
        return pixelMatrix

    def _bresenhamLine(self, x0 : int, y0 : int, x1 : int, y1 : int) -> list[(int, int)]:

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        m = dy/dx
        
        flag = True
        
        line_pixel = []
        line_pixel.append((x0,y0))
        
        step = 1
        if x0 > x1 or y0 > y1:
            step = -1

        mm = False   
        if m < 1:
            x0, x1 ,y0 ,y1 = y0, y1, x0, x1
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            mm = True
            
        p0 = 2 * dx - dy
        x = x0
        y = y0
        
        for i in range(abs(y1-y0)):
            if flag:
                x_previous = x0
                p_previous = p0
                p = p0
                flag = False
            else:
                x_previous = x
                p_previous = p
                
            if p >= 0:
                x = x + step

            p = p_previous + 2*dx -2*dy*(abs(x-x_previous))
            y = y + 1
            
            if mm:
                line_pixel.append((y,x))
            else:
                line_pixel.append((x,y))
        
        return line_pixel

    def _defineCirclePoints(self, xc : int, yc : int, x : int, y : int, points : list[(int, int)]) -> None:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))

    def _bresenhamCircle(self, xc : int, yc : int, r : int) -> list[(int, int)]:
        points = []
        x = 0
        y = r
        self._defineCirclePoints(xc, yc, x, y, points)

        D = 3 - 2 * r

        while x <= y:

            if D < 0:
                D = D + 4 * x + 2

            else:
                y -= 1
                D = D + 4 * (x - y) + 2

            self._defineCirclePoints(xc, yc, x, y, points)
            x += 1
        return points
    
    def drawRectangle(self, x : int, y : int, width : int, height : int, color : Pixel) -> None:
        assert x >= 0, "Value is out of range"
        assert y >= 0, "Value is out of range"
        assert width > 0, "Value is out of range"
        assert height > 0, "Value is out of range"
        assert x + width <= len(self._pixelMatrix[0]), "Value is out of range"
        assert y + height <= len(self._pixelMatrix), "Value is out of range"


        for h in range(y, y + height):
            self._pixelMatrix[h][x] = color
            self._pixelMatrix[h][x + width - 1] = color
        for w in range(x, x + width):
            self._pixelMatrix[y][w] = color
            self._pixelMatrix[y + height - 1][w] = color

    def drawLine(self, x0 : int, y0 : int, x1 : int, y1 : int, color : Pixel) -> None:
        assert x0 >= 0, "Value is out of range"
        assert y0 >= 0, "Value is out of range"
        assert x1 >= 0, "Value is out of range"
        assert y1 >= 0, "Value is out of range"

        if y0 == y1:
            for w in range(x0, x1):
                self._pixelMatrix[y0][w] = color
        elif x0 == x1:
            for h in range(y0, y1):
                self._pixelMatrix[h][x0] = color
        else:
            points = self._bresenhamLine(x0, y0, x1, y1)
            for point in points:
                if(point[0] == len(self._pixelMatrix[0])):
                    self._pixelMatrix[point[1]][point[0] - 1] = color
                else:
                    self._pixelMatrix[point[1]][point[0]] = color
                
    
    def drawCicrle(self, xc : int, yc : int, r : int, color : Pixel) -> None:
        assert xc > 0, "Value is out of range"
        assert yc > 0, "Value is out of range"
        assert r > 0, "Value is out of range"
        assert (xc - r) > 0 and (yc - r) > 0, "Value is out of range"
        assert (xc + r) < len(self._pixelMatrix[0]) and (yc + r) < len(self._pixelMatrix), "Value is out of range"

        points = self._bresenhamCircle(xc, yc, r)
        for point in points:
            self._pixelMatrix[point[1]][point[0]] = color
    
    def drawChar(self, x : int, y : int, ch : str, color : Pixel) -> None:
        assert ch in pixelFont, "Char is not supported"
        assert (x + charWidth) <= len(self._pixelMatrix[0]), "Text is out of bound"
        assert (y + charHeight) <= len(self._pixelMatrix), "Text is out of bound"

        for h in range(0, charHeight):
            for w in range(0, charWidth):
                if pixelFont[ch][h][w] == 1:
                    self._pixelMatrix[y + h][x + w] = color
    
    def drawText(self, x : int, y : int, text : str, color : Pixel) -> None:
        assert x >= 0, "Value is out of range"
        assert y >= 0, "Value is out of range"
        assert (len(text) * charWidth + x) <= len(self._pixelMatrix[0]), "Text is out of bound"
        assert (y + charHeight) <= len(self._pixelMatrix), "Text is out of bound"

        text = text.upper()

        xp = x

        for c in text:
            self.drawChar(xp, y, c, color)
            xp = xp + charWidth + 1

    def exportPPM(self, filename : str) -> None:
        with open(filename, 'w') as file:
            file.write(f"P3\n\n{len(self._pixelMatrix[0])}\n\n{len(self._pixelMatrix)}\n\n255\n\n")
            for row in self._pixelMatrix:
                for column in row:
                    file.write(f"{column.getRed()} {column.getGreen()} {column.getBlue()}\t\t")
                file.write("\n")