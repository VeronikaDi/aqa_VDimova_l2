import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


response = requests.get(url, params=params)
data = response.json()

if 'photos' in data and len(data['photos']) > 0:
    for index, photo in enumerate(data['photos']):
        photo_url = photo['img_src']
        img_response = requests.get(photo_url)

        with open(f'mars_photo{index + 1}.jpg', 'wb') as file:
            file.write(img_response.content)

    print("Photos successfully uploaded!")
else:
    print("Photos not found.")
