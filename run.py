import gspread
import os
import tabulate
from google.oauth2.service_account import Credentials
from art import logo

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('botw_quiz')

# Get a list of dictionaries for all questions
questions_data = SHEET.worksheet("questions")
questions_dict = questions_data.get_all_records()

# Get a list of dictionaries for all answers
answers_data = SHEET.worksheet("answers")
answers_dict = answers_data.get_all_records()

# Get a list of dictionaries for all correct answers
correct_answers_data = SHEET.worksheet("correct_answers")
correct_answers_dict = correct_answers_data.get_all_records()

question_number_list = []
question_list = []
option_a_list = []
option_b_list = []
option_c_list = []
option_d_list = []
correct_option_list = []
correct_answer_list = []

# Unpack the dictionary of questions to access the values of the question numbers & questions
for questions in questions_dict:
    question_number = questions['question_number']
    question = questions['question']
    question_number_list.append(question_number)
    question_list.append(question)
# Unpack the dictionary of answers to access the values of options a, b, c & d
for answers in answers_dict:
    option_a = answers['option_a']
    option_b = answers['option_b']
    option_c = answers['option_c']
    option_d = answers['option_d']
    option_a_list.append(option_a)
    option_b_list.append(option_b)
    option_c_list.append(option_c)
    option_d_list.append(option_d)

# Unpack the dictionary of correct answers to access the values of the correct option & correct answer
for correct_answers in correct_answers_dict:
    correct_option = correct_answers['correct_option']
    correct_answer = correct_answers['correct_answer']
    correct_option_list.append(correct_option)
    correct_answer_list.append(correct_answer)


# Get a list of dictionaries containing the user's names and scores
scores = SHEET.worksheet("scoreboard")
scores_dict = scores.get_all_records()

# Quiz variables 
username = ""
score = 0
questions_answered = 0

QUIZ_QUESTIONS = {
    question_list[0]: "B",
    question_list[1]: "A",
    question_list[2]: "D",
    question_list[3]: "A",
    question_list[4]: "C",
    question_list[5]: "B",
    question_list[6]: "D",
    question_list[7]: "B",
    question_list[8]: "A",
    question_list[9]: "C",
}

QUIZ_ANSWERS = [
    [option_a_list[0], option_b_list[0], option_c_list[0], option_d_list[0]],
    [option_a_list[1], option_b_list[1], option_c_list[1], option_d_list[1]],
    [option_a_list[2], option_b_list[2], option_c_list[2], option_d_list[2]],
    [option_a_list[3], option_b_list[3], option_c_list[3], option_d_list[3]],
    [option_a_list[4], option_b_list[4], option_c_list[4], option_d_list[4]],
    [option_a_list[5], option_b_list[5], option_c_list[5], option_d_list[5]],
    [option_a_list[6], option_b_list[6], option_c_list[6], option_d_list[6]],
    [option_a_list[7], option_b_list[7], option_c_list[7], option_d_list[7]],
    [option_a_list[8], option_b_list[8], option_c_list[8], option_d_list[8]],
    [option_a_list[9], option_b_list[9], option_c_list[9], option_d_list[9]],
]

def load_title_screen():
    print(logo)
    title_screen_input = input("Press ENTER to begin")
    if title_screen_input == "":
        clear_terminal()
        get_username()


def get_username():
    print("Greetings, Hylian!\n")
    while True:
        try:
            global username
            username = input("Please enter your name: \n").capitalize()
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
                raise ValueError("Please enter a number between 1-3.")
        except ValueError as e:
            print(f"Invalid input: {e}")
                  

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
    global score
    global questions_answered
    clear_terminal()
    for load_questions in QUIZ_QUESTIONS:
        print(load_questions)
        for load_answers in QUIZ_ANSWERS:
            print(*load_answers, sep="\n")
            user_answer = input("Your answer: ")
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
                questions_answered += 1
                continue
            else:
                print(f"Not quite! The correct answer was {correct_option}: {correct_answer}.")
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
        
        
def clear_terminal():
    os.system('clear')


def main():
    load_title_screen()
    load_main_menu()

main()
