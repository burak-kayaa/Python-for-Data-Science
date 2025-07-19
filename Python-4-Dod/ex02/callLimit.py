from typing import Any

def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwargs: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                raise Exception("Function call limit exceeded")
        return limit_function
    return callLimiter