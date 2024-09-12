
from shutil import move
import time, windowFunction


windowFunction.ClearWindow_()

print("Loading", end='\r') #Print loading, do a carriage return
time.sleep(0.3) #Pause for 0.3 seconds
print("Loading.", end='\r')
time.sleep(0.3)
print("Loading..", end='\r')
time.sleep(0.3)
print("Loading...")
windowFunction.MoveUpTop_()

windowFunction.ClearWindow_
windowFunction.BeholdAnimate()

name = input("                                                       ") #NAME PROMPT
windowFunction.Center_() #CENTER NAME PROMPT
windowFunction.typeSlow_("Welcome to a perilous journey. There will be challenges and triumphs. You have seen nothing as of far.") #SLOW TYPE 1 LINE
time.sleep(1)
windowFunction.storySetup("Mladav Bolen - 1654", 0)
windowFunction.Text_("you are surrounded by an air of desolateness. (ENTER to continue)")
windowFunction.Text_("A faint rustle breaks the silence for a second.")
windowFunction.Text_("Is it time..? I'm probably not going to come out walking but it's worth a try.")
