from decorators import log_args_results_decorator, catch_handle_exception_decorator


@log_args_results_decorator
def add(a, b):
    return a + b


add(6, 15)


@catch_handle_exception_decorator
def divide(a, b):
    return a / b


divide(35, 27)
