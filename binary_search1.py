import random


#asking the user to insert the minimum and maximum numbers and chech if the values are integer.
#also in the second while loop we check if the minimum is lower than maximum by at least 2 units.
def inputs():
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

    #since the input is received as str it needs to be converted to integer
    low = int(low_input)
    high = int(high_input)
    your_number = int(your_number_input)

    return low, high, your_number



def binary_search():
    low, high, your_number = inputs()
    guess = random.randint(low, high)
    pre_guess = []
    pre_guess.append(guess)
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

            if low == high:
                print(f'I think the answer is {low}, if it is not, then you made a mistake in one of your answers to guide me -.- ')
                response = input('would you like to play one more time? yes or no: ')
                while response.lower() not in ['yes', 'no']:
                    response = input("Invalid input. Please enter 'yes' or 'no': ")
                if response.lower() == 'no':
                    break
                elif response.lower() =='yes':
                    binary_search()
                    break 

            if response.lower() == 'lower':
                print('darn! let me try harder')
                previous_guess = guess
                high = previous_guess
                while True:
                    guess = random.randint(low,high)
                    if guess not in pre_guess:
                        pre_guess.append(guess)
                        break

                
            elif response.lower() == 'higher':
                print('darn! let me try harder')
                previous_guess = guess
                low = previous_guess + 1
                while True:
                    guess = random.randint(low,high)
                    if guess not in pre_guess:
                        pre_guess.append(guess)
                        break
   
          
binary_search()