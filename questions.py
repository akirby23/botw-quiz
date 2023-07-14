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

QUIZ_QUESTIONS = {
    question_list[0]: correct_option_list[0],
    question_list[1]: correct_option_list[1],
    question_list[2]: correct_option_list[2],
    question_list[3]: correct_option_list[3],
    question_list[4]: correct_option_list[4],
    question_list[5]: correct_option_list[5],
    question_list[6]: correct_option_list[6],
    question_list[7]: correct_option_list[7],
    question_list[8]: correct_option_list[8],
    question_list[9]: correct_option_list[9],
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