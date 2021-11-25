import requests

# make this a user input string
#URL = 'http://localhost:8000/teacher_login/'

url = 'http://localhost:8000/teacher_login/'
payload = {'password':'123'}

response = requests.post(url,data=payload)

print (response)

#lient = requests.Session()
#client.get(URL)
