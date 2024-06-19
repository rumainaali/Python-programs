''' Date:19/06/2024
Day 17 Hw(OOPS)
1. Define a class for movie theatre. 
Properties should be Name, current movie, Location, and Owner name.
All fields except Current movie should have value.
Add a constructor to create a new theatre.
Add functions to change the current movie.

In the program, creaet 5 moview theatres.
List all the theatres in Madurai
List all the theatres that is running the movie "Captain America"
'''
class Theatre:
    def __init__(self, name, location, owner_name, current_movie=None):
        self.name = name
        self.location = location
        self.owner_name = owner_name
        self.current_movie = current_movie

    def change_current_movie(self, new_movie):
        self.current_movie = new_movie

# Creating 5 theatres
theatre1 = Theatre("Vetri Cinema Hall", "Madurai", "Owner A", "Captain America")
theatre2 = Theatre("Sakthi Cinema Hall", "Madurai", "Owner B", "Avengers")
theatre3 = Theatre("Nexus Vijaya Mall", "Chennai", "Owner C", "Captain America")
theatre4 = Theatre("Akash Cinemas", "Bangalore", "Owner D", "Spider-Man")
theatre5 = Theatre("Guru Cinema Hall", "Madurai", "Owner E")

# Stores the theatres in a list
theatres = [theatre1, theatre2, theatre3, theatre4, theatre5]

# Lists the theatres in a specific location
def list_theatres_in_location(theatres, location):
    for theatre in theatres:
        if theatre.location == location:
            print(theatre.name)

#Lists the theatres running a specific movie
def list_theatres_running_movie(theatres, movie):
    for theatre in theatres:
        if theatre.current_movie == movie:
            print(theatre.name)

# List all the theatres in the Madurai
print("Theatres in the 'Madurai':")
list_theatres_in_location(theatres, "Madurai")

# Lists all theatres that are running the movie"Captain America"
print("\nTheatres running the movie 'Captain America':")
list_theatres_running_movie(theatres, "Captain America")
