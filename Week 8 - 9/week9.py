#Functions

def greetings(name):
    print(f"Hello, {name}")
    
greetings("Testing Function")

def adds(a, b):
    return a + b

result = adds(2, 10)
print(result)

def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def change_greeting(name, greet = "Hello"):
    print(f"{greet}, {name}")
    
    
change_greeting("durara")
change_greeting('dandandan', "wassup")