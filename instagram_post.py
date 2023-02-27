import requests
import json

# Instagram API credentials
ACCESS_TOKEN = 'your_access_token'

def post_to_instagram(listing):
    # get the image from the listing URL
    image_url = listing['MainImage']['url_570xN']
    image = requests.get(image_url).content

    # upload the image to Instagram
    response = requests.post('https://api.instagram.com/v1/media/upload',
                             files={'photo': ('image.jpg', image)},
                             data={'access_token': ACCESS_TOKEN})
    response_data = json.loads(response.text)
    media_id = response_data['media_id']

    # create the Instagram post
    caption = f"New listing on Etsy: {listing['title']} - {listing['url']}"
    payload = {
        'access_token': ACCESS_TOKEN,
        'media_ids': [media_id],
        'caption': caption
    }
    response = requests.post('https://api.instagram.com/v1/users/self/media/recent/',
                             data=payload)
