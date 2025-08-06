# greetings.py

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

print(greet("Martin", "Martin"))
print(greet("John", "Martin"))     
