﻿import time
import types


def ClearWindow_(): #CLEAR THE WHOLE WINDOW
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def MoveUpTop_(): #MOVE TEXT TO TOP
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def Center_(): #CENTER TEXT
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def BeholdAnimate(): #ANIMATE PROJECT BEHOLDER TITLE
    logo = """\                                                                                                 
                                              █                                                                  
                      █  █ █  ▒  █ █ ░░░██    █                                                                  
                      ███▒ █  ███  █ ███  ███ ██              ██     ░░▓█████████                                
                      █          ░█           █      ███       ██▒   ░█████████████                              
                                 █            ███    ███       ███    ██████ ███████            ██▓              
                      ▓████████████           ███    ███       ███     █████  ░██████           ████████         
                     ██████ ███████▓       ██ ███    ▓██       ███     █████   ███████          █████████████░   
                    ▒██████ ███████░    █████ ██▒ ██████ █████ ░██      ████   ███████          ████   ███████   
                    ██████████░ ░███ ░███████ ██████░███ ██░██  ██      ████▓   ██████░         ░███▓     ░██    
                    ███████████████  ███ ████ ██░    ███ ██ ██  ██       ████   ██████▒░█        ████            
                    ████████░██████ ███████   ██     ███ ██ ██░ ██░      ░███   ███████ ████████ ████▒           
                    ██████   █████  ██        ██    ▒███ ██ ░██ ▓████████ ███    ██████ ███ ████ █████           
                    ██████▓▓▒████▓ ██████████ ██    ████ ██████  █████████ ███░  ██████ ███████▒ █████▒          
                    █████████████ ▓▒                                    ░█ ████████████ ██      ▒██████          
                                                                                  ████  ███████  ██████░         
                                                                                            ░▓   ███████         
                                                                                                     ███░        
                                                                                                        █        
                                                                                                 
                                                                                                 """
    logoCenter = logo.center(20) #Center the logo.

    typeSlow_("Welcome to Project BEHOLDER")
    time.sleep(0.5)
    print(logoCenter)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                               ⚔Enter your name to begin.⚔")

def CenterMini_(): #SLIGHTLY CENTER TEXT
    print("")
    print("")
    print("")
    print("")
    print("")


def art(index): #INDEX FOR ASCII ART
    if index == 0:
        print("""                                                                                                 
                      ▓░                                                                             
                ███████████                                                            ▓███████      
                █████████████                                                          ████████▒     
                ████████████████████                                          █████▒   ████████████  
               █████████████████████                                          █████████████████████  
               ██████████████████████    ████████████░                        ░████████████████████  
              ░█████████████████         ██████████████                        ███    ▒█████   ████  
              ████████████               ███████████████                       ███▒▒████████   ████  
                  ▒███   █░              █████████████████                     ░███████████████████  
                          ██             ███████████████████                      ░████████████████  
                          ███                 ██▒█                             ████████████████████  
                           ███                   ██                            ███      ███████████  
                           ███░                  ██                            ████     ███████████  
                          ████                   ███                           ████     ███████████  
                       ░██████████████           ███░                      █████████    ███████████  
                 ▓███████████████████████████▓░░░████                 █████████████████████████████▓▒
    █████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████████████████████████████████████████████████████████████████""")


def Text_(text): #PLAY ONE LINE OF TEXT
    typeSlow_(text)
    tempLine = input("")

def storySetup(text, index): #SET CUTSCENE
    ClearWindow_()
    CenterMini_()
    typeSlow_(text)
    art(index)
    CenterMini_()

def typeSlow_(text): #SLOW TYPING
    text = str(text)
    for letter in text:
        print(letter, end='')
        time.sleep(0.075)