def is_palindromic(number):
    return str(number) == str(number)[::-1]

def largest_palindrom_from_products(_range):
    return max([x*j for x in _range for j in _range if (is_palindromic(x*j))])

print(largest_palindrom_from_products(range(100,1000)))