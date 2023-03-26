import requests
from getpass import getpass


auth_endpoint = 'http://localhost:8000/api/token/'
email = input("Please enter your email: ")
password = getpass('Please enter your password: ')
auth_response = requests.post(auth_endpoint, json={"email":email, "password": password }) 

print(auth_response.json())
