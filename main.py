from Feed import *
from User import *

def main():
    session_user_id = account()
    feed()
    users_choice = input('What would you like to do? (Cook a recipe(1), create a recipe(2), search a recipe(3) or a use the smart recipe function(4)) ')

    if users_choice == '1':
        chosen_recipe = choose_recipe()



if __name__ == '__main__':
    main()
