print("Mic check, one-two...") #Boot-up sequence. If this all runs it should be golden
x = 0
import time #Importing necessary modules
import math
time.sleep(2) #2 second delay, to make it seem less automatic

print("Setting up under-the-hood features...")
time.sleep(2)
print("Testing features...")
time.sleep(1)
print("Features seem to work.")
time.sleep(1)
input("Press Enter/Return to begin.") #Begin interactivity

print("\nWelcome to Python Squared! I'm excited to be able to show you\nthe wonders of programming.")
time.sleep(3)
print("\nThis is a quick tutorial sequence that will show you a few of Python's basics\nso you can get a handle on it.")
time.sleep(2)
print("\nIf you find this isn't for you, that's okay! I hope this might make that decision easier.")
time.sleep(1)
print("\nStep 1: Your First Print\n\nMany tutorials begin with the user typing the function:\nprint('Hello, world!') into Python and watching it do so.")
time.sleep(2)
print("\nFor this tutorial, you'll be able to see letters and numbers\nyou input be printed out, though as this is a completed script\nit'll work differently.")
print("\nHello, world!")
time.sleep(2)
print("\nThat's what happens when the script does the beginner's function.\nAs you might notice, it just happened. It was already in the script,\nand you didn't get to do it yourself.")
time.sleep(2)
print("\nBut don't panic! Users running the script can still print what they want with the help of the\ninput() function.")
time.sleep(2)
print("\nInput takes something the user types in, and the script can\nassign it to a variable if the scriptwriter did so.\nThen, we can print the variable.\nThis lets you print what you want.")
time.sleep(3)

userprint = input("Go ahead. Type something here, then press Enter/Return. Try to keep it basic: ") #Input tutorial, to demonstrate the concept to a user, as it's key for the script
time.sleep(2)

print(userprint)
time.sleep(1)
print("There we go! You just made the script print out something you wanted.")
time.sleep(1)

#Mini-function for users to keep printing stuff, or move on

input_tut = 0
print("If you want, you can keep printing. There's a lot you can say!")
time.sleep(1)
print("Type 'quit' when you want to move on. Otherwise, fire away!")

while input_tut != 'quit':
    input_tut = input("\nEnter something to print, or type 'quit' to exit: ")
    print(input_tut)


print("\nThat's printing with inputs. As you can see, we can make the program do \ndifferent things by using specific inputs.")
time.sleep(2)
print("\nBehind the scenes was a function that, while you told it to keep going,\ndid so, and when you said to quit, it quit.")
time.sleep(1)
print("\nUser inputs will be key to this tutorial.\nThat way, you can see the fruits of your labor right away.")
time.sleep(3)


    
    
