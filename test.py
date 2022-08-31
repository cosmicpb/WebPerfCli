from jsonpath_rw import jsonpath, parse
import requests

newUser = 

credLogin = {
  "email": "fulano@qa.com",
  "password": "teste"
}

loginPost = requests.post('https://serverest.dev/login', credLogin)

#print(loginPost.json())

loginJson = loginPost.json()

auth = parse('$.authorization')
tokenJson = auth.find(loginJson)
token = tokenJson[0].value

print(token)

headers = {'Authorization' : token}

newUser = {
  "nome": "TESTEPAULO",
  "preco": 470,
  "descricao": "Mouse",
  "quantidade": 381
}

rpost = requests.post('https://serverest.dev/produtos', newUser, headers=headers)

print(rpost.json())