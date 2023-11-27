import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from UI_MainWindow import Ui_mainWindow
from PyQt5 import  QtMultimedia
import random



# From the mainline project
def errorcheck(word):
        if len(word) <= 8 and len(word) >= 1:
            if word.isalpha():
                return True
            else:
                return_message = "Ensure your input contains no spaces, numbers, or symbols"
                return return_message
        
        if len(word) > 8:
            return_message = "Ensure your input is less than or equal to 8 characters"
            return return_message

# Defines the length of the correct list displayed to the user
def initialisation(hword):
    global correct
    correct = []
    for i in range(len(hword)):
        correct.append("*")

# Error checking Module
def guess_checker(guess, hword):
    hword_list = []
    guess_list = []

#Changes guess and hword to lowercase
    hword = hword.lower()
    guess = guess.lower()

#if the hidden word is the same as the guess
#returns the value 'True'  
    if hword == guess:
            return True

# Add each letter of the hidden word to the hidden word list
    for i in hword:
        hword_list.append(i)

# Add each letters of the guess to the guess list
    for i in guess:
        guess_list.append(i)

# Adds the * character to the correct list as many times as the length of the hidden word list    
# for each letter in the guess list
# if that letter is in the hidden word list
# Find the index of the letter in the hidden word list
# Add letter to the correct list at specific index
# Change the value of that letter in hidden word list to '@' so same index is not given for duplicate letters
        
    for i in guess_list:
        if i in hword_list:
            index = hword_list.index(i)
            correct[index] = i
            hword_list[index] = "@"

    # Compares the contents of the correct list as a string to the string variable hword
    correct_string = ''.join([str(item) for item in correct])    
    if hword == correct_string:
        return True


    return correct

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.intro_screen)

        # Button for selecting mode
        self.ui.intro_submit_btn.clicked.connect(self.mode)

        self.counter = 10 # declaring a global counter variable used later in the code.

        self.ui.word_submit_btn.clicked.connect(self.hword_input)
        self.ui.guess_submit_btn.clicked.connect(self.guess_input)
        
        #Calls function if enter key is pressed instead of the submit button
        self.ui.word_input.returnPressed.connect(self.hword_input)
        self.ui.user_input.returnPressed.connect(self.guess_input)
        
        #Setting the game_time global variable to 60.
        self.game_time = 60
        # Creating a QT timer object and connecting it to a function called interval_complete when it runs out.
        self.timer = QTimer()
        self.timer.timeout.connect(self.interval_complete)
    
    # Function for 1 or 2 player
    # Creates word_array filled with random words less than 8 characters without numbers or symbols.
    # Generates a random number from 0 to the length of the word_array
    # Uses this random number as the index for the word_array, which then is assigned to the hidden word variable 'hword'.
    # Changes the current window the guessing screen
    # Starts the timer for to loop every second
    def mode(self):
        if self.ui.one_player_btn.isChecked():
            word_array = ('clapped','slapped','feet', 'bear', 'smacked', 'clown', 'midget', 'hands', 'random', 'alien', 'absolute', 'mountain', 'word', 'sentence', 'agony', 'death', 'nitrogen', 'fast', 'dylan')
            index = random.randint(0,(len(word_array)-1))
            self.hword = (word_array[index])
            print (self.hword) #TESTING PRINT STATEMENT
            bkmus.stop()
            game_music.play()
            self.ui.stackedWidget.setCurrentWidget(self.ui.guess_screen)
            self.timer.start(1000)
            
            #Creates correct list
            hword = self.hword
            initialisation(hword)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.input_screen)
    
    def show(self):
        self.main_win.show()

    # Once the timer runs out
    # If the remaining time is greater than 0
    # reduce self.game_time variable by one
    # Display that variable to the timer label with the appropriate CSS.
    def interval_complete(self):
        if self.game_time > 0:
            self.game_time = self.game_time - 1
            self.ui.time_lbl.setText("<html><head/><body><p><span style='color:#ffffff;'>"+str(self.game_time)+"</span></p></body></html>")
        else:
            self.timer.stop()
            game_music.stop()
            losemus.play()
            hword = self.hword
            self.ui.stackedWidget.setCurrentWidget(self.ui.lose_screen)
            self.ui.lose_lbl.setText("Out of time LOSER, the word was: " + hword)
            
    # function for when the hword input button is clicked
    # stores the plain text of the user hidden word input into variable hword
    # runs the errorcheck function with the hword
    # if the result returns true, then the user gains  access the next screen
    # else the user receives the appropriate error message provided by the errorcheck function
    def hword_input(self):
        self.hword = self.ui.word_input.text() #global variable hword that can be referenced in a different function
        hword = self.hword 
        error_check_result = errorcheck(hword)
        if error_check_result is True:
            bkmus.stop()
            game_music.play()
            self.ui.stackedWidget.setCurrentWidget(self.ui.guess_screen)
            #This timer runs out every second, allowing us to decrease the value of the timer on screen every second.
            self.timer.start(1000) #starts the timer to run for 1 second after hidden word is inputted.

            initialisation(hword) # Creates correct list used for comparison
            
        else:
            self.ui.input_error_lbl.setText(error_check_result)

    # Function for comparing the guess to the hidden word
    # Clears the error label of any previous messages
    # stores the value of both the guess and the hidden word into string variables.
    # Calls error check function on the user guess
    # If the error check function is true
    # reduce the value of the counter by 1
    # Calls the guess checking function with the user guess and hidden word as parameters
    # If the user gusssed correctly, change the win flag to true.
    # else changes the user hint label to whatever mutual letters they've revealed.
    # else provides the appropriate error message to the user.
    # Display the value of the counter variable
    def guess_input(self):
        self.ui.guess_error_lbl.setText("")
        guess = self.ui.user_input.text()
        hword = self.hword
        error_check_result = errorcheck(guess)

        if self.counter > 0 and self.game_time > 0:
            if error_check_result is True:
                self.counter = self.counter - 1
                comparison = guess_checker(guess, hword)
                if comparison is True:
                    self.timer.stop() #Stops the timer
                    game_music.stop() #stops the kahoot background music
                    winmus.play()
                    self.ui.guess_error_lbl.setText("Guesser Wins")
                    self.ui.stackedWidget.setCurrentWidget(self.ui.win_screen)
                    

                else:
                    output1 = ''.join(comparison) # converts list to string
                    self.ui.hint_lbl.setText("<html><head/><body><p><span style=' color:#ffffff;'>"+output1+"</span></p></body></html>")
                    if self.counter == 0:
                        self.ui.stackedWidget.setCurrentWidget(self.ui.lose_screen)
                        self.ui.lose_lbl.setText("You LOSER, the word was: " + hword)
                        self.timer.stop()
                        game_music.stop()
                        losemus.play()


            else:
                self.ui.guess_error_lbl.setText(error_check_result)
        self.ui.guess_count_lbl.setText("<html><head/><body><p><span style='color:#ffffff;'>"+str(self.counter)+"</span></p></body></html>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()

    bkmus_file = ':/sound/sounds/kahoot.wav' #plays kahoot music MUST BE .wav
    bkmus = QtMultimedia.QSound(bkmus_file)
    bkmus.play()
    bkmus.setLoops(-1) #Loops indefinitely

    #Lose screen music
    loser_file = ':/sound/sounds/loser.wav'
    losemus = QtMultimedia.QSound(loser_file)

    #Win screen music
    winner_file = ':/sound/sounds/win.wav'
    winmus = QtMultimedia.QSound(winner_file)

    #intense game music
    game_music_file = ':/sound/sounds/intense.wav'
    game_music = QtMultimedia.QSound(game_music_file)
    game_music.setLoops(-1)
    

    sys.exit(app.exec_())