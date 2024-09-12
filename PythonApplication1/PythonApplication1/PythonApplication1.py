
from shutil import move
import time
import windowFunction


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

name = input("                                                       ")
windowFunction.Center_()
windowFunction.typeSlow_("Welcome to a perilous journey. There will be challenges and triumphs. You have seen nothing as of far.")
time.sleep(1)
windowFunction.storySetup("Mladav Bolen - 1654", 0)
windowFunction.Text_("you are surrounded by an air of desolateness. (ENTER to continue)")
windowFunction.Text_("A faint rustle breaks the silence for a second.")
