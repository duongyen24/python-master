def greet(name, be_nice=True):  
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name

#We can utilize it.
def greet_all(people):
    for person in people:
        print(greet(person)) #because it returns string

people_to_greet = ["Johnny", "Jimmy", "Jacob"]
greet_all(people_to_greet)