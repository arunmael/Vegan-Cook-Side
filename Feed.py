from SQL_File import db

"""
test = 'SELECT * FROM "User"'
test_result = db.execute_query(test)
print(test_result)
"""

best_to_worst_recipe = ('select "Recipe"."Name", "Recipe"."Author", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions", avg("Rating"."Rating") as "Rating" '
                        'from "Recipe" '
                        'join "Rating" on "Recipe"."RecipeID" = "Rating"."RecipeID" '
                        'join "Origin" on "Recipe"."OriginID" = "Origin"."OriginID" '
                        'join "User" on "Recipe"."Author" = "User"."UserID" '
                        'group by "Recipe"."Name", "Recipe"."Author", "Recipe"."Description", "Recipe"."Time", "Recipe"."Instructions" '
                        'order by "Rating" DESC'
                        )

best_to_worst_recipe = db.execute_query(best_to_worst_recipe)
for recipe in best_to_worst_recipe:
    print(f'Name: {recipe["Name"]}    Author: {recipe["Author"]}    Rating: {recipe["Rating"]}    Time: {recipe["Time"]}\n      Instructions: {recipe["Instructions"]}')