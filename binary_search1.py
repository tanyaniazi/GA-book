import random


#asking the user to insert the minimum and maximum numbers and chech if the values are integer.
#also in the second while loop we check if the minimum is lower than maximum by at least 2 units.
while True:
    low_input = int(input('please insert the minimum integer number: '))
    try:
        value_low = int(low_input)
        break
    except ValueError:
        print("Invalid minimum input. Please enter an integer.")

while True:    
    high_input = int(input('please insert the maximum integer number: '))
    try:
        value_high = int(high_input)
        while value_high <= value_low + 1:
            print("Maximum input should be at least 2 units greater than minimum input. Please try again.")
            high_input = input('please insert the maximum integer number: ')
            value_high = int(high_input)
        break
    except ValueError:
        print("Invalid maximum input. Please enter an integer.")


while True:    
    your_number_input = input('please choose an integer number within the range: (I promise I will not see it ;)')
    try:
        value = int(your_number_input)
        while value > value_high or value < value_low:
            print("your number must be within the range you provided.")
            your_number_input = input('please choose your number again: ')
            value = int(your_number_input)
        break
    except ValueError:
        print("Invalid maximum input. Please enter an integer.")



def binary_search(low, high, your_number):
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

binary_search(low_input,high_input, your_number_input)

#also the game could be deceived and put to an infinity loop if the player answers the questions wrong (for lower or higher)