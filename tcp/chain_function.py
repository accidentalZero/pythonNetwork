def create_chaining_function():
    count = 0

    def chained_function():
        nonlocal count
        count += 1
        print(f"Chained function called {count} times")
        return chained_function  # Return itself for chaining

    return chained_function

chain = create_chaining_function()
chain()()()()()()  # Output: Chained function called 1 times, 2 times, 3 times, 4 times