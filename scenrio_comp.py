# class Catalog:
#     def __init__(self):
#          # Initialize an empty list to store book titles
#         self.books_title = [] 
#     def add(self, book_title):
#          # Add book title to the list
#         self.books_title.append(book_title) 

#     def display(self):
#          # Return the list of book titles
#         return self.books_title 

# class Library:
#     def __init__(self):
#         # Composition: Library creates and manages a Catalog instance
#         self.catalog = Catalog()  

#     def add_book(self, book_title):
#          # Add book to the catalog
#         self.catalog.add(book_title) 

#     def display_books(self):
#          # Display books from the catalog
#         return self.catalog.display() 

# # Create a Library instance
# library = Library()

# # Add books
# library.add_book('Alchemist')
# library.add_book('AI Revolution')

# # Display books
# print("Books in the library catalog:", library.display_books())


# class Camera:
#     def __init__(self,megapixle):
#         self.megapixle=megapixle
#     def capture(self):
#         print(f"Photo captured! {self.megapixle}MP")

# class Battery:
#     def __init__(self,capacity):
#         self.capacity=capacity
#     def status(self):
#         print(f'the capcity of battey is {self.capacity}')
    

# class Smartphone:
#     def __init__(self, megapixle, capacity):
#         self.camera = Camera(megapixle)
#         self.battery = Battery(capacity)
    
#     def result(self):
#         self.camera.capture()
#     def batt(self):
#          self.battery.status()


# obj = Smartphone(megapixle=18, capacity=4000)
# obj.result()  # Captures a photo
# obj.batt()  # D

        
# class  Engine:
#     def __init__(self,capcity):
#         self.capcity=capcity
#     def start(self):
#         print(f'Engine started with a capacity of {self.capcity}')
# class  MusicSystem:
#     def __init__(self,brand):
#         self.brand=brand
#     def play_music(self):
#         print(f"Playing music from {self.brand} Music System!")

# class Car:
#     def __init__(self,capcity,brand):
#         self.engine=Engine(capcity)
#         self.musicsystem=MusicSystem(brand)
    
#     def start_engine(self):
#         self.engine.start()
#     def play_music(self):
#         self.musicsystem.play_music()



# obj=Car(capcity='1500CC',brand='ODI')
# obj.start_engine()
# obj.play_music()
        
        
# class Thermostat:    
#     def set_temperature(self,temp):
#         print(f"Temperature set to {temp} degrees.")

# class LightSystem:
   
#     def turn_on_lights(self):
#         print("Lights are now ON.")

# class SecuritySystem:
   
#     def activate_alarm(self):
#         print("Security alarm activated!")

# class SmartHome :
#     def __init__(self):
#         self.thermo=Thermostat()
#         self.light=LightSystem()
#         self.security=SecuritySystem()
    
#     def thermos_stat(self,temp):
#         self.thermo.set_temperature(temp)
#     def light_system(self):
#         self.light.turn_on_lights()
#     def secuirty_system(self):
#         self.security.activate_alarm()    


# obj = SmartHome()
# obj.thermos_stat('22C')
# obj.light_system()
# obj.secuirty_system()


