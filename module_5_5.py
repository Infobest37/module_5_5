class User:
    """
    Классы пользователей которые хранят данные о пользователе
    """
    def __init__(self, name, password , pasword_confirm):
        self.name = name
        if pasword_confirm == password:
                self.password = password

