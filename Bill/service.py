def calculate_denominations(amount):
    denominations = [500, 200, 100, 50, 20, 10]
    result = {}

    for note in denominations:
        count = amount // note
        if count > 0:
            result[note] = count
            amount = amount % note

    return result