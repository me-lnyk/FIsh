class Fish:
    def __init__(self, breed, location):
        self.breed = breed
        self.location = location

    def run(self):
        print("The fucking fish is running the fuck way, catch the damn fish")

    def eat(self, fish):
        print(f"{self.breed} has eated {fish.breed}")


GoldenFish = Fish('rearfish', 'goldenocean')

BlackEye = Fish('black', 'blackwoods')

print(GoldenFish.breed)
GoldenFish.run()
GoldenFish.eat(BlackEye)
