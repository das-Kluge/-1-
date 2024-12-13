class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        print("пароль изменен")

    def check_password(self, password):
        if password == self.__password:
            return True
        else:
            return False


user1 = UserAccount(input('имя '), input('почта '), input('пароль '))
new_password = input('введите новый пароль ')
user1.set_password(new_password)
check_result = user1.check_password(new_password)
print("результат проверки:", check_result)
