class Cat:
    def __init__(self, name, color, gender):
        self.name = name
        self.color = color
        self.gender = gender

    def meow(self):
        print('Mreow!')

    def describe(self):
        print('My name is {}, i am {} {}'.format(
            self.name, self.color, self.gender
        ))

barsik = Cat('barsik', 'black', 'male')
# barsik.meow()
# barsik.describe()
barsik_voice = getattr(barsik, 'meow')
barsik_look = getattr(barsik, 'describe')
# print(barsik_voice)
barsik_voice()
barsik_look()


# puzik = Cat('puzik', 'white', 'female')
# puzik.meow()
# puzik.describe()