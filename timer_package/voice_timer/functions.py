import sys
import time
import threading 
import time
import os
import speech_recognition as sr
import re 
import json

def check(hour,min,sec):
    
    c= ":"
    while hour > -1:
        while min > -1:
            while sec > 0:
                sec=sec-1
                time.sleep(1)
                sec1 = ('%02.f' % sec)  # format
                min1 = ('%02.f' % min)
                hour1 = ('%02.f' % hour)
                f = sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))
     
                if str(hour1) == "00" and  str(min1) == "00" and str(sec1) == "07":                   
                    print("Time up")

            min=min-1
            sec=60
        hour=hour-1
        min=59

    print('Countdown Complete.')
    return f

def voice():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:    
        print("Speak Anything :")
        audio = r.listen(source)       
        try:
            text = r.recognize_google(audio)                
            t = str(text)
            # print("You said : {}".format(t)) 
            res = [int(i) for i in t.split() if i.isdigit()] 
            res_len = len(res)         
            g = str(t.split())
            # print("You said : {}".format(t))      
            return  text, res, res_len, g
            
        except:
            val = "Sorry could not recognize your voice"
            # print("Sorry could not recognize your voice") 
            return val
                