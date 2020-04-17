import voice_timer
import threading

def len1():
    if "seconds" in txt:
        voice_timer.check(0,0,int(v[1][0]))

    elif "minutes" in txt:
        voice_timer.check(0,int(v[1][0]),0)
    
    elif "hours" in txt:
        voice_timer.check(int(v[1][0]),0,0)

def len2():
    if "hours" and "hour" in txt:
        voice_timer.check(int(v[1][0]),int(v[1][1]),0)
        
    elif "minutes" or "minute" in v[0]:
        voice_timer.check(int(v[1][0]),int(v[1][1]),0)
    

while True:
    v = voice_timer.voice()
    print(v)
    txt = v[3]
    print(txt)
  
    if v[2] == 1:           
        t6 = threading.Thread(target=len1, args=(), daemon = 'true') 
        t6.start()

    elif v[2] == 2:    
        t7= threading.Thread(target=len2, args=(), daemon = 'true') 
        t7.start()