class Car:
    # Class-level attribute (shared by all Car objects)
    # This might represent a constant, like the number of wheels a standard car has.
    num_wheels = 4

    # The __init__ method is a special method (a "dunder" method)
    # It's called automatically when you create a new Car object.
    # 'self' refers to the specific object being created/operated on.
    def __init__(self, make, model, color):
        # Attributes (instance variables)
        # These store the unique data for each individual Car object.
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0  # All new cars start with 0 speed
        self.engine_on = False # All new cars start with engine off

    # Methods: Actions that a Car object can perform

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            return f"The {self.color} {self.make} {self.model} engine started."
        else:
            return f"The {self.color} {self.make} {self.model} engine is already on."

    def stop_engine(self):
        if self.engine_on and self.speed == 0:
            self.engine_on = False
            return f"The {self.color} {self.make} {self.model} engine stopped."
        elif self.speed > 0:
            return f"Cannot stop engine! The {self.model} is still moving at {self.speed} mph."
        else:
            return f"The {self.color} {self.make} {self.model} engine is already off."

    def accelerate(self, amount):
        if self.engine_on:
            self.speed += amount
            return f"The {self.model} accelerated to {self.speed} mph."
        else:
            return "Cannot accelerate, engine is off!"

    def brake(self, amount):
        if self.speed - amount >= 0:
            self.speed -= amount
            return f"The {self.model} slowed down to {self.speed} mph."
        else:
            self.speed = 0
            return f"The {self.model} came to a stop."

    def get_info(self):
        return (f"This is a {self.color} {self.make} {self.model}."
                f" Current speed: {self.speed} mph. Engine: {'On' if self.engine_on else 'Off'}.")


# 2. Create Objects (Instances) from the Class

# Creating the first Car object
my_car = Car("Toyota", "Camry", "Blue")

# Creating a second Car object
friends_car = Car("Honda", "Civic", "Red")

# Creating a third Car object
dream_car = Car("Tesla", "Model S", "Black")


# 3. Interact with the Objects (Access Attributes and Call Methods)

print("--- My Car ---")
print(my_car.get_info()) # Initial state
print(my_car.start_engine())
print(my_car.accelerate(50))
print(my_car.brake(20))
print(my_car.get_info())
print(my_car.stop_engine()) # Cannot stop if moving
print(my_car.brake(30)) # Stop completely
print(my_car.stop_engine())
print(f"My car has {my_car.num_wheels} wheels.") # Accessing class attribute


print("\n--- Friend's Car ---")
print(friends_car.get_info())
print(friends_car.start_engine())
print(friends_car.accelerate(60))
print(friends_car.get_info())
print(f"Friend's car has {friends_car.num_wheels} wheels.")


print("\n--- Dream Car ---")
print(dream_car.get_info())
print(dream_car.start_engine())
print(dream_car.accelerate(100))
print(dream_car.get_info())


# Demonstrate that objects are independent
print("\n--- Comparing Objects ---")
print(f"My car's color: {my_car.color}")
print(f"Friend's car's color: {friends_car.color}")
print(f"Dream car's speed: {dream_car.speed}")