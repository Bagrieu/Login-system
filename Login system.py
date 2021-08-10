logins = ['admin','guest']
passwords = ['admin','guest12345']
cont = 0
keep = True
while keep:
    if cont == 0:
        login = str(input('Login: ').strip().lower())
        password = str(input('Password: ').strip().lower())
        cont += 1
    else:
        cont+=1
        print('Invalid login or password, try again!')
        login = str(input('Retype your login: ').strip().lower())
        password = str(input('Retype your password: ').strip().lower())
    for t in range(len(logins)):
        if login == logins[t] and password == passwords[t]:
            keep = False
print(f"You're in! After {cont} attempts.")