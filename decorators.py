


def start_and_end(func):

    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("This is the end")
    return wrapper

@start_and_end
def print_name():
    print("Oleg")

# print_name = start_and_end(print_name)
print_name()











# def first_deco(func_to_decorate):
#     def wrapper():
#         print("Before")
#         func_to_decorate()
#         print("After")
#     return wrapper
#
# @first_deco
# def test_function():
#     print("something")
#
#
# test_function()

# def first_deco(age):
#     def inner_func(func_to_decorate):
#         def wrapper(name):
#             print("Before first {age}")
#             func_to_decorate(name)
#             print("After first")
#         return wrapper
#     return inner_func
#
#
# def second_deco(func_to_decorate):
#     def wrapper(name):
#         print("Before second")
#         func_to_decorate(name)
#         print("After second")
#     return wrapper
#
# @first_deco(16)
# @second_deco
# def test_function(name):
#     print(f"{name} is calling")
#
#
# test_function("John")