import requests
from PIL import Image
from io import BytesIO

r = requests.get(
    "https://images.pexels.com/photos/8107880/pexels-photo-8107880.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
i = Image.open(BytesIO(r.content))
fp = open("img.jpg", "wb")
i.save(fp)
fp.close()
