login = input('Login: ')
senha = input('Senha: ')
email = input('E-mail: ')

senha_bd = '123456'
login_bd = 'admin'
email_bd = 'email'

# if login_bd == login and senha_bd == senha:
#     print('ok')
# else:
#     print('error')

if (login == login_bd or email == email_bd) and senha == senha_bd:
    print('ok')
else:
    print('error')