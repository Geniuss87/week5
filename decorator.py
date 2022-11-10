def remove_duplicate(func):
    def wrapper(*args, **kwargs):
        set_list = set(func(*args, **kwargs))
        return list(set_list)

    return wrapper


@remove_duplicate
def same_lists_elements_check(first_list):
    result = first_list
    return result


@remove_duplicate
def same_list(first_list, second_list):
    sum_list = first_list + second_list
    return sum_list


@remove_duplicate
def same_lists(first_list, second_list, third_list):
    sum_list = first_list + second_list + third_list
    return sum_list


print(same_lists_elements_check([0, 1, 2, 1, 3, 4, 5, 5, 0, 1, 5, 5, 5]))
print(same_list([1, 2, 3, 3], [1, 2, 3, 3, 3, 1, 4, 4]))
print(same_lists([1, 2, 3, 3], [0, 0, 0], [4, 8, 8, 4]))
