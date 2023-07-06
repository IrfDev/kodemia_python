def check_is_string_palindrome(text_arg):
    string_arg = str(text_arg).replace(" ", "")

    return string_arg == str(string_arg[::-1])


input_text = input("Ingresa un texto: ")

IS_STRING_PALINDROME = check_is_string_palindrome(input_text)

TERNARY_TEXT = "" if IS_STRING_PALINDROME else "NOT "

print(f"{input_text} is {TERNARY_TEXT}a palindrome")
