# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

#Let's begin :)
#Data structrures our program will use

#easy level
easy_paragraph = '''A common first thing to do in a language is to display
'Hello __0__!'  In __1__ this is particularly easy; all you have to do
is type in:
__2__ "Hello __0__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __2__ command, and
produces a program which does something, so it is useful in that capacity.

You can also read input from a user using the __3__ command.
This very program utilizes both commands written in __1__ to interact with you.'''

#medium level
medium_paragraph = '''A __0__ is created with the def keyword. You specify the inputs a __0__ takes by
adding __1__ separated by commas between the parentheses. __0__s by default return __2__ if you
don't specify the value to return. __1__ can be standard data types such as string, number, dictionary,
tuple, and __3__ or can be more complicated such as objects and lambda functions.'''

#hard level
hard_paragraph = '''According to the recent Paradise Papers, __0__, __1__, __2__, __3__,
Nike, Walmart, Allianz, Siemens, McDonald's, and Yahoo! are among the corporations that own offshore companies,
as well as Allergan, the manufacturer of Botox. According to The Express Tribune, "Apple, Nike, and Facebook
avoided billions of dollars in tax using offshore companies." Source: https://en.wikipedia.org/wiki/Paradise_Papers'''

#original_paragraph dictionary will store our original paragraph questions, one for each level of difficulty.
original_paragraph = {'easy': easy_paragraph, 'medium': medium_paragraph, 'hard': hard_paragraph}

#The answers to the original_paragraphs above, one for each level of difficulty.
#easy level
easy_answers = ['World', 'Python', 'print', 'raw_input']
#medium level
medium_answers = ['function', 'arguments', 'None', 'list']
#hard level
hard_answers = ['Facebook', 'Apple', 'Disney', 'Uber']
answers = {'easy': easy_answers, 'easy_min_length': 0, 'easy_max_length': len(easy_answers),
           'medium': medium_answers, 'medium_min_length': 0, 'medium_max_length': len(medium_answers),
           'hard': hard_answers, 'hard_min_length': 0, 'hard_max_length': len(hard_answers)}

#Conceptually different steps, broken down into seperate functions
#Use Google format for Python doctstrings
#https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
def prompt_user_difficulty_level():
    '''
    Prompt user for difficulty level.

    Args:
        None

    Returns:
        Interact with user until a valid difficulty level is selected and returned.

    Raises:
        None
    '''
    print 'Please select a game difficulty by typing it in!'
    user_level = ''
    while user_level not in ['easy', 'medium', 'hard']:
        print 'Possible choices include easy, medium, and hard.'
        user_level = raw_input()

    print 'You have chosen ' + user_level + '!'
    return user_level

def prompt_user_number_of_trials():
    '''
    Prompt user for number of trials with a maximum boundary.

    Args:
        None

    Returns:
        Interact with user until a valid number of trials is selected and returned.

    Raises:
        None
    '''
    print 'How many chances would you like to try, up to 5 per problem:'
    guesses = raw_input()
    while guesses not in ['1','2','3','4','5']:
        print 'How many chances would you like to try, up to 5 per problem:'
        guesses = raw_input()

    print "Great! Let's start with " + str(guesses) + " guesses per problem."
    return int(guesses)

def ask_user_paragraph(difficulty_level, guesses):
    '''
    Ask the user to fill in the blanks in a paragraph.

    Args:
        param1: difficulty_level
        param2: guesses

    Returns:
        A new paragraph based on the user's input.

    Raises:
        None
    '''

    if difficulty_level in ['easy', 'medium', 'hard']:
        paragraph = original_paragraph[difficulty_level]

    print '\nThe current paragraph reads as such:'
    print paragraph
    initial_blank_id = 0
    return [paragraph, initial_blank_id]

def update_paragraph(paragraph, blank_id, answer):
    '''
    Update a given paragraph with the answer for the blank provided.

    Args:
        param1: paragraph
        param2: blank_id
        param3: answer

    Returns:
        Return updated paragraph and blan_id.

    Raises:
        None
    '''

    paragraph = paragraph.replace('__' + str(blank_id) + '__', answer)
    print '\nThe current paragraph reads as such:'
    print paragraph
    blank_id += 1
    return [paragraph, blank_id]

def update_guesses(guesses):
    '''
    Update the number of guesses in case of an incorrect answer.

    Args:
        param1: guesses

    Returns:
        The updated number of guesses.

    Raises:
        None
    '''

    guesses -= 1
    if guesses > 1:
        print "That isn't the correct answer!  Let's try again; you have " + str(guesses) + " trys left!"
    elif guesses == 1:
        print "That isn't the correct answer! You only have " + str(guesses) + " try left! Make it count!"
    else:
        print "You've failed too many straight guesses!  Game over!"
    return guesses

def verify_answer_update_paragraph(difficulty_level, paragraph, blank_id, guesses):
    '''
    Verify an answer entered by a user and if correct, update the paragraph.

    Args:
        param1: difficulty_level
        param2: blank_id
        param3: answer

    Returns:
        Verify an answer and return the updated paragraph.

    Raises:
        None
    '''

    if difficulty_level in ['easy', 'medium', 'hard']:
        difficulty_min_length = answers[difficulty_level + '_min_length']
        difficulty_max_length = answers[difficulty_level + '_max_length']

        while guesses > 0 and blank_id >= difficulty_min_length and blank_id < difficulty_max_length:
            print 'What should be substituted in for __' + str(blank_id) + '__?'
            answer = raw_input()

            if answers[difficulty_level][blank_id] == answer:
                [paragraph, blank_id] = update_paragraph(paragraph, blank_id, answer)
            else:
                guesses = update_guesses(guesses)

            if blank_id == difficulty_max_length:
                print '\n*** You won! ***'

    return [paragraph, blank_id]

#Main logic and function calls
#Prompt user for difficulty level.
user_level = prompt_user_difficulty_level()

#Prompt user for number of trials with a maximum boundary.
guesses = prompt_user_number_of_trials()

#Ask the user to fill in the blanks in a paragraph.
[paragraph, blank_id] = ask_user_paragraph(user_level, guesses)

#Verify an answer entered by a user and if correct, update the paragraph.
[paragraph, blank_id] = verify_answer_update_paragraph(user_level, paragraph, blank_id, guesses)
