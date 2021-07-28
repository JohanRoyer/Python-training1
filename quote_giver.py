# -*- coding: utf8 -*-


import random  #for picking a random element in a list




################################### QUOTE GIVER ######################################################

#####         Global description :     #####
# We want to take a random character and make it say a random quote until the user press b. When The user press b, the program ends.
# the characters and quotes are both in a list 



######################################    DATA LISTS  ################################################



characters_list = ["persoa", "persob", "persoc"] #list of characters

quotes_list = ["a","b","c", "d", "e"] #list of quotes

info_dump = {"characters": characters_list, "quotes" : quotes_list} #dictionnary with both lists


################################  FUNCTION ###########################################

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
    
    #program loop, runs while the user doesn't press b
    while 1: # while 1 faster than while true
        print(sentence())

        answer = input("Voulez-vous une autre citation ? \n Si ce n'est pas le cas tappez \'B\'").upper() # .upper because "==" for string is case sensitive

        if answer == "B":
            break

#####################################################################################################################################################


###########################  EXECUTION ############################################

#prevent the program from being called if quote_giver.py is imported in another *.py
if __name__ == '__main__':
    program()
  
