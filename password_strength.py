import getpass
import argparse
import string
import os


def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            return file.read().splitlines()
    else:
        return []


def check_digits(password):
    return any(symbol.isdigit() for symbol in password)


def check_letters(password):
    return any(symbol.isalpha() for symbol in password)


def check_case_sensitivity(password):
    lower_letter = any(symbol.islower() for symbol in password)
    upper_letter = any(symbol.isupper() for symbol in password)
    return lower_letter and upper_letter


def check_special_symbols(password):
    return any(symbol in string.punctuation for symbol in password)


def count_length_points(password):
    bad_length = 5
    normal_length = 10
    good_length = 15
    points = 0
    if len(password) < bad_length:
        points -= 1
    elif normal_length < len(password) <= good_length:
        points += 1
    elif len(password) > good_length:
        points += 2
    return points


def check_password_in_blacklist(password, blacklist):
    return password in blacklist


def get_password_strength(password, blacklist):
    init_strength = 2
    return (init_strength +
            check_digits(password) +
            check_letters(password) +
            2 * check_case_sensitivity(password) +
            2 * check_special_symbols(password) -
            check_password_in_blacklist(password, blacklist) +
            count_length_points(password))


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to blacklist file')
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    blacklist = load_data(args.filepath)
    if not blacklist:
        print('Warning: your blacklist is empty')
    password = getpass.getpass('Password:')
    print('Password strength is:', get_password_strength(password, blacklist))
