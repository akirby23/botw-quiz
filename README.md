# The Legend of Zelda: Breath of the Wild Quiz

## Description 

Welcome to botw-quiz, a Python terminal-based multiple choice quiz inspired by the iconic Nintendo Switch game, The Legend of Zelda: Breath of the Wild!

[Deployed app on Heroku](https://botw-quiz-259e8e0dd0c5.herokuapp.com/)

![Breath of the Wild Quiz app - title screen](documentation/readme/design/botw-quiz-title-screen.PNG)

## How to play

The quiz itself consists of 10 questions in total based on the lore & gameplay mechanics of The Legend of Zelda: Breath of the Wild. 

The user will have a choice of 4 answers for each question. 

Each correct answer equates to 1 point toward the final score.

Once all 10 questions have been answered, the final score will be provided to the user, and the user’s name & final score will be added to the scoreboard, which can be accessed via the main menu. 

## Features

### Existing Features

#### Title Screen

![Breath of the Wild Quiz - Title Screen](documentation/readme/design/features/title-screen.gif)

- Once the program starts, the user is greeted with the Legend of Zelda: Breath of the Wild Quiz ASCII art logo printed to the terminal. 
- The title screen is set up to automatically clear the terminal & prompt the user to enter their name after 5 seconds. 

#### Username Input

![Username Input](documentation/readme/design/features/username.gif)

- The user is greeted before being prompted to enter their name. 
- The input field is set up to only accept names that are between 2-10 characters long. 
- An exception will be thrown if the username does not meet the requirement above. 
- Otherwise, the username will be updated to the global variable. 
- A welcome message will be printed to the terminal including the user's name before the main menu loads. 


#### Main Menu

![Main Menu](documentation/readme/design/features/main-menu.PNG)

- The main menu title is printed to the terminal in ASCII text for an authentic game feel. 
- The user is given 3 options: 
    - Start Quiz
        - If the user selects this option, they will be taken to the quiz [instructions](#instructions-page) page.
    - Scoreboard
        - If the user selects this option, they will be taken to the [scoreboard page](#scoreboard-page). 
    - Exit Quiz
        ![Exit Quiz](documentation/readme/design/features/exit-quiz.gif)
        If the user selects this option, the Triforce crest will be printed to the terminal, followed by a thank you message. The user will be prompted to click on "RUN QUIZ" at the top of the terminal to run the program again before it stops running. 

![Main Menu Exception](documentation/readme/design/features/main-menu-exception.gif)
- A ValueError will be thrown if the user enters a blank value or any value that is not 1, 2 or 3 & the user will be prompted to try again. 

#### Scoreboard Page

![Scoreboard (contains a table containing user's that have taken the quiz & their respective scores)](documentation/readme/design/features/scoreboard.PNG)

- The scoreboard title is printed to the terminal in ASCII text for an authentic game feel. 
- A table is printed to the terminal containing two columns: name & score. 
- The table data is stored within a [Google Sheet](https://docs.google.com/spreadsheets/d/1nyocvizezU-y-m0PedQcAAGDziM1yjVJAMwC1k_DBCg/edit#gid=0). 
- Every time a user completes the quiz, their name & final score are automatically appended to the relevant columns in the Google Sheet and will be displayed on this page so they can check back on them and potentially compete with friends.  
- The user can return to the main menu by entering "Q". 
![Scoreboard ValueError](documentation/readme/design/features/load-scoreboard-exception.gif)
- A ValueError will be thrown if the user enters a value other than "Q" & the user will be prompted to try again. 

#### Instructions Page

![Instructions Page](documentation/readme/design/features/instructions.PNG)

- The title is printed to the terminal in ASCII text for an authentic game feel. 
- A list of game instructions are printed to the terminal so that the user knows what to expect once they start the quiz. 
- A spoiler warning is printed to the terminal. 
- The user is prompted to confirm if they want to start the quiz or return to the main menu, allowing them to return to the main menu if they do not want to proceed or if they are not okay with spoilers.  
![Instructions page ValueError](documentation/readme/design/features/instructions-page-exceptions.gif)
- A ValueError is thrown if the user enters a value that is not "Y" or "N" & the user will be prompted to try again.  

#### Quiz
- Once the user selects "Y" on the Instructions page, the quiz will run. 
![Quiz - first question](documentation/readme/design/features/quiz.PNG)
- The questions and answers are stored within the [Google Sheet](https://docs.google.com/spreadsheets/d/1nyocvizezU-y-m0PedQcAAGDziM1yjVJAMwC1k_DBCg/edit#gid=0) which is linked to the program.
- The questions & correct answers are stored within a list of dictionaries that access the worksheet's values. The answer options are stored within a list of lists that also accesses the the worksheet's values. 
- By accessing the quiz data via the worksheet, we allow for the questions & answers to be updated without the need to change the code, as long as the number of questions remains the same. 
- The program loops through the quiz questions & answer options and prints them to the terminal. 
![Quiz checking answers](documentation/readme/design/features/quiz-correct-incorrect-answers.gif)
- A message is printed in green if the user selects the correct answer, or in red if the user selects the incorrect answer. 
- The next question will load 2 seconds after the user gets feedback on the answer they submitted. 
- Once all 10 questions have been answered, the quiz will automatically end and the final score will be presented to the user. 
- Feedback is given based on the number of questions answered correctly: 
    - 10 correct answers
    ![Feedback to the user when 10 questions have been answered correctly](documentation/readme/design/features/10-finish-quiz.gif)
    - 7-9 correct answers
    ![Feedback to the user when 7-9 questions have been answered correctly](documentation/readme/design/features/7-9-finish-quiz.gif)
    - 5-6 correct answers
    ![Feedback to the user when 5-6 questions have been answered correctly](documentation/readme/design/features/5-6-finish-quiz.gif)
    - 0-4 correct answer
    ![Feedback to the user when 0-4 questions have been answered correctly](documentation/readme/design/features/0-4-finish-quiz.gif)
- The user is then given the option to play again if they want or to exit the quiz. 
![Play again screen](documentation/readme/design/features/play-again.PNG)
    - If the user opts to play again, the score & questions answered variables will be reset to allow them to attempt to beat their score if they weren't happy with it. 
    - Otherwise, they can exit the quiz program.
- A ValueError is thrown if the users enters a value that is not "Y" or "N" & the user will be prompted to try again. 

#### General Features

- Slow-printing text is featured throughout the program for better readability. 
- The terminal is cleared between functions & questions answered to keep it clean and free from information overload. 
- The execution of certain code throughout the program is delayed to visually inform the user that actions are being taken. 
- User input fields are set up to automatically capitalize the user's response to ensure that commands are executed regardless of whether or not they are entered in uppercase or lowercase fonts. 

### Future Features

- Expand the quiz by introducing sets of questions for other Legend of Zelda games. Allow the user to select which game they would like the quiz to be based on. 
- Randomize the questions for an added challenge if the user opts to play again. 
- Add a time limit to each question to add a competetive aspect to the quiz.
- Add an option for the user to exit the quiz while it is running.  

## Design

### Flowchart 

![Breath of the Wild Quiz - flowchart](documentation/readme/design/botw_quiz_flowchart.png)

The flowchart above was created during the planning phase of the project. 
A few aspects were changed during the production of the quiz. 

- Instead of prompting the user to click "Enter" to proceed on the title screen, the user is now automatically directed to the main menu 5 seconds after the program starts running. 
    - I felt that it would negatively impact the user experience if an error was thrown if the user happened to press a key that is not "Enter". 
- The username is now appended to the scoreboard at the end of the quiz, rather than at the start. 
    - This was done to ensure that there would be no blank scores next to any of the names on the scoreboard. 
- The user now has the option to play again or exit the quiz once all questions have been answered. 

### Colours

#### ANSI colours

ANSI colours were imported from the colorama library.

- Yellow: used for aesthetic purposes to print the quiz logo & triforce ASCII art.
- Green: used to provide visual feedback to the user when they select a correct answer.
- Red: used to provide visual feedback to the user when they select an incorrect answer.

#### HEX colours

Slight modifications were made to the Code Institute Mock Terminal for aesthetic purposes & to match the theme of the quiz. 

![Breath of the Wild Quiz - Colour palette](documentation/readme/design/botw-colour-palette.png)
- #d9dec5: Used as a fallback background colour. 
- #94aba2: Used as a border colour for the "RUN QUIZ" button to add contrast.
- #638139: Used to colour the "RUN QUIZ" button. 

The colour palette was generated from the background image below. 


### Imagery

![Breath of the Wild Quiz - background image](documentation/readme/design/botw-background-image.png)

The image above, featuring a glimpse of the vast kingdom of Hyrule, was added as a background image to compliment the theme of the quiz. 

## Technologies Used

### Languages

- Python was used to program the quiz.
- HTML & CSS were used to make adjustments to the Code Institute mock terminal for Heroku.

### Frameworks, Libraries & Programs

- [CodeAnywhere](https://app.codeanywhere.com/): to write the code.
- [Git](https://git-scm.com/): to commit & push the code to GitHub for version control.
- [GitHub](https://github.com/): to store the code in its repository.
- [Heroku](https://id.heroku.com/login): to deploy the app.
- [Imgur](https://imgur.com/): to host the background image. 
- [ImageColorPicker](https://imagecolorpicker.com/en): used to generate colours from the background image for the “RUN QUIZ” button.
- [gspread](https://docs.gspread.org/en/v5.10.0/): to access & manipulate the data stored in the [botw-quiz](https://docs.google.com/spreadsheets/d/1nyocvizezU-y-m0PedQcAAGDziM1yjVJAMwC1k_DBCg/edit#gid=0) Google Sheet.
- [os](https://docs.python.org/3/library/os.html): to create a function that clears the terminal once the function is called for better readability.
- [tabulate](https://pypi.org/project/tabulate/): to print the scoreboard data to the terminal in a table format for aesthetic and readability purposes. 
- [time](https://docs.python.org/3/library/time.html): to delay functions/actions from being executed to prevent the user from being overloaded with information.
- [sys](https://docs.python.org/3/library/sys.html): to allow for text to be printed slowly once the slow_print() function is called. For better readability & to emulate updates within the program. 
- [colorama](https://pypi.org/project/colorama/): to print coloured text to the terminal for aesthetic purposes and to enhance the visual feedback once questions are answered correctly/incorrectly. 
- [LucidChart](https://www.lucidchart.com/pages/): to create the flowchart. 
- [coolors](https://coolors.co/): to create the colour pallette for the README. 

## Testing

The testing details are documented within the [TESTING.md](TESTING.md) file. 

## Deployment

This project was deployed to Heroku using Code Institute's mock terminal.

- Steps for deployment: 
    - Fork or clone this repository.
    - Create a new Heroku app.
    - Set a buildback to Python and NodeJS in that order.
    - Set another buildback to Port and 8000.
    - Link the Heroku app to the repository.
    - Click on “Deploy”.

## Credits

### Code

- [Stack Overflow](https://stackoverflow.com/questions/40056747/print-a-list-of-dictionaries-in-table-form) was consulted for guidance on how to print the scoreboard data to the terminal in the form of a table using Tabulate.
- Credit to [gnuton](https://gist.github.com/gnuton/3c7a46447d2be0aee0b2) on GitHub for the code within the "slow_print()" function.
- [Fsymbols](https://fsymbols.com/generators/carty/) was used to generate the ASCII text for the Main Menu, Scoreboard & Instructions pages.
- [Python Pool](https://www.pythonpool.com/python-colorama/) was consulted for guidance on how to print coloured text to the terminal using Colorama.
- The “logo” ASCII art was obtained from [asciiart.eu](https://www.asciiart.eu/video-games/zelda) & modified by me to fit the terminal.
- The “triforce” ASCII art was obtained from [emojicombos.com](https://emojicombos.com/legend-of-zelda-ascii-art).
- The code within the “clear_terminal()” function was provided by my mentor, Derek McAuley. 

### Media

- The background image was sourced from [Imgur](https://imgur.com/xs0uO5R).

### Content

- The quiz questions & answers were written by me, based on the Nintendo Switch game The Legend of Zelda: Breath of the Wild. 
- [wikipedia.org](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Breath_of_the_Wild) & [zelda.fandom.com](https://zelda.fandom.com/wiki/The_Legend_of_Zelda:_Breath_of_the_Wildhttps://zelda.fandom.com/wiki/The_Legend_of_Zelda:_Breath_of_the_Wild) were consulted for inspiration for the questions & answers.

### Acknowledgements

- Special thanks to my mentor Derek McAuley for his support with the project, particularly with helping me to troubleshoot an issue I was having with deployment  and for providing guidance on throwing exceptions and printing ASCII art to the terminal for a more visually appealing program. Derek also provided me with code to clear the terminal, which is compatible on multiple operating systems. 
- I would also like to thank Oisin from the tutor support team for helping me to troubleshoot an issue I had with iterating through the questions & answers for the quiz. 