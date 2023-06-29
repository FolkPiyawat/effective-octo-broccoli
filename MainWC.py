from datetime import timedelta, datetime
import cv2 
import serial
import time
from database import *
from threading import Thread

# from testarduino import *
ArduinoUnoSerial = serial.Serial(port='COM5', baudrate=115200, timeout=.1) #create Serial object *REMEMBER to check the number of COM
print(ArduinoUnoSerial.readline()) #read the serial data and print it as line
print("You have new message from Arduino")

tasks1 = []
tasks2 = []
tasks3 = []
tasks4 = []

status1 = {'door' : 'open'}
status2 = {'door' : 'open'}
status3 = {'door' : 'open'}
status4 = {'door' : 'open'}

# ------------------------------- TASK #1 -------------------------------- #

def close_door1():
    status1['door'] = 'close'
    ArduinoUnoSerial.write('b'.encode())

def open_door1():
    status1['door'] = 'open'
    ArduinoUnoSerial.write('a'.encode())
    add_task1(5, 'close_door1')

def check_task1():
    current_time = datetime.datetime.now()
    if tasks1:
        for task in tasks1:
            if current_time >= task['target-time']:
                if task['function'] == 'close_door1':
                    close_door1()
                    tasks1.remove(task)
                if task['function'] == 'open_door1':
                    open_door1()
                    tasks1.remove(task)

def add_task1(in_seconds, function_name):
    current_time = datetime.datetime.now()
    target = current_time + timedelta(seconds=in_seconds)
    task = {
        'target-time' : target,
        'function' : function_name
    }
    tasks1.append(task)

# ------------------------------- TASK #1 -------------------------------- #

# ------------------------------- TASK #2 -------------------------------- #
def close_door2():
    status2['door'] = 'close'
    ArduinoUnoSerial.write('d'.encode())

def open_door2():
    status2['door'] = 'open'
    ArduinoUnoSerial.write('c'.encode())
    add_task2(5, 'close_door2')

def check_task2():
    current_time = datetime.datetime.now()
    if tasks2:
        for task in tasks2:
            if current_time >= task['target-time']:
                if task['function'] == 'close_door2':
                    close_door2()
                    tasks2.remove(task)
                if task['function'] == 'open_door2':
                    open_door2()
                    tasks2.remove(task)

def add_task2(in_seconds, function_name):
    current_time = datetime.datetime.now()
    target = current_time + timedelta(seconds=in_seconds)
    task = {
        'target-time' : target,
        'function' : function_name
    }
    tasks2.append(task)

# ------------------------------- TASK #2 -------------------------------- #

# ------------------------------- TASK #3 -------------------------------- #

def close_door3():
    status3['door'] = 'close'
    ArduinoUnoSerial.write('f'.encode())

def open_door3():
    status3['door'] = 'open'
    ArduinoUnoSerial.write('e'.encode())
    add_task3(5, 'close_door3')

def check_task3():
    current_time = datetime.datetime.now()
    if tasks3:
        for task in tasks3:
            if current_time >= task['target-time']:
                if task['function'] == 'close_door3':
                    close_door3()
                    tasks3.remove(task)
                if task['function'] == 'open_door3':
                    open_door3()
                    tasks3.remove(task)

def add_task3(in_seconds, function_name):
    current_time = datetime.datetime.now()
    target = current_time + timedelta(seconds=in_seconds)
    task = {
        'target-time' : target,
        'function' : function_name
    }
    tasks3.append(task)

# ------------------------------- TASK #3 -------------------------------- #

# ------------------------------- TASK #4 -------------------------------- #

def close_door4():
    status4['door'] = 'close'
    ArduinoUnoSerial.write('h'.encode())

def open_door4():
    status4['door'] = 'open'
    ArduinoUnoSerial.write('g'.encode())
    add_task4(5, 'close_door4')

def check_task4():
    current_time = datetime.datetime.now()
    if tasks4:
        for task in tasks4:
            if current_time >= task['target-time']:
                if task['function'] == 'close_door4':
                    close_door4()
                    tasks4.remove(task)
                if task['function'] == 'open_door4':
                    open_door4()
                    tasks4.remove(task)

def add_task4(in_seconds, function_name):
    current_time = datetime.datetime.now()
    target = current_time + timedelta(seconds=in_seconds)
    task = {
        'target-time' : target,
        'function' : function_name
    }
    tasks4.append(task)

# ------------------------------- TASK #4 -------------------------------- #

# define a video capture object
vid1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# vid2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
# vid3 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
# vid4 = cv2.VideoCapture(3, cv2.CAP_DSHOW)

detector = cv2.QRCodeDetector()

# ------------------------- LIGHT CONTROL ROOM - 1 ------------------------ #
def light_control_r_1(datafromqrcode):

	timestamp_hour = datetime.datetime.now().hour
	timestamp_minute = datetime.datetime.now().minute
	action_time = timedelta(hours=timestamp_hour,minutes=timestamp_minute)

	end_hour = get_time_for_control_light(datafromqrcode)[0]				
	end_minute = get_time_for_control_light(datafromqrcode)[1]
	end_time = timedelta(hours=int(end_hour),minutes=int(end_minute))

	find_second = end_time - action_time
	time_for_light_control = timedelta.total_seconds(find_second)

	ArduinoUnoSerial.write('i'.encode())
	time.sleep(time_for_light_control)
	ArduinoUnoSerial.write('j'.encode())
# ------------------------- LIGHT CONTROL ROOM - 1 ------------------------ #

# ------------------------- LIGHT CONTROL ROOM - 2 ------------------------ #
def light_control_r_2(datafromqrcode):

	timestamp_hour = datetime.datetime.now().hour
	timestamp_minute = datetime.datetime.now().minute
	action_time = timedelta(hours=timestamp_hour,minutes=timestamp_minute)

	end_hour = get_time_for_control_light(datafromqrcode)[0]				
	end_minute = get_time_for_control_light(datafromqrcode)[1]
	end_time = timedelta(hours=int(end_hour),minutes=int(end_minute))

	find_second = end_time - action_time
	time_for_light_control = timedelta.total_seconds(find_second)

	ArduinoUnoSerial.write('k'.encode())
	time.sleep(time_for_light_control)
	ArduinoUnoSerial.write('l'.encode())
# ------------------------- LIGHT CONTROL ROOM - 2 ------------------------ #

# ------------------------- LIGHT CONTROL ROOM - 3 ------------------------ #
def light_control_r_3(datafromqrcode):

	timestamp_hour = datetime.datetime.now().hour
	timestamp_minute = datetime.datetime.now().minute
	action_time = timedelta(hours=timestamp_hour,minutes=timestamp_minute)

	end_hour = get_time_for_control_light(datafromqrcode)[0]				
	end_minute = get_time_for_control_light(datafromqrcode)[1]
	end_time = timedelta(hours=int(end_hour),minutes=int(end_minute))

	find_second = end_time - action_time
	time_for_light_control = timedelta.total_seconds(find_second)

	ArduinoUnoSerial.write('m'.encode())
	time.sleep(time_for_light_control)
	ArduinoUnoSerial.write('n'.encode())
# ------------------------- LIGHT CONTROL ROOM - 3 ------------------------ #

# ------------------------- LIGHT CONTROL ROOM - 4 ------------------------ #
def light_control_r_4(datafromqrcode):

	timestamp_hour = datetime.datetime.now().hour
	timestamp_minute = datetime.datetime.now().minute
	action_time = timedelta(hours=timestamp_hour,minutes=timestamp_minute)

	end_hour = get_time_for_control_light(datafromqrcode)[0]				
	end_minute = get_time_for_control_light(datafromqrcode)[1]
	end_time = timedelta(hours=int(end_hour),minutes=int(end_minute))

	find_second = end_time - action_time
	time_for_light_control = timedelta.total_seconds(find_second)

	ArduinoUnoSerial.write('o'.encode())
	time.sleep(time_for_light_control)
	ArduinoUnoSerial.write('p'.encode())
# ------------------------- LIGHT CONTROL ROOM - 4 ------------------------ #

while True:

	check_task1()
	check_task2()
	check_task3()
	check_task4()

	timenow = datetime.datetime.now()
	hourstr = timenow.strftime("%H")
	minutstr = timenow.strftime("%M")
	hourtostr = hourstr + "." + minutstr
	
	ret, frame1 = vid1.read()
	# ret, frame2 = vid2.read()
	# ret, frame3 = vid3.read()
	# ret, frame4 = vid4.read()

	data_from_qrcode_1,bbox,_ = detector.detectAndDecode(frame1)
	# data_from_qrcode_2,bbox,_ = detector.detectAndDecode(frame2)
	# data_from_qrcode_3,bbox,_ = detector.detectAndDecode(frame3)
	# data_from_qrcode_4,bbox,_ = detector.detectAndDecode(frame4)

# --------------------------------- Room - 1 ----------------------------------- #

	if data_from_qrcode_1:
		if "Room 2" in check_qr_code(data_from_qrcode_1):
			if  float(get_time_for_qr_scan(data_from_qrcode_1)[0]) <= float(hourtostr) and float(get_time_for_qr_scan(data_from_qrcode_1)[1]) >= float(hourtostr):
				open_door2()
				Thread(target=light_control_r_2,args=(data_from_qrcode_1,)).start()
			else:
				print("Not this time")
		else:
			print("ไม่มีห้อง 1")
	
	# if ShowBusyRoom1() == None:
		# time.sleep(0.015625)
		# print("Loop Continue Room 1")
		# ArduinoUnoSerial.write('j'.encode())
	# elif float(ShowBusyRoom1()) <= float(hourtostr):
		# time.sleep(0.015625)
		# print("In Else Room 1")
		# ArduinoUnoSerial.write('i'.encode())

# --------------------------------- Room - 1 ----------------------------------- #

# --------------------------------- Room - 2 ----------------------------------- #

	# if data_from_qrcode_2:
	# 	if "Room 2" in check_qr_code(data_from_qrcode_2):
	# 		if  float(get_time_for_qr_scan(data_from_qrcode_2)[0]) <= float(hourtostr) and float(get_time_for_qr_scan(data_from_qrcode_2)[1]) >= float(hourtostr):
	# 			open_door2()
	# 			Thread(target=light_control_r_2,args=(data_from_qrcode_2,)).start
	# 		else:
	# 			print("Not this time")
	# 	else:
	# 		print("ไม่มีห้อง 2")
	

	# if ShowBusyRoom2() == None:
		# time.sleep(0.015625)
		# print("Loop Continue Room 2")
	# 	ArduinoUnoSerial.write('l'.encode())
	# elif float(ShowBusyRoom2()) <= float(hourtostr):
		# time.sleep(0.015625)
		# print("In Else Room 2")
		# ArduinoUnoSerial.write('k'.encode())

# --------------------------------- Room - 2 ----------------------------------- #

# --------------------------------- Room - 3 ----------------------------------- #

	# if data_from_qrcode_3:
	# 	if "Room 3" in check_qr_code(data_from_qrcode_3):
	# 		if  float(get_time_for_qr_scan(data_from_qrcode_3)[0]) <= float(hourtostr) and float(get_time_for_qr_scan(data_from_qrcode_3)[1]) >= float(hourtostr):
	# 			open_door3()
	# 			Thread(target=light_control_r_3,args=(data_from_qrcode_3,)).start
	# 		else:
	# 			print("Not this time")
	# 	else:
	# 		print("ไม่มีห้อง 3")

	# if ShowBusyRoom3() == None:
		# time.sleep(0.015625)
		# print("Loop Continue Room 3")
		# ArduinoUnoSerial.write('n'.encode())
	# elif float(ShowBusyRoom3()) <= float(hourtostr):
		# time.sleep(0.015625)
		# print("In Else Room 3")
		# ArduinoUnoSerial.write('m'.encode())

# --------------------------------- Room - 3 ----------------------------------- #

# --------------------------------- Room - 4 ----------------------------------- #
	
	# if data_from_qrcode_4:
	# 	if "Room 4" in check_qr_code(data_from_qrcode_4):
	# 		if  float(get_time_for_qr_scan(data_from_qrcode_4)[0]) <= float(hourtostr) and float(get_time_for_qr_scan(data_from_qrcode_4)[1]) >= float(hourtostr):
	# 			open_door4()
	# 			Thread(target=light_control_r_4,args=(data_from_qrcode_4,)).start
	# 		else:
	# 			print("Not this time")
	# 	else:
	# 		print("ไม่มีห้อง 4")


	# if ShowBusyRoom4() == None:
		# time.sleep(0.015625)
		# print("Loop Continue Room 4")
		# ArduinoUnoSerial.write('p'.encode())
	# elif float(ShowBusyRoom4()) <= float(hourtostr):
		# time.sleep(0.015625)
		# print("In Else Room 4")
		# ArduinoUnoSerial.write('o'.encode())

# --------------------------------- Room - 4 ----------------------------------- #

	cv2.imshow('QRcode Detector 1', frame1)
	# cv2.imshow('QRcode Detector 2', frame2)
	# cv2.imshow('QRcode Detector 3', frame3)
	# cv2.imshow('QRcode Detector 4', frame4)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()

