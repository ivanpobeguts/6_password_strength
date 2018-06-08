import getpass
import argparse


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def check_digits(pwd):
    return any(symbol.isdigit() for symbol in pwd)


def check_letters(pwd):
    return any(symbol.isalpha() for symbol in pwd)


def check_case_sensitivity(pwd):
    lower_letter = any(symbol.islower() for symbol in pwd)
    upper_letter = any(symbol.isupper() for symbol in pwd)
    return lower_letter and upper_letter


def check_special_symbols(pwd):
    return any(symbol in "!@#$%^&*()[]{}" for symbol in pwd)


def check_length(pwd):
    points = 0
    if len(pwd) < 5:
        points -= 1
    elif 10 < len(pwd) <= 15:
        points += 1
    elif len(pwd) > 15:
        points += 2
    return points


def check_pwd_in_blacklist(pwd, blacklist):
    return pwd in blacklist


def get_password_strength(pwd):
    strength = 2
    if check_digits(pwd): strength += 1
    if check_letters(pwd): strength += 1
    if check_case_sensitivity(pwd): strength += 2
    if check_special_symbols(pwd): strength += 2
    if check_pwd_in_blacklist(pwd, blacklist): strength -= 1
    return strength + check_length(pwd)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to blacklist file')
    return parser


if __name__ == '__main__':
    try:
        args = get_parser().parse_args()
        blacklist = load_data(args.filepath)
        pwd = getpass.getpass('Password:')
        print('Password strength is:', get_password_strength(pwd))
    except FileNotFoundError:
        print('File not found.')
