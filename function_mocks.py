# Mocks

"""

These are objects that replace the real implementation of a method or function
with a test implementation. In Python, we can use the unittest.mock library to create a mock.

"""

from unittest.mock import MagicMock

# Create a mock object.
my_mock = MagicMock()

# Replace the real implementation of the add method with the mock implementation. 
my_mock.add = MagicMock(return_value=42)

# Call the add method on the mock object.
result = my_mock.add(1, 2)

# Assert that the result is equal to 42.
assert result == 42


"""
Mocks can be used to replace the implementation of a method
 or function with a test implementation. For example, suppose we have a
   function that interacts with a remote API and returns some data:

"""

import requests

def get_data():
    response = requests.get('https://example.com/api/data')
    return response.json()


# To test this function, we could create a mock object that simulates the behavior of the API:

from unittest.mock import MagicMock

def test_get_data():
    # Create a mock object for requests.get
    requests.get = MagicMock()
    requests.get.return_value.json.return_value = {'foo': 'bar'}
    
    # Call the function being tested
    result = get_data()
    
    # Assert that the result is equal to the expected value
    assert result == {'foo': 'bar'}


"""
In this example, we create a mock object for requests.get using MagicMock.
 We then set the return value of the json method on the mock object to {'foo': 'bar'}. 
 When the get_data function is called, it will use the mock object instead of making a real HTTP request.
 
"""