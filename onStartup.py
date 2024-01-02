#On Startup
import os
from gpiozero import Button
import time

os.system("pip install openai")
yellowButton = Button(22)
redButton = Button(27)


#os.system("stty -F /dev/serial0 19200")
#os.system("echo 'Diagnostics Sheet:\n\nIf you see this than remove it \nand the printer should be ready \nshortly. If problems persist, \ncontact Harrison Gilbert at \nharrison.gilbert@stu.eminence.kyschools.us\n\nTesting...\nTesting...\nTesting...\n\n\n\n' > /dev/serial0")

def studentStories():
    print("you pressed student stories")
    os.system('python /home/pi/Desktop/studentStories.py')
    #print("This is for diagnostic purposes, but it would print. Just uncomment line 15 of onStartup.py and comment out line 16.")
    

def chatGPTStories():
    print("you pressed GPT button")
    os.system('python /home/pi/Desktop/chatGPTprint.py')
    

while True:
#student stories
    yellowButton.when_pressed = studentStories
    redButton.when_pressed = chatGPTStories
    
#os.system("stty -F /dev/serial0 19200")
#os.system("echo 'Diagnostics Sheet:\n\nIf you see this than remove it \nand the printer should be ready \nshortly. If problems persist, \ncontact Harrison Gilbert at \nharrison.gilbert@stu.eminence.kyschools.us\n\nTesting...\nTesting...\nTesting...\n\n\n\n' > /dev/serial0")

#os.system("python /home/pi/Desktop/ButtonTest.py")
 