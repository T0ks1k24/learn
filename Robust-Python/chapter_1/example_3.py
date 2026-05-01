import example_2

text = "This is some  generic text"


# 1
def iterate1():
    index = 0
    while index < len(text):
        print(text[index])
        index += 1

    print("\n", index)


# 2
def iterate2():
    for character in text:
        print(character)


# 3
def iterate3():
    for cookbook in example_2.library:
        print(cookbook.title)


# 4
def is_cookbook_open(book):
    return book.pages > 0


def narrate(book):
    print(f"Читаємо {book.title}... Залишилося сторінок: {book.pages}")
    book.pages -= 1


def iterate4(cookbook):
    while is_cookbook_open(cookbook):
        narrate(cookbook)
    print("Книгу прочитано")


# 5
# Comprehensions
def print_author():
    authors = [cookbook.author for cookbook in example_2.library]
    return authors


# 6
class PrepredIngredient:
    def __init__(self, name, sub_ingredients):
        self.name = name
        self.sub_ingredients = sub_ingredients


# recursion
def list_ingredients(item):
    if isinstance(item, PrepredIngredient):
        print(f"-- {item.name} --")
        for sub_item in item.sub_ingredients:
            list_ingredients(sub_item)
    else:
        print(f"-- {item}")


if __name__ == "__main__":
    # iterate4(example_2.lib)
    # print(print_author())
    # pass

    flour = "Flour"
    water = "Water"
    yeast = "Yeast"
    cheese = "Mozzarella Cheese"
    pizza_dough = PrepredIngredient("Pizza Dough", [flour, water, yeast])
    pizza_recipe = PrepredIngredient("Margherita Pizza", [pizza_dough, cheese])
    list_ingredients(pizza_recipe)
