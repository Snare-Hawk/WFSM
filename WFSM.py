secret = "pneumonoultramicroscopicsilicovolcanoconiosis"
secret = secret.upper()
permSecret = secret
output = ""
results = []
tries = 1

print("Wordle for the Simple-Minded")

while (tries < 7):
    guess = input(f"Guess {tries}: ")
    guess = guess.upper()
    guessLength = len(guess)
    for i in range(guessLength):
        currentLetter = guess[i]
        if currentLetter in secret:
            for o in range(i, guessLength):
                try:
                    if guess[o] == secret[o]:
                        output = output + '🟩'
                    else:
                        output = output + '🟨'
                except:
                    output = output + '🟨'
                secret = secret.replace(currentLetter, '*', 1)
                break
        else:
            output = output + '⬛'

    print("Output: " + output)
    results.append(output)

    if set(output) == {'🟩'}:
        print(f"Wordle for the Simple-Minded X {tries}/6\n")
        for i in results:
            print(i)
        tries = 42

    output = ""
    secret = permSecret
    tries = tries + 1