import string, random, time
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

userPassword = input("What do you want to use as your password: ")

attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(userPassword)))

completed = False
guesses = 0

while completed == False:
    print(attemptThis)
    time.sleep(0.1)
    attemptNext = ""
    completed = True
    for i in range(len(userPassword)):
        if attemptThis[i] != userPassword[i]:
            completed = False
            attemptNext = attemptNext + random.choice(possibleCharacters)
        else:
            attemptNext = attemptNext + userPassword[i]
    guesses = guesses + 1
    attemptThis = attemptNext
    
print("Password Cracked! That took", guesses, "guesses.")
