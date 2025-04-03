import random

password = "" 
bull = 0
cow = 0
score = 0
running = True

def create_password():
    global password
    for i in range(4): 
        password += random.choice("0123456789")

def reset_bc():
    global bull
    global cow 
    
    bull = 0
    cow = 0

def answer():
    global bull
    global cow
    global running
    global score

    answer = input("Your answer> ")

    if answer == "esc":
        running = False
    else:
        score +=1
        if answer != password: 
            for char in answer:
                charp = answer.index(char)

                if char in password and char == password[charp]:
                    bull += 1
                if char in password and char != password[charp]:
                    cow += 1

            print(f"\033[34mCows: {cow} | Bulls: {bull}\033[0m")
        else:
            print(f"\033[32mYou Won with {score} attempts\033[0m")
            if input("Play again?[y/n] ") == "y": 
                score = 0
                game() 
            else:
                running = False

def loop():
    global running
    while running:
        reset_bc()
        answer()

def game():
    create_password()
    loop()
    
game()
print(f"\033[32mThanks for Playing\033[0m")
