class User:
    
    def __init__(self, first_name, last_name, age, gen):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gen = gen
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"Primeiro nome: {self.first_name}\n"
              f"Ultimo nome : {self.last_name}\n"
              f"Idade : {self.age}\n"
              f"Genero : {self.gen}")
        
    def greet_user(self):
        print("Bem vindo(a), {} {}\n" .format(self.first_name, self.last_name))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(User):

    def __init__(self, first_name, last_name, age, gen):
        super().__init__(first_name, last_name, age, gen)
        self.privilegios = Privileges()


class Privileges:

    def __init__(self):
            self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for i in self.privileges:
            print('privilegio: ', i)


user1 = User('Wesley', "Silva", "19", "M")
user1.describe_user()
user1.greet_user()
i = 0
while i <= 5:
    user1.increment_login_attempts()
    i += 1
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

admin = Admin("Morgan", "WOS", '19', 'M')
admin.describe_user()
admin.greet_user()
admin.privilegios.show_privileges()