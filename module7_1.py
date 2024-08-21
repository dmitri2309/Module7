from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        self.products = list(products)
        #file = open(self.__file_name, 'r')
        #info = pprint(file.read())
        get_= self.get_products()
        file = open(self.__file_name, 'a')
        for i in self.products:
            if i.name not in get_:
                #file = open(self.__file_name, 'a')
                #file.write(i.name, i.weight, i.category + '\n')
                file.write(i.name)
                file.write(', ')
                file.write(i.weight)
                file.write(', ')
                file.write(i.category + '\n')
            else:
                print(f'Продукт {i} уже есть в магазине')
        return

        file.close()


s1 = Shop()
p1 = Product('Potato', "50.5", 'Vegetables')
p2 = Product('Spaghetti', '3.4', 'Groceries')
p3 = Product('Potato', '5.5', 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
print(s1.get_products())



