# Test doubles
Test doubles are objects that stand in for other objects during a test. There are different types of test doubles with different purposes: 

## Stubs
* Mechanism for injecting data directly into the class .
* Usually created using a mocking framework.
* Does not provide validation of how the class uses the depandancy. 
* Used when data is required by the class but the process 
used to obtain it isn't relevent to what's being tested. 


## Mocks 
* Mechanism for validating how a dependency is used for the class. 
* Created using a mocking framework. 
* Can provide data and/or logic required by the class .
* Used when the test requires that the class performs specific 
actions on the dependency.

## Fake 
* Simplified implementation of a dependancy.
* Usually codded directly, without the use of a framework.
* Does not provide direct validation of how the class usses the depandency.
* Used when the class being tested requires specific logic in depeandency.
