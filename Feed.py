from SQL_File import db
import User

"""
test = 'SELECT * FROM "User"'
test_result = db.execute_query(test)
print(test_result)
"""
#todo Anzahl Votes ins Ergebnis reinehmen
def feed():
    best_to_worst_recipe = ('select "Recipe"."Name", "User"."UserName", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions", avg("Rating"."Rating") as "Rating" '
                            'from "Recipe" '
                            'join "Rating" on "Recipe"."RecipeID" = "Rating"."RecipeID" '
                            'join "Origin" on "Recipe"."OriginID" = "Origin"."OriginID" '
                            'join "User" on "Recipe"."Author" = "User"."UserID" '
                            'group by "Recipe"."Name", "User"."UserName", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions", "Recipe"."CookCounter" '
                            'order by "Rating" DESC, "Recipe"."CookCounter" DESC '
                            )

    best_to_worst_recipe = db.execute_query(best_to_worst_recipe)
    for recipe in best_to_worst_recipe:
        print(
            f'Name: {recipe["Name"]}    Author: {recipe["UserName"]}    Rating: {recipe["Rating"]}    Time: {recipe["Time"]}\n      Instructions: {recipe["Instructions"]}')


def choose_recipe(users_choice):
    users_choice = input('Which recipe do you want? ')
    counter = 0
    chosen_recipe = (
        f'select "Recipe"."Name", "User"."UserName", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions", avg("Rating"."Rating") as "Rating", "Ingredient"."Ingredient", "IngredientRecipe"."Amount", "IngredientRecipe"."AmountName", "Origin"."OriginID", "Origin"."Origin" '
        f'from "Recipe" '
        f'left join "Rating" on "Recipe"."RecipeID" = "Rating"."RecipeID" '
        f'join "Origin" on "Recipe"."OriginID" = "Origin"."OriginID" '
        f'join "User" on "Recipe"."Author" = "User"."UserID" '
        f'join "IngredientRecipe" on "Recipe"."RecipeID" = "IngredientRecipe"."RecipeID" '
        f'join "Ingredient" on "IngredientRecipe"."IngredientID" = "Ingredient"."IngredientID" '
        f'where "Recipe"."Name" = \'{users_choice}\' '
        f'group by "Recipe"."Name", "User"."UserName", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions", "Ingredient"."Ingredient", "IngredientRecipe"."Amount", "IngredientRecipe"."AmountName", "Origin"."OriginID", "Origin"."Origin" '
        )
    chosen_recipe = db.execute_query(chosen_recipe)

    erstes_ergebnis = chosen_recipe[0]

    print("\n" + "=" * 55)
    print(f" 🍽️  {erstes_ergebnis['Name'].upper()}  🍽️ ")
    print("=" * 55)
    print(f"👨‍🍳 Von: {erstes_ergebnis['UserName']}  |  🌍 Herkunft: {erstes_ergebnis['Origin']}")
    print(f"⏱️  Dauer: {erstes_ergebnis['Time']} Min. |  ⭐ Rating: {erstes_ergebnis['Rating']}")
    print("-" * 55)
    print("📝 BESCHREIBUNG:")
    print(f"{erstes_ergebnis['Description']}")
    print("-" * 55)

    print("🛒 ZUTATEN:")
    for row in chosen_recipe:
        print(f"  • {row['Amount']} {row['AmountName']} {row['Ingredient']}")

    print("-" * 55)
    print("🍳 ZUBEREITUNG:")
    print(f"{erstes_ergebnis['Instructions']}")
    print("=" * 55 + "\n")

    return chosen_recipe

def new_rating(session_user_id):
    choose_rating = int(input('Please rate the recipe from 1 to 5: '))
    new_rating_user = """insert into "Rating """
