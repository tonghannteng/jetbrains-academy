import random
import string

print('H A N G M A N')

while True:

    command = input('Type "play" to play the game, "exit" to quit: ')
    if command == 'exit':
        print('exit')
        break
    elif command == 'play':
        words = ['python', 'java', 'kotlin', 'javascript']
        random_word = random.choice(words)
        mask = list('-' * len(random_word))

        attempts = 8
        count = 0
        types = []
        while count < attempts:

            join_word = ''.join(mask)

            if join_word == random_word:
                print('You guessed the word ' + random_word + '!\nYou survived!\n')
                break

            print('\n' + join_word)
            s = input('Input a letter:')

            if len(s) != 1:
                print('You should input a single letter')
                continue

            if s not in string.ascii_lowercase:
                print('Please enter a lowercase English letter')
                continue

            if s in types:
                print("You've already guessed this letter")
                continue

            types.append(s)
            indexes = [i for i in range(len(random_word)) if s == random_word[i]]
            if indexes:
                for j in indexes:
                    mask[j] = random_word[j]
            else:
                print("That letter doesn't appear in the word")
                count = count + 1

            if count == 8:
                print('You lost!\n')
                break
