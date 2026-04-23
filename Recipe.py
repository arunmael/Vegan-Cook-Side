from SQL_File import db


def create_recipe(session_user_id):
    recipe_name = input("Enter the recipe name: ")
    recipe_description = input("Enter the recipe description: ")
    recipe_duration = int(input("Enter the recipe duration in minutes: "))
    recipe_instructions = input("Enter the recipe instructions: ")
    recipe_picture = input("Upload a picture of the recipe: ")
    recipe_origin = input("Enter the recipe origin (One country only): ")
    cook_counter = 0

    origin_query = f"""SELECT "OriginID" FROM "Origin" WHERE "Origin" = '{recipe_origin}';"""
    origin_result = db.execute_query(origin_query)
    origin_id = origin_result[0]['OriginID']


    recipe_insert = f"""INSERT INTO "Recipe" ("OriginID", "Author", "Name", "Description", "Time", "Instructions", "Picture", "CookCounter") 
                        VALUES ({origin_id}, {session_user_id}, '{recipe_name}', '{recipe_description}', {recipe_duration}, '{recipe_instructions}', '{recipe_picture}', {cook_counter});"""
    db.execute_query(recipe_insert)

    recipe_id_query = f"""SELECT "RecipeID" FROM "Recipe" WHERE "Name" = '{recipe_name}' AND "Description" = '{recipe_description}';"""
    recipe_id_result = db.execute_query(recipe_id_query)
    recipe_id = recipe_id_result[0]['RecipeID']

    recipe_category = input("Enter the recipe category (To stop press Enter): ")
    while recipe_category != '':
        # Zuerst prüfen, ob Kategorie schon existiert
        check_category = f"""SELECT "CategoryID" FROM "Category" WHERE "Category" = '{recipe_category}';"""
        category_result = db.execute_query(check_category)
        if not category_result:  # Wenn leer, dann existiert sie nicht -> neu anlegen
            category_insert = f"""INSERT INTO "Category" ("Category") VALUES ('{recipe_category}');"""
            db.execute_query(category_insert)
            # Danach die neu erstellte ID holen
            category_result = db.execute_query(check_category)
        category_id = category_result[0]['CategoryID']
        category_recipe_insert = f"""INSERT INTO "CategoryRecipe" ("CategoryID", "RecipeID") VALUES ({category_id}, {recipe_id});"""
        db.execute_query(category_recipe_insert)

        recipe_category = input("Enter another category (To stop press Enter): ")


    new_ingredients = input("Enter ingredient (To stop press Enter): ")
    while new_ingredients != '':
        amount_name = input("What's the unit (e.g. gram, ml, pieces): ")
        amount = input("Enter the amount (number): ")

        check_ingredient = f"""SELECT "IngredientID" FROM "Ingredient" WHERE "Ingredient" = '{new_ingredients}';"""
        ingredient_result = db.execute_query(check_ingredient)

        if not ingredient_result:
            ingredient_insert = f"""INSERT INTO "Ingredient" ("Ingredient") VALUES ('{new_ingredients}');"""
            db.execute_query(ingredient_insert)
            ingredient_result = db.execute_query(check_ingredient)

        ingredient_id = ingredient_result[0]['IngredientID']

        insert_ingredient_recipe = f"""INSERT INTO "IngredientRecipe" ("IngredientID", "RecipeID", "AmountName", "Amount") 
                                       VALUES ({ingredient_id}, {recipe_id}, '{amount_name}', {amount});"""
        db.execute_query(insert_ingredient_recipe)

        new_ingredients = input("\nEnter next ingredient (To stop press Enter): ")

    print('Recipe successfully added!')