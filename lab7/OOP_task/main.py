from models import Animal, Dog, Cat


def main():

    animal1 = Animal("GenericAnimal", 5, 20)
    dog1 = Dog("Rex", 3, 25, "German Shepherd")
    cat1 = Cat("Misty", 2, 8, "Gray")

    animals = [animal1, dog1, cat1]

    for animal in animals:
        print(animal)
        print(animal.eat())
        print(animal.move())
        print(animal.speak())
        print("---------------------")


if __name__ == "__main__":
    main()