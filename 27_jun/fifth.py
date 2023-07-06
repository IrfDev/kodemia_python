VOWELS = ['a','e','i','o','u']

input_letter = input('Por favor ingresa una letra: ')

is_input_letter_a_vowel = VOWELS.__contains__(input_letter.lower())

if is_input_letter_a_vowel:
    print(f"The letter {input_letter} is a vowel")
else:
    print(f"The letter {input_letter} is not a vowel")
    

    