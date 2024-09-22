import requests

files = {'image': open('example.jpg', 'rb')}
upload_response = requests.post('http://127.0.0.1:8080/upload', files=files)
print("Upload Response:", upload_response.json())

filename = 'example.jpg'
get_response = requests.get(f'http://127.0.0.1:8080/image/{filename}', headers={'Content-Type': 'text'})
print("Get Image Response:", get_response.json())

delete_response = requests.delete(f'http://127.0.0.1:8080/delete/{filename}')
print("Delete Response:", delete_response.json())
