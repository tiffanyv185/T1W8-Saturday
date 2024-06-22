# Virtual Environment
- They help create isolated environments for your projects, ensuring each project has its own dependencies.

# Testing
- Allows us to confirm whether the application works as intended or not.
- It helps catch  bugs early and ensure that your code behaves smoothly

## Types of testing 
- Manual vs Automated
    - Manual: When a person manually performs tasks, based on events.
    - Automated: Programmed tests, called scripts, to automatically perform tasks without human involvment.

- Unit Testing: testing specific components/functions/methods
- Integration testing:  Testing the compatability with other modules/packages,
- Chaos testing: Making a program break on purpose by disabling a function or featureto see how errors are handled.
- Stress testing: Testing in high volume of data/inputs (depending on use-case)
- End to End/ Acceptance testing: Testing done towards the end of the project, when its almost complete, to ensure things work effectively.

Note: It is important to organise your directory structure for maintenance and easy access.

## pytest
- Power and user friendly testing framework
- Simple yet powerful
- pytest follows the principle of 'assert' -ing that things are true in order for a test to pass
- For a test to pass, the assert value must be true

- Reading test output: . (means pass), F(means failed), E (exceptions)

### Exceptions
- Used to check what happens when things go wrong
- How your program is handled when things go wrong

### Parameterised tests
- Make sure you initialise packages to use them in other folders.
- Might want to test the same function with multiple inputs
- Parametrise creates test cases for all inputs provided

