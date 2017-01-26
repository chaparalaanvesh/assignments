import random

def get_random_word():
    words = ['apples','ballons','cats']
    word = words[random.randint(0,len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print character
        print ""

def get_guess():
    print "enter a letter: "
    return input()
                 
def play_wordgame():
    strikes = 0
    max_strikes = 3
    playing = True
    word = get_random_word()
    blanked_word = '_' * len(word)
                 
    while playing:
        show_word(blanked_word)
        strikes += 1

        if strikes >=max_strikes:
            playing = False

    if strikes >= max_strikes:
        print 'loser'
    else:
        print 'winner'

print 'game started'
play_wordgame()
print 'game over'
