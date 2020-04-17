import speech_recognition as sr
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
            return  text            
        except:
            val = "Sorry could not recognize your voice"
            # print("Sorry could not recognize your voice") 
            return val
                