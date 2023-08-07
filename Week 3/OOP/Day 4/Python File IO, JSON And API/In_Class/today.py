class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat('Whiskers', 5)
cat2 = Cat('Felix', 3)
cat3 = Cat('Oscar', 6)

def oldest(*cats):
    old = cats[0]
    for cat in cats:
        if cat.age > old.age:
            old = cat
    return old

print(f"The oldest cat is {oldest(cat1, cat2, cat3).age} years old.")