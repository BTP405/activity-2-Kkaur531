#(25 points) Write a Python function `printStats(t)` which retrives data in a text file _t_ which reads in lines of numbers.  For each line read in, the function must call a _decorator_ function which prints 
#* the numbers read
#* the count of the numbers read
#* the average of the numbers
#* the maximum of the numbers
#decorator
def decorator(func):
    def wrapper(numbers):
        print(f'Numbers read: {numbers}')
        print(f'Count: {len(numbers)}')
        print(f'Avg: {sum(numbers) / len(numbers)}')
        print(f'Max: {max(numbers)}')
        print('')
        return func(numbers)
    return wrapper

@decorator#syntax to call the decorator , This means that when processNumbers is called, it will actually call the wrapper function defined in the decorator
def processNumbers(numbers):
    pass  # Additional processing can be added here if needed
  
#processes each line to extract the numbers, and then calls the decorated processNumbers function for each line
def printStats(t):
    with open(t, 'r') as file:
        for line in file:
            numbers = [int(word) for word in line.split()]
            processNumbers(numbers)

