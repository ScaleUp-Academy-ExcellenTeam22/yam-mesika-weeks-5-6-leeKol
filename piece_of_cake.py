def get_recipe_price(prices, optionals=[], **quantities):
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
    price = 0
    for key in prices:
        if key not in optionals:
            price += prices.get(key) * int(quantities.get(key)/100)
    return price
