from random import randint
while True:
    cpu = randint(1,11)
    user = int(input("Guess the number between 1 to 10: \n"))
    score = 1
    while cpu != user:
        user = int(input("Guess the number again between 1 to 10: \n"))
        score += 1
        if cpu == user:
            break
    print("Your score is :",score)
    if input("type 'exit' or 'restart'.\n").lower() == 'exit' :break