import gspread
import os
import tabulate
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('botw_quiz')

# Get a list of dictionaries for all questions, answer options & correct answers
data = SHEET.worksheet("questions_and_answers")
questions_dict = data.get_all_records()

# Unpack the list of dictionaries to access the questions, answer options & correct answers
for x in questions_dict: 
    question_number = x['question_number']
    question = x['question']
    option_a = x['option_a']
    option_b = x['option_b']
    option_c = x['option_c']
    option_d = x['option_d']
    correct_answer = x['correct_answer']


# Get a list of dictionaries containing the user's names and scores
scores = SHEET.worksheet("scoreboard")
scores_dict = scores.get_all_records()


def get_username():
    print("Greetings, Hylian!\n")
    while True:
        try:
            username = input("Please enter your name: \n")
            if len(username) < 2 or len(username) > 10:
                raise ValueError("Username needs to be between 2 and 10 characters.")
            else: 
                print(f"Welcome, {username}!\n")
                break
        except ValueError as e:
            print(f"Invalid input: {e} Please try again.")
    

def load_main_menu():
    print("Please select one of the following options:\n")
    print("1. Start Quiz")
    print("2. Scoreboard")
    print("3. Exit Quiz\n")
    while True:
        try:
            menu_choice = int(input("Enter your choice (1-3): "))
        except ValueError as e:
            print(f"Invalid input: {e} Please enter a number between 1-3.")
            continue
        if menu_choice >= 1 and menu_choice <= 3:
            if menu_choice == 1:
                start_quiz()
                break
            elif menu_choice == 2:
                load_scoreboard()
                break
            elif menu_choice == 3:
                print("Exiting...")
                break
        else:
            print("Invalid input. Please enter a number between 1-3.")


def start_quiz():
    clear_terminal()
    print("This multiple-choice quiz will test your knowledge on the iconic action-adventure game The Legend of Zelda: Breath of the Wild.\n")
    print("Instructions:\n")
    print("1. There are 10 questions in total. Each question will have 4 potential answers.")
    print("2. To choose your answer, type the corresponding letter (a, b, c, d) for the option you believe to be correct and click enter.")
    print("3. You can choose one option per question. Once you submit your answer, you cannot change it.")
    print("4. You will earn 1 point for each correct answer.")
    print("5. Once you have answered all 10 questions, your final score will be revealed.\n")
    print("Important note: This quiz may contain spoilers relating to the gameplay & storyline of The Legend of Zelda: Breath of the Wild. If you want to experience the game without spoilers, it may be best to avoid the quiz for now.\n")
    print("Are you ready to prove yourself as a hero of Hyrule?")
    print("y - Start Quiz")
    print("n - Return to Main Menu\n")
    while True:
        try:
            user_input = input("Enter your choice (y/n): ")
            if user_input == "y":
                clear_terminal()
                run_quiz()
                break
            elif user_input == "n":
                clear_terminal()
                load_main_menu()
                break
            else:
                raise ValueError
                continue
        except ValueError as e:
            print(f"Invalid input: {e}, please enter 'y' or 'n'.")
        

def run_quiz():
    score = 0
    questions_answered = 0
    clear_terminal()
    while len(questions_dict) <= 10:
        print(question_number, question)
        print(option_a)
        print(option_b)
        print(option_c)
        print(option_d)
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
            questions_answered += 1
            continue
        else:
            print(f"Not quite! The correct option was {correct_answer}.")
            questions_answered += 1
            continue


def load_scoreboard():
    """
    Print user names & scores in the form of a table
    Written with the help of Stack Overflow
    """
    clear_terminal()
    header = scores_dict[0].keys()
    rows = [y.values() for y in scores_dict]
    print(tabulate.tabulate(rows, header, tablefmt='rst'))
    while True:
        try:
            user_input = input("Enter 'q' to return to the main menu: ")
            if user_input != "q":
                raise ValueError
                continue
            else:
                clear_terminal()
                load_main_menu() 
                break
        except ValueError as e:
            print(f"Invalid input: {e}, please enter 'q' to return to the main menu.")
        
        
def clear_terminal():
    os.system('clear')


def main():
    get_username()
    load_main_menu()

main()
