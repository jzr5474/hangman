import urllib
import urllib.request
import re
from urban import urban
import random
from pic import pic

def random_urban():
    word = urllib.request.urlopen("http://www.urbandictionary.com/random.php")
    word = word.read()
    word = word.decode()
    lst = word.splitlines()
    for index in range(len(lst)):
        if "<title>Urban Dictionary:" in lst[index]:
            thing = lst[index]
            a = list(thing)
            for i in range(25):
                a.pop(0)
            for j in range(8):
                a.pop()
            print(a.join(a).lower())
            print("sahhh dude")
            return "".join(a).lower()
def hangman():
    word = random_urban()
    nums = [0,1,2,3,4,5,6,7,8,9]
    a = list(word)
    for i in a:
        if i in nums:
            word = random_urban
            a = list(word)
            break
    b = []
    already_guessed = []
    for x in range(len(a)):
        if a[x]==" ":
            b.append("  ")
        else:
            b.append("*")
    x = 0
    while x < 7 and "*" in b:
        pic(x)
        #print("You have",7-x,"guesses left. Go!", end = "  ")
        print()
        print(" ".join(b))
        print("Already guessed:"," ".join(already_guessed))
        guess1 = input()
        guess = guess1.lower()
        if len(list(guess)) > 1:
            print("Too many characters dumbass. Try again")
            continue
        elif guess in already_guessed:
            print("Already guessed, you lose a guess")
            x = x+1
            continue
        elif len(list(guess)) == 0:
            print("You gotta enter something moron")
            continue
        else:
            if guess in a:
                q = a.count(guess)
                v = 0
                print("Hit")
                while v < q:
                    i = a.index(guess)
                    b[i] = guess
                    a[i] = "@"
                    v=v+1
                a = list(word)
            else:
                print("Miss")
                x = x+1
            already_guessed.append(guess)
    else:
        if "*" in b:
            print("You lose. The word was")
            print(word)
            print(urban(word))
            print("Kill yourself")
        else:
            pic(x)
            print("    ___{You did it!!}")
            print("   /")
            print("  O")
            print(" \|/")
            print("  |")
            print(" / \ " )
            print(word.upper())
            print("Congrats!" "You win!")
            print("The word was: ",word.lower(),":",urban(word))
        
            
print("Let's Play Urban Hangman!")
print(random_urban)
for i in range(100):
    hangman()
