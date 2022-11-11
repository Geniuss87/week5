import functools
# def remove_duplicate(func):
#     def wrapper(*args, **kwargs):
#         set_list = set(func(*args, **kwargs))
#         return list(set_list)
#
#     return wrapper
#
#
# @remove_duplicate
# def same_lists_elements_check(first_list):
#     return first_list
#
#
# @remove_duplicate
# def same_list(first_list, second_list):
#     return first_list + second_list
#
#
# @remove_duplicate
# def same_list2(first_list, second_list, third_list):
#     return first_list + second_list + third_list
#
#
# @remove_duplicate
# def same_list3(first_list, second_list, third_list, forth_list):
#     return first_list + second_list + third_list + forth_list
#
# print(same_lists_elements_check([0, 1, 2, 1, 3, 4, 5, 5, 0, 1, 5, 5, 5]))
# print(same_list([1, 2, 3, 3], [1, 2, 3, 3, 3, 1, 4, 4]))
# print(same_list2([1, 0, 2, 3, 3], [0, 0, 0], [4, 8, 8, 4]))
# print(same_list3([1, 0, 2, 3, 3], [0, 0, 0], [4, 8, 8, 4], [2, 2]))

def name_by(func):
    @functools.wraps(func)
    def wrapper():
        names = func()
        filtered = [x for x in names if x.lower().startswith('a')]
        # filtered = list(filter(lambda x: x.lower().startswith('a'), names))
        return filtered

    return wrapper

@name_by
def list_of_names():
    """Returns list of names"""
    return ['Aman', 'Askat', 'Bolot', "Gulnaz"]

print(list_of_names.__doc__)
print(list_of_names())