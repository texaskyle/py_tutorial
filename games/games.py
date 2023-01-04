import messages
import random


"""messages.hello("Evans")
messages.bye("safaricom")"""


while True:
    def results():
        print("computer: " + computer)
        print("player: " + player)


    # rock, paper and scissors game
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    player = None
    while player not in options:
        player = input("rock, paper or scissors? ").lower()
    if player == computer:
        results()
        print("This is a tie!!")
    elif player == "rock":
        if computer == "paper":
            results()
            print("The computer has won")
        elif computer == "scissors":
            results()
            print("The player has won")
    elif player == "scissors":
        if computer == "rock":
            results()
            print("Computer has won")
        elif computer == "paper":
            results()
            print("The player has won")
    elif player == "paper":
        if computer == "scissors":
            results()
            print("Computer has won")
        elif computer == "rock":
            results()
            print("player has won")

    play_again = input("play again? yes/ no: ").lower()
    if play_again != "yes":
        break
print("Bye")


 


# --------------------------------
# a quiz game


"""def new_game():

    guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print("--------------------------------" )
        print(key)
        for row in options[question_num-1]:
            print(row)
        guess = input("Enter (A, B, C, or D)").upper()
        guesses.append(guess)

        correct_guess += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guess, guesses)
# --------------------------------


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!!")
        return 1
    else:
        print("WRONG!!")
        return 0


# --------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("RESULTS")
    print("--------------------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(f"Your score is: {score} %")
# --------------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# --------------------------------


# a dictionary to hold the question and the correct answer
questions = {
    "Who created Python?": "A",
    "What year was python created?": "B",
    "Python is tributed to which comedy group?": "C",
    "Is the earth round?": "A"
}

# answers in a 2d list
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2008"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. Snl"],
           ["A. True", "B. False", "C. sometimes", "D. Not sure"]]


new_game()

while play_again():
    new_game()
print("Byee..it was nice seeing you play")"""



