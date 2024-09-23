import requests

files = {'image': open('example.jpg', 'rb')}
upload_response = requests.post('http://127.0.0.1:8080/upload', files=files)

if upload_response.status_code == 201:
    print("Upload Response:", upload_response.json())
else:
    print(f"Error during upload: {upload_response.status_code} - {upload_response.text}")

filename = 'example.jpg'
get_response = requests.get(f'http://127.0.0.1:8080/image/{filename}', headers={'Content-Type': 'text'})

if get_response.status_code == 200:
    print("Get Image Response:", get_response.json())
else:
    print(f"Error during image retrieval: {get_response.status_code} - {get_response.text}")

delete_response = requests.delete(f'http://127.0.0.1:8080/delete/{filename}')

if delete_response.status_code == 200:
    print("Delete Response:", delete_response.json())
else:
    print(f"Error during image deletion: {delete_response.status_code} - {delete_response.text}")
