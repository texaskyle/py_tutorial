def kg_to_pounds(weight):
    return weight * 0.45


def pounds_to_kg(pounds):
    return pounds / 0.45


def find_max(numbers):
    max_no = numbers[0]
    for number in numbers:
        if number > max_no:
            max_no = number
    return max_no