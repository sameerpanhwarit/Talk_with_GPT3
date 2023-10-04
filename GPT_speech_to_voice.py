import requests
import openai
import json
from time import sleep
import os
import sys
import speech_recognition 
import pyttsx3 

r = speech_recognition.Recognizer() 

openai.api_key = 'your Api key Here'
logo = "----------ChatGPT Python----------"
def main():
    os.system('cls')
    print(logo)
    menu=['1.Start ChatGPT',"2.Exit"]
    for i in menu:
        print(i)
    print('-'*20)
    opt = int(input("Choose Option: "))
    if opt == 1:
        voice()
    elif opt == 2:
        pass
    else: 
        print("Invalid Option")
        sleep(0.5)
        os.system('cls')
        main()

def chatGPT(mytext):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user",
            "content":mytext}]
    )
    data=response["choices"][0]["message"]['content']
    print("Getting Response...")
    sleep(1)
    result(mytext,data)

def result(query,data):
    os.system('cls')
    print(logo)
    print("Question in voice:",query)
    print(data)
    SpeakText(data)
    # print("_"*27)
    # option1 = input("Save response in file? y/n:")
    # if option1== 'y' or 'Y':
    #     filename = input("Enter output filename: ")
    #     filename= filename+".txt"
    #     file = open(filename,'w')
    #     file.write(data)
    #     file.close()
    #     print("Save Data in File Successfully.")
    # else:
    #     pass
    option2 = input("Go back to main menu? y/n:")
    if option2 == "y" or "Y":
        main()
    else:
        exit()

def voice():
    while(1):
        os.system('cls')
        print("Talk to GPT3 in Voice: ")
        try:
            with speech_recognition.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                myvoice =r.listen(source)
                toText = r.recognize_google(myvoice)
                toText=toText.lower()
                chatGPT(toText)
        except speech_recognition.RequestError as err:
            print(f"Found{err} error.")
            
def SpeakText(answer):
	engine = pyttsx3.init()
	engine.say(answer) 
	engine.runAndWait()

if __name__ == "__main__":
    main()