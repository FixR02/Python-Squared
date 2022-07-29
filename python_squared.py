print("Mic check, one-two...") #Boot-up sequence. If this all runs it should be golden
x = 0
import time #Importing necessary modules
import math
import statistics
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
input("Press Enter/Return to continue.")
print("\nStep 1: Your First Print\n\nMany tutorials begin with the user typing the function:\nprint('Hello, world!') into Python and watching it do so.")
time.sleep(2)
print("\nFor this tutorial, you'll be able to see letters and numbers\nyou input be printed out, though as this is a completed script\nit'll work differently.")
input("Press Enter/Return to continue.")
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
input("Press Enter/Return to continue.")

#Tuple tutorial; referencing parts of one
print("You might have noticed a mention of variables earlier.\nWell, let's talk about that. Rather, sets of variables as used in Python:\ntuples, lists, and dicts.")
time.sleep(1)
print("\nFirst are tuples. These are sets that are bounded by parentheses, like so:")
T = (1, 2, 3, 4, 5)
print("T = (1, 2, 3, 4, 5) <-- Like this.")
time.sleep(2)
print("\nJust name a variable and assign it a tuple of whatever length.\nPython does require some restrictions regarding this, though.")
print("Variables need to be one word, or at least contain no spaces, instead underscores must be used. They cannot start with special characters or numbers.")
time.sleep(2)
print("\nMost Python scriptwriters will format variables like so: var_a.\ncamelCase is also an option, like so: varA.\nHowever most will opt for the first one, and if you would rather use camelCase, keep it consistent.")
time.sleep(3)
input("Press Enter/Return to continue.")

print("\nBack to tuples, and the most important distinction about them is that\nthey are immutable. In layman's terms, they cannot be changed after you\ncreate them.")
time.sleep(1)
print("\nIndividual parts of a tuple can be referenced by typing in this: the name of the tuple, and in brackets, the index.")
print("\nNote that in most Python cases, the index, or position, begins at 0.\nThat is, the first number is referenced with T[0] and the second number T[1],\nand so on.")
T[2]
time.sleep(1)
T[4]
time.sleep(1)
T[1]
time.sleep(3)
print("\nYou can also reference a slice of a tuple, that is, a multiple number part.\nT[1:3] <-- Like this.")
T[1:3]
time.sleep(2)
print("\nSlices work in a certain way. \nThe first number is the index the slice begins at, but does not include.\nThe second number is the end index, which is included.")
time.sleep(1)
print("\nA slice of 1:3 would have the second and third indices appear,\nor the third and fourth numbers, as again, the index begins at 0.")
time.sleep(1)
print("\nAlternatively, slices can be one-sided, that is, if one number is left blank.\nT[1:], T[:4] <-- Like these.")
time.sleep(2)
print("\nIf one part of a slice is blank, it automatically begins at index 0\nfor the first number, or ends at the last index for the second.")
time.sleep(1)
print("\n(A quick note: tuples can also have words, or in Python, strings, as their subvariables,\nbut mixing them up with numbers tends to cause problems.\nFor this tutorial, we'll stick to numbers.)")
time.sleep(2)
input("Press Enter/Return to continue.")

#List tutorial; building your own data
print("\nThat's a tuple! While situational, it has its uses. Let's move on to lists, as I think they're much better- and interactable for you.")
time.sleep(1)
L = []
print("\nLists are like tuples, except you define them with brackets [ instead of parentheses (.\nLike tuples, you can reference one of their numbers in the same formats,\nfrom singles to slices.")
time.sleep(1)
print("\nL = [1, 2, 3, 4, 5] <-- Like this.\nL[0], L[2], L[1:3] <-- And like these.")
time.sleep(1)
print("\nWhat makes a list useful is that it's mutable,\nwhich means it can be changed, added onto, cut down, et cetera, after it's defined.\nYou can even make an empty list to start and add onto it.")
time.sleep(2)
print("I've defined a list already with the variable L. It's empty, so let's have you add onto it!")
input("Press Enter/Return to continue.")
list_data = ""
print("\nGo and get some data: maybe the height of your family, or your ages, or your favorite numbers, or something made up! Anything is fine.")
time.sleep(1)

while list_data != 'done':
    list_data = input("\nEnter any number. Put in at least 5, but you can do more. Type 'done' to finish: ")
    
    if list_data != 'done':
        L.append(int(list_data))
        print(L)


time.sleep(2)
print("\nIf you want to remove some data, you can: I'll give you a chance, too.")
list_data = ""
time.sleep(2)
print(L)

while list_data != 'done':
    list_data = input("\nEnter a number you put into the data set. Each time you use this, it will remove the first instance of it.\nOr, just enter 'done' to move on: ")
    
    if list_data != 'done':
        L.remove(int(list_data))
        print(L)

#dicts tutorial, and increasing complexity
time.sleep(2)
input("Press Enter/Return to continue.")
print("\nThat looks like some good data. We'll come back to this in a bit. First, I'd like to go over one more set type: dicts.")
time.sleep(2)
print("\nDicts, short for dictionaries, are a more complex version of data sets.\nYou know how a dictionary defines words, right? Well, Python dictionaries work much the same.")
time.sleep(1)
print("\nDicts are formed with braces {. Like lists, they are mutable and can be changed after first creating them.\nThey can be referenced, sliced, et cetera as well.")
time.sleep(2)
print("\nWhat sets dicts apart is that their subvariables come in pairs.\nD = {k1:v1, k2:v2} <-- Like this.")
D = {1:'Alpha', 2:'Bravo', 3:'Charlie', 4:'Delta', 5:'Echo', 6:'Foxtrot', 7:'Golf', 8:'Hotel', 9:'India', 10:'Juliet', 11:'Kilo', 12:'Lima', 13:'Mike', 14:'November', 15:'Oscar', 16:'Papa', 17:'Quebec', 18:'Romeo', 19:'Sierra', 20:'Tango', 21:'Uniform', 22:'Victor', 23:'Whiskey', 24:'X-Ray', 25:'Yankee', 26:'Zulu'}
time.sleep(2)
input("Press Enter/Return to continue.")
print("\nThat's what it means by defining: k1 and v1 are shorthand for key 1 and variable 1.\nWhen referencing with D[k1], v1 will appear.\nThis also means the 0 index doesn't apply- the index is whatever we set the keys\nas when we define the dict.")
time.sleep(1)
print("\nBoth keys and values can be numbers or strings: for example, H is the eighth letter in the English alphabet.\nWe can put this in a dict like so: alpha = {8:'H'}, or alpha = {'H':8}.")
time.sleep(1)
print("Note that strings must be surrounded by single or double quotes.\nIf not, Python will try to call variables, and if they haven't been defined, it'll break.")
input("Press Enter/Return to continue.")
#Calling dict keys tutorial
time.sleep(2)
print("\nLet's practice calling keys ourselves.\nI've defined a dict D with the keys as numbers 1 through 26 and the variables as the aviation alphabet,\nwhich is used to better distinguish individual letters.")
time.sleep(3)
print("\nWe'll reference 3 keys of your choice, and print them out.")
time.sleep(1)
avialph_1 = D[int(input("Input a number from 1-26 here: "))]
print(avialph_1)
avialph_2 = D[int(input("Input a number from 1-26 here: "))]
print(avialph_2)
avialph_3 = D[int(input("Input a number from 1-26 here: "))]
print(avialph_3)
time.sleep(2)
input("Press Enter/Return to continue.")
print("Once you get into the thick of it, it really isn't too hard. That's Python for you.\nShallow at the start, and while it gets deep, you don't have to dive far to learn a lot.")
time.sleep(2)
print("\nHow about we do a bit of math? Use Python to learn something about that list you made earlier?")
time.sleep(1)

print(L)
list_data = ""
print("Here's your list as it is now. I'll give you one more chance to change it.")


#Doing math and data analysis on some user-entered data; one extra chance to change the data being used
while list_data != 'done':
    list_data = input("\nEnter a number to add, or type 'done' to finish: ")
    
    if list_data != 'done':
        L.append(int(list_data))
        print(L)
        
           
print(L)
list_data = ""
print("\nHere's your list again. Remove what you don't need; keep at least 5 numbers.")

while list_data != 'done':
    list_data = input("\nEnter a value from the list above to remove, or type 'done' to finish: ")
    
    if list_data != 'done':
        L.remove(int(list_data))
        print(L)
        
time.sleep(2)
input("Press Enter/Return to continue.")
#The actual data analysis part
print("Now that your data is ready, let's learn... something about it.")
print("\nPython comes with several modules included in the install,\nand plenty more online made by third parties. We'll use a couple to understand your data.")
time.sleep(2)
print("\nAt the beginning of the script, behind the scenes, \nI imported the math and statistics modules.")
print("(Importing a module is as simple as typing import /module/,\nwith /module/ being the name of the module you want imported. You can also use the from command,\nformatted from /module/ import /function/, to import just certain parts of a module.)")
time.sleep(3)
print("\nThere's a huge list of functions we can use from these modules.\nWe could find factorials, square roots, permutations, exponents and logarithms, trigonometrics, et cetera.")
input("Press Enter/Return to continue.")
time.sleep(3)
print("\nDepending on your data and its context it could be useful\nto run any one of these functions and then some. For this tutorial, we'll keep\nit a bit simpler.")
demo = [1, 11, 6, 15, 85, 30, 7, 2, 45, 30]
print(demo)
time.sleep(2)
print("\nHere I've made a demo list of 10 numbers. Let's use functions to learn about it a bit more.")
print("\nWe can figure out the mean, median and mode, among other things. \n(Quick note: functions imported from a module need the module name first, dot the function name, \nsuch as time.sleep (the sleep function from the time module).)")
time.sleep(1)
print(statistics.mean(demo))
time.sleep(1)
print(statistics.median(demo))
time.sleep(1)
print(statistics.mode(demo))
input("Press Enter/Return to continue.")
#Basic data analysis terminal
print("\nThat's just to demonstrate what it can do. What can we find out about your list?")
time.sleep(2)
print(L)
print("Here it is again, just in case.")

time.sleep(3)
#I meant to give the user more control here, but the ability to input is limited.
print("Well, we can look for the same mean, median and mode:")
time.sleep(1)
a = statistics.mean(L)
print(a)
time.sleep(1)
b = statistics.median(L)
print(b)
time.sleep(1)
c = statistics.mode(L)
print(c)
input("Press Enter/Return to continue.")

print("Or perhaps how long it is, its standard deviation and variance...")

time.sleep(1)
d = len(L)
print(d)
time.sleep(1)
e = statistics.stdev(L)
print(e)
time.sleep(1)
f = statistics.variance(L)
print(f)
input("Press Enter/Return to continue.")

print("Check if a certain value is in the list, reverse its index order... or combine it with another list, like the demo one, then sort it!")

time.sleep(1)
print('22' in L)
time.sleep(1)
R = L.reverse()
print(R)
time.sleep(1)
C = L + demo
print(C)
time.sleep(2)
S = (C.sort)
print(S)
time.sleep(1)
input("Press Enter/Return to continue.")


time.sleep(2)
print("\nI'm thankful for you sticking around to try this out!\nI thought to demonstrate my understanding of basic Python concepts\nby teaching them to you in a very Python way.")
time.sleep(2)
print("\nThis is only the tip of the iceberg. Python is absolutely full of potential\nand learning, and I hope this was a window for you to look into\nin order to see if it's for you or not.")
time.sleep(2)
print("\nI, for one, thought it was fun to make this, even if I could've done a bit better.")
print("\nI'll leave you with the ability to print whatever you want\nas a parting gift. Or, if you want, you can exit this script, and just type python\ninto your command prompt to open the wide world of Python for yourself to unleash!")
print("\nIf you decide you like it, maybe I'll see you again out there.\nEither way... thank you!")
input_tut = ''
while input_tut != 'quit':
    input_tut = input("\nEnter something to print, or type 'quit' to exit: ")
    print(input_tut)