import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance=cls(*args, **kwargs)
        return wrapper.instance
    wrapper.instance=None
    return wrapper

@singleton
class one:
    pass
first=one()
second=one()
print(first is second)

#Nested Decorators
def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value=func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat
@repeat(num=5)
def function(name):
    print(f"{name}")
function("Python")