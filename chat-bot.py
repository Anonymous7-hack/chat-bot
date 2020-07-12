#This My First Chat Bot Program
#! usr/bin/python 
#Chat Bot
import time

print("")
print ("~~~~~~WELLCOME~~~~~~")
time.sleep(0.3)
print ("~~~Please guy's enter a valid values~~~")
print ("")
print ("~~~I'm Make Simple Bot : ) ~~~" )
print("")
time.sleep(3)
print("~~Created by Prem~~ ")
print("")
time.sleep(3)
print ("    ---Hello Friends--- ")
print ("~~My Name Is Sara~~")
print("")
print("What Is Your Name ")
time.sleep(0.5) 
usrname=str(input("=>"))
print("")
time.sleep(1)
a= ("Ohh , Nice Name")
print(a)
print("")
print("Hello, " + usrname )
time.sleep(0.3)
print("")
time.sleep(1)
print ("This is my first program am sorry for any errors:( ")
print("")
time.sleep(1)
print ("~~HIT ENTER~~ ")
b=str(input("=>"))  
print ("Really Thanks")
print("")
print("how are you " + usrname )
print("")
usrinput=str(input("=> "))
print("")
print (" What is your dad name  " +  usrname )
usrinput=str(input("=>"))
print("")
print ("ohh  :) Nice Name  "+ usrname)
print("")
print(usrname  +  " what is your work? ")
usrinput=str(input("=>"))
print("")
time.sleep(2)
print ("are you married ? ")
def married():
  import time
  print("") 
question1 = str(input("=>"))
  
married = str(question1.lower())
yeslist='yes', 'Yes', 'yha', 'YHA'
nolist='no', 'No', 'nha', 'Nha'
if married in yeslist:
  print("ohh, enjoy  ; ) ")
  print ("")
  time.sleep(0.3)
  
elif married in nolist:
   print ("No Problem :) ")
print("~~Enter~~")
usrinput=str(input("=>"))
print ("hmm,  ;) ")
print ("")
print("what is your age ?   " + usrname )
usrinput=str(input("=>"))
print ("Hmm ")
print("")  
print("are you play pubg : ) ")
def user():
  import time
  time.sleep(2)
  print("")
question = str(input("=>"))

user = str(question.lower())
yes='yes', 'Yes'
no='no', 'No'
if user in yes:
 print("Ohh , Nice")
 print("ohhh")
 print ("im so sad :(  im not play with You, im just  a program "  )
 print("")
 
  
elif user in no:
  print("")
  print("No, problem ")
  print("")
  print("i can geometry  : ) ")
  
  
  
  
  geometry()
  
  
  
def geometry():
  import time
  print("")
  print("Can you draw geometric shapes?:")
  print("")
  bot_question2 = str(input("=> "))

  user_reply2 = str(bot_question2.lower())
  yeplist = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  neplist = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"
  if user_reply2 in yeplist:
    print("")
    print("Owh nice, I can draw too :D")
    print("")
    time.sleep(1)
    drawing()

  elif user_reply2 in neplist:
    print("")
    print("Oh, No problem :)")
    print("")
    time.sleep(1)
    print("I can draw some :)")
    drawing()
  else:
    print("")
    print("Sorry! Couldn't understand. :|")
    print("")
    geometry()

def drawing():
  import time
  print("")
  print("I can draw only four shapes :)")
  print("")
  time.sleep(1)
  print("They are:")
  print("      -> Triangle, Rectangle, Square and Rhombus")
  print("")
  print("Which one do you want me to draw? ;)")
  print("")
  bot_question3 = str(input("=> "))
  print("")
  user_reply3 = str(bot_question3.lower())
  rectangle = "Rectangle", "rectangle", "RECTANGLE", "2nd", "2ND", "Second", "second", "SECOND", "Second one", "second one", "SECOND ONE", "2nd one", "2ND ONE", "2ND one", "2nd ONE", "2"
  square = "Square", "square", "SQUARE", "3RD", "3rd", "Third", "third", "THIRD", "Third one", "third one", "THIRD ONE", "3rd one", "3RD ONE", "3RD one", "3rd ONE", "3"
  rhombus = "Rhombus", "rhombus", "RHOMBUS", "4th", "4TH", "Fourth", "fourth", "FOURTH", "Last", "last", "LAST", "Fourth one", "fourth one", "FOURTH ONE", "4th one", "4TH ONE", "4TH one", "4th ONE", "Last one", "last one", "LAST ONE", "4"
  triangle = "Triangle", "triangle", "TRIANGLE", "First one", "first one", "FIRST ONE", "1st one", "1ST ONE", "1ST one", "1st ONE", "1"
  reject_list = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "None", "none", "NONE", "0", "Zero", "zero", "ZERO", "Nothing", "nothing", "NOTHING", "No one", "no one", "NO ONE", "None of these", "none of these", "NONE OF THESE", "No one", "no one", "NO ONE"

  if user_reply3 in rectangle:
    print("")
    print("Oh great, here you go.")
    print("")
    time.sleep(1)
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|                         |")
    print("|                         |")
    print("|                         |")
    print("|_________________________|")
    print("")
    print("This is a rectangle :D")
    print("")
    draw_again()

  elif user_reply3 in square:
    print("")
    print("Oh great, here you go.")
    time.sleep(1)
    print("")
    print("|¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|            |")
    print("|            |")
    print("|            |")
    print("|____________|")
    print("")
    print("This is a square :D")
    draw_again()

  elif user_reply3 in rhombus:
    print("")
    print("Oh great, here you go.")
    print("")
    time.sleep(1)
    print("     /¯¯¯¯¯¯¯¯¯¯¯¯¯¯/")
    print("    /A            B/")
    print("   /              /")
    print("  /              /")
    print(" /D            C/")
    print("/______________/")
    print("")
    print("This is a Rhombus :D")
    draw_again()

  elif user_reply3 in triangle:
    print("")
    print("Oh great, here you go.")
    time.sleep(1)
    print("             A /|")
    print("              / |")    
    print("             /  |")
    print("            /   |")
    print("           /    |")
    print("          /     |")
    print("         /      |")
    print("        /       |")
    print("       /        |")
    print("      /         |")
    print("     /          |")
    print("    /           |")
    print("   /   .        |")
    print("  /             |")
    print(" /C            B|")
    print("/_______________|")
    print("")
    print("This is a Triangle. :D")
    draw_again()
  elif user_reply3 in reject_list:
    print("")
    print("Okay, no problem.")
  else:
    print("")
    print("Maybe I can't draw that! :( ")
    print("")

    drawing()

def feedback():

  print("")
  print("How was my drawing?")
  print("")
  bot_question4 = str(input("=> "))
  print("")
  print("I will try to improve. :) ")
  print("")


def draw_again():
  import time
  print("")
  print("Shall I draw again? :)")
  
  qus_again = str(input("=> "))
  ans_again = str(qus_again.upper())
  yeslist2 = "Yes", "Yeah", "yes", "yeah", "YES", "YEAH", "Sure", "sure", "SURE", "Of course", "of course", "OF COURSE", "1", "Yep", "yep", "YEP", "Yup", "yup", "YUP", "Yap", "yap", "YAP", "Ok","ok", "OK", "Okay", "okay", "OKAY", "Okh", "okh", "OKH", "Yah", "yah", "YAH"
  nolist2 = "No", "no", "NO", "Nope", "nope", "NOPE", "Nah", "nah", "NAH", "No need", "no need", "NO NEED", "2"

  if ans_again in yeslist2:
    drawing()

  elif ans_again in nolist2:
    print("Okay")
    time.sleep(1)
    
    feedback()

    

  else:
    print("Couldn't understand :|")
    draw_again()

geometry()

def owner_text():
  
  owner_text() 
print("Have a good day, :)")
print("")
print("BYE")
end = str(input("Hit Enter: "))
print("EXIT")
print("-----------------------------")

#python 3.8.3

