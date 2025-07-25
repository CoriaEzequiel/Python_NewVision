import requests

#funcion get(url) / solicitud http a la url: devuelve objeto como respuesta

#url= 'https://jsonplaceholder.typicode.com/posts'
#response = requests.get(url)
#print(response.status_code)
#print(response.json())


#función post(url, data) 
url= 'https://jsonplaceholder.typicode.com/posts'
datos ={'title':'Nuevo título', 'body':'Contenido del cuerpo', 'userId':1}
response = requests.post(url, data= datos)
print(response.status_code)
print(response.json())


#put(url, data) 
new_url = 'https://jsonplaceholder.typicode.com/posts/1'
datos ={'title':'titulo actualizado', 'body':'Contenido actualizado'}
response = requests.put(new_url, data= datos)
print(response.status_code)
print(response.json())

#delete (url)

url_ = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.delete(url_)
print(response.status_code)