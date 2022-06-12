from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

redled = LED(14)
yellowled = LED(15)
greenled = LED(18)

win = Tk()
win.title("LED Toggler")
myFont =  tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

value = IntVar()

def redLedToggle():
    yellowled.off()
    yellowLedButton["text"] = "Turn YELLOW LED on"
    greenled.off()
    greenLedButton["text"] = "Turn GREEN LED on"
    if redled.is_lit:
        redled.off()
        redLedButton["text"] = "Turn RED LED on"
    else:
        redled.on()
        redLedButton["text"] = "Turn RED LED off"

def yellowLedToggle():
    redled.off()
    redLedButton["text"] = "Turn RED LED on"
    greenled.off()
    greenLedButton["text"] = "Turn GREEN LED on"
    if yellowled.is_lit:
        yellowled.off()
        yellowLedButton["text"] = "Turn YELLOW LED on"
    else:
        yellowled.on()
        yellowLedButton["text"] = "Turn YELLOW LED off"

def greenLedToggle():
    yellowled.off()
    yellowLedButton["text"] = "Turn YELLOW LED on"
    redled.off()
    redLedButton["text"] = "Turn RED LED on"
    if greenled.is_lit:
        greenled.off()
        greenLedButton["text"] = "Turn GREEN LED on"
    else:
        greenled.on()
        greenLedButton["text"] = "Turn GREEN LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

redLedButton = Button(win, text = "Turn RED LED on", font = myFont, variable = value, value = 1, command = redLedToggle, bg = 'bisque2', height = 1, width = 24)
redLedButton.grid(row = 0, column = 1)

yellowLedButton = Button(win, text = "Turn YELLOW LED on", font = myFont, variable = value, value = 2, command = yellowLedToggle, bg = 'bisque2', height = 1, width = 24)
yellowLedButton.grid(row = 0, column = 2)

greenLedButton = Button(win, text = "Turn GREEN LED on", font = myFont, variable = value, value = 3, command = greenLedToggle, bg = 'bisque2', height = 1, width = 24)
greenLedButton.grid(row = 0, column = 3)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row = 2, column = 1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()