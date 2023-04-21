# Name: Aaron Ducote
# Class: CS 361
# Filename: Milestone1.py
# Description: Implements the individual side of my project through user input. Program asks user what they would like
# to see images of and how many images they would like to see, and the program reads that input.

"""Three Quality Attributes: Accuracy, Usability, Evolvability

Quality Attribute 1: Accuracy - The program displays accuracy by ensuring that the user has given the input
that they intend to give so that the program can find the correct input. This way, the user is guaranteed to find
a result that meets their requests.

Quality Attribute 2: Usability - The program displays usability by providing explicit directions throughout the
program so that those who are not familiar with coding can still understand the program. The program consistently
takes the user's input to make the experience more user-friendly.

Quality Attribute 3: Evolvability - The program displays evolvability by showing what the program can become with
more tinkering and optimization. Once the program is connected to its microservice, it will be able to read input
from the user and then actually display that input to the user through an image search.

"""


def image_requester():
    # CSH6: Provide an explicit path through the task.
    # The program provides explicit steps for each part of the program so that the user is not confused by what
    # the program is asking them to do. For example, the program is very clear about what it is requesting in
    # the photo request and number of requests sections.

    # CSH8 : Encourage tinkerer to tinker mindfully.
    # This program has explicit directions that make it very easy to use. If the user is tinkering around and makes
    # a simple mistake, then the program will catch that mistake and tell them how to fix it. This way, tinkerers
    # can tinker without having to worry about making permanent mistakes.

    name = input("Hello and welcome to Aaron's Image Searcher! What is your name? ")

    photo_request = input("Hi " + name + ", what would you like to see images of today? ")

    continue_request = input("We read your request as " + photo_request + ". Is this correct? Enter Yes "
                                                                          "if so, and No otherwise. ")

    # CSH1 : Explain the Benefits of using new and existing features: Using the feature of having the program ask the
    # user if they have read the correct input makes the program more usable and efficient. There is less likelihood
    # for an incorrect output.

    # CSH5 : Make undo/redo and backtracking available.
    # If the user makes an incorrect input or the program reads the input incorrectly, then the user can simply
    # see their mistake and tell the program that an incorrect request is being made. This way, the user can
    # backtrack so that no incorrect requests are made.

    if continue_request == 'No':
        print('We apologize! We will restart the image searcher to gather your request.')
        return image_requester()

    # CSH2 : Explain the costs of using new and existing features
    # If we had just taken that input, and it was correct, then the last few lines of code were run for no reason.
    # So, we are sacrificing some time for accuracy.

    num_request = input("Okay, how many photos of " + photo_request + " would you like to see today? ")

    # CSH3 : Let people gather as much information as they want, and no more than they want
    # The program asks the user how many images they want to see so that they are not given too few or too many
    # results. This allows them to control the amount of information they receive.
    # print(num_request)

    final_request = ("Okay " + name + ", so you would like to see " + num_request + " pictures of "
                     + photo_request + ". We will find your results now!")

    print(final_request)

    return photo_request, num_request


def how_many_requests():
    initial_request = image_requester()
    print(initial_request)
    another_request = input("Would you like to make any more requests today? Enter Yes or No: ")

    # CSH4 : Keep familiar features available.
    # The program only runs the program one time initially, and gives the user the choice for if they want to make
    # more requests. This way, the user has the choice over if they want to run the program simply 1 time instead of
    # running it multiple times.

    if another_request == 'No':
        return initial_request
    else:
        new_request = image_requester()
        return new_request

    # CSH7 : Provide ways to try out different approaches.
    # If a user does not like the result of their first request, then they are permitted to try multiple requests
    # so that they will eventually end up with a desired output.


print(how_many_requests())
