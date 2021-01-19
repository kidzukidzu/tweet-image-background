import os
import time
import random
import string
from PIL import Image
from selenium import webdriver
from io import BytesIO
import random
from selenium.webdriver.chrome.options import Options

currentDirectory = os.getcwd()
path = os.path.join(currentDirectory, "tweet") 
pathhasil = os.path.join(currentDirectory, "hasil") 
pathbackground = os.path.join(currentDirectory, "background") 
if not os.path.isdir(path) and not os.path.isdir(pathhasil):
    print('Membuat folder tweet dan hasil')
    os.mkdir(path)
    os.mkdir(pathhasil)

chrome_options = Options()
chrome_options.add_argument("--headless")

url = input("Masukkan link tweet: ")
ukuran = input("Pilih ukuran background\na. 1920x1080\nb. 1080x1920\nMasukkan a/b : ")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
randstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10))
time.sleep(5)
element = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]')
location = element.location
size = element.size
raw_filename = path+"/tweet-"+randstring+".png"
driver.save_screenshot(raw_filename)

x = location['x']
y = location['y']

width = location['x']+size['width']
height = location['y']+size['height']

im = Image.open(raw_filename)
im = im.crop((int(x), int(y), int(width), int(height)))
im.save(raw_filename)


if ukuran == 'a' :
    imagebackground = ['background1.jpg', 'background2.jpg', 'background3.jpg', 'background4.jpg']
    tweetposition = [(1100, 600), (100, 300), (100, 600), (1100, 100)]
    background = Image.open("background/"+random.choice(imagebackground))
elif ukuran == 'b':
    imagebackground = ['backgroundandro1.jpg', 'backgroundandro2.jpg', 'backgroundandro3.jpg', 'backgroundandro4.jpg']
    tweetposition = [(100, 100), (400, 100), (400, 1100), (100, 1250)]
    background = Image.open("background/"+random.choice(imagebackground))

print(background)
tweet = Image.open(raw_filename)
tweet.putalpha(185)

background.paste(tweet, random.choice(tweetposition), tweet)
path_filename = pathhasil+"/"+randstring+".png"
background.save(path_filename)
print("\n\ngambar disimpan difolder hasil dengan nama "+randstring+".png")