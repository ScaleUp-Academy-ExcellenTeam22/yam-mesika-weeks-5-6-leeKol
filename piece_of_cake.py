from functools import reduce

def get_recipe_price(prices : dict, optionals : list =[], **quantities : int) -> int:
    """
    The function gets the ingredients needed to make a particular recipe, their prices per 100 grams,
    and the quantities needed, and returns the price to be paid for buying the ingredients.
    The function can get a list of ingredients that should be ignored when calculating.
    :param prices: A dictionary of ingredients needed to make a particular recipe- the dictionary key will be the name
    of the product, and the value of the dictionary will be its price per 100 grams.
    :param optionals: A list of ingredients to be ignored while calculating the price.
    :param quantities: For each ingredient- the amount in grams that we want to buy for the recipe.
    :return: The price to pay for buying all the ingredients.
    """
    new_prices = dict(filter(lambda ingredient: ingredient[0] not in optionals, prices.items()))
    total_price = reduce(lambda price_sum, ingredient: price_sum + new_prices[ingredient] * int(quantities[ingredient] / 100), new_prices, 0)
    return total_price
