'''

 .d8888b.  888 d8b          888                             .d8888b.  888 d8b          888                       
d88P  Y88b 888 Y8P          888                            d88P  Y88b 888 Y8P          888                       
888    888 888              888                            888    888 888              888                       
888        888 888  .d8888b 888  888  .d88b.  888d888      888        888 888  .d8888b 888  888  .d88b.  888d888 
888        888 888 d88P"    888 .88P d8P  Y8b 888P"        888        888 888 d88P"    888 .88P d8P  Y8b 888P"   
888    888 888 888 888      888888K  88888888 888          888    888 888 888 888      888888K  88888888 888     
Y88b  d88P 888 888 Y88b.    888 "88b Y8b.     888          Y88b  d88P 888 888 Y88b.    888 "88b Y8b.     888     
 "Y8888P"  888 888  "Y8888P 888  888  "Y8888  888           "Y8888P"  888 888  "Y8888P 888  888  "Y8888  888     
                                                                                                                 
                                                                                                                 
                                                                                                                 
v0.1.0

Github @JUST7LING
https://nogotit.tistory.com

'''

# IMPORT
import pyautogui
import tkinter
import threading
import time
import keyboard
from PIL import Image, ImageTk

# GUI
window = tkinter.Tk()
window.title("Clicker Clicker")
window.geometry("400x420")

icon = tkinter.PhotoImage(file="./cookie.png")
window.iconphoto(True, icon)

# IMAGE
cookie_image = Image.open("./cookie.png")
cookie_image = cookie_image.resize((130, 130))
cookie_tk_image= ImageTk.PhotoImage(cookie_image)
cookie_label = tkinter.Label(window, image=cookie_tk_image)
cookie_label.place(x=135, y=25)

# INIT SETTING

''' 좌표 '''
x = 0
y = 0

''' 메시지 '''
alert_color = "#4264ad"
warning_color = "#911719"
init_alert = "클릭할 영역 위에 프로그램을 겹치고\n'쿠키 위치 맞추기' 버튼을 누르세요."

''' 클릭 속도 '''
click_per_sec = 1
click_per_sec_var = tkinter.IntVar(value=click_per_sec)
max_click_speed = 5
min_click_speed = 1

''' 클릭 유지 '''
continue_click = True

''' 알림/경고 '''
alert_message = tkinter.StringVar()
alert_message.set(init_alert)

# ACTIONS
def locate():
    global x, y
    x, y = pyautogui.position()
    
def alert(message, is_warning):
    alert_message.set(message)
    if is_warning:
        alert_message_label.config(fg=warning_color)
        return
    alert_message_label.config(fg=alert_color)
        
    
def click_per_sec_setter(i):
    global click_per_sec
    if i > max_click_speed :
        alert(f"클릭 횟수는 {max_click_speed}를 초과할 수 없습니다!", True)
        return

    if i < min_click_speed :
        alert(f"클릭 횟수는 {min_click_speed} 이상이어야 합니다!", True)
        return
    click_per_sec = i
    click_per_sec_var.set(i)
    alert(f"1초에 {i}번 클릭이 수행됩니다.", False)
    
    
def speed_up():
    click_per_sec_setter(click_per_sec + 1)

def speed_down():
    click_per_sec_setter(click_per_sec - 1)
    
def stop():
    global continue_click
    continue_click = False
    alert(init_alert)

def stop_trigger():
    keyboard.wait('esc')
    stop()

def click():
    def click_loop():
        global continue_click
        interval = 1 / click_per_sec
        alert("ESC 버튼을 눌러 멈출 수 있습니다.", False)
        continue_click = True
        while continue_click:
            pyautogui.click(x, y)
            time.sleep(interval)
    threading.Thread(target=click_loop).start()
    threading.Thread(target=stop_trigger).start()
    
# GUI_BUTTONS
locate_button = tkinter.Button(window, text="쿠키 위치 맞추기", command=locate)
locate_button.place(x=50, y=175, width=150, height=40)

start_button = tkinter.Button(window, text="클릭 시작하기", command=click)
start_button.place(x=50, y=225, width=150, height=40)

stop_button = tkinter.Button(window, text="클릭 멈추기", command=stop)
stop_button.place(x=210, y=175, width=140, height=90)

click_speed_up_button = tkinter.Button(window, text="▲", command=speed_up)
click_speed_up_button.place(x=350, y=270, width=40, height=40)

click_speed_down_button = tkinter.Button(window, text="▼", command=speed_down)
click_speed_down_button.place(x=350, y=370, width=40, height=40)

# GUI_LABELS
speed_label = tkinter.Label(window, textvariable=click_per_sec_var)
speed_label.place(x=350, y=315, width=40, height=50)

alert_message_label = tkinter.Label(window, textvariable=alert_message, fg=alert_color)
alert_message_label.place(x=50, y=315, width=250, height=40)

window.attributes("-topmost", True)
window.mainloop()
