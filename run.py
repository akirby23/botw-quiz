import gspread
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

def get_username():
    print("Greetings, Hylian!\n")

    username = input("Please enter your name: \n")

    print(f"Welcome, {username}!\n")

def load_main_menu():
    print("Please select one of the following options:\n")
    print("1. Start Quiz")
    print("2. Scoreboard")
    print("3. Exit Quiz")
    menu_choice = input("Enter your choice (1-3): ")

data = SHEET.worksheet("questions_and_answers")
questions_dict = data.get_all_records()

for x in questions_dict: 
    question = x['question']
    option_a = x['option_a']
    option_b = x['option_b']
    option_c = x['option_c']
    option_d = x['option_d']
    correct_answer = x['correct_answer']

def run_quiz():
    print(question)
    print(option_a)
    print(option_b)
    print(option_c)
    print(option_d)
    user_answer = input("Your answer: ")

run_quiz()

