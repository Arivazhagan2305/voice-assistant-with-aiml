#import libraries for the program
import voice
import datetime
import smtplib
import wikipedia
import os
import webbrowser




MASTER=str(input("Enter your Name:"))
#code for voice.speak
print("Intializing Jarvis..")
voice.speak("Initailizing Jarvis...")
loop_close = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']
c=webbrowser.get("C://Program Files (x86)/Google//Chrome//Application//chrome.exe %s")
url="google.com"
import aiml

kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

 
#wish function
def wishme():
    hour = datetime.datetime.now().hour
        
    if hour>=0 and hour<12:
        voice.speak("Good Morning"+ MASTER)
        
        
    elif hour>=12 and hour<18:
        voice.speak("GoodAfternoon"+ MASTER)
        
    else:
        voice.speak("GoodEvening" +MASTER)



def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    email_id=str(input("Enter your mail Id:"))
    password=str(input("Enter your password"))
    receiver_mail=str(input("Enter receiver mail:"))
    server.login(email_id,password)
    content=input("Enter the Content:")
    server.sendmail(email_id,receiver_mail,content)
    server.close()
    

wishme()
while (True):
    query = voice.takecommand()
    
        
    if query.lower().replace(" ", "") in loop_close:
        break
    
               

    elif 'wikipedia' in query.lower():
        
        voice.speak('searching wikipedia')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        print(results)
        voice.speak(results)
        
    elif 'who is' in query.lower():
        voice.speak('searching wikipedia')
        query = query.replace("who is","")
        results = wikipedia.summary(query,sentences=2)
        print(results)
        voice.speak(results)
        
    
    elif 'open youtube' in query.lower():
        url="youtube.com"
        c.open(url)
        
        
    elif 'open google' in query.lower():
        voice.speak("I'm on it sir")
        url="google.com"        
        c.open(url)

    elif 'google about' in query.lower():
        query=query.replace("google about","")
        voice.speak('searching')
        url = "http://www.google.com/?#q="        
        query= url + query.replace(" ","%20")
        webbrowser.open_new(query)
        

    elif 'search google' in query.lower():
        query =query.replace("search google","")
        voice.speak('searching')
        url = "http://www.google.com/?#q="
        query= url + query.replace(" ","%20")
        webbrowser.open_new(query)
                       
    
    elif 'send email' in query.lower():
        try:
            sendEmail()
            voice.speak("email has been sent successfully")
            break
        except:
            print("Check mail and password")
            voice.speak("Check mail and password")
            break

    elif "write a note" in query:
        voice.speak("What should i write , sir")
        note= voice.takecommand()
        file = open('jarvis.txt','w')
        voice.speak("Sir, Should i include date and time")
        snfm = voice.takecommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
        
    elif "show note" in query:
        voice.speak("Showing Notes")
        file = open("jarvis.txt", "r") 
        print(file.read())
        voice.speak(file.read(6))
    else:
         reply= kernel.respond(query)
         print(reply)
         voice.speak(reply)
         

    
    
    
    
    

  
    





