import random

low_input = input('please insert the minimum integer number: ')
high_input = input('please insert the maximum integer number: ')

#need to put a checker to control if the number is actually integer
#need to put a checker to control if the max > min 

your_number_input = input('please choose an integer number within the range: (I promise I will not see it ;)')

low = int(low_input)
high = int(high_input) + 1
your_number = int(your_number_input)

def binary_search(low, high):
    guess = random.randint(low, high)
    while True:
        response = input(f'aha! I guess I got it! is your number {guess}? say yes or no, do not lie buddy! ;)')
        while response.lower() not in ['yes', 'no']:
            response = input("Invalid input. Please enter 'yes' or 'no': ")

        if response.lower() == 'yes':
            if guess == your_number:
                print(f'woohoo I am so smart! :D')
                break
            else:
                print('I have a lie detecter you liar m@th**f***! -_-')
                response = input('tell me is your number higher or lower...')
                while response.lower() not in ['lower', 'higher']:
                    response = input("Invalid input. Please enter 'lower' or 'higher': ")
        elif response.lower() == 'no':
            response = input('hmm, is your number higher or lower than my guess?')
            while response.lower() not in ['higher', 'lower']:
                response = input("Invalid input. Please enter 'higher' or 'lower': ")

            if response.lower() == 'lower':
                print('darn! let me try harder')
                high = guess
                guess = random.randint(low,high)      
                
            elif response.lower() == 'higher':
                print('darn! let me try harder')
                low = guess + 1
                guess = random.randint(low,high)

binary_search(low,high)

#also the game could be deceived and put to an infinity loop if the player answers the questions wrong (for lower or higher)