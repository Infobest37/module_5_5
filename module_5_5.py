class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password
class User:
    """
    Классы пользователей которые хранят данные о пользователе
    """
    def __init__(self, name, password, pasword_confirm):
        self.name = name
        if password == pasword_confirm:
                self.password = password



if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Приветствую! Выбиррите действие: \n1 - Вход\n2 - Регистрация\n")
        if choice == '1':
            login = input("Введите Ваш логин: ")
            password = input("Введите ваш пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else: print("Неверный пароль")

            else:

                print("Пользовтель не найден")

        if  choice == '2':
            user = User(input("Введите логин: "), password := input("Введите пароль:"),
                        password2 := input("Введите пароль второй раз:"))
            if password != password2:
                print(" Ваши пароли не совпадают" )
                continue
            elif len(password) and len(password2) <= 3:

                print("Пароль не может быть меньше 8 символов")
                continue

            elif (password == password.upper() or password == password.lower() and password2 == password2.upper() or
                  password2 == password2.lower()):
                print("В вашем пароле должны быть большие и маленькие буквы")

                continue

            database.add_user(user.name, user.password)
            print(database.data)
