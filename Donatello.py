import pyautogui
from PIL import Image
import time
import itertools


#Requiriments

#pip install PyAutoGUI
#pip install Pillow

#How to use
# Run the script and then you have 5 seconds to switch to the emulator and leave it selected.
# Maybe after running switch the time until suspension and time it takes the screen to turn off setting in windows
# Just in case it might break, i dindt test that.


# Opens a image in RGB mode
# WARNING USE BIG PICTURES(over 300px) or it might break. I didnt have time to fix it lol.
# Use jpg format.
im = Image.open(r"input.jpg")

# Size of the image in pixels (size of original image)
width, height = im.size

# we code the palettes
palette = [
        0, 0, 0, #negro
        0, 204, 68, #verde medio
        102, 255, 153, #verde claro
        0, 0, 153, #azul oscuro
        102, 102, 255, #azul claro
        255, 51, 0, #rojo
        0, 255, 255, #celeste
        255, 51, 153, #rosa
        255, 179, 217, #rosa claro
        255, 255, 0, #amarillo
        255, 255, 153, #amarillo claro
        0, 77, 26, #verde oscuro
        207, 52, 118, #magenta
        127, 127, 127, #gris
        255, 255, 255 #blanco
        ]

paletteRGB = [
        (0, 0, 0), #negro
        (0, 204, 68), #verde medio
        (102, 255, 153), #verde claro
        (0, 0, 153), #azul oscuro
        (102, 102, 255), #azul claro
        (255, 51, 0), #rojo
        (0, 255, 255), #celeste
        (255, 51, 153), #rosa
        (255, 179, 217), #rosa claro
        (255, 255, 0), #amarillo
        (255, 255, 153), #amarillo claro
        (0, 77, 26), #verde oscuro
        (207, 52, 118), #magenta
        (127, 127, 127), #gris
        (255, 255, 255) #blanco
        ]

palleteCommandLetter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","r",]


def GetWorkableImage():
    newHeight = height * (((width*100)/110) / 100) # Escalamos x el mismo porcentaje
    if(newHeight > 130):
        newHeight = 130
    newsize = (110, newHeight)
    img2 = im.resize(newsize)

    ## Convertimos la imagen a la paleta
    img3 = Image.new('P', (int(newsize[0]), int(newsize[1])))
    img3.putpalette(palette)

    conv = img2.quantize(palette=img3, dither=0)
    return conv

def TypeAnything(text):
    inputText = text
    for letter in inputText:
        pyautogui.keyDown(letter)
        pyautogui.keyUp(letter)
    PressEnter()

def PressEnter():
    pyautogui.keyDown("Enter")
    pyautogui.keyUp("Enter")

def PressEscape():
    pyautogui.keyDown("Escape")
    pyautogui.keyUp("Escape")

def SetUpPixel():
    TypeAnything("para p")
    PressEnter()
    TypeAnything("at 1 de 90")
    TypeAnything("ad 1 iz 90")
    TypeAnything("ad 1")
    PressEscape()

def SetUpMoveToNextPixel():
    TypeAnything("para q")
    PressEnter()
    TypeAnything("de 90 ad 1")
    TypeAnything("iz 90")
    PressEscape()

def SendToStartPoint():
    TypeAnything("sp")
    TypeAnything("ad 70 iz 90")
    TypeAnything("ad 120 de 90")
    TypeAnything("cp")

def GoToNextLine():
    TypeAnything("s")

def DibujarLinea(longPixeles):
    if longPixeles > 110:
        longPixeles = 110
    if longPixeles <= 3:
        for pixel in range(longPixeles):
            TypeAnything("p")
            time.sleep(0.2)
            TypeAnything("q")
    else:
        texto = "repetir " + str(longPixeles) + " [p q]"
        TypeAnything(texto)
    cantidad = ((8.5 * (longPixeles))/ 110) # revisar si no hace falta el x2
    time.sleep(cantidad)

def _GetColor(indice):
    TypeAnything(palleteCommandLetter[indice])

def SetUpColors():
    TypeAnything("para a")
    PressEnter()
    TypeAnything("fcolorp 1")
    PressEscape()
    TypeAnything("para b")
    PressEnter()
    TypeAnything("fcolorp 2")
    PressEscape()
    TypeAnything("para c")
    PressEnter()
    TypeAnything("fcolorp 3")
    PressEscape()
    TypeAnything("para d")
    PressEnter()
    TypeAnything("fcolorp 4")
    PressEscape()
    TypeAnything("para e")
    PressEnter()
    TypeAnything("fcolorp 5")
    PressEscape()
    TypeAnything("para f")
    PressEnter()
    TypeAnything("fcolorp 6")
    PressEscape()
    TypeAnything("para g")
    PressEnter()
    TypeAnything("fcolorp 7")
    PressEscape()
    TypeAnything("para h")
    PressEnter()
    TypeAnything("fcolorp 8")
    PressEscape()
    TypeAnything("para i")
    PressEnter()
    TypeAnything("fcolorp 9")
    PressEscape()
    TypeAnything("para j")
    PressEnter()
    TypeAnything("fcolorp 10")
    PressEscape()
    TypeAnything("para k")
    PressEnter()
    TypeAnything("fcolorp 11")
    PressEscape()
    TypeAnything("para l")
    PressEnter()
    TypeAnything("fcolorp 12")
    PressEscape()
    TypeAnything("para m")
    PressEnter()
    TypeAnything("fcolorp 13")
    PressEscape()
    TypeAnything("para n")
    PressEnter()
    TypeAnything("fcolorp 14")
    PressEscape()
    TypeAnything("para r")
    PressEnter()
    TypeAnything("fcolorp 15")
    PressEscape()

def SetUpGoToNextLine():
    TypeAnything("para s")
    PressEnter()
    TypeAnything("sp")
    TypeAnything("at 1 iz 90")
    TypeAnything("ad 220 de 90") # Es 220 xq es el tama;o que estoy usando maximo de imagen aca..
    TypeAnything("cp")
    PressEscape()
    



# Codigo  del programa ####################

time.sleep(5)
print("Started Clock.")
start_time = time.time()

img = GetWorkableImage()
rgb_img = img.convert('RGB')

#Setup process
SendToStartPoint()
SetUpPixel()
SetUpGoToNextLine()
SetUpMoveToNextPixel()
SetUpColors()
print("Done setting up!.")

#It scans each line from left to right and draw it.
# Usa el algoritmo de Run-length encoding , para saber cuantos pixeles tiene que pintar del mismo color.
lastUsedColor = None

for pixelY in range(rgb_img.size[1]):
    linea = [rgb_img.getpixel((x, pixelY)) for x in range(110)] # Valor hasta 110 ANCHO
    g = [(x, len(list(y))) for x, y in itertools.groupby(linea)]
    #print(g)
    for color, cant in g:
        if(lastUsedColor != color):
            _GetColor(paletteRGB.index(color))
            lastUsedColor = color
        DibujarLinea(cant)
        print(f"Pinto {cant} de {color} T:" + str(int((pixelY*100)/rgb_img.size[1])) + "%")
    GoToNextLine()

# Cuando termino de pintar
TypeAnything("ot")
TypeAnything("bt")
        
print("Done")
# Get the total runtime.
print(" Tardo --- %s minutos ---" % (int((time.time() - start_time)/60)))
# Show the image it was based on for comparison
rgb_img.show()






