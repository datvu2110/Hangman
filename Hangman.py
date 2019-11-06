import random
def main():
    cont = input('Would you like to play hangman enter "y": ')
    while cont == 'y':
        hangman()
        cont = input('Would you like to play again, enter "y": ')
def hangman():
    words = ['sesame chicken','orange chicken','bejing beef','fried rice','chow mein','black pepper chicken',
             'eggrolls','kungpao chicken','sweet and fire chicken','shanghai angus steak']
    guess = words[random.randint(0,len(words)-1)]
    wrong = 3
    display = '-' * len(guess)
    won = False
    while wrong > 0 and not won:
        print(display)
        letter = input('Enter a character: ').lower()
        while len(letter) != 1:
            letter = input('You bonehead!!! Only one letter. Enter again: ').lower()
        if letter in guess:
            l = list(display)
            for i in range(len(guess)):
                if guess[i] == letter:
                    l[i] = letter
            display = "".join(l)
        else:
            wrong -= 1
            print(wrong,'guesses left')
        if guess == display:
            won = True
    if won:
        print('You won!!!')
    else:
        print('You suck, the word was', guess)
main()

