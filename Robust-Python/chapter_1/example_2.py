class Cookbook:
    id: int
    author: str
    title: str


class Author1:
    def create_author_count_mapping(cookbooks: list[Cookbook]):
        counter = {}
        for cookbook in cookbooks:
            if cookbook.author not in counter:
                counter[cookbook.author] = 0
            counter[cookbook.author] += 1
        return counter


from collections import defaultdict

class Author2:
    def create_author_count_mapping(cookbooks: list[Cookbook]):
        counter = defaultdict(lambda: 0)
        for cookbook in cookbooks:
            counter[cookbook.author] += 1
        return counter

from collections import Counter

class Author3:
    def create_author_count_mapping(cookbooks: list[Cookbook]):
        return Counter(book.author for book in cookbooks)
