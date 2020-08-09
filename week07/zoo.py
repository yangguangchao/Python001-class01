from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, animal_type, body_type, character):
        self.animal_type = animal_type
        self.body_type = body_type
        self.character = character

    @property
    def is_ferocious(self):
        if (self.animal_type == '食肉' and self.body_type != '小'
            and self.character == '凶猛'):
            return True
        else:
            return False

class Cat(Animal):
    barking = '喵喵喵'
    def __init__(self, name, animal_type, body_type, character):
        super().__init__(animal_type, body_type, character)
        self.name = name

    def is_pet(self):
        if super().is_ferocious:
            return False
        else:
            return True

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = set()

    def add_animal(self, animal):
        if animal in self.animals:
            return False
        else:
            self.animals.add(animal)

    def __getattr__(self, item):
        for i in self.animals:
            if type(i).__name__ == item:
                print('动物园里有这种动物')
                return True
            print('动物园没有这种动物')
            return False

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
