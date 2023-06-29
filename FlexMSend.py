from linebot.models import (FlexSendMessage)
import datetime
from database import *

def file_name(room,time):
  if room == 'Room 1':
    qr_name_room = '1'
  elif room == 'Room 2':
    qr_name_room = '2'
  elif room == 'Room 3':
    qr_name_room = '3'
  elif room == 'Room 4':
    qr_name_room = '4'

  if time == '8.30':
    qr_name_time = '1'
  elif time == '10.30':
    qr_name_time = '2'
  elif time == '12.30':
    qr_name_time = '3'
  elif time == '14.30':
    qr_name_time = '4'

  file_name = qr_name_room + '-' + qr_name_time
  return file_name

def show_time_in_flex_function_in_info(time):

    if( time == "8.30"):
        showtime = "ช่วงเวลา 8.30 น. - 10.30 น."
        return showtime
    if( time == "10.30"):
        showtime = "ช่วงเวลา 10.30 น. - 12.30 น."
        return showtime
    if( time == "12.30"):
        showtime = "ช่วงเวลา 12.30 น. - 14.30 น."
        return showtime
    if( time == "14.30"):
        showtime = "ช่วงเวลา 14.30 น. - 16.30 น."
        return showtime
    else:
        return None

def show_room_num_in_flex(text):
    a = text
    FlexSelectRoom = FlexSendMessage(
        alt_text='กรุณาเลือกห้องที่ต้องการ',
        contents={
                "type": "bubble",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "กรุณาเลือกห้องที่ต้องการ",
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 1",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 1"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 2",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 2"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 3",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 3"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 4",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 4"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 5",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 5"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 6",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 6"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 7",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 7"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 8",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 8"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 9",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 9"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 10",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 10"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    }
                    ]
                }
                }
        )
    return FlexSelectRoom

def show_room_num(num):
    if "1" in num:
        roomnum = "Room 1"
        return roomnum
    if "2" in num:
        roomnum = "Room 2"
        return roomnum
    if "3" in num:
        roomnum = "Room 3"
        return roomnum
    if "4" in num:
        roomnum = "Room 4"
        return roomnum

def info_flex(StudentID,Time,Num,Day):
    StuID_List = StudentID.split( )
    showtime = show_time_in_flex_function_in_info(Time)

    if len(StuID_List) == 3: 
        FlexShowInfo3 = FlexSendMessage(
        alt_text='รายละเอียดการจองห้อง',
        contents={
            "type": "bubble",
            "direction": "ltr",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "รายละเอียดการจองห้อง",
                    "weight": "bold",
                    "size": "lg",
                    "align": "center",
                    "contents": []
                }
                ]
            },
            "hero": {
                "type": "image",
                "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                "size": "full",
                "aspectRatio": "1.51:1",
                "aspectMode": "fit"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": Num,
                    "weight": "bold",
                    "size": "lg",
                    "align": "center",
                    "contents": []
                },
                {
                    "type": "separator",
                    "margin": "md",
                    "color": "#FFFFFFFF"
                },
                {
                    "type": "text",
                    "text": "รหัสผู้จอง",
                    "weight": "bold",
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[0],
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[1],
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[2],
                    "contents": []
                },
                {
                    "type": "separator",
                    "margin": "lg",
                    "color": "#FFFFFFFF"
                },
                {
                    "type": "text",
                    "text": "ช่วงเวลาในการจอง",
                    "weight": "bold",
                    "contents": []
                },
                {
                    "type": "box",
                    "layout" : "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "วันที่",
                        "flex": 1,
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": Day + " " + showtime,
                        "flex": 7,
                        "color": "#666666",
                        "margin": "none",
                        "size": "sm"
                    }
                    ],
                    "spacing" : "sm"
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ต้องการยืนยันการจองหรือไม่",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md",
                        "color": "#FFFFFFFF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "ยืนยัน",
                            "text": "ยืนยัน"
                            },
                            "style": "primary"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "ย้อนกลับ",
                            "text": "ย้อนกลับ"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "ยกเลิก",
                            "text": "ยกเลิก"
                            },
                            "style": "secondary"
                        }
                        ]
                    }
                    ]
                }
                ]
            }
            }
    )
        return FlexShowInfo3
    elif len(StuID_List) == 4:
        FlexShowInfo4 = FlexSendMessage(
            alt_text='รายละเอียดการจองห้อง',
            contents={
                "type": "bubble",
                "direction": "ltr",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "รายละเอียดการจองห้อง",
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                    }
                    ]
                },
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                    "size": "full",
                    "aspectRatio": "1.51:1",
                    "aspectMode": "fit"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": Num,
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "md",
                        "color": "#FFFFFFFF"
                    },
                    {
                        "type": "text",
                        "text": "รหัสผู้จอง",
                        "weight": "bold",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": StuID_List[0],
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": StuID_List[1],
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": StuID_List[2],
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": StuID_List[3],
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "md",
                        "color": "#FFFFFFFF"
                    },
                    {
                        "type": "text",
                        "text": "ช่วงเวลาในการจอง",
                        "weight": "bold",
                        "contents": []
                    },
                    {
                    "type": "box",
                    "layout" : "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "วันที่",
                        "flex": 1,
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": Day + " " + showtime,
                        "flex": 7,
                        "color": "#666666",
                        "margin": "none",
                        "size": "sm"
                    }
                    ],
                    "spacing" : "sm"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "ต้องการยืนยันการจองหรือไม่",
                                "weight": "bold",
                                "size": "lg",
                                "align": "center",
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "ยืนยัน",
                                "text": "ยืนยัน"
                                },
                                "style": "primary"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "ย้อนกลับ",
                                "text": "ย้อนกลับ"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "ยกเลิก",
                                "text": "ยกเลิก"
                                },
                                "style": "secondary"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                }
                }
        )
        return FlexShowInfo4
    elif len(StuID_List) == 5:
        FlexShowInfo5 = FlexSendMessage(
        alt_text='รายละเอียดการจองห้อง',
        contents={
            "type": "bubble",
            "direction": "ltr",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "รายละเอียดการจองห้อง",
                    "weight": "bold",
                    "size": "lg",
                    "align": "center",
                    "contents": []
                }
                ]
            },
            "hero": {
                "type": "image",
                "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                "size": "full",
                "aspectRatio": "1.51:1",
                "aspectMode": "fit"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": Num,
                    "weight": "bold",
                    "size": "lg",
                    "align": "center",
                    "contents": []
                },
                {
                    "type": "separator",
                    "margin": "md",
                    "color": "#FFFFFFFF"
                },
                {
                    "type": "text",
                    "text": "รหัสผู้จอง",
                    "weight": "bold",
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[0],
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[1],
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[2],
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[3],
                    "contents": []
                },
                {
                    "type": "text",
                    "text": StuID_List[4],
                    "contents": []
                },
                {
                    "type": "separator",
                    "margin": "md",
                    "color": "#FFFFFFFF"
                },
                {
                    "type": "text",
                    "text": "ช่วงเวลาในการจอง",
                    "weight": "bold",
                    "contents": []
                },
                {
                    "type": "box",
                    "layout" : "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "วันที่",
                        "flex": 1,
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": Day + " " + showtime,
                        "flex": 7,
                        "color": "#666666",
                        "margin": "none",
                        "size": "sm"
                    }
                    ],
                    "spacing" : "sm"
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ต้องการยืนยันการจองหรือไม่",
                            "weight": "bold",
                            "size": "lg",
                            "align": "center",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md",
                        "color": "#FFFFFFFF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "ยืนยัน",
                            "text": "ยืนยัน"
                            },
                            "style": "primary"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "ย้อนกลับ",
                            "text": "ย้อนกลับ"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "ยกเลิก",
                            "text": "ยกเลิก"
                            },
                            "style": "secondary"
                        }
                        ]
                    }
                    ]
                }
                ]
            }
            }
    )
        return FlexShowInfo5
    else:
        return None

def show_time_in_flex(text):
    a = text
    FlexSelectTime = FlexSendMessage(
        alt_text='กรุณาเลือกเวลาที่ต้องการ',
        contents={
            "type": "bubble",
            "direction": "ltr",
            "hero": {
                "type": "image",
                "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "กรุณาเลือกเวลาที่ต้องการ",
                    "weight": "bold",
                    "size": "lg",
                    "align": "center",
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "8.30 น. - 10.30 น.",
                                "weight": "regular",
                                "size": "md",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "เลือก",
                                "text": "8.30"
                                },
                                "style": "primary"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "sm",
                        "color": "#FFFFFFFF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "10.30 น. - 12.30 น.",
                                "weight": "regular",
                                "size": "md",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "เลือก",
                                "text": "10.30"
                                },
                                "style": "primary"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "sm",
                        "color": "#FFFFFFFF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "12.30 น. - 14.30 น.",
                                "weight": "regular",
                                "size": "md",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "เลือก",
                                "text": "12.30"
                                },
                                "style": "primary"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "sm",
                        "color": "#FFFFFFFF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "14.30 น. - 16.30 น.",
                                "weight": "regular",
                                "size": "md",
                                "align": "center",
                                "gravity": "center",
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "เลือก",
                                "text": "14.30"
                                },
                                "style": "primary"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                }
                ]
            }
            }
    )
    return FlexSelectTime

def flex_c_time_room(stuid):
    a = stuid
    FlexSelectTimeOrRoom = FlexSendMessage(
        alt_text='กรุณาเลือก ห้อง หรือ เวลา',
        contents={
            "type": "bubble",
            "direction": "ltr",
            "hero": {
                "type": "image",
                "url": "https://sv1.picz.in.th/images/2022/07/23/X4dFqZ.jpg",
                "align": "center",
                "gravity": "center",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                "type": "uri",
                "label": "Line",
                "uri": "https://linecorp.com/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "เลือกรายการที่ต้องการแสดง",
                    "weight": "bold",
                    "size": "lg",
                    "align": "center",
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "flex": 0,
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "ห้อง",
                    "text": "ห้อง"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "ช่วงเวลา",
                    "text": "เวลา"
                    }
                }
                ]
            }
            }
    )
    return FlexSelectTimeOrRoom

# def c_way_flex(word):
    if word == 'ห้อง':
        FlexSelectRoom = FlexSendMessage(
            alt_text='กรุณาเลือก ห้อง',
            contents={
                "type": "bubble",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "กรุณาเลือกห้องที่ต้องการ",
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 1",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 1"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 2",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 2"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 3",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 3"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 4",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 4"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 5",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 5"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 6",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 6"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 7",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 7"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 8",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 8"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 9",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 9"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Room 10",
                                    "weight": "regular",
                                    "size": "lg",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "Room 10"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    }
                    ]
                }
                }
        )
        return FlexSelectRoom
    
    if word == 'เวลา':
        FlexSelectTime = FlexSendMessage(
            alt_text='กรุณาเลือก เวลา',
            contents={
                "type": "bubble",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "กรุณาเลือกเวลาที่ต้องการ",
                        "weight": "bold",
                        "size": "lg",
                        "align": "center",
                        "contents": []
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "8.30 น. - 10.30 น.",
                                    "weight": "regular",
                                    "size": "md",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "8.30"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "10.30 น. - 12.30 น.",
                                    "weight": "regular",
                                    "size": "md",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "10.30"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "12.30 น. - 14.30 น.",
                                    "weight": "regular",
                                    "size": "md",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "12.30"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "sm",
                            "color": "#FFFFFFFF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "14.30 น. - 16.30 น.",
                                    "weight": "regular",
                                    "size": "md",
                                    "align": "center",
                                    "gravity": "center",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "เลือก",
                                    "text": "14.30"
                                    },
                                    "style": "primary"
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    }
                    ]
                }
                }
        )
        return FlexSelectTime

def info_success_flex(StudentID,Time,Num,Day):

    StuID_List = StudentID.split( )
    name_List = CheckUserByID(StudentID)
    showtime = show_time_in_flex_function_in_info(Time)
    id_reserv = get_id_reserv(Num,Time,StudentID,Day)

    if len(StuID_List) == 3: 
        success_info_3 = FlexSendMessage(
            alt_text='รายละเอียดการจองห้อง',
            contents={
                        "type": "bubble",
                        "direction": "ltr",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "รายละเอียดการจองห้อง",
                                "weight": "bold",
                                "size": "lg",
                                "align": "center",
                                "contents": []
                            }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                            "size": "full",
                            "aspectRatio": "1.51:1",
                            "aspectMode": "fit"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": Num,
                                "weight": "bold",
                                "size": "lg",
                                "align": "center",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รหัสผู้จอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[0],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[1],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[2],
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รายชื่อผู้จอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[0] + " " + name_List[1],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[2] + " " + name_List[3],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[4] + " " + name_List[5],
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "ช่วงเวลาในการจอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                            "type": "box",
                            "layout" : "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "วันที่",
                                "flex": 1,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": Day + " " + showtime,
                                "flex": 7,
                                "color": "#666666",
                                "margin": "none",
                                "size": "sm"
                            }
                            ],
                                "spacing" : "sm"
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รหัสสำหรับการขอ QR Code",
                                "weight": "bold",
                                "align": "center",
                                "contents": []
                            },
                             {
                                "type": "text",
                                "text": id_reserv,
                                "align": "center",
                                "size": "xxl",
                                "color": "#666666"
                            }
                            ]
                        }
                        }
        )
        return success_info_3

    elif len(StuID_List) == 4: 
        success_info_4 = FlexSendMessage(
            alt_text='รายละเอียดการจองห้อง',
            contents={
                        "type": "bubble",
                        "direction": "ltr",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "รายละเอียดการจองห้อง",
                                "weight": "bold",
                                "size": "lg",
                                "align": "center",
                                "contents": []
                            }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                            "size": "full",
                            "aspectRatio": "1.51:1",
                            "aspectMode": "fit"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": Num,
                                "weight": "bold",
                                "size": "lg",
                                "align": "center",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รหัสผู้จอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[0],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[1],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[2],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[3],
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รายชื่อผู้จอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[0] + " " + name_List[1],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[2] + " " + name_List[3],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[4] + " " + name_List[5],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[6] + " " + name_List[7],
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "ช่วงเวลาในการจอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                            "type": "box",
                            "layout" : "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "วันที่",
                                "flex": 1,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": Day + " " + showtime,
                                "flex": 7,
                                "color": "#666666",
                                "margin": "none",
                                "size": "sm"
                            }
                            ],
                                "spacing" : "sm"
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รหัสสำหรับการขอ QR Code",
                                "weight": "bold",
                                "align": "center",
                                "contents": []
                            },
                             {
                                "type": "text",
                                "text": id_reserv,
                                "align": "center",
                                "size": "xxl",
                                "color": "#666666"
                            }
                            ]
                        }
                        }
        )
        return success_info_4

    elif len(StuID_List) == 5: 
        success_info_5 = FlexSendMessage(
            alt_text='รายละเอียดการจองห้อง',
            contents={
                        "type": "bubble",
                        "direction": "ltr",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "รายละเอียดการจองห้อง",
                                "weight": "bold",
                                "size": "lg",
                                "align": "center",
                                "contents": []
                            }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://sv1.picz.in.th/images/2022/07/26/XkaDzn.png",
                            "size": "full",
                            "aspectRatio": "1.51:1",
                            "aspectMode": "fit"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": Num,
                                "weight": "bold",
                                "size": "lg",
                                "align": "center",
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รหัสผู้จอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[0],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[1],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[2],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[3],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": StuID_List[4],
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รายชื่อผู้จอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[0] + " " + name_List[1],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[2] + " " + name_List[3],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[4] + " " + name_List[5],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[6] + " " + name_List[7],
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": name_List[8] + " " + name_List[9],
                                "contents": []
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "ช่วงเวลาในการจอง",
                                "weight": "bold",
                                "contents": []
                            },
                            {
                            "type": "box",
                            "layout" : "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "วันที่",
                                "flex": 1,
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": Day + " " + showtime,
                                "flex": 7,
                                "color": "#666666",
                                "margin": "none",
                                "size": "sm"
                            }
                            ],
                                "spacing" : "sm"
                            },
                            {
                                "type": "separator",
                                "margin": "md",
                                "color": "#FFFFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "รหัสสำหรับการขอ QR Code",
                                "weight": "bold",
                                "align": "center",
                                "contents": []
                            },
                             {
                                "type": "text",
                                "text": id_reserv,
                                "align": "center",
                                "size": "xxl",
                                "color": "#666666"
                            }
                            ]
                        }
                        }
        )
        return success_info_5

def qrcode_require_flex_message(passcode,studentidforqrcode):

    day = qrcode_requirement_from_user(studentidforqrcode,passcode)[0]
    start_time = qrcode_requirement_from_user(studentidforqrcode,passcode)[1]
    end_time = qrcode_requirement_from_user(studentidforqrcode,passcode)[2]
    qrcodefilename = find_filename(passcode)
    directory = "qr_codes/"
    http = "https://ebab-49-228-240-42.ngrok.io/"

    QrcodeFlexMessage = FlexSendMessage(
        alt_text='QRCode ของคุณ',
        contents=
        {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "QRCode ของคุณ",
                "size": "xl",
                "weight": "bold",
                "align": "center",
                "color": "#FFFFFF"
            }
            ],
            "backgroundColor": "#1AE65B"
        },
        "body": {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "วันที่ / เวลา :",
                "size": "sm",
                "flex": 1,
                "align": "center",
                "margin": "none"
            },
            {
                "type": "text",
                "text": "วันที่ " + day + " เวลา " + start_time +" - "+ end_time,
                "flex": 2,
                "size": "sm",
                "color": "#696969",
                "align": "center"
            }
            ]
        },
            "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "image",
                "url": http + directory + qrcodefilename,
                "size": "5xl",
                "margin": "xs"
                }
            ]
            }
            }
    )
    return QrcodeFlexMessage
