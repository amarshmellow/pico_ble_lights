import time
import ws2812
import random

numberofleds = ws2812.NUM_LEDS

ledslist = [] # 0 to 128
blueorwhite = [] # 1 or 2


for i in range(numberofleds):
    ledslist.append(0)
    blueorwhite.append(1)

while True:
    
    if random.randint(1,100) > 95:
        
        num1 = random.randint(0,(numberofleds-1))
        
        if ledslist[num1] == 0: 
            ledslist[num1] = 318
            num2 = random.randint(1,2)
            blueorwhite[num1] = num2
        else:
            pass
        
        
    
        
    for i in range(numberofleds):
        
        if ledslist[i] > 254: # fade in if bigger than 254
            
            colour =  4 * abs(ledslist[i]-318)
            
            if blueorwhite[i] == 1:
                ws2812.pixels_set(i, ((colour,colour,colour)))
            else:
                ws2812.pixels_set(i, ((0,colour,colour)))
                
        else: #if not bigger than 254 
            
            if blueorwhite[i] == 1: # fade out
                ws2812.pixels_set(i, ((ledslist[i],ledslist[i],ledslist[i])))
            else:
                ws2812.pixels_set(i, ((0,ledslist[i],ledslist[i])))
                
    ws2812.pixels_show()
            
    for i in range(numberofleds):
        if ledslist[i] != 0:
            ledslist[i] =  ledslist[i] - 2                 
    
    
    time.sleep(0.01)