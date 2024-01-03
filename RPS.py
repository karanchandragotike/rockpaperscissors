import random
cpu=0
user=0

options=["rock","paper","scissors"]

while True:
    user_input=input("Enter rock/paper/scissors or q to quit:").lower()
    if user_input=="q":
        break
    if user_input not in ["rock","paper","scissors"]:
        continue
    random_num=random.randint(0,2)
    cpu_option=options[random_num]
    print("cpu picked",cpu_option)
    if user_input=="rock" and cpu_option=="scissors":
        print("You win!")
        user+=1
    elif user_input=="paper" and cpu_option=="rock":
        print("You win!")
        user+=1
    elif user_input=="scissors" and cpu_option=="paper":
        print("You win!")
        user=1
    elif user_input==cpu_option:
        print("draw")
    else:
        print("you lost")
        cpu+=1


print("GAME OVER")
print("you won ",user," times")
print("cpu won ",cpu," times")