try: 
    x = 5
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An Exeption Occured")
finally:
    print("The try-catch is finished")
    
    
try: 
    print(y)
except:
    print("Variable y is not defined")
else: 
    print("Everything went wrong")

x = 1

if x < 0 :
    raise Exception("Sorry no numbers below 0")