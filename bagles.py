import random 

def bagles():

    dict_ ={"Pico": "One digit is correct but in the wrong position",
            "Fermi":"One digit is correct and in the right position.",
             "Bagles":"No digit is correct." }
    print("I am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:")
    print(f'When i say:           That means:')
    for key,value in dict_.items():
        print(f'{key}:           {value}')

    print("\nI have thought up a number.\nYou have 10 guesses to get it.")

    choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    three_digit_number = [str(random.choice(choices)),
                          str(random.choice(choices)),
                          str(random.choice(choices))]
    
    is_playing = True
    guess = 1

    while is_playing:


        print(f"Guess: {guess} \n")
        
        input_digits = input("Enter a three digit number of your choice: ")

        if len(input_digits) != 3 or input_digits.isalpha():
            print("input not a three digit number: ")

        elif list(input_digits) == three_digit_number:
            print("You got it")
            is_playing = False

        elif guess >= 10:
            print("Reached max number of guess!!")
            is_playing = False

        else:
            print()
            input_list = list(input_digits)
            
            for i in range(3):
                if input_list[i] == three_digit_number[i]:
                    print("Fermi")

                elif input_list[i] in three_digit_number:
                    print("Pico")

                else:
                    print("Bagles")

        guess = guess + 1

            
                    
            
        

bagles()
