import random
import os


# array of students
# Title, Author, Story
haikus = [	[ "The Night Sky", "Kaylee Wethington", "The stars in the sky\nAre brighter than at daylight\nBeautiful indeed"],   
            [ "A Sunset", "Jenna Carter", "Green grass reflects light\nThe warm sun sets in the West\nIt is glorious"],
            [ "Haiku about Haikus", "Aidan Hinton", "I made this hiaku\nSo that I may inform you\nHow I hate haikus"],
            [ "Floating Stars", "Dezzmon Runion", "Like holes in the sky\nThe stars float far far away\nOut of touch from me"],
            [ "The Wind", "Dominic Tillet", "The sun takes flight\nI feel the pollen flowing\nThe wind is taking over"],
            [ "The cycle", "Messiah Sanders", "Green trees breeze on leafs\nAt ease bees freeze to flowers appease\nCycle continues from air disease"],
            [ "The Cold World", "Collin Legg", "A river can be cold\nLike the way that peoples hearts are\nIts a very cold world"],
            [ "Mirrored Light", "Logan Sisco", "The shining night sky\nLights the river below me\nAnd shines back to me"],
            [ "Spring Returns", "Landon Tindle", "The reborn forest\nit melts in the evening sunset\nspring returns again"],
            [ "Charlie", "Emma Roberts", "Charlie is black dog\nCharlie barks at sam for fun\nSam was on his phone"],
            [ "Rainbows", "Talayha Dixie", "Rain is beautiful\nI love rainbows alot\nEnd of the rainbow"],
            [ "Ocean in the Sky", "Sam Kirkland", "Sky has flowed over\nexpressing lights of\ndiamond circuilating fluidly"],
            [ "love", "Malaah W.", "Love is like some space\ni think space is great to make\nmakes me want to shake"],
            [ "Bugs Annoy Me", "Malcolm Fitzgerald", "Creepy crawly bugs\ngetting on all my nerves\nI feel like squishing"],
            [ "Me", "Micah Dale", "Sun has tripped over\nupturned a pail of\ngold paint color permeates!" ],
            [ "Good Ole Sunrises", "Tanner Malone", "Sunrises are bright\nSunrises are beautiful\nShining through the sky"],
            [ "Summer", "Adriana Reese", "She likes the summer\nshe also enjoys swimming\nthis is her life style"],
            [ "Life annoys me", "Ryan Perry", "People annoy me a lot\nwhy am i being forced to write\ni just want to go"],
            [ "Slithery Sloth", "Landen Greer", "Snails are very slimy\nSnails move very slow through the grass\nsnails are very intelligent"],
            [ "kmart kid", "\"Lil Diesel\"", "kmart is the best\nkmart is my life cuh\nkmart is the best"],
            [ "Rise High", "\"Me\"", "The moon rises high\nsilently lighting the night\nNatures lullaby"],
            [ "Turtles", "Kiya Sacra", "Turtles move very slowly\nSnapping turtles can bite very hard\nturtles love the playground"],
            [ "Loss", "Isaiah Hillard", "Impermanent life\nEmotions flow like water\nFalling like the leaves"],
            [ "dogs", "Lana Truglio", "dogs can run very fast\ndogs love squeaky chew toys and food\ndogs can be very wild"],
            [ "Animals", "Adam", "Graceful deer in fields\nWild and free, untouched by man\nNature\'s beauty thrives."],
            [ "Trees", "Nathan Armstrong", "The trees are so bright\nTrees also grow tall and wide\nThe leafs blow and shake"],
            [ "Hellos", "Maia King", "Golden shines on us\nYellow rays paint our skin from within\nwe will be renewed"],
            [ "Deer", "Adam", "Leaves rustle gently,\nBirds sing sweetly in the trees,\nNatures symphony."],
            [ "Monkeys", "Bryonna Masic", "Monkeys swing on monkey bars,\nthey act very crazy with bananas\nmonkeys love to eay bananas"],
            [ "Biggest Heartbreak", "Keyla Michelle Rios", "Ode to keyla\nTrue love, we swore\nyou and I always\nyou and I through time\nBut our kiss is just a ghost\nif cuts me more than you could ever know\nyou never believed\nwe are now just two lonely hearts."]
            
          ]

def printAll(array):
    counter = len(array)
    while counter > 0:
        print(array[counter-1][0] + "\n\nBy: " + array[counter-1][1] + "\n\n" + array[counter-1][2])
        print("\n--------------------------------------------\n")
        counter = counter - 1

#printAll(haikus)

#  prints a random student written story

rand = random.randint(0, len(haikus)-1)

os.system("stty -F /dev/serial0 19200")
os.system("echo \"" + haikus[rand][0] + "\n\nBy: " + haikus[rand][1] + "\n\n" + haikus[rand][2] + "\n\nCC BY-NC-SA\n\n\n\n\" > /dev/serial0")
#print("stty -F /dev/serial0 19200\n" +"echo '" + haikus[rand][0] + "\n\nBy: " + haikus[rand][1] + "\n\n" + haikus[rand][2] + "\n\n\n\n' > /dev/serial0")  
 