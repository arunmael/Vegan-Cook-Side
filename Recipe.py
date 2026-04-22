from SQL_File import db

def create_recipe(session_user_id):
    recipe_name = input("Enter the recipe name: ")
    recipe_description = input("Enter the recipe description: ")
    recipe_duration = int(input("Enter the recipe duration in minutes: "))
    recipe_instructions = input("Enter the recipe instructions: ")
    recipe_picture = input("Upload a picture of the recipe: ")
    recipe_origin = input("Enter the recipe origin (One country only): ")
    cook_counter = 0

    #Origin Select für FK machen!!!
    origin_id = f"""select "Origin"."OriginID" from "Origin" where "Origin"."Origin" = '{recipe_origin}';"""
    origin_id = db.execute_query(origin_id)
    recipe_insert = f"""insert into "Recipe" ("OriginID", "Author", "Name", "Description", "Time", "Instructions", "Picture", "CookCounter") values ({origin_id}, {session_user_id}, '{recipe_name}', '{recipe_description}', {recipe_duration}, '{recipe_instructions}', '{recipe_picture}', {cook_counter});"""

    recipe_category = input("Enter the recipe category(To stop press Enter): ")
    while recipe_category != '':
        # todo den insert an die richtigen Orte (2 Orte) schreiben
        recipe_category = input("Enter the recipe category(To stop press Enter): ")



    new_ingredients = input("Enter ingredients (To stop press Enter): ")
    while new_ingredients != '':
        # todo den insert an die richtigen Orte (2 Orte) schreiben
        new_ingredients = input("Enter ingredients (To stop press Enter): ")



