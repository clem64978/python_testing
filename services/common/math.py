# import timeit

# def functionMeasure(func):
#     def wrapper():
#         func()
#         print(func.__name__ + " : " + str(timeit.timeit(func, number=10000)))
#     return wrapper


def timeit(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f} ms to execute'.format(fn.__name__, execution_time * 1000))
        return to_execute
    return inner



@timeit
def makeList1():
    squares = []
    for i in range(10):
        squares.append(i * i)
    return squares

@timeit
def makeList2():
    txns = [1.09, 23.56, 57.84, 4.56, 6.78]
    TAX_RATE = .08
    def get_price_with_tax(txn):
        return txn * (1 + TAX_RATE)

    final_prices = map(get_price_with_tax, txns)
    return list(final_prices)

@timeit
def makeList3():
    return [i * i for i in range(10)]

@timeit
def remove_duplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]
    return unique