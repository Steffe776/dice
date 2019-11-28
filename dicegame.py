import random 
import time
dice = input("Tjena, vill du slå en tärning? (ja/nej) ") 
num = random.randint(1,6)
while dice == "ja":
    result = random.randint(1,6)
    time.sleep(2) 
    print (result)
    dice = input ("Vill du slå en tärning? (ja/nej) ")
else:
    time.sleep(2)
    print ("Ok, ha det bra")

    


    



