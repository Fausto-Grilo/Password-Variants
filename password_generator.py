#!/bin/python3

import itertools
import argparse

def generate_variants(password, max_length):
    # Define possible modifications
    numbers = '0123456789'
    special_chars = '!@#$%^&*_+.?'
    
    variants = set()
    
    # Basic variants: add a number at the end
    for i in range(1, 11):  # You can adjust the range as needed
        variants.add(f"{password}{i}")
    
    # Basic variants: add a special character at the end
    for char in special_chars:
        variants.add(f"{password}{char}")
    
    # Case variations: generate all case combinations
    def case_variations(pw):
        cases = itertools.product(*[(c.lower(), c.upper()) if c.isalpha() else (c,) for c in pw])
        return set(''.join(case) for case in cases)
    
    # Add all case variations
    variants.update(case_variations(password))
    
    # Adding numbers at random positions
    for i in range(1, len(password) + 1):
        for num in numbers:
            if len(f"{password[:i]}{num}{password[i:]}") <= max_length:
                variants.add(f"{password[:i]}{num}{password[i:]}")
    
    # Adding special characters at random positions
    for i in range(1, len(password) + 1):
        for char in special_chars:
            if len(f"{password[:i]}{char}{password[i:]}") <= max_length:
                variants.add(f"{password[:i]}{char}{password[i:]}")
    
    # Ensure variants are within the max length
    variants = {var for var in variants if len(var) <= max_length}
    
    return variants

def save_variants_to_file(variants, filename='password_variants.txt'):
    with open(filename, 'w') as file:
        for variant in variants:
            file.write(variant + '\n')

def main():
    parser = argparse.ArgumentParser(description='Generate password variants.')
    parser.add_argument('-p', '--password', type=str, required=True, help='Original password.')
    parser.add_argument('-l', '--length', type=int, default=20, help='Maximum length of the password variants.')

    args = parser.parse_args()
    
    password = args.password
    max_length = args.length
    
    variants = generate_variants(password, max_length)
    save_variants_to_file(variants)
    print(f"Generated {len(variants)} variants. Saved to 'password_variants.txt'.")

if __name__ == "__main__":
    main()
