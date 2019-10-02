# Complete the repeatedString function below.
def repeatedString(s, n):
    actual_len_string = len(s)
    len_of_string = actual_len_string
    no_of_as_in_actual_string = list(s).count("a")
    no_of_as = no_of_as_in_actual_string

    while len_of_string <= n:
        if len_of_string + actual_len_string > n:
            add = n - len_of_string
            no_of_as = no_of_as + list(s)[:add].count("a")
            break

        len_of_string = len_of_string + actual_len_string
        no_of_as = no_of_as + no_of_as_in_actual_string
        if len_of_string == n:
            break

    return no_of_as

def test(s, n):
    actual_len_string = len(s)
    len_of_string = actual_len_string
    no_of_as_in_actual_string = list(s).count("a")
    counter = 1

    while n > len_of_string + actual_len_string:
        len_of_string = len_of_string + actual_len_string
        counter += 1

    add = n - len_of_string
    no_of_as = no_of_as_in_actual_string * counter
    no_of_as += list(s)[:add].count("a")

    return no_of_as


def test2(s, n):
    count_of_as = list(s).count("a")
    total_count = 0

    divisor = n / len(s)

    total_count += count_of_as * int(divisor)

    reminder = n % len(s)

    total_count = total_count + list(s)[:reminder].count("a")

    return int(total_count)




if __name__ == '__main__':
    # result = repeatedString("baa", 10)
    result = test2("aba", 10)
    print(result)