import datetime
import pymongo
import random
import qrcode
import os
import time as T
from calendar import monthrange
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DBForProject"]

# ---------------------------------------------------- QR Code Function ---------------------------------------------- 
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def genqrcode(data,room,time,day):

  Day = str(day)

  if room == 'Room 1':
    qr_name_room = '1'
  elif room == 'Room 2':
    qr_name_room = '2'
  elif room == 'Room 3':
    qr_name_room = '3'
  elif room == 'Room 4':
    qr_name_room = '4'
  elif room == 'Room 5':
    qr_name_room = '5'
  elif room == 'Room 6':
    qr_name_room = '6'
  elif room == 'Room 7':
    qr_name_room = '7'
  elif room == 'Room 8':
    qr_name_room = '8'
  elif room == 'Room 9':
    qr_name_room = '9'
  elif room == 'Room 10':
    qr_name_room = '10'

  if time == '8.30':
    qr_name_time = '1'
  elif time == '10.30':
    qr_name_time = '2'
  elif time == '12.30':
    qr_name_time = '3'
  elif time == '14.30':
    qr_name_time = '4'

  file_name = qr_name_room + '-' + qr_name_time +"-"+ str(Day) +'.png'
  qr = qrcode.QRCode(version=1, box_size=10,border=2)

  qr.add_data(data)
  qr.make(fit = True)

  img = qr.make_image(fill = 'black', back_color = 'white')
  img.save("qr_codes/"+file_name)
  return file_name

def check_qr_code(data):
    index = []
    today = datetime.date.today()
    collection_ticket = mydb["ticket"]
    myquery = {"QRCode" : data ,"Date" : str(today.day)}
    mydoc = collection_ticket.find(myquery)
    for data_in_ticket in mydoc:
      print("Data in ticket find by QRCode :",data_in_ticket)
      index.append(data_in_ticket["Room"])
    return index

def get_time_for_qr_scan(data):
  time = []
  fail = ["9999" , "99999" , "999999"]
  collection_ticket = mydb["ticket"]
  myquery = {"QRCode" : data}
  mydoc = collection_ticket.find(myquery)
  for x in mydoc:
    time.append(x["Start-Time"])
    time.append(x["End-Time"])
  if time == []:
    return fail
  else:
    return time

# ---------------------------------------------------- QR Code Function ---------------------------------------------- 

# ---------------------------------------------------- Function ROOM ----------------------------------------------- 
def ShowEmptyRoom(): # ฟังก์ชั่นแสดงห้องที่ว่าง
  mycol = mydb["room"]
  myquery = { "Status": "empty" }
  mydoc = mycol.find(myquery)
  roomList = []
  for x in mydoc:
    print(x)
    roomList.append(x)
    print("Room List",roomList)
  return x,roomList

def ShowBusyRoom1():
  mycol = mydb["room"]
  time = datetime.datetime.now()
  today = time.strftime("%d")
  hour = time.strftime("%H")
  secon = time.strftime("%M")
  hoursec = hour + "." + secon

  room1 = {"Room":"Room 1","Status": "busy", "Date" : today}

  mydocR1 = mycol.find(room1)

  room1List = None

  for x in mydocR1:
    if float(hoursec) >= float(x["Start-Time"]) and float(hoursec) <= float(x["End-Time"]):
      room1List = float(x["Start-Time"])

  return room1List

def ShowBusyRoom2():
  mycol = mydb["room"]
  time = datetime.datetime.now()
  today = time.strftime("%d")
  hour = time.strftime("%H")
  secon = time.strftime("%M")
  hoursec = hour + "." + secon

  room2 = {"Room":"Room 2","Status": "busy", "Date" : today}

  mydocR2 = mycol.find(room2)

  room2List = None

  for x in mydocR2:
    if float(hoursec) >= float(x["Start-Time"]) and float(hoursec) <= float(x["End-Time"]):
      room2List = float(x["Start-Time"])

  return room2List

def ShowBusyRoom3():
  mycol = mydb["room"]
  time = datetime.datetime.now()
  today = time.strftime("%d")
  hour = time.strftime("%H")
  secon = time.strftime("%M")
  hoursec = hour + "." + secon

  room3 = {"Room":"Room 3","Status": "busy", "Date" : today}

  mydocR3 = mycol.find(room3)

  room3List = None

  for x in mydocR3:
    if float(hoursec) >= float(x["Start-Time"]) and float(hoursec) <= float(x["End-Time"]):
      room3List = float(x["Start-Time"])

  return room3List

def ShowBusyRoom4():
  mycol = mydb["room"]
  time = datetime.datetime.now()
  today = time.strftime("%d")
  hour = time.strftime("%H")
  secon = time.strftime("%M")
  hoursec = hour + "." + secon

  room4 = {"Room":"Room 4","Status": "busy", "Date" : today}

  mydocR4 = mycol.find(room4)

  room4List = None

  for x in mydocR4:
    if float(hoursec) >= float(x["Start-Time"]) and float(hoursec) <= float(x["End-Time"]):
      room4List = float(x["Start-Time"])

  return room4List

def SelectTimeToShow(time): # ฟังก์ชั่นเลือกเวลาเพื่อแสดงห้องที่ว่าง
  mycol = mydb["room"]
  myquery = { "Start-Time": time , "Status" : "empty"}
  mydoc = mycol.find(myquery)
  room_list = []
  for x in mydoc:
    room_list.append(x['Room'])
  return room_list

def SelectRoomToShow(room): # ฟังก์ชั่นเลือกห้องเพื่อแสดงช่วงเวลาที่ห้องว่าง 
  time = datetime.datetime.now()
  time2 = time.strftime("%d")
  time_list = []
  y = []
  mycol = mydb["roomTest"]
  myquery = {"Room" : room , "Date" : time2}
  myquery2 = {"Room" : room}
  mydoc = mycol.find(myquery)
  mydoc2 = mycol.find(myquery2)
  for a in mydoc:
      y.append(a["Start-Time"])
  for b in mydoc2:
    time_list.append(b["Start-Time"])
  list_to_show = [i for i in time_list if i not in y]
  return list_to_show
  
def time_for_info_room(time):
  timenow = datetime.datetime.now()
  today = timenow.strftime("%d")
  mycol = mydb["room"]
  myquery = { "Start-Time": time , "Date" : today , "Status" : "empty"}
  mydoc = mycol.find(myquery)
  room_List = []
  for x in mydoc:
    room_List.append(x["Room"])
  return room_List

def SelectOwnerToShow(Owner): # ฟังก์ชั่นค้นหาห้องที่ทำการจองไว้ ด้วยรหัสนักศึกษา
  mycol = mydb["room"]
  myquery = { "Owner": Owner }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print(x)
    if x == None:
      return False
    else:
      return True

def SelectOwnerToShowV2(Owner):
  Ownerlist = Owner.split( )
  data = []
  for x in range(len(Ownerlist)):
    mycol = mydb["room"]
    myquery = { "Owner": Ownerlist[x] }
    mydoc = mycol.find(myquery)
    for y in mydoc:
      data.append(y)
    if data == []:
      return False
    else:
      return True

def get_data_before_set_empty_room(Owner):
  if SelectOwnerToShow(Owner) == True:
    mycol = mydb['room']
    myquery = { "Owner" : Owner}
    mydoc = mycol.find(myquery)
    data = []
    for x in mydoc:
      data.append(x["Room"])
      data.append(x["Start-Time"])
    return data
  
def SetStatusRoomToEmpty(passcode,studentid): # ฟังก์ชั่นแก้ไขสถานะให้เป็นห้องว่าง
  dataforfilename = []
  collection_ticket = mydb["ticket"]
  myquery = {"_id" : passcode, "Student-ID" : {"$in" : studentid}}
  for index_for_delete in collection_ticket.find(myquery):
    dataforfilename.append(index_for_delete["Room"])
    dataforfilename.append(index_for_delete["Start-Time"])
    dataforfilename.append(index_for_delete["Date"])
  if dataforfilename[0] == "Room 1":
    namepart1 = "1-"
  elif dataforfilename[0] == "Room 2":
    namepart1 = "2-"
  elif dataforfilename[0] == "Room 3":
    namepart1 = "3-"
  elif dataforfilename[0] == "Room 4":
    namepart1 = "4-"

  if dataforfilename[1] == "8.30":
    namepart2 = "1-"
  elif dataforfilename[1] == "10.30":
    namepart2 = "2-"
  elif dataforfilename[1] == "12.30":
    namepart2 = "3-"
  elif dataforfilename[1] == "14.30":
    namepart2 = "4-"
  namepart3 = dataforfilename[2]
  filename = namepart1 + namepart2 + namepart3 +(".png")
  T.sleep(0.015625)
  if os.path.exists(filename):
    os.remove(filename)
    print("Room Cleared")
  
def SetStatusRoomToBusy(room,time,stuid,day): # ฟังก์ชั่นแก้ไขสถานะให้เป็นห้องไม่ว่าง
  mycol = mydb["ticket"]
  stuid_list = stuid.split( )
  data_qr = random.uniform(10,1000)
  data_qr_str = str(data_qr)
  keynum = random.randrange(999999999, 10000000000)

  if time == "8.30":
    start_time = "8.30"
    end_time = "10.30"
  elif time == "10.30":
    start_time = "10.30"
    end_time = "12.30"
  elif time == "12.30":
    start_time = "12.30"
    end_time = "14.30"
  elif time == "14.30":
    start_time = "14.30"
    end_time = "16.30"

  myquery = {
    "_id" : str(keynum),
    "Date" : str(day),
    "Room" : room,
    "Start-Time" : start_time,
    "End-Time" : end_time,
    "StudentID" : stuid_list,
    "QRCode" : data_qr_str
  }
  mycol.insert_one(myquery)

  if os.path.exists(genqrcode(data_qr,room,time,day)):
    os.remove(genqrcode(data_qr,room,time,day))
  T.sleep(0.015625)
  genqrcode(data_qr,room,time,day)
  print("Added Successful")

def GetDataDateRoom(stuid):
  stuid_list = stuid.split(' ')
  time = datetime.datetime.now()
  time2 = time.strftime("%d")
  date = []

  for x in range(len(stuid_list)):
    mycol = mydb["room"]
    myquery = {"Owner" : stuid_list[x]}
    mydoc = mycol.find(myquery)
    for y in mydoc:
      if int(y["Date"]) == int(time2):
        date.append(y["Date"])
        return date

def date_room():
  time = datetime.datetime.now()
  today = time.strftime("%d")
  boolean = True
  mycol = mydb["room"]
  myquery = {"Date" : today}
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print(x)
    if x:
      boolean = False
      return boolean
    else:
      return boolean

def get_id_reserv(room,time,stuid,day):
  collection_ticket = mydb["ticket"]
  stuidList = stuid.split(' ')
  query = {"StudentID" : {"$in" : stuidList}, "Room" : room, "Start-Time" : time, "Date" : day}
  for id_in_ticket in collection_ticket.find(query):
    id_reserv = id_in_ticket["_id"]
  return id_reserv

# ---------------------------------------------------- END Function ROOM ----------------------------------------------- 
  
# ---------------------------------------------------- Function USER --------------------------------------------------- 

def ShowAllUser(): # ฟังก์ชั่นแสดงรายชื่อ USER ทั้งหมด
  mycol = mydb["user"]
  for x in mycol.find({},{ "_id" : 0,"Student ID": 1, "Name": 1, "LastName": 1, "Major": 1}):
    print(x)

def CheckUserByID(StudentID): #ฟังก์ชั่นค้นหา USER จากรหัสนักศึกษา
  mycol = mydb["user"]
  StudentID = StudentID.split(" ")
  items = mycol.find({"Student ID" : {"$in" : StudentID}})
  count = len(StudentID)
  foundcount = 0
  y = []
  for x in items:
    foundcount += 1
    y.append(x['Name'])
    y.append(x["LastName"])
    print(x)
  if count != foundcount:
    return False
  else:
    return y

def CheckUserByName(Name): #ฟังก์ชั่นค้นหา USER จากชื่อนักศึกษา
  mycol = mydb["user"]
  myquery = {"Name" : Name,}
  mycol.find_one(myquery)
  x = mycol.find_one(myquery)
  print(x)

def CheckUserByLastName(LastName): #ฟังก์ชั่นค้นหา USER จากนามสกุลนักศึกษา
  mycol = mydb["user"]
  myquery = {"LastName" : LastName,}
  mycol.find_one(myquery)
  x = mycol.find_one(myquery)
  print(x)

# ---------------------------------------------------- END Function USER ----------------------------------------------- 

def CheckStudentIDinDatabase(stucheck): #ฟังก์ชั่นตรวจสอบว่ามีรหัสนักศึกษาที่ผู้ใช้ป้อนอยู่ในระบบหรือไม่
  mycol = mydb["user"]
  stucheck = stucheck.split(" ")
  items = mycol.find({"Student ID" : {"$in" : stucheck}})
  count = len(stucheck)
  foundcount = 0
  y = []
  for x in items:
    foundcount += 1
    y.append(x['Name'])
    print(x)
  if count != foundcount:
    return False
  else:
    return True

def find_filename(passcode):
  collection_ticket = mydb["ticket"]
  myquery = {"_id" : passcode}
  mydoc = collection_ticket.find(myquery)
  ticket_data = []
  for data_in_ticket in mydoc:
    ticket_data.append(data_in_ticket["Room"])
    ticket_data.append(data_in_ticket["Start-Time"])

  if "Room 1" in ticket_data:
    if "8.30" in ticket_data:
      filename = "1-1"
    if "10.30" in ticket_data:
      filename = "1-2"
    if "12.30" in ticket_data:
      filename = "1-3"
    if "14.30" in ticket_data:
      filename = "1-4"
    
  elif "Room 2" in ticket_data:
    if "8.30" in ticket_data:
      filename = "2-1"
    if "10.30" in ticket_data:
      filename = "2-2"
    if "12.30" in ticket_data:
      filename = "2-3"
    if "14.30" in ticket_data:
      filename = "2-4"

  elif "Room 3" in ticket_data:
    if "8.30" in ticket_data:
      filename = "3-1"
    if "10.30" in ticket_data:
      filename = "3-2"
    if "12.30" in ticket_data:
      filename = "3-3"
    if "14.30" in ticket_data:
      filename = "3-4"

  elif "Room 4" in ticket_data:
    if "8.30" in ticket_data:
      filename = "4-1"
    if "10.30" in ticket_data:
      filename = "4-2"
    if "12.30" in ticket_data:
      filename = "4-3"
    if "14.30" in ticket_data:
      filename = "4-4"

  thelastname =filename +"-"+ data_in_ticket["Date"]+".png"

  return thelastname

def day_avaliable(Studentid,reserv_time,reserv_room):
  collection_ticket = mydb["ticket"]
  today = datetime.date.today()
  dayofmonth = monthrange(today.year,today.month)[1]
  delta2 = datetime.timedelta(days = today.day)
  delta3 = dayofmonth - delta2.days
  dayList = ["กรุณาพิมวันที่ต้องการจอง :"]
  remove_date = []
  StudentList = Studentid.split(' ')
  for index_in_query in range(delta3 + 1):
    date = today.day + index_in_query
    dayList.append(str(date))
    myquery = {"Date" : str(date), "Start-Time" : reserv_time, 
              "StudentID" : {"$in" : StudentList}, "Room" : reserv_room}
    for index_of_ticket in collection_ticket.find(myquery):
      dayList.remove(index_of_ticket["Date"])
  for index_in_query_in_for in range(delta3 + 1):
    date = today.day + index_in_query_in_for
    myquery2 = {"Date" : str(date), "Start-Time" : reserv_time,
                "Room" : reserv_room}
    for index_of_ticket2 in collection_ticket.find(myquery2):
      dayList.remove(index_of_ticket2["Date"])
      remove_date.append(index_of_ticket2["Date"])
      dayaval = [i for i in dayList if i not in remove_date]
  return dayList

def qrcode_requirement_from_user(StudentID,Passcode):
  collection_ticket = mydb["ticket"]
  stuList = StudentID.split(" ")
  myquery = {"_id" : Passcode, "StudentID" : {"$in" : stuList}}
  
  for index_of_qrcode in collection_ticket.find(myquery):
    day = index_of_qrcode["Date"]
    starttime = index_of_qrcode["Start-Time"]
    endtime = index_of_qrcode["End-Time"]
  return day,starttime,endtime

def check_passcode_with_studentid(passcode,studentcode):
  collection_ticket = mydb["ticket"]
  myquery = {"_id" : passcode, "StudentID" : studentcode}
  checkList = []
  for checkindex in collection_ticket.find(myquery):
    checkList.append(checkindex)
  if checkList == []:
    return False
  else:
    return True

def DeleteDataTicket(StudentIDCCRoom,Passcode):
  collection_ticket = mydb["ticket"]
  dataforfilename = []
  StudentIDCCRoomList = StudentIDCCRoom.split(" ")
  query = {"_id" : Passcode, "StudentID" : {"$in":StudentIDCCRoomList}}
  for index_in_ticket in collection_ticket.find(query):
    print("Index in Collection Ticket :",index_in_ticket)
    dataforfilename.append(index_in_ticket["Room"])
    dataforfilename.append(index_in_ticket["Start-Time"])
    dataforfilename.append(index_in_ticket["Date"])
    if index_in_ticket:
      if dataforfilename[0] == "Room 1":
        namepart1 = "1-"
      elif dataforfilename[0] == "Room 2":
        namepart1 = "2-"
      elif dataforfilename[0] == "Room 3":
        namepart1 = "3-"
      elif dataforfilename[0] == "Room 4":
        namepart1 = "4-"
      elif dataforfilename[0] == "Room 5":
        namepart1 = "5-"
      elif dataforfilename[0] == "Room 6":
        namepart1 = "6-"
      elif dataforfilename[0] == "Room 7":
        namepart1 = "7-"
      elif dataforfilename[0] == "Room 8":
        namepart1 = "8-"
      elif dataforfilename[0] == "Room 9":
        namepart1 = "9-"
      elif dataforfilename[0] == "Room 10":
        namepart1 = "10-"

      if dataforfilename[1] == "8.30":
        namepart2 = "1-"
      elif dataforfilename[1] == "10.30":
        namepart2 = "2-"
      elif dataforfilename[1] == "12.30":
        namepart2 = "3-"
      elif dataforfilename[1] == "14.30":
        namepart2 = "4-"
      namepart3 = dataforfilename[2]
      filename = namepart1 + namepart2 + namepart3 +(".png")

      T.sleep(0.015625)
      
      if os.path.exists(filename):
        os.remove(filename)
        print("Room Cleared")
      collection_ticket.delete_one(query)
      return True
    else:
      return False

def get_time_for_control_light(qrcode):
  collection_ticket = mydb["ticket"]
  myquery = {"QRCode" : qrcode}
  dummyList = ["0","0"]
  for document in collection_ticket.find(myquery):
    find_time = document["End-Time"]
    timeList = find_time.split(".")
    if document != None:
      return timeList
  return dummyList

def get_Room_List():
  collection_ticket = mydb["roomTest"]
  roomList = []
  for data_room_in_ticket in collection_ticket.find({}):
    roomList.append(data_room_in_ticket["Room"])
  return roomList
