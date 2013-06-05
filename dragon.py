import random
import time
def name():
    print("What's your name?")
    name = input()
    return name

    
def displayIntro(name):
    print(' ' + name + ',You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()



def chooseCave(name):
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into, ' + name + '? (1 or 2)')
        cave = input()
        
    return cave

def checkCave(chosenCave, name):
    print('You aproach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('' + name + ', a large dragon jumps out infront of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Asks you if you want the princess or the secret treasure? (princess- 1 or treasure- 2)')
        good = input()
        if good == '1':
            print("Yay. You get the princess!")
        if good == '2':
            print("Yay. You are rich now!")
    

    else:
        print('Gives you the choice to be eaten alive, or to be sufficated by puppies. (eaten- 1 suffacated- 2)!')
        bad = input()
        if bad == '1':
            print("The dragon has a toothache so he takes a long time in eating you")
        if bad == '2':
            print("The puppies are soft and furry and...")
            time.sleep(1)
            print("Suffocating!")
     
    
        

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    name = name()
    displayIntro(name)
    
    caveNumber = chooseCave(name)

    checkCave(caveNumber, name)

    print('Do you want to play again, ' + name + '? (yes or no)')
    playAgain = input()
            
    
