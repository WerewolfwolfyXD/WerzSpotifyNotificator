import requests
from PIL import Image, ImageTk
import io


def get_url_as_byte(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    resp = requests.get(url, verify=False, headers=headers)
    return resp.content


def load_byte_as_tkimage(byte):
    resized_image_size = (128, 128)
    image = Image.open(io.BytesIO(byte))
    image = image.resize(resized_image_size, Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    return photo


def load_tkimage_from_url(url):
    return load_byte_as_tkimage(get_url_as_byte(url))
