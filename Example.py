from HMIEmulator import *

if __name__ == "__main__":
    
    #Filename for the PPM-Export
    filename = "Example.ppm"

    #Define some colors
    redPixel = Pixel(255,0,0)
    greenPixel = Pixel(0,255,0)
    bluePixel = Pixel(0,0,255)
    lightYellowPixel = Pixel(255,255,224)
    blackPixel = Pixel(0,0,0)
    whitePixel = Pixel(255,255,255)
    lightBlue = Pixel(75,81,229)
    
    hmi = HMIEmulator(160, 80, lightBlue)

    #Draw 4 Rectangles on the bottom
    hmi.drawRectangle(0,60,40,20,whitePixel)
    hmi.drawRectangle(40,60,40,20,whitePixel)
    hmi.drawRectangle(80,60,40,20,whitePixel)
    hmi.drawRectangle(120,60,40,20,whitePixel)

    #Draw Crosses
    hmi.drawLine(1,61,40,79,whitePixel)
    hmi.drawLine(41,61,80,79,whitePixel)
    hmi.drawLine(81,61,120,79,whitePixel)
    hmi.drawLine(121,61,160,79,whitePixel)

    #Draw Text
    hmi.drawText(2,2, "GITHUB: BBMBB", redPixel)

    #Draw Circle
    hmi.drawCicrle(79,39,10,blackPixel)
    hmi.drawCicrle(25,25,10,blackPixel)
    hmi.drawCicrle(92,39,10,blackPixel)

    #Draw Lines
    hmi.drawLine(80,20,150,55,greenPixel)

    #Export PPM File
    hmi.exportPPM(filename)