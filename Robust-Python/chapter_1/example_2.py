class Cookbook:
    def __init__(self, id: int, author: str, title: str, pages: int = 50):
        self.id = id
        self.author = author
        self.title = title
        self.pages = pages


class Author1:
    def create_author_count_mapping(self, cookbooks: list[Cookbook]):
        counter = {}
        for cookbook in cookbooks:
            if cookbook.author not in counter:
                counter[cookbook.author] = 0
            counter[cookbook.author] += 1
        return counter


from collections import defaultdict


class Author2:
    def create_author_count_mapping(self, cookbooks: list[Cookbook]):
        counter = defaultdict(lambda: 0)
        for cookbook in cookbooks:
            counter[cookbook.author] += 1
        return counter


from collections import Counter


class Author3:
    def create_author_count_mapping(self, cookbooks: list[Cookbook]):
        return Counter(book.author for book in cookbooks)


library = [
    Cookbook(1, "toxa", "cake"),
    Cookbook(2, "toxa", "pie"),
    Cookbook(3, "maria", "bread"),
    Cookbook(4, "toxa", "cookies"),
    Cookbook(5, "maria", "soup"),
]

lib = Cookbook(6, "Loli", "milk", 10)

a1 = Author1()
a2 = Author2()
a3 = Author3()


def print_author_count():
    print("-------------------------------")
    print(a1.create_author_count_mapping(library))
    print("-------------------------------")
    print(dict(a2.create_author_count_mapping(library)))
    print("-------------------------------")
    print(dict(a3.create_author_count_mapping(library)))
    print("-------------------------------")
