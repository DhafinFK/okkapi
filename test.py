import math


class Movie():
    def __init__(self, id, genre, price, capacity, percentage):
        self.id = id
        self.genre = genre
        self.price = price
        self.capacity = capacity
        self.member_capacity = math.ceil(capacity * (percentage)/100)


movie_genre = []

horror = Movie('1', 'Horror', 1000, 12, 30)
horror = Movie('2', 'Action', 1000, 12, 30)
horror = Movie('3', 'Sci-Fi', 1000, 12, 30)