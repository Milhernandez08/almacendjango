from faker import Faker
from urllib.parse import urlencode
from urllib.request import Request, urlopen

fake = Faker()

url = 'http://192.168.0.16:8000/api/products/'
code        = fake.random_number()
name        = fake.first_name()
description = fake.text()
image       = fake.url()
quantity    = fake.random_int(5, 50)
price       = fake.coordinate(center=None, radius=0.001)
tax         = 0.2
# for _ in range(3):
    # code        = fake.random_number()
    # name        = fake.first_name()
    # description = fake.text()
    # image       = fake.url()
    # quantity    = fake.random_int(5, 50)
    # price       = fake.coordinate(center=None, radius=0.001)
    # tax         = 0.2

    # if price < 0:
    #     price = price * -1
    
    # payload = {'code':code, 'name':name, 'description':description, 'image':image,
    #             'quantity':quantity, 'price':float(price), 'tax':tax}
payload = {'code':255, 'name':'ldj', 'description':'sjfhkhfl kafksf KFK', 'image':'',
           'quantity':12, 'price':1.3, 'tax':0.2}

    # print(payload)
    # r = Request(url, urlencode(payload).encode())

    # json = urlopen(r).read().decode()

    # print(json)
print(payload)
r = Request(url, urlencode(payload).encode())

json = urlopen(r).read().decode()

print(json)