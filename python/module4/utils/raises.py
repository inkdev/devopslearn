from functools import wraps

def raises(except_error):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                raise except_error

        return wrapper
    return decorator

