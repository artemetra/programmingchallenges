# here i define "digits" of all supported bases, up to 64,
# where lowercase latin letters are different from
# uppercase and have lower significance
import string

digits = string.digits + string.ascii_letters
digits_dict = {i: idx for idx, i in enumerate(digits)}

def convert_to_decimal(number: str, base: int) -> int:
    """Converts a number from a given base back to decimal.
    
    :param number: a string with the number. only positive ints are supported
    :param base: an int radix base, must be between 2 and 62, or 0 to guess

    :returns: on success, 
    otherwise returns -1
    """
    if any(([x not in digits[:base] for x in number])):
        # if any of the digits don't "fit" in the given base,
        # then the number is invalid.
        return -1

    result = 0
    for idx, dig in enumerate(number):
        # for each digit in the number, going from the most significant
        # digit to the least, multiply the corresponding decimal
        # representation of that digit by the base to the power of
        # the digit's position relative to the numbers end. the last
        # digit of a number has the significance of 0, thus explaining
        # the -1 in len(number)-idx-1
        # 
        # result += (digit's decimal value)*base^(digit's significance)
        result += digits_dict[dig]*pow(base,(len(number)-idx-1))

    return result


if __name__ == '__main__':
    print("Simple radix base converter.")
    base = -1
    while not 2<=base<=62:
        base = int(input("Enter a base from 2 to 62: "))
    
    number = input("""Enter a number.\nPlease note that digits above base 10 are *case sensitive*, meaning 'a1' != 'A1', where 'a' has a lower value then 'A'\n""").strip()
    
    decimal = convert_to_decimal(number, base)
    if decimal == -1:
        print(f"Invalid input: some digits of the number are out of bounds for the given base ({base}).")
    else:
        print(decimal)

