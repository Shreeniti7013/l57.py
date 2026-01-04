def intToRoman(num: int) -> str:
    """
    Converts an integer to its Roman numeral representation.
    Handles numbers from 1 to 3999.
    """
    # Mapping of values to symbols in descending order, including subtractive forms
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = []
    i = 0
    # Iterate through the values until the input number becomes zero
    while num > 0:
        for _ in range(num // val[i]):
            roman_num.append(syb[i])
            num -= val[i]
        i += 1
    
    return "".join(roman_num)

# Example Usage:
number1 = 3
number2 = 58
number3 = 1994

print(f"{number1} in Roman numerals is: {intToRoman(number1)}")
print(f"{number2} in Roman numerals is: {intToRoman(number2)}")
print(f"{number3} in Roman numerals is: {intToRoman(number3)}")