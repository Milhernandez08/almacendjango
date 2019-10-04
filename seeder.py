from faker import Faker
from urllib.parse import urlencode
from urllib.request import Request, urlopen

fake = Faker()

url = 'http://192.168.0.16:8000/api/registration/'
for _ in range(3):
    username  = fake.first_name()
    email     = fake.email()
    password1 = fake.password()
    password2 = password1

    payload = {'username' : username, 'email' : email, 'password1' : password1, 'password2' : password2}

    print(payload)
    r = Request(url, urlencode(payload).encode())

    json = urlopen(r).read().decode()

    print(json)