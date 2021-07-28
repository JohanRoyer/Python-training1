# -*- coding: utf8 -*-


import random  #for picking a random element in a list
import json    #in order to stock the lists in external files



################################### QUOTE GIVER ######################################################

#####         Global description :     #####
# We want to take a random character and make it say a random quote until the user press b. When The user press b, the program ends.
# the characters and quotes are both in a list 



######################################    GLOBAL VARIABLES  ################################################



info_dump = {} #dictionnary with both lists


################################  FUNCTIONS ###########################################



#read json file and take a list from it

def take_list_from_file(path, key):
    extracted_list = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            extracted_list.append(entry[key])
    return extracted_list



#takes the quotes and the characters in the .json files and creates a dictionnary with both lists
def gather_data():

    characters_list = take_list_from_file("characters.json", "character")
    quotes_list = take_list_from_file("quotes.json", "quote")
    global info_dump
    info_dump = {"characters": characters_list, "quotes": quotes_list}    #change global variable info_dump to create a dictionnary with both lists
    






#take a list from the dictionnary and return a random item from this list

def random_item_in_list(list_name):
    select_list = info_dump[list_name]                              #take the list in the dictionnary with the corresponding key = list_name
    list_size = len(select_list)
    random_number = random.randint(0, list_size - 1)          #rand numb within the range of the list size
    return select_list[random_number]



#return a random quote from the list
def random_quote():
    return random_item_in_list("quotes")                #quotes = key for the quotes' list in the dictionnary


#return a random character name from the list
def random_character():
    return random_item_in_list("characters")           #characters = key for the characters' list in the dictionnary


#create a sentence with a random character saying a random quote

def sentence():

    selected_quote = random_quote()
    selected_character = random_character()

    message = "{character} a dit : {quote}".format(character = selected_character ,quote = selected_quote)
    return message



# principal program that print a quote as long as the user doesn't press B. When he does the program is over.
def program():
    gather_data()             #takes the data from the json files and put them in the dictionnary info_dump (global variable)
    #program loop, runs while the user doesn't press b
    while 1: # while 1 faster than while true
        print(sentence())

        answer = input("Voulez-vous une autre citation ? \n Si ce n'est pas le cas tappez \'B\'").upper() # .upper because "==" for string is case sensitive

        if answer == "B":
            break

#####################################################################################################################################################


###########################  EXECUTION ############################################


if __name__ == '__main__':     #prevent the program from being called if quote_giver.py is imported in another *.py
    program()
  
