import sys
import random
#import urllib.request
import urllib

image_url = "http://status.co.il/wp-content/uploads/2015/09/rosh-hashana-600x350.jpg"

def download_image(image_url):
    urllib.urlretrieve(image_url, "sv.jpg")
    print image_url

def download_image_targil(image_url):
    pic_name = random.randrange(1, 1000)
    full_name = str(pic_name) + '.jpg'
    urllib.urlretrieve(image_url, full_name)

def main():
    download_image(image_url)
    download_image_targil(image_url)
if __name__ == '__main__':
   main()