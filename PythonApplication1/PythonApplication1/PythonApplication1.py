
from shutil import move
import time, windowFunction



health = 100
level = 1
xp = 10
location = 0
section = 1
location = 1
locationName = "Test"
selection = 0

def areaLevel_(index):
    global section
    global location
    global locationName
    global selection
    windowFunction.ClearFrame_()
    print("Level: " + str(level) + "            " + "XP - " + str(xp))
    if section in range(0,6):
        location = 1
    elif section in range(6, 11):
        location = 2
    if location == 1:
        locationName = "Granfield"
    elif location == 2:
        locationName = "Granfield - Hills"
    sectionReal = section - ((location-1) * 5)
    print(locationName, "-", str(sectionReal))
    windowFunction.locationArt(index)
    print("1 - Search Location \n2 - View Inventory \n3 - Progress")
    selection = int(input(""))
    if selection == 1:
        pass
    elif selection == 2:
        pass
    elif selection == 3:
        section = section + 1
        areaLevel_(0)
    else:
        areaLevel_(0)


windowFunction.ClearFrame_()
print("Loading", end='\r') #Print loading, do a carriage return
time.sleep(0.3) #Pause for 0.3 seconds
print("Loading.", end='\r')
time.sleep(0.3)
print("Loading..", end='\r')
time.sleep(0.3)
print("Loading...")
windowFunction.ClearWindow_

windowFunction.BeholdAnimate()

name = input("                                                       ") #NAME PROMPT
windowFunction.Center_() #CENTER NAME PROMPT
windowFunction.typeSlow_("Welcome to a perilous journey. There will be challenges and triumphs. You have seen nothing as of far.") #SLOW TYPE 1 LINE
time.sleep(1)
windowFunction.storySetup("Mladav Bolen - 1654", 0) #SHOW TEXT ON TOP OF IMAGE, PRINT IMAGE BELOW
windowFunction.Text_("you are surrounded by an air of desolateness. (ENTER to continue)")
windowFunction.Text_("A faint rustle breaks the silence for a second.")
windowFunction.Text_("Is it time..? I'm probably not going to come out walking but it's worth a try.")
windowFunction.flashAnim_() #CHANGE SCENE WITH FLASHING ANIMATION
windowFunction.Text_("Oh. What's this then... another one? Bloody hell.. they're like vermin.")
windowFunction.Center_()

areaLevel_(0) #INITALISE MAIN GAMEPLAY MENU
