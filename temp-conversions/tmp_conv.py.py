from stt_conversion import voice
from temp_conv import kel_cel, cel_kel, cel_far, far_cel, kel_far, far_kel

# pip install stt_conversion, temp_conv
# Example say: "convert 50 degree celsius to fahrenheit"

temps = ["Celsius", "Fahrenheit", "Kelvin"]
v = voice()
op = v.split()
print(op)
value = int(op[1])

# celsius to fahrenheit
if op[3] == temps[0] and op[5] == temps[1] :
    t = cel_far(value)
    print(t)

# fahrenheit to celsius
if op[3] == temps[1] and op[5] == temps[0] :
    t = far_cel(value)
    print(t)

# kelvin to fahrenheit
if op[3] == temps[2] and op[5] == temps[1] :
    t = kel_far(value)
    print(t)
 
# fahrenheit to kelvin
if op[3] == temps[1] and op[5] == temps[2] :
    t = far_kel(value)
    print(t)

# celcius to kelvin
if op[3] == temps[0] and op[5] == temps[2] :
    t = cel_kel(value)
    print(t)

# kelvin to celcius
if op[3] == temps[2] and op[5] == temps[0] :
    t = kel_cel(value)
    print(t)