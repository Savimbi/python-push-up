import pytest


def calc(m, n):
    return m * n // 2 % 7


def count_and_sum_div_of_2_or_7(max_excluded):
    count = 0
    sum = 0
    for i in range(1, max_excluded):
        if i % 2 == 0 or i % 7 == 0:
            count += 1
            sum += i
    return {"sum": sum, "count": count}


def number_as_text(n):
    value = ""
    remaining_value = n
    while remaining_value > 0:
        remainder_as_text = digit_as_text(remaining_value % 10)
        remaining_value = int(remaining_value / 10)
        value = remainder_as_text + " " + value
    return value.strip()


def digit_as_text(n):
    value_to_text_mapping = {
        0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"
    }
    return value_to_text_mapping[n % 10]


def is_perfect_number(number):
    #Always divisible by 1
    sum_of_multipliers = 1

    for num in range(2, int(number / 2) + 1):
        if number % num == 0:
            sum_of_multipliers += num
    return sum_of_multipliers == number


def calc_perfect_num(max_exclussive):
    result = []
    for num in range(2, max_exclussive):
        if is_perfect_number(num):
            result.append(num)
    return result


@pytest.mark.parametrize("n,expected",
                         [(6, True),
                          (28, True),
                          (496, True),
                          (8128, True),
                          (2, False)])
def test_is_perfect_number(n, expected):
    assert is_perfect_number(n) == expected


@pytest.mark.parametrize("n,expected", [
    (50, [6, 28]),
    (1000, [6, 28, 496]),
    (10000, [6, 28, 496, 8128])
])
def test_calc_perfect_num(n, expected):
    assert calc_perfect_num(n) == expected


@pytest.mark.parametrize("m,n, expected", [(6, 7, 0), (3, 4, 6), (5, 5, 5)])
def test_calc(m, n, expected):
    assert calc(m, n) == expected


@pytest.mark.parametrize("n,expected", [(3, {"sum": 2, "count": 1}),
                                        (8, {"sum": 19, "count": 4}),
                                        (15, {"sum": 63, "count": 8})])
def test_count_and_sum_div_of_2_or_7(n, expected):
    assert count_and_sum_div_of_2_or_7(n) == expected


@pytest.mark.parametrize("num, expected", [(7, "SEVEN"),
                                           (5, "FIVE"),
                                           (45, "FOUR FIVE"),
                                           (79, "SEVEN NINE"),
                                           (37659, "THREE SEVEN SIX FIVE NINE"),
                                           (24680, "TWO FOUR SIX EIGHT ZERO"),
                                           (13579, "ONE THREE FIVE SEVEN NINE")])
def test_number_as_text(num, expected):
    assert number_as_text(num) == expected
