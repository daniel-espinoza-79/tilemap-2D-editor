from pygame import image, transform

BASE_IMG_PATH = 'data/images/'

def load_image(path, width=0, height=0):
    img = image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return transform.scale(img, (width, height))