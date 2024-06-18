from imageai.Detection import ObjectDetection
import os
import cv2
from gtts import gTTS
from translate import Translator
from playsound import playsound
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24

print("Distance Mesurement In Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
print("Waiting for Sensor Data")
translator=Translator(from_lang ='english',to_lang='telugu')

def detect1(cnt):
 execution_path = os.getcwd()
 detector = ObjectDetection()
 detector.setModelTypeAsRetinaNet()
 detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
 detector.loadModel()
 detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "images.jpg"),output_image_path=os.path.join(execution_path, "imagenew.jpg"))
 print(detections)

 for eachObject in detections:
 print(eachObject["name"], " : ", eachObject["percentage_probability"])
 result = translator.translate(eachObject["name"])
 res = "hello" + " " + result + " " + "vundhi" + " " + str(distance) + " " + "distance"
 tts = gTTS(text=res, lang='te')
 print(res)
 tts.save('hello.mp3')
 playsound('hello.mp3')
 os.remove('hello.mp3')
 return

cap = cv2.VideoCapture(0)
print('camera is initialized')
count = 0
while (True):
 # Capture frame-by-frame
 ret, frame = cap.read()
 # do what you want with frame
 # and then save to file
 cv2.imwrite('/Users/Tejaswini/PycharmProjects/project4/venv/Scripts/images.jpg', frame)
 count = count + 1
 img = cv2.imread('images.JPG')
 cv2.imshow("images1", img)
 GPIO.output(TRIG, False)
 time.sleep(2)
 GPIO.output(TRIG, True)
 time.sleep(0.00001)
 GPIO.output(TRIG, False)
 while GPIO.input(ECHO) == 0:

 pulse_start = time.time()
 while GPIO.input(ECHO) == 1:
 pulse_end = time.time()
 pulse_duration = pulse_end - pulse_start
 # 34300=Distance/Time/2, 17150=Distance/Time, 17150 X Time = Distance (cm)
 distance = pulse_duration * 17150
 distance = round(distance, 0)
 if (distance < 15):
    detect1(count)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()