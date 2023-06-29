import random
import time

class NumGame:
    round = 0
    score = 0
    play = True
    final_score = 0
    guess_res = 0
    
    # Checks the guess and the provides a response to guide the user 
    # if another guess is required
    def checkGuess(s, guess):
        if guess == ans:
            print(f"Great job, the number was {guess}")
            return True
        elif guess > ans: 
            print('Guess lower')
        elif guess < ans: 
            print('Guess higher')

    # called by run_game, takes the guess from the user and passes it 
    # to checkGuess, loops until True is returned from checkGuess
    def guess(s):
        while s.guess_res != ans:
            s.guess_res = input('\nWhat is your guess? ')
            # if float(s.guess_res):
            #     print(f'Guesses must be whole numbers only, your guess was {s.guess_res}')
            # elif int(s.guess_res):
            s.guess_res = int(s.guess_res)
            if s.checkGuess(s.guess_res):
                s.score = s.score + 1
            # else:
            #     print(f'Guesses must be a number, your guess was {s.guess_res}')
            s.round = s.round + 1
            print(f"\nYour current score is {s.score}/{s.round} or {'%.2f'%((s.score/s.round)*100)}%")

    # Receives input from the user to determine max guess range
    def guessRange(user_val):
        global guess_range_res
        guess_range_res = int(input('\nPlease enter a number to guess between 1 and your number: '))
        global ans
        ans = random.randrange(1, guess_range_res)

    # Used to start the game and loop through for as long as the user 
    # wants to play, when the user is done, it will print a final score
    def runGame(s):
        while s.play:
            print("Setting up game! :) \n")
            time.sleep(1)
            s.guessRange()
            s.guess()
            run_game = input('Would you like to play again? (y/n) ').lower()
            if run_game != 'y':
                if s.round == 0 :
                    s.final_score = 0
                else:
                    s.final_score = ('%.2f' % ((s.score/s.round)*100))
                break

        print(f'Your final score was: {s.score}/{s.round} or {s.final_score}%')

class RockPSGame:
    round = 0
    uscore = 0
    cscore = 0
    ties = 0
    play = True
    options = ["rock", "paper", "scissors"]
    
    # Determines the winner for RPS by accepting an input from compChoice
    # and userChoice then uses a str comparison and returns a
    # a number to pass to score()
    def battle(s, comp, user):
        print(f"You chose {user}, computer chose {comp}")
        if user == comp:
            print(f"Both players chose {user}. It's a tie.\n")
            return 0
        elif user == "rock":
            if comp == "scissors":
                print(f"{user} beats {comp}! You win!\n")
                return 1
            else:
                print(f"{comp} beats {user}! You lose!\n")
                return -1
        elif user == "paper":
            if comp == "rock":
                print(f"{user} beats {comp}! You win!\n")
                return 1
            else:
                print(f"{comp} beats {user}! You lose!\n")
                return -1
        elif user == "scissors":
            if comp == "paper":
                print(f"{user} beats {comp}! You win!\n")
                return 1
            else:
                print(f"{comp} beats {user}! You lose!\n")
                return -1
    
    # Evaluates the number passed from battle() to determine who gets a 
    # point
    def scoring(s, sval):
        if sval == 1:
            s.uscore = s.uscore + 1
        elif sval == -1:
            s.cscore = s.cscore + 1
        else:
            s.ties = s.ties + 1
    
    # Receives a string input and returns the value to pass to battle()
    def userChoice(s):
        global user_choice
        print("Are you ready?\n")
        time.sleep(1)
        user_choice = input('Make your choice: Rock, Paper, or Scissors: \n').lower()
        return user_choice
    
    # Uses a random choice gen on the options array and returns the 
    # value to pass to battle()
    def compChoice(s):
        print("Computer is preparing to make a move...\n")
        time.sleep(1)
        global comp_choice
        comp_choice = random.choice(s.options)
        return comp_choice
    
    # Used to start the game and loop through for as long as the user
    # wants to play, when the user is done, it will print a final score
    def runGame(s):
        while s.play:
            print("Setting up game! :) \n")
            time.sleep(1)
            s.scoring(s.battle(s.compChoice(), s.userChoice()))
            s.round = s.round + 1
            print(f"Current round is: {s.round}, scores are: \nUser: {s.uscore}, Computer: {s.cscore}, Ties:{s.ties}")
            run_game = input('\nWould you like to play again? (y/n) ').lower()
            if run_game != 'y': 
                break
            
        print(
            f"\nFinal score was: User: {s.uscore} of {s.round}, Computer's score {s.cscore} of {s.round}, Ties:{s.ties}")

# class WordGame: 
#     def guess():
#         print()
#     def guess():
#         print()
#     def guess():
#         print()
#     def guess():
#         print()


games = [NumGame(), RockPSGame()]

# Accepts the users input to determine which game to initialize for game play
while True: 
    playing = games[int(input('''What game would you like to play?

    ---- Use the corresponding number ----

    Number Guess - 1
    Rock, Paper, Scissors - 2
    Word Guess Game - 3
    
Your response here: ''')) - 1]

    playing.runGame()
    
    run_game = input('\nWould you like to play another game? (y/n) ').lower()
    if run_game != 'y':
        break

print('\n Thank you for playing!')
