class Animal:
    def __init__(self):
        self.num_of_eyes = 2
        self.num_of_nose = 2

    def greetings(self):
        print("How are you all? Hope you will be fine.")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Dog can run easily.")

labrador = Dog()
labrador.greetings()
labrador.run()
print(labrador.num_of_eyes)
print(labrador.num_of_nose)