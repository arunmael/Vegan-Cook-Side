from SQL_File import db


def login_account():
    success = False
    while success is False:
        user_name = input('Enter your username: ')
        password = input('Enter your password: ')
        counter = 0

        find_account = f"""select "UserName", "Password", "UserID"
         from "User" 
         where "UserName" = '{user_name}' and "Password" = '{password}'"""


        find_account = db.execute_query(find_account)
        for row in find_account:
            counter += 1
        if counter == 1:
            print('Successfully logged in')
            session_user_id = find_account[0]['UserID']
            success = True
        else:
            print('Login failed')
    return session_user_id


def create_account():
    counter = 0
    user_name = input('Enter your username: ')
    password = input('Enter your password: ')
    email = input('Enter your email: ')
    new_account = f"""insert into "User" ("UserName", "Password", "Email") values ('{user_name}', '{password}', '{email}');"""
    try:
        db.execute_query(new_account)
        print('User created successfully')
    except Exception as e:
        if 'duplicate key' in str(e):
            print('User already exists')
        else:
            print('Something went wrong')

    get_user_id = f"""select "UserID" from "User" where "UserName" = '{user_name}' and "Password" = '{password}';"""
    get_user_id = db.execute_query(get_user_id)
    for row in get_user_id:
        counter += 1
    if counter == 1:
        session_user_id = get_user_id[0]['UserID']
    else:
        print('Something went wrong')
    return session_user_id

def account():
    login_or_create_account = input('Login to your account(1)\ncreate a new account(2): ')
    if login_or_create_account == '1':
        session_user_id = login_account()
    if login_or_create_account == '2':
        session_user_id = create_account()

    return session_user_id
account()