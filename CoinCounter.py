def coin_counter_function(change_owed, coin_list):
    """
    Function that returns the optimal change in the fewest possible coins/bills.
    :param change_owed: (INT) The total change owed.
    :param coin_list: (LIST[INT]) The individual values of coins/bills available, in any order.
    :return: {coin/bill: amount} (STRING: INT)
    """
    change = {}
    coin_list.sort(reverse=True)
    change_owed = change_owed * 100
    for i in coin_list:
        if change_owed < i:
            break
        coin_value = i * 100
        amount_coins = int(change_owed / coin_value)
        change_owed -= coin_value * amount_coins
        change[f"{i}"] = amount_coins
    return change
