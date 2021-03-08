# project with if else

print("wellcome  to my first game")
name = input("what is your name?" )
age = int(input("what is your age?"))
print("you are", name, age, "year old")

if age >=18:
    print("you are old enough to play")  
    want_to_play = input("do you want to play").lower()
    if want_to_play == "yes":
        print("lets play")
else:
    print("get out!")  

