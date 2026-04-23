from SQL_File import db


"""
test = 'SELECT * FROM "User"'
test_result = db.execute_query(test)
print(test_result)
"""

def feed():
    best_to_worst_recipe = ('select "Recipe"."Name", "User"."UserName", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions", avg("Rating"."Rating") as "Rating", "Recipe"."CookCounter" '
                            'from "Recipe" '
                            'left join "Rating" on "Recipe"."RecipeID" = "Rating"."RecipeID" '
                            'left join "Origin" on "Recipe"."OriginID" = "Origin"."OriginID" '
                            'left join "User" on "Recipe"."Author" = "User"."UserID" '
                            'group by "Recipe"."Name", "User"."UserName", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions", "Recipe"."CookCounter" '
                            'order by "Rating" DESC, "Recipe"."CookCounter" DESC '
                            )

    best_to_worst_recipe = db.execute_query(best_to_worst_recipe)
    for recipe in best_to_worst_recipe:
        print(f'Name: {recipe["Name"]}    Author: {recipe["UserName"]}    Rating: {recipe["Rating"]}    Time: {recipe["Time"]}    Cookcounter: {recipe["CookCounter"]}\n      Instructions: {recipe["Instructions"]}')


def choose_recipe(session_user_id):
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


    cook_counter_update = f"""UPDATE "Recipe" SET "CookCounter" = "CookCounter" + 1 WHERE "Name" = '{chosen_recipe[0]['Name']}';"""
    db.execute_query(cook_counter_update)

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

    new_rating(session_user_id, chosen_recipe)


    return chosen_recipe

def new_rating(session_user_id, chosen_recipe):
    recipe_name = chosen_recipe[0]['Name']
    choose_rating = int(input('Please rate the recipe from 1 to 5 (Press 6 if you do not want to rate the recipe): '))

    if choose_rating < 6 and choose_rating > 0:
        recipe_id_query = f"""select "Recipe"."RecipeID" from "Recipe" where "Recipe"."Name" = '{recipe_name}'"""
        recipe_id_result = db.execute_query(recipe_id_query)

        recipe_id = recipe_id_result[0]['RecipeID']
        #todo Das Rating funktioniert theoretisch allerdings muss ich es noch anpassen dass wenn ein User es noch ein zweites mal zu raten versucht es nicht abstürtzt sondern ein Nachricht bekommt wie Du hast das Rezept bereits bewertet
        new_rating_user = f"""insert into "Rating" ("UserID", "RecipeID", "Rating") values ('{session_user_id}', '{recipe_id}', '{choose_rating}');"""
        db.execute_query(new_rating_user)

        print('Danke für deine Bewertung')
        return

    else:
        print('Rating skipped')
        return