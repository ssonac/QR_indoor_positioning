from picamera import PiCamera
from time import sleep
import time
import requests
import os

url='http://192.168.0.180:8000/upload'
camNum = '1'
camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()

while(True):
	sleep(1)

	image_time =str(time.time())
	image_name = image_time+'_' + camNum + '.jpg'

	camera.capture('/home/pi/o4ocart/%s'%image_name)
	file={'content':open('/home/pi/o4ocart/%s' %image_name,'rb')}
	param = {'image_name': image_name}
	req=requests.post(url,files=file, params = param )
	os.remove('/home/pi/o4ocart/%s' %image_name)

	req_result = req.content
	print(req_result)

camera.stop_preview()

