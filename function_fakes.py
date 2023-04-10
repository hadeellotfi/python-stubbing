# Fakes

"""

Fakes: These are objects that have a simplified implementation 
of a complex interface, used to simulate the behavior of the real object.
In Python, a simple example of a fake object would be a database in memory.

"""

class FakeDatabase:
    def __init__(self):
        self.data = {}
    
    def add(self, key, value):
        self.data[key] = value
    
    def get(self, key):
        return self.data.get(key)

# Create a fake database object
my_fake_database = FakeDatabase()

# Add a value to the fake database
my_fake_database.add("foo", "bar")

# Get the value from the fake database
result = my_fake_database.get("foo")

# Assert that the result is equal to "bar"
assert result == "bar"


"""
Fakes can be used to simulate the behavior of a real object in a
 simplified way. For example, suppose we have a class that interacts
   with a database and has a get_user method that retrieves a user by ID:
   
"""

class UserDatabase:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        
    def get_user(self, user_id):
        # Connect to the database and retrieve the user by ID
        return {'id': user_id, 'name': 'John Doe'}
    

# To test this class, we could create a fake object that uses an in-memory dictionary instead of a real database:

class InMemoryUserDatabase:
    def __init__(self):
        self.users = {}
        
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def add_user(self, user):
        self.users[user['id']] = user


def test_user_database():
    # Create a fake user database object
    user_database = InMemoryUserDatabase()
    
    # Add a user to the fake database
    user_database.add_user({'id': 1, 'name': 'John Doe'})
    
    # Get the user from the fake database
    result = user_database.get_user(1)
    
    # Assert that the result is equal to the expected value
    assert result == {'id': 1, 'name': 'John Doe'}

"""

In this example, we create a fake object for the UserDatabase class using
 InMemoryUserDatabase. We add a user to the fake database using the add_user method,
   and then retrieve the user using the get_user method. The fake database stores 
   the user data in memory, which allows us to test the UserDatabase class without
     needing a real database connection.
     
"""
   
