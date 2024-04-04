from abc import ABC, abstractmethod


# superClass for a movie/game rental
class Rental(ABC):
    number_rentals = 0

    def __init__(self, serial, title='NULL'):
        self.title = title
        self.serial = serial
        self.number_rentals += 1

    @classmethod
    def get_number(cls):
        return cls.number_rentals

    # get and set methods
    def get_title(self):
        return self.title

    def set_title(self, new_title):
        wrong = True
        while wrong:
            if type(new_title) == str:
                self.title = new_title
                wrong = False
            else:
                new_title = input("Please type an apropriate title: ")

    def get_serial(self):
        return self.serial

    # the charging options shall be different depending on the rental type
    @abstractmethod
    def price(self):
        pass


# movie rentals
class Movie(Rental):
    def __init__(self, genre, serial, title='NULL'):
        super().__init__(serial, title)
        self.genre = genre
        Rental.number_rentals += 1

    def get_genre(self):
        return self.genre

    def price(self):
        num_days = int(input("How many days will the movie be rented"))
        value = 5.00 + float(num_days) * 0.25
        return value


class Game(Rental):
    def __init__(self, rating, serial, title='NULL'):
        super().__init__(serial, title)
        self.rating = rating
        Rental.number_rentals += 1

    def get_rating(self):
        return self.rating

    def set_rating(self, new_rating):
        self.rating = new_rating

    def price(self):
        num_days = int(input("How many days will the game be rented"))
        value = 5.00 + float(num_days) * 0.75
        return value


if __name__ == '__main__':
    movie1 = Movie('action', 13402, 'Speed Racer')
    game1 = Game(4.30, 99999, "Hollow Knight")

    print(movie1.get_title())
    print(movie1.price())
    print(game1.get_title())
    print(game1.price())
    print(f'''The number of objects were: {Rental.get_number()}''')