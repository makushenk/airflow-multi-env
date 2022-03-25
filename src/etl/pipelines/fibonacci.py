from dynaconf import LazySettings


def fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def run(config: LazySettings):
    print(f"fib({config.FIB_N}) = {fib(config.FIB_N)}")
