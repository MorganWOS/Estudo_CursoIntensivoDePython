class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0


    def describe_restaurant(self):
        print(f"Nome do restaurante: {self.name} e culinaria {self.cuisine}")

    def open_restaurant(self):
        print("O restaurante {} esta aberto !!!" .format(self.name))

    def set_number_served(self, number_served):
        self.number_served += number_served

    def increment_served(self, number_served):
        self.number_served += number_served
        print("Foram atendido {} clientes no dia!" .format(self.number_served))


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['baunilha', 'chocolate', 'doce de leite', 'caramelo']

    def print_flavors(self):
        for i in self.flavors:
            print('Sabor: ', i)

restaurant = Restaurant("Morgan's", 'Italiana')
restaurant.describe_restaurant()
restaurant.set_number_served(10)
restaurant.increment_served(25)
sorveteria = IceCreamStand('ICE MAN', 'paleta')
sorveteria.print_flavors()