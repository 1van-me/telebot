def add_user(store):
    user = raw_input('Create Username: ')
    password = raw_input('Create Password: ')
    if user in store:
        print ("That user already exsist")
        return False
    else:
        store[user] = password
        return True

global_store = dict()
for i in range(10):
    add_user(global_store)
if user in store_user:
    print ("That user already exsist")
else:
    store_user.append(user)
    store_pass.append(password)
store = dict()
store[user] = password 
while not (userguess in store and store[userguess] == passwordguess):
    for item in list:
    if input=="item":
        break
        def check_user(user, user_list):
    for item in list:
        if user == item:
            return True
            break
        return False

