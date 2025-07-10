try: 
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An Exeption Occured")
finally:
    print("The try-catch is finished")
    
