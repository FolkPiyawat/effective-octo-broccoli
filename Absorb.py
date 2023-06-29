from flask import Flask, request, abort, send_from_directory, send_file
from os import getcwd
from linebot import (
    LineBotApi, 
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TextMessage,
    FlexSendMessage
)

import time

#----------------------------- File --------------------------------------#

from database import *
from FlexMSend import *

#----------------------------- File --------------------------------------#

app = Flask(__name__)
line_bot_api = LineBotApi('C4krgSGdcn2E7b+G8IhkXlG+fRKrRtpQRsYRb4R4WGBHRSScZoQ5mCV+ad2J/RwHfsvkc0HfKcIxUdRNboLjhMKXVuhhEOhO09wQZZ/MArQgO7e43yRCsfGZ729e6JDMmutHbt7zizrs2v60gEJGFAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('218cf7c06686a017fdec641da3e21f56')

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@app.route("/qr_codes/<string:image_name>")
def img(image_name):
    directory = getcwd() + "/qr_codes/"
    print("request access to", image_name)
    try:
        return send_from_directory(directory,path = image_name)
    except FileNotFoundError:
        abort(404)

userList = {}

#------------------------------ Function -----------------------------------#

def isUserAvaliable(user_id): # Function เช็คว่ามี ID Line นี้ใน User หรือไม่
    if user_id in userList:
        return True
    else:
        return False

def getUserState(user_id): # Function โชว์ State ของ User ที่กำลังทำรายการ
    if isUserAvaliable(user_id):
        return userList[user_id]["State"]
    else:
        return None

def setUserState(user_id, State):
    if isUserAvaliable(user_id):
        userList[user_id]["State"] = State

def addUserID(user_id):
    userList[user_id] = {}

def checkStuID(stuID_list):
    a = True
    for x in stuID_list:
        if not x[11] == "-": ## ในกรณีที่รหัสนักศึกษาในช่องที่ 12 ไม่ใช่ - (Ex 62543206036-0) 
            a = False
    return a

def listToString(s): 
    # initialize an empty string
    str1 = " " 
    # return string  
    return (str1.join(s))

def studentid_for_cc_room(user_id,studentidforccroom):
    if isUserAvaliable(user_id):
        userList[user_id]["Student-ID"] = studentidforccroom

def passcode_for_cc_room(user_id,passcode):
    if isUserAvaliable(user_id):
        userList[user_id]["Pass-CCRoom"] = passcode

def pass_for_qrcode_require(user_id,passcode):
    if isUserAvaliable(user_id):
        userList[user_id]["Pass-QRCode"] = passcode

def student_id_require_qrcode(user_id,studentidrequire):
    if isUserAvaliable(user_id):
        userList[user_id]["Student-ID"] = studentidrequire

def stu_id_for_reservation(user_id,studentID):
    if isUserAvaliable(user_id):
        userList[user_id]["Student-ID"] = studentID

def room_num_for_reservation(user_id,roomNum):
    if isUserAvaliable(user_id):
        userList[user_id]["Room-Number"] = roomNum

def room_time_for_reservation(user_id,roomtime):
    if isUserAvaliable(user_id):
        userList[user_id]["Room-Time"] = roomtime

def day_for_reservation(user_id,studentID):
    if isUserAvaliable(user_id):
        userList[user_id]["Day"] = studentID

def get_studentid_for_cc_room(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Student-ID"]

def get_passcode_for_cc_room(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Pass-CCRoom"]

def get_passcode_qrcode_require(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Pass-QRCode"]
    else:
        return None

def get_student_id_require_qecode(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Student-ID"]
    else:
        return None

def get_day_for_reservation(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Day"]
    else:
        return None

def get_stu_id_for_reservation(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Student-ID"]
    else:
        return None

def get_room_num_for_reservation(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Room-Number"]
    else:
        return None

def get_room_time_for_reservation(user_id):
    if isUserAvaliable(user_id):
        return userList[user_id]["Room-Time"]
    else:
        return None

#------------------------------ End Function -----------------------------------#

roomList = get_Room_List()
timeList = ["8.30", "10.30", "12.30", "14.30"]
Student_ID_List = []

#------------------------------ Main -------------------------------------------#

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    if event.message.text == "จองห้อง":
        addUserID(user_id)
        print(userList)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "กรุณากรอกรหัสนักศึกษาตั้งแต่ 3 คนขึ้นไป แต่ไม่เกิน 5 คนสำหรับการจองห้อง (เว้นวรรคเพื่อแบ่งจำนวน)"))
        setUserState(user_id,"wait_Student_ID")
    
    if event.message.text == "ยกเลิกการจองห้อง":
        addUserID(user_id)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "กรุณากรอกรหัสนักศึกษา"))
        setUserState(user_id,"wait_Student_ID_For_CC_Room_Reser")
        print(userList)
    
    if event.message.text == "ขอ QR Code":
        addUserID(user_id)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "กรุณากรอกรหัสนักศึกษาที่ใช้ในการจองห้องเพียง 1 ท่าน"))
        setUserState(user_id,"StudentID_QRCode_require")

    elif getUserState(user_id) == "StudentID_QRCode_require":
        print(userList)
        if CheckStudentIDinDatabase(event.message.text) == True:
            student_id_require_qrcode(user_id,event.message.text)
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "รหัสนักศึกษาไม่ถูกต้อง กรูณาลองใหม่อีกครั้ง"))
            return
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "กรอกรหัส QR Code ของวันที่ต้องการ"))
        setUserState(user_id,"QRCode_require")

    elif getUserState(user_id) == "QRCode_require":
        print(userList)
        pass_for_qrcode_require(user_id,event.message.text)
        passcode = get_passcode_qrcode_require(user_id)
        studentidforqrcode = get_student_id_require_qecode(user_id)
        if check_passcode_with_studentid(passcode,studentidforqrcode) == True:
            line_bot_api.reply_message(event.reply_token,qrcode_require_flex_message(passcode,studentidforqrcode))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "ไม่พบข้อมูลที่ตรงกัน กรุณาทำรายการใหม่อีกครั้ง"))
        pass_for_qrcode_require(user_id," ")
        student_id_require_qrcode(user_id," ")
        setUserState(user_id," ")

    elif getUserState(user_id) == "wait_Student_ID_For_CC_Room_Reser":
        print(userList)
        studentid_for_cc_room(user_id,event.message.text)
        ID_cc_room_reser = get_studentid_for_cc_room(user_id)
        if CheckUserByID(ID_cc_room_reser) != False:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "กรุณากรอกรหัส QRCode ของห้องที่ต้องการทำรายการ"))
            setUserState(user_id,"wait_passcode_for_cc_room")
        else:
            print(CheckUserByID(ID_cc_room_reser))
            setUserState(user_id,"wait_Student_ID_For_CC_Room_Reser")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "รหัสนักศึกษาไม่ถูกต้อง"))
        return
    
    elif getUserState(user_id) == "wait_passcode_for_cc_room":
        print(userList)
        passcode_for_cc_room(user_id,event.message.text)
        passcodeforccroom = get_passcode_for_cc_room(user_id)
        ID_cc_room_reser = get_studentid_for_cc_room(user_id)
        print(get_studentid_for_cc_room(user_id))
        if DeleteDataTicket(ID_cc_room_reser,passcodeforccroom) == True:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "ทำการยกเลิกการจองห้องเรียบร้อยแล้ว"))
            setUserState(user_id," ")
            passcode_for_cc_room(user_id,"")
            studentid_for_cc_room(user_id,"")
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "ไม่พบข้อมูลดังกล่าว กรุณาทำรายการใหม่อีกครั้ง"))
            setUserState(user_id,"")
            passcode_for_cc_room(user_id,"")
            studentid_for_cc_room(user_id,"")

    elif getUserState(user_id) == "wait_Student_ID":
        Student_ID = event.message.text
        Student_List = Student_ID.split( )
        stu_id_for_reservation(user_id,Student_ID)
        print(userList)
        if len(Student_List) >= 3 and len(Student_List) <= 5:
            if CheckStudentIDinDatabase(Student_ID) == True:
                setUserState(user_id,"wait_Select")
                line_bot_api.reply_message(event.reply_token,flex_c_time_room(Student_ID))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "รหัสนักศึกษาไม่ถูกต้อง"))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "กรุณาใส่รหัสนักศึกษาไม่ต่ำกว่า 3 คน และไม่เกิน 5 คน"))
        return
 
    elif getUserState(user_id) == "wait_Select":
        if event.message.text == "ห้อง":
            print(userList)
            setUserState(user_id,"wait_Room")
            line_bot_api.reply_message(event.reply_token,show_room_num_in_flex(event.message.text))
        if event.message.text == "เวลา":
            print(userList)
            setUserState(user_id,"wait_Time")
            line_bot_api.reply_message(event.reply_token,show_time_in_flex(event.message.text))

    elif getUserState(user_id) == "wait_Room":
        if event.message.text in roomList:
            room_num_for_reservation(user_id,event.message.text)
            print(userList)
            line_bot_api.reply_message(event.reply_token,show_time_in_flex(event.message.text))
            setUserState(user_id,"Selec_Room_wait_Time")
        
        elif event.message.text == "ย้อนกลับ":
            setUserState(user_id,"wait_Select")
            line_bot_api.reply_message(event.reply_token,flex_c_time_room(event.message.text))

    elif getUserState(user_id) == "wait_Time":
        if event.message.text in timeList:
            room_time_for_reservation(user_id,event.message.text)
            print(userList)
            line_bot_api.reply_message(event.reply_token,show_room_num_in_flex(event.message.text))
            setUserState(user_id,"Selec_Time_wait_Room")

        if event.message.text == "ย้อนกลับ":
            setUserState(user_id,"wait_Select")
            line_bot_api.reply_message(event.reply_token,flex_c_time_room(event.message.text))

    elif getUserState(user_id) == "Selec_Room_wait_Time":
        # if event.message.text in (listToString(SelectRoomToShow(get_room_num_for_reservation(user_id)))):
        if event.message.text in timeList:
            setUserState(user_id,"wait_User_Selec_Day")
            room_time_for_reservation(user_id,event.message.text)
            Studentcode = get_stu_id_for_reservation(user_id)
            roomresev = get_room_num_for_reservation(user_id)
            timereserv = get_room_time_for_reservation(user_id)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = listToString(day_avaliable(Studentcode,timereserv,roomresev))))
            setUserState(user_id,"wait_User_Selec_Day")
            print(userList)
            
        elif event.message.text == "ย้อนกลับ":
            setUserState(user_id,"wait_Select")
            line_bot_api.reply_message(event.reply_token,flex_c_time_room(event.message.text))
        
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text= "เกิดข้อผิดพลาด"))

    elif getUserState(user_id) == "Selec_Time_wait_Room":
        if event.message.text in roomList:
            setUserState(user_id,"wait_User_Selec_Day")
            room_num_for_reservation(user_id,event.message.text)
            Studentcode = get_stu_id_for_reservation(user_id)
            roomresev = get_room_num_for_reservation(user_id)
            timereserv = get_room_time_for_reservation(user_id)
            dayListText = listToString(day_avaliable(Studentcode,timereserv,roomresev))
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = dayListText))
            print(userList)

        if event.message.text == "ย้อนกลับ":
            setUserState(user_id,"wait_Select")
            line_bot_api.reply_message(event.reply_token,flex_c_time_room(event.message.text))

    elif getUserState(user_id) == "wait_User_Selec_Day" :
        Studentcode = get_stu_id_for_reservation(user_id)
        roomresev = get_room_num_for_reservation(user_id)
        timereserv = get_room_time_for_reservation(user_id)
        if event.message.text in day_avaliable(Studentcode,timereserv,roomresev):
            setUserState(user_id,"wait_User_CF_Reserv_Room")
            day_for_reservation(user_id,event.message.text)
            dayreserv = get_day_for_reservation(user_id)
            line_bot_api.reply_message(event.reply_token,info_flex(Studentcode,timereserv,roomresev,dayreserv))
        
        elif event.message.text not in day_avaliable(Studentcode,timereserv,roomresev):
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "กรุณาพิมพ์วันที่ว่างเพื่อทำการลงเวลาจองห้อง"))
            return
            
        elif event.message.text == "ย้อนกลับ":
            setUserState(user_id,"wait_Select")
            line_bot_api.reply_message(event.reply_token,flex_c_time_room(event.message.text))

    elif getUserState(user_id) == "wait_User_CF_Reserv_Room":
        if event.message.text == "ยืนยัน":
            Room = get_room_num_for_reservation(user_id)
            Time = get_room_time_for_reservation(user_id)
            StudentID = get_stu_id_for_reservation(user_id)
            Day = get_day_for_reservation(user_id)

            setUserState(user_id, "")
            SetStatusRoomToBusy(Room,Time,StudentID,Day)
            line_bot_api.reply_message(event.reply_token,info_success_flex(StudentID,Time,Room,Day))
            room_num_for_reservation(user_id," ")
            room_time_for_reservation(user_id," ")
            stu_id_for_reservation(user_id," ")
            day_for_reservation(user_id," ")

        if event.message.text == "ย้อนกลับ":
            setUserState(user_id,"wait_Select")
            room_num_for_reservation(user_id, "")
            room_time_for_reservation(user_id, "")
            day_for_reservation(user_id," ")
            line_bot_api.reply_message(event.reply_token,flex_c_time_room(event.message.text))

        if event.message.text == "ยกเลิก":
            setUserState(user_id, "")
            room_num_for_reservation(user_id," ")
            room_time_for_reservation(user_id," ")
            stu_id_for_reservation(user_id," ")
            day_for_reservation(user_id," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "ต้องการทำรายการใด จองห้อง หรือ เช็คสถานะการจองห้อง"))

#------------------------------ Main -------------------------------------------#

if __name__ == "__main__":
    app.run(debug = True)