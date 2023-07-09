import gspread
import os
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

# Get a dictionary of all questions, answer options & correct answers
data = SHEET.worksheet("questions_and_answers")
questions_dict = data.get_all_records()

# Unpack the dictionary to access the questions, answer options & correct answers
for x in questions_dict: 
    question = x['question']
    option_a = x['option_a']
    option_b = x['option_b']
    option_c = x['option_c']
    option_d = x['option_d']
    correct_answer = x['correct_answer']


def get_username():
    print("Greetings, Hylian!\n")
    try:
        username = input("Please enter your name: \n")
    except ValueError as e:
        print(f"Invalid input: {e}, please enter a name between 2-10 characters long.")
    if len(username) < 2 and len(username) > 10:
        raise ValueError(
            "Invalid input. Please enter a name between 2-10 characters long."
            )


    print(f"Welcome, {username}!\n")

def load_main_menu():
    menu_choice = 0
    print("Please select one of the following options:\n")
    print("1. Start Quiz")
    print("2. Scoreboard")
    print("3. Exit Quiz")
    while True:
        try:
            menu_choice = int(input("Enter your choice (1-3): "))
        except ValueError as e:
            print(f"Invalid input: {e} Please enter a number between 1-3.")
            continue
        if menu_choice >= 1 and menu_choice <= 3:
            if menu_choice == 1:
                run_quiz()
                break
            elif menu_choice == 2:
                print("Load scoreboard (placeholder)")
                break
            elif menu_choice == 3:
                print("Exiting...")
                break
        else:
            print("Invalid input. Please enter a number between 1-3.")



def run_quiz():
    clear_terminal()
    for key, value in x.items():
       print(question)
       print('a.', option_a)
       print('b.', option_b)
       print('c.', option_c)
       print('d.', option_d)
       user_answer = input("Your answer: ")


def clear_terminal():
    os.system('clear')


def main():
    get_username()
    load_main_menu()

main()