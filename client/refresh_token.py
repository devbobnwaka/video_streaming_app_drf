import requests
from getpass import getpass

# token = {'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTg3NzQ5MiwiaWF0IjoxNjc5NzkxMDkyLCJqdGkiOiI1MmEwY2Q3YThjZGM0NmMyYTdlMjU1MTQyYmExNWY1MSIsInVzZXJfaWQiOjd9.jqWuwtbH6r2C8o1TNEn_HSstLrQCxXTKiSZIyRtNHZU', 
#     'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5NzkxMzkyLCJpYXQiOjE2Nzk3OTEwOTIsImp0aSI6IjlkMDg5Mjc5YjdmYjQ5YjhiODY4OTJjZTVhMDM2ZGU5IiwidXNlcl9pZCI6N30.IhLDBv0LEZGEAul7DOs8NyzoLlpIRVixiZssH3Ck9ig'
# }
refresh_token = {
    'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTg3NzQ5MiwiaWF0IjoxNjc5NzkxMDkyLCJqdGkiOiI1MmEwY2Q3YThjZGM0NmMyYTdlMjU1MTQyYmExNWY1MSIsInVzZXJfaWQiOjd9.jqWuwtbH6r2C8o1TNEn_HSstLrQCxXTKiSZIyRtNHZU', 
}
auth_endpoint = 'http://localhost:8000/api/token/refresh/'
auth_response = requests.post(auth_endpoint, json=refresh_token) 

print(auth_response.json())