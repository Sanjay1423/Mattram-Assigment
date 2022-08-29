
from datetime import date
a = date(2022, 10, 14)
print(str(a), repr(a))


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # The __str__ or str() function returns a user-friendly description of an object.
    def __str__(self):
        return f'{self.name} is released in {self.year}'

    # The __repr__ or  repr() method returns a developer-friendly string representation of an object.
    def __repr__(self):
        return f'Movie({self.name},{self.year}'


print(Movie('joker', 1990))
