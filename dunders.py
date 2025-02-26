class Movie:
    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director
    def __str__(self):
        return f'{self.title} {self.year} - Directed by {self.director}'
    def __repr__(self):
        return f"Movie(title='{self.title}', year={self.year}, director='P{self.director}')"
    
movies1=Movie('Inception ','(2010)','christopher Nolan')
movie2 = Movie("The Matrix", 1999, "The Wachowskis")
print(movies1)
print(repr(movie2))
movies1