import re

def validate_postal_code(postal_code):
    postal_code_pattern = re.compile(r'^[1-9][0-9]{4}$')
    return postal_code_pattern.match(postal_code) is not None

def main():
    postal_codes = ["12345", "98765", "10234", "99999", "1234", "ABCDE"]
    for code in postal_codes:
        print(f"Postal Code: {code}, Valid: {validate_postal_code(code)}")

if __name__ == "__main__":
    main()
