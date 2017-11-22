import os
import random
import time

print('Hi my name is Qwerty, your personal chatbot')
print('For a better quality please use uppercase for the first character')
print('What is your first name?')
firstName = input()
    
print('Hello,', firstName, 'how old are you?')
age = input()
age = int(age)
if age > 99:
    print('Wow, you are a true legend!')
elif age > 60:
    print('How is your retirement going?')
elif age < 18:
    print('Please try not to use alcohol')
  
print('Have you ever wanted to play football?')
question1=input()
if question1 in ['Yes', 'Of course', 'I would like to',"yes","yes i do","Yes I do","Yes i do"]:
    print('Ok, then what are you waiting for?')
    answer1=input()
    if answer1 in ["I dont have money", "I need football equipment", "I dont have enough time"]:
          print('Oh...I see...')
    elif answer1 in ['I already play football', "I'm playing it", 'I do', 'I need to improve my skills']:
          print('Then work harder if you want to be a football star')
    else:
        print("I understand you")
            
elif question1 in ["No", "I don't like football", "Once", "Twice"]:
    print('Then you should start doing a sport!')
    
print("Would you like to talk about food?")
question2=input()
if question2 in ["Yes","yes","Of course","of course","I would like to","i would like to","yea","ok"]:
      print('Ok, firstly what do you prefer romanian or italian food?')
      answer2=input()
      if answer2 in ["Romanian","romanian"]:
          print("Nice, i like romanian food too so have you ever heard about sarmale or mamaliga?")
          answer3=input()
          if answer3 in ["Yes","yes"]:
            print("Delicious!")
          elif answer3 in ["No","no"]:
            print("Oh god...I think you should try it, trust me")
      elif answer2 in ["Italian","italian"]:
          print("Good choice, but you know Italy is famous for pizza , spaghetti and pasta.")
          print("What do you prefer?")
          answer4=input()
          if answer4 in ["Pizza","pizza"]:
              print("My favourite pizza is double peperoni")
          elif answer4 in ["Spaghetti","spaghetti"]:
              print("I think that someone is loving Italian food")
          elif answer4 in ["Pasta","pasta"]:
              print("So we are dealing with a pasta lover")
          
elif question2 in ["No","no","Not right now","Anything else","not right now","anything else"]:
    print("K, sorry.... but I need to tell you something")
    answer5=input()
    if answer5 in ["Ok","ok","OK","What?","what?","what","What","Tell me","tell me"]:
      print("Can you tell me what the time is?")
    elif answer5 in ["No","no","no you cant","No you cant"]:
      print("Ok i will not ask you anymore question")  
      

      
      #Here,please use this format (time: 20.57) because this is the format of Qwerty:D
print("Can you tell me the time please?")
answer6=int(input())
if answer6 > 20.0:
  print("Oh, I need to eat something fast...can you excuse me for a moment?")
  answer7=input()
  if answer7 in ["Yes","yes"]:
    print("I have already ate:))")
  elif answer7 in ["No","no"]:
    print("You are bad, now you need to say sorry..")
  answer8=input()
  if answer8 in ["Sorry","sorry","Im sorry","im sorry","excuse me","Excuse me"]:
    print("It is alright mate")
  elif answer8 in ["No","no","Why?","why?","why","Why","but why?","But why?"]:
    print("Because if you do not I will nevere speak to you again..")
  elif answer8 in ["No","no"]:
    print("Try again..")
elif answer6 < 20.0:
  print("Oh, good then, should i ask you who you rather prefer between CR7 and Messi?")
footballq1=input()
if footballq1 in ["CR7","cr7","Cristiano Ronaldo","Cristiano ronaldo","cristiano ronaldo"]:
  print("Many people say that Cristiano Ronaldo is selfish,what do you think?")
  footballq2=input()
  if footballq2 < 10:
    print("Yea..i know")
  elif footballq2 > 20:
    print("From my point of view I think people are not right")
  else:
    print("I do not know what to say..")
elif footballq1 in ["Messi","messi","Lionel Messi","Lionel messi","lionel messi"]:
  print("I though that Lionel Messi was the best player some years ago, so sorry")
          
elif answer6 >23.59:
            print("So...i think i will ask you another question so we can know each other better")
            print("Do you know which is the best university in UK?")
generalq=input()
if generalq in ["Coventry","coventry","cov university","Cov university","Coventry university","coventry university"]:
  print("Yeah, you got it. Do not forget to give our team a thumbs up")
else:
  print("Possible, but for we it is Coventry University")
        
print("So you want to talk again?")
personalq=input()
if personalq in ["Yes","yes","yea"]:
    print("I do not have much time left so are you male or female?")
personalq2=input()
if personalq2 in ["male","Male"]:
    print("Have you had a girlfriend recently?")
personalq3=input()
if personalq3 in ["Yes","yes","yea","yeah","Yes I do","Yes i do","yes i do","Yea","Yeah"]:
    print("Was she blonde or brunette?")
    personalq4=input()
    if personalq4 in ["Blonde","blonde"]:
        print("Russian blonde girls are the best!")
    elif personalq4 in ["Brunette","brunette"]:
        print("Romanian brunette girls are the best!")
    elif personalq4 in ["Neither","neither","none of those","None of those","none","None"]:
        print("Then does not matter , sorry")
    else:
        print("Ok, nice")    
elif personalq3 in ["No"]:
    print("Wish you all the luck then")
elif personalq2 in ["female","Female"]:
    print("Have you ever had a boyfriend recently?")
personalq5=input()
if personalq5 in ["Yes","yes","yea","yeah","Yes I do","Yes i do","yes i do","Yea","Yeah"]:
    print("Was he romanian or not?")
    personalq6=input()
    if personalq6 in ["Yes","yes","yea","yeah","Yes I do","Yes i do","yes i do","Yea","Yeah"]:
        print("Nice , Robert is romanian too")
    elif personalq6 in ["No","no","not"]:
        print("oK,OK")
    else:
        print("Ok then")
elif personalq5 in ["No","no","not yet","Not yet","Not","not","No i do not","No i dont","no i do not","no i dont"]:
    print("Oh, sorry then...good luck i think")
            
elif personalq in ["No","no","No sorry","no sorry","no bye","no ty"]:
    print("Ok then... see you!")
    
        
      
      
    
    
  
 
