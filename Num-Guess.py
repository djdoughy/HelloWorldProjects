import random
secret = random.randint(1, 10)
guess = 0
tries = 0
print "Choose your fate by guessing the number I have chosen"
print "It lands between 1 and 10, you have 5 tries"
while guess != secret and tries < 5:
    guess = input("Choose your number. ")
    if guess < secret:
        print "LOW, TRY AGAIN"
    elif guess > secret:
        print "TOO MUCH, TRY AGAIN"

    tries = tries + 1

if guess == secret:
    print "You win this time"
else:
    print "YOU FAIL, YA DINGUS"
    print "The number to pass was", secret
