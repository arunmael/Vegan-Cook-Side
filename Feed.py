from SQL_File import db

test = 'SELECT * FROM "User"'
test_result = db.execute_query(test)
print(test_result)