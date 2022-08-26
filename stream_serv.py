# these two function inhecnce our streaming program by adding user and allow users to choose a specifc username i think it is great! 
user_name = []
def add_user(name = ''):
    user_name = []
    if not name:
        name = input("please input your new username? ")
        user_name.append(name)
def choose_user():
    new_current = ""
    while True:
        print("Welcome! ")
        for user in user_name:
            print(user)
            current = input("select your username unfortunately there is no GUI, so you have to write it haha!: ")
            if current in user_name:
                break
            else:
                print(f"{current} is not a user please.")