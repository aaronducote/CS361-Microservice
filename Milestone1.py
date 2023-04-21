# Name: Aaron Ducote
# Class: CS 361
# Filename: Milestone1.py
# Description: Implements the individual side of my project through user input. Program asks user what they would like
# to see images of and how many images they would like to see, and the program reads that input.

"""Three Quality Attributes: Accuracy, Usability, Evolvability"""


def image_requester():
    name = input("Hello and welcome to Aaron's Image Searcher! What is your name? ")
    # print(name)

    photo_request = input("Hi " + name + ", what would you like to see images of today? ")

    # print(photo_request)

    continue_request = input("We read your request as " + photo_request + ". Is this correct? Enter Yes "
                                                                          "if so, and No otherwise. ")

    if continue_request == 'No':
        print('We apologize! We will restart the image searcher to gather your request.')
        return image_requester()

    num_request = input("Okay, how many photos of " + photo_request + " would you like to see today? ")

    # print(num_request)

    final_request = ("Okay " + name + ", so you would like to see " + num_request + " pictures of "
                     + photo_request + ". We will find your results now!")

    print(final_request)

    return photo_request, num_request


print(image_requester())
