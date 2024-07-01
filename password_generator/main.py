from password_logic.simple_password import *

include_upper = False
include_lower = False
include_symbols= False
include_numbers = False



def single_valued_base(length: int):
    """
    Generates a single based password
    Args:
        length (int): password length

    Returns:
        str : password
    """
    if include_lower:
        return only_lower_case(length)
    elif include_upper:
        return only_upper_case(length)
    elif include_symbols:
        return only_symbols(length)
    else:
        return numbers_only(length)


def double_valued_base(length: int):

    if include_lower and include_upper:
        return lower_case_and_upper_case(length)

    elif include_lower and include_numbers:
        return lower_case_and_numbers(length)

    elif include_lower and include_symbols:
        return lower_case_and_symbols(length)

    elif include_upper and numbers:
        return upper_case_and_numbers(length)

    elif include_upper and include_symbols:
        return upper_case_and_symbols(length)

    return numbers_and_symbols



def password_length():
    while True:

        length = input("How long would you like the password to be: ")
        if length.isdigit():
            length = int(length)
            if length >= 8 and length <=64:
                return int(length)
            else:
                print("Invalid password length (min 8 and max 64\n")

def generate_base():
    print("""\nThe generated password may Consist of uppercase, lowercase, symbols and numbers.
Please select the symbols

U) Uppercase
L) Lowercase
N) Numbers
S) Symbols)
""")

    print("Enter the corresponding letters to start the salt generation (Example: L N S):")

    while True:
        base = input("Configure salt (leave empty for random cased password): ").upper()

        if base == "":
            return base
        else:
            base = list(base)
            return [char for char in base if char in ["L","U","N","S"]]

def main():
    global include_upper, include_lower, include_numbers, include_symbols

    length = password_length()
    base = generate_base()

    include_upper = "U" in base
    include_lower = "L" in base
    include_symbols= "S" in base
    include_numbers = "N" in base


    if len(base) == 0:
        password = all_the_chars(length)
    elif len(base) == 1:
        password = single_valued_base(base, length)
    elif len(base) == 2:
        password = double_valued_base(length)
    else:
        password = all_the_chars(length)
    print(f"\nGenerated password: {password}")


if __name__ == "__main__":
    main()