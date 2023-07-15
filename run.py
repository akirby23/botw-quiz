import gspread
import os
import tabulate
import time
import sys
import colorama
colorama.init(autoreset = True)
from colorama import init, Fore, Style
from google.oauth2.service_account import Credentials
from art import logo, main_menu, scoreboard, instructions, triforce
from questions import QUIZ_QUESTIONS, QUIZ_ANSWERS

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('botw_quiz')


# Get a list of dictionaries containing the user's names and scores
scores = SHEET.worksheet("scoreboard")
scores_dict = scores.get_all_records()

# Quiz variables 
username = ""
score = 0
questions_answered = 0


def load_title_screen():
    """
    Prints the logo to the terminal. 
    Automatically loads the main menu after 5 seconds.
    """
    print(Fore.YELLOW + Style.DIM + logo)
    print()
    print()
    text = "Loading..."
    centered_text = text.center(40)
    slow_print(centered_text)
    time.sleep(5)
    clear_terminal()
    get_username()


def get_username():
    """
    Prompts the user to enter their name. 
    Throws a ValueError if the name is less than 2 characters or more than 10 characters
    """
    slow_print("Greetings, Hylian!\n")
    while True:
        try:
            global username
            username = input("Please enter your name: \n").capitalize()
            if len(username) < 2 or len(username) > 10:
                raise ValueError("Username needs to be between 2 and 10 characters.")
            else:
                clear_terminal()
                print(f"Welcome, {username}!\n")
                time.sleep(3)
                load_main_menu()
                break
        except ValueError as e:
            print(f"Invalid input: {e} Please try again.")
    

def load_main_menu():
    """
    Loads the main menu, allowing the user to start the game, view the
    scoreboard or exit the game.
    Throws a ValueError if the user submits a value that is not 1, 2 or 3.  
    """
    clear_terminal()
    print(main_menu)
    slow_print("Please select one of the following options:\n")
    slow_print("1. Start Quiz")
    slow_print("2. Scoreboard")
    slow_print("3. Exit Quiz\n")
    while True:
        try:
            menu_choice = int(input("Enter your choice (1-3): "))
            if menu_choice == 1:
                start_quiz()
                break
            elif menu_choice == 2:
                load_scoreboard()
                break
            elif menu_choice == 3:
                exit_quiz()
                break
            else:
                raise ValueError("Please enter a number between 1-3.")
        except ValueError as e:
            print(f"Invalid input: {e}")
                  

def start_quiz():
    """
    Prints the quiz instructions to the terminal. 
    Prompts the user to confirm whether or not they are ready to proceed with the
    quiz. 
    Throws a ValueError if the user enters a value that is not 'Y' or 'N'
    """
    clear_terminal()
    print(instructions)
    print("This multiple-choice quiz will test your knowledge on the iconic action-adventure game The Legend of Zelda: Breath of the Wild.\n")
    print("1. There are 10 questions in total. Each question will have 4 potential answers.")
    print("2. To choose your answer, type the corresponding letter (a, b, c, d) for the option you believe to be correct and click enter.")
    print("3. You can choose one option per question. Once you submit your answer, you cannot change it.")
    print("4. You will earn 1 point for each correct answer.")
    print("5. Once you have answered all 10 questions, your final score will be revealed.\n")
    print("Important note: This quiz may contain spoilers relating to the gameplay & storyline of The Legend of Zelda: Breath of the Wild. If you want to experience the game without spoilers, it may be best to avoid the quiz for now.\n")
    slow_print("Are you ready to prove yourself as a hero of Hyrule?")
    slow_print("Y - Start Quiz")
    slow_print("N - Return to Main Menu\n")
    while True:
        try:
            user_input = input("Enter your choice (Y/N): ").capitalize()
            if user_input == "Y":
                clear_terminal()
                run_quiz()
                break
            elif user_input == "N":
                clear_terminal()
                load_main_menu()
                break
            else:
                raise ValueError("'Y' or 'N' required")
                continue
        except ValueError as e:
            print(f"Invalid input: {e}, please try again.")
        

def run_quiz():
    """
    Loops through the questions stored in QUIZ_QUESTIONS and answers stored in 
    QUIZ_ANSWERS and prints them to the terminal. 
    The user is prompted to enter 'A', 'B', 'C' or 'D' to select their answer. 
    If the user enters a value other than the values above, a ValueError will be thrown.
    Answers are checked. 
    'score' is incremented for every correct answer submitted by the user. 
    'questions_answer' is incremented for every question answered.
    The quiz will finish once all 10 questions have been answered.
    """
    global score
    global questions_answered
    clear_terminal()
    for (q, a), ans in zip(QUIZ_QUESTIONS.items(), QUIZ_ANSWERS):
        correct_answer = a
        slow_print(q)
        print(*ans, sep="\n")
        user_answer = input("Your answer: ").capitalize()
        if user_answer == correct_answer:
            print(Fore.GREEN + "Correct!")
            score += 1
            questions_answered += 1
            continue
        else:
            print(Fore.RED + f"Not quite! The correct answer was option: {a}.")
            questions_answered += 1
            continue
    while questions_answered == 10:
        finish_quiz()
        break


def finish_quiz():
    """
    Congratulations/commiserations given depending on the user's score. 
    Username and final scores are updated on the scoreboard worksheet. 
    User is prompted to confirm whether or not they want to play again.
    """
    global score
    global questions_answered
    clear_terminal()
    if score == 10:
        slow_print(f"Congratulations, {username}! You have well and truly proven yourself as a hero of Hyrule!\n")
        slow_print(f"Your final score is: {score}.\n")
        update_scoreboard()
        time.sleep(3)
        clear_terminal()
        play_again()
    elif score >= 7:
        slow_print(f"Well done, {username}! You are well on your way to proving yourself as a hero of Hyrule.\n")
        slow_print(f"Your final score is: {score}.\n")
        update_scoreboard()
        time.sleep(3)
        clear_terminal()
        play_again()
    elif score >= 5:
        slow_print(f"Not bad, {username}. With a little more exploration you will be well on your way to proving yourself as a hero of Hyrule!\n")
        slow_print(f"Your final score is: {score}.\n")
        update_scoreboard()
        time.sleep(3)
        clear_terminal()
        play_again()
    elif score < 5:
        slow_print(f"Thank you for playing, {username}.\n")
        slow_print(f"Your final score is: {score}.\n")
        slow_print("We hope that you see this as an opportunity to delve deeper into the vast kingdom of Hyrule!\n")
        update_scoreboard()
        time.sleep(3)
        clear_terminal()
        play_again()

def load_scoreboard():
    """
    Print user names & scores in the form of a table
    Written with the help of Stack Overflow
    """
    clear_terminal()
    print(scoreboard)
    header = scores_dict[0].keys()
    rows = [y.values() for y in scores_dict]
    print(tabulate.tabulate(rows, header, tablefmt='rst'))
    while True:
        try:
            user_input = input("Enter 'Q' to return to the main menu: ")
            if user_input != "q":
                raise ValueError("'Q' needs to be entered to return to the main menu")
                continue
            else:
                clear_terminal()
                load_main_menu() 
                break
        except ValueError as e:
            print(f"Invalid input: {e}, please try again.")


def update_scoreboard():
    """
    Appends the username & final score to the scoreboard worksheet.
    """
    slow_print("Updating scoreboard...")
    global username
    global score
    scoreboard_data = (username, score)
    scores.append_row(scoreboard_data)
    slow_print("Scoreboard updated.")


def reset_quiz():
    """
    Sets the score & questions_answered variables back to 0
    """
    global score
    global questions_answered
    score = 0
    questions_answered = 0


def play_again():
    """
    Prompts the user to confirm whether or not they want to play again. 
    If they do want to play again, the game will be reset and the quiz will run again. 
    If they don't want to play again, they will be redirected to the title screen. 
    A ValueError will be thrown if the user enters a value that is not 'Y' or 'N'. 
    """
    slow_print("Would you like to play again?\n")
    slow_print("Y - Play again")
    slow_print("N - Exit quiz\n")
    while True:
        try:
            user_input = input("Enter your choice (Y/N): ").capitalize()
            if user_input == "Y":
                clear_terminal()
                print("Restarting quiz...")
                reset_quiz()
                run_quiz()
                break
            elif user_input == "N":
                clear_terminal()
                exit_quiz()
                break
            else:
                raise ValueError("Please select 'Y' or 'N' to continue.")
        except ValueError as e:
            print(f"Invalid input: {e}")
      
        
def clear_terminal():
    """
    Clears the terminal
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def slow_print(s): 
    """
    Prints each character at a speed of 0.04s. 
    Code borrowed from gnuton on GitHub. 
    Link to the source code within the Credits section of the README file.
    """ 
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)


def exit_quiz():
    clear_terminal()
    print(Fore.YELLOW + Style.DIM + triforce)
    slow_print(f"Thank you for playing, {username}!\n")
    slow_print("Exiting quiz...\n")
    time.sleep(1)
    slow_print("Click 'Run Quiz' to play again.")



def main():
    """
    Runs the main functions
    """
    load_title_screen()

main()

