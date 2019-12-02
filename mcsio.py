#/usr/bin/python3
import time
import sys
import http.client as http
Import urllib
import json
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO.IN,pull_up_down=GPIO.PUD_UP)

deviceId = "DmLid0ga"
deviceKey ="k8cJqZepbj5GLN5g" 
def post_to_mcs(payload): 
	headers = {"Content-type": "application/json", "deviceKey": deviceKey} 
	not_connected = 1 
	while (not_connected):
		try:
			conn = http.HTTPConnection("api.mediatek.com:80")
			conn.connect() 
			not_connected = 0 
		except (http.HTTPException, socket.error) as ex: 
			print ("Error: %s" % ex)
 			time.sleep(10)
			 # sleep 10 seconds 
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close() 

	while true:
		SwitchStatus=GPIO.input(24)
		h0, t0= Adafruit_DHT.read_retry(sensor, pin)
		if Humidity is not None and Temp is not None && SwitchStatus==0:
			print('Temp={0:0.1f}*  Humidity={1:0.1f}% Button pressed'.format(t0, h0))
		
		payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":Humidity}},{"dataChnId":"Temp","values":{"value":Temp}}]} 
		post_to_mcs(payload)
		time.sleep(10) 
		else if h0 is not None and t0 is not None && SwitchStatus!=0:
                        print('Temp={0:0.1f}*  Humidity={1:0.1f}% Button released'

               		payload = {"datapoints":[{"dataChnId":"Hum","values":{"value":humidity}},
					{"dataChnId":"Temp","values":{"value":Temp}},{dataChnId":SwitchStatus","values":{"value":SwitchStatus}}]} 

                post_to_mcs(payload)

		else:
			print('Failed to get reading. Try again!')
			sys.exit(1)
