class mammals:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def walk(self):
        print('walk')

class dog(mammals):
    def bark(self):
        print('bark')

class cat(mammals):
    def be_annoying(self):
        print('all cats are annoying')


dog1 = dog('dastun', 'local')
print(dog1.breed)
dog1.walk()

dog2 = dog('tom', 'bull dog')
print(dog2.breed, dog2.name)

cat1 = cat('pussy', 'international')
print(cat1.name, cat1.breed)
cat1.walk()
cat1.be_annoying()



