# decorators.py

# Logger decorator (logs function name, args, kwargs, and result) takes another function as its arg.
def logger(func):
    # This function inside that logger function
    def wrapper(*args, **kwargs):
        # This displays function name with positional and keyword arguments
        print(f"🚀 Running '{func.__name__}' with args: {args} kwargs: {kwargs}")
        # The result is stored in result variable
        result = func(*args, **kwargs)
        # Displays the result with function name
        print(f"✅ Finished '{func.__name__}', returned: {result}")
        print("-" * 40)
        # returns result and wrapper
        return result
    return wrapper

# Timer decorator (counts the function execution time)
def timer(func):
    # Imports time module
    import time
    # A wrapper function takes args and kwargs as args.
    def wrapper(*args, **kwargs):
        # Notes the start time before passing argsument into func()
        start_time = time.time()
        result = func(*args, **kwargs)
        # After processing function notes end time
        end_time = time.time()
        # Calculates how much time by subracting from endTime with startTime.
        execution_time = end_time - start_time
        # Displays the function name with time it executed with 4 points of precesion
        print(f"⏱️ Execution Time of '{func.__name__}': {execution_time:.4f} seconds")
        # Returns result and wrapper function
        return result
    return wrapper
