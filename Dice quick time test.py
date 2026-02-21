from inputimeout import inputimeout
import time

dice = [1,2,3,4,5,6]
user_input = 0
flag = False
while flag != True:
    for i in range(len(dice)):
        
        try:
            user_input = inputimeout( prompt = ">>" , timeout = 0.3)
        except:
            print(dice[i],  end = "\r")
            time.sleep(0.3)
        else:
            user_input = dice[i]
            flag = True
            break
    

print(user_input)
        
        