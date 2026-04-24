from Feed import *
from User import *
from Recipe import *

def main():
    session_user_id = account()
    feed()
    loop = True
    while loop == True:
        users_choice = input('What would you like to do? (Cook a recipe(1), create a recipe(2), search a recipe(3) or a use the smart recipe function(4))\n: ')
        if users_choice == '1':
            choose_recipe(session_user_id)

        if users_choice == '2':
            create_recipe(session_user_id)


        users_choice = input('What would you like to do? (Cook a recipe(1), create a recipe(2), search a recipe(3) or a use the smart recipe function(4))\n: ')


if __name__ == '__main__':
    main()
