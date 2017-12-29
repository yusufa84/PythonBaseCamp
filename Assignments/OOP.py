class Animal(object):
    def __init__(self):
        print('Animal created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cat created')
    def whoAmI(self):
        print('Cat')
    def bark(self):
        print('Barking')

class Dog(object):
    #Class object attribute
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab','Sammy')
print(sam.breed)
print(sam.species)
print(sam.name)

class Circle(object):
    #class object attributes
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.perimeter = 2 * self.pi * radius

    def area(self):
        return self.pi * (self.radius**2)

    def set_radius(self,new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def get_perimeter(self):
        return self.perimeter

c = Circle(4)
print(c.get_radius())
print(c.get_perimeter())
print(c.perimeter)

cat = Cat()
cat.eat()
cat.bark()

#Special methods
class Book(object):
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return 'Title: %s, Author: %s, Pages: %s' %(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Book is deleted')

b = Book("Python",'Jose',295)
print(b)
print(len(b))
del b
