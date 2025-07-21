def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"[API LOG] Function called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
