import itertools


def join(*lists : list, separator : str='-') -> list or None:
    """
        The function receives an unlimited number of lists and another parameter called separator (optional)
        and returns one list consisting of all the lists received as parameters. If the separator parameter is provided,
        it threads it as an object between any two lists, and if it is not provided, it threads the character "-" instead.
        If the function does not receive lists at all - it will return None.
        :param lists: The lists to be merged into one list.
        :param separator: The separator between the lists.
        :return: The merged list or None.
    """
    if not lists:
        return None
    [lst.append(separator) for lst in lists]
    result_list = list(itertools.chain(*lists))
    result_list.pop()
    return result_list
