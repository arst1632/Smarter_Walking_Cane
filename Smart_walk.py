# cook your code here
import subprocess
import requests
import RPi.GPIO as GPIO
import base64
import time
import pyttsx
from espeak import espeak
import numpy as np
espeak.synth("Helloo! This is your assistant. push button for describing your surrounding.")

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP )
def imagedescription():
                        subprocess.call("fswebcam -d/dev/video0  -r 640x480 -S 20 /home/pi/client_img/image/image.jpg",shell=True) 
			print('PIC CAPTURED')
			with open("/home/pi/client_img/image/image.jpg", "rb") as image_file:
			#with open("/home/pi/1.jpg","rb") as image_file:
			#encoded_string = base64.b64encode(image_file.read())
			#print type(encoded_string), type(image_file), image_file
                                r = requests.post("http://192.168.0.254:9004/getimage", files={'media': open('/home/pi/client_img/image/image.jpg','rb')})
                                print(r.status_code, r.reason)
                                print(r.text)
				#f = open("~/abc.jpg","w+")
                                '''engine = pyttsx.init()
                                engine.say(r.text)
                                engine.runAndWait()
                                '''
                                espeak.synth(r.text)



try:

	while True:
		
		

                TRIGL = 5
                ECHOL = 6
                TRIGR = 12
                ECHOR = 13
                TRIGF1 = 22
                ECHOF1 = 23
                TRIGF2 = 26
                ECHOF2 = 20
                ledpin = 21
                GPIO.setup(TRIGL, GPIO.OUT)
                GPIO.setup(ECHOL, GPIO.IN)
                GPIO.setup(TRIGR, GPIO.OUT)
                GPIO.setup(ECHOR, GPIO.IN)
                GPIO.setup(TRIGF1, GPIO.OUT)
                GPIO.setup(ECHOF1, GPIO.IN)
                GPIO.setup(TRIGF2, GPIO.OUT)
                GPIO.setup(ECHOF2, GPIO.IN)
                GPIO.setup(ledpin, GPIO.OUT)
                GPIO.output(ledpin,True)
                time.sleep(2)
                GPIO.output(ledpin,False)
                while True:
                  GPIO.output(TRIGL, False)
                  time.sleep(.002)
                  GPIO.output(TRIGL, True)
                  time.sleep(0.01)
                  GPIO.output(TRIGL, False)

                  while GPIO.input(ECHOL)==0:
                    pulse_start = time.time()
                    
                  pulse_end=pulse_start
                  while GPIO.input(ECHOL)==1 and (pulse_end-pulse_start)<=.020:
                    pulse_end = time.time()
                  pulse_durationL = pulse_end - pulse_start
                 
                   
                  GPIO.output(TRIGR, False)
                  time.sleep(.002)
                  GPIO.output(TRIGR, True)
                  time.sleep(0.01)
                  GPIO.output(TRIGR, False)

                  while GPIO.input(ECHOR)==0:
                    pulse_start = time.time()
                  pulse_end=pulse_start
                  while GPIO.input(ECHOR)==1 and (pulse_end-pulse_start)<=.020:
                    pulse_end = time.time()
                  pulse_durationR = pulse_end - pulse_start

                  GPIO.output(TRIGF1, False)
                  time.sleep(.002)
                  GPIO.output(TRIGF1, True)
                  time.sleep(0.01)
                  GPIO.output(TRIGF1, False)
                 


                  while GPIO.input(ECHOF1)==0:
                    pulse_start = time.time()
                  pulse_end=pulse_start
                  while GPIO.input(ECHOF1)==1 and (pulse_end-pulse_start)<=.020:
                    pulse_end = time.time()
                  pulse_durationF1 = pulse_end - pulse_start

                  GPIO.output(TRIGF2, False)
                  time.sleep(.002)
                  GPIO.output(TRIGF2, True)
                  time.sleep(0.01)
                  GPIO.output(TRIGF2, False)

                  while GPIO.input(ECHOF2)==0:
                    pulse_start = time.time()
                  pulse_end=pulse_start
                  while GPIO.input(ECHOF2)==1 and (pulse_end-pulse_start)<=.020:
                    pulse_end = time.time()
                  pulse_durationF2 = pulse_end - pulse_start
                  pulse_duration_array = np.array([pulse_durationL,pulse_durationR,pulse_durationF1,pulse_durationF2])
                  minpulse_duration = min(pulse_duration_array)
                  mindistance = minpulse_duration * 17150
                  mindistance = round(mindistance, 2)
                  print (mindistance)

                  if mindistance > 1 and mindistance < 100:
                      {  # voice output 'obstacle'
                          GPIO.output(ledpin,True)
                      }
                  else:
                      {
                          GPIO.output(ledpin,False)
                      }
                  distanceF1 = pulse_durationF1 * 17150
                  print (distanceF1)

                  distanceF2 = pulse_durationF2 * 17150
                  print (distanceF2)

                  distanceF_array = np.array ([distanceF1,distanceF2])
                  distanceF = min(distanceF_array)

                  distanceL = pulse_durationL * 17150
                  print (distanceL)

                  distanceR = pulse_durationR * 17150
                  print (distanceR)
                  if distanceF < 100 and distanceL > 100 and distanceR > 100:
                      text = "forward obstacle"
                      espeak.synth(text) 
                      time.sleep(2)
                      if GPIO.input(18)==0:
                              imagedescription()

                  if distanceF > 100 and distanceL < 100 and distanceR > 100:
                      text = "left obstacle"
                      espeak.synth(text) 
                      time.sleep(2)
                      if GPIO.input(18)==0:
                              imagedescription()

                  if distanceF > 100 and distanceL > 100 and distanceR < 100:
                      text = "right obstacle"
                      espeak.synth(text) 
                      time.sleep(2)
                      if GPIO.input(18)==0:
                              imagedescription()

                  if distanceF < 100 and distanceL < 100 and distanceR > 100:
                      text = "forward left obstacle"
                      espeak.synth(text) 
                      time.sleep(2)
                      if GPIO.input(18)==0:
                              imagedescription()

                  if distanceF < 100 and distanceL > 100 and distanceR < 100:
                      text = "forward right obstacle"
                      espeak.synth(text) 
                      time.sleep(2)
                      if GPIO.input(18)==0:
                              imagedescription()

                  if distanceF > 100 and distanceL < 100 and distanceR < 100:
                      text = "left right obstacle"
                      espeak.synth(text) 
                      time.sleep(2)
                      if GPIO.input(18)== 0:
                              imagedescription()

                  if distanceF < 100 and distanceL < 100 and distanceR < 100:
                      text = "obstacle everywhere"
                      espeak.synth(text) 
                      time.sleep(2)
                      if GPIO.input(18) == 0:
                              imagedescription()

                  if distanceF > 100 and distanceL > 100 and distanceR > 100:
                      time.sleep(2)
                      if GPIO.input(18) == 0:
                              imagedescription()

                  distanceL0 = distanceL
                  distanceR0 = distanceR

                  #bluetooth remote operation

			
                        

                
except KeyboardInterrupt:
	GPIO.cleanup()

