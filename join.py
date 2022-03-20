import itertools


def join(*lists, sep='-'):
    """
    The function receives an unlimited number of lists and another parameter called sep (optional)
    and returns one list consisting of all the lists received as parameters. If the sep parameter is provided,
    it threads it as an object between any two lists, and if it is not provided, it threads the character "-" instead.
    :param lists: The lists to be merged into one list.
    :param sep: The separator between the lists.
    :return: The merged list.
    """
    if not lists:
        return None
    res_lst = []
    for lst in lists:
        res_lst += list(itertools.chain(lst))
        res_lst.append(sep)
    res_lst.pop()
    return res_lst
