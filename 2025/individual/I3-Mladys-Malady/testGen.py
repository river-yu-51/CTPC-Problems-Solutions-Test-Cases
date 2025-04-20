import random

# set parameters
TOTALPOTIONS = 1700
POTIONLENGTHMIN = 5
POTIONLENGTHMAX = 10
STORESMIN = 10**7
STORESMAX = 10**8
P = 1000
N = 1000

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
potions = [] # potions[-1] -> target potion

def randomWord(chars, length):
    word = ""
    for i in range(length):
        word += random.choice(chars)
    return word

for i in range(TOTALPOTIONS):
    word = randomWord(letters, random.randint(POTIONLENGTHMIN, POTIONLENGTHMAX))
    if word not in potions:
        potions.append(word)

f = open("./testGenfile.txt", 'w')
f.truncate()

line2 = str(P) + ' ' + str(N) + '\n'
line3 = ""
line4 = ""

for i in range(P):
    line3 += potions[i]
    line3 += ' '
    line4 += str(random.randint(STORESMIN, STORESMAX))
    line4 += ' '

f.write(potions[-1] + '\n')
f.write(line2)
f.write(line3[:-1] + '\n')
f.write(line4[:-1] + '\n')

for i in range(N):
    productIndex = TOTALPOTIONS - i - 1
    reactant2Index = random.randint(0, productIndex - 2)
    reactant1Index = random.randint(0, reactant2Index)
    f.write(potions[reactant1Index] + ' ' + potions[reactant2Index] + ' ' + potions[productIndex])
    if i != N - 1: f.write('\n')


