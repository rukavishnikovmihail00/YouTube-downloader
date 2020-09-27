from tkinter import *
from tkinter.ttk import Combobox, Progressbar
import pytube
import time


def donothing():
    pass
# https://www.youtube.com/watch?v=dSVpA7i-9Pk

def getHelp():
    print("HELP")

def getInfo():
    print("INFO")



def progressCheck(stream, chunk = bytes,  remaining = int):
    #Gets the percentage of the file that has been downloaded.
    percent = (100*(file_size-remaining))/file_size
    print(percent)
    if percent > 99.9:
        download_label = Label(window, text="Видео загружено!", font=("Arial", 18), background='#00a1db')
        download_label.place(x=225, y=100)
        dl_status.destroy()
        window.update()
    


def download(quality, streams_list):
    btn_down.destroy()
    lbl_video.destroy()
    lbl_info.destroy()
    combo.destroy()
    lbl_quality.destroy()
    global dl_status
    dl_status = Label(window, text="Видео загружается...", font=("Arial", 18), background='#00a1db')
    dl_status.place(x=225, y=100)
    window.update()

    quality = str(quality) + 'p'
    temp = 0
    print(quality)
    print(streams_list)
    for video in streams_list:
        if video.resolution==quality:
            temp = video
            break
    global file_size
    file_size = temp.filesize
    

    temp.download('downloads')
    



def clicked():
    res = txt.get()
    
    # https://www.youtube.com/watch?v=Joq6QU9Fm3Y
    try:
        video = pytube.YouTube(res, on_progress_callback=progressCheck)
        name = video.title
        videos = video.streams.filter(progressive=True).all()
    except:
        #print("Некорректная ссылка")
        global error_message
        error_message = Label(window, text="Некорректная ссылка", font=("Arial", 14), background='#00a1db')
        error_message.place(x=230, y=100)
        window.update()
        return 0
    
    streams_list = []
    res_list = []
    res_list_p = []
    count = 0
    for vid in videos:
        count += 1
        if vid.resolution != 'None':
            streams_list.append(vid)
            print(f"{count})", vid.resolution)

    for i in range(len(streams_list)):
        current = streams_list[i].resolution
        res_list_p.append(current)
        current = int(current.replace('p',''))
        res_list.append(current)
    
    global lbl_info
    lbl_info = Label(window, text="Вы планируете загрузить:", background='#00a1db')
    lbl_info.place(x=5,y=5)
    global lbl_video
    lbl_video = Label(window, text=name, font=("Helvetica", 12), background='#54fa2a')
    lbl_video.place(x=5,y=30)

    global btn_down, combo, lbl_quality
    lbl_quality = Label(window, text="Качество:", background='#00a1db')
    lbl_quality.place(x=260, y=60)
    combo = Combobox(window)  
    combo['values'] = res_list  
    combo.current(0)
    combo.place(x=260, y=80)
    print(res_list_p)
    
    btn_down = Button(window, image=file_img_dl,bd=0, command=lambda: download(combo.get(), streams_list))
    btn_down.place(x=256, y=160)
    txt.destroy()
    btn.destroy()
    if error_message != 13:
        error_message.destroy()
    window.update()

    
window = Tk()
window.resizable(height = False, width = False)
window.title("YouTube Downloader")
window.geometry('660x250') 
window.configure(background='#00a1db')


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=donothing)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Помощь", command=getHelp)
helpmenu.add_command(label="Об авторе", command=getInfo)
menubar.add_cascade(label="Информация", menu=helpmenu)

window.config(menu=menubar)

error_message = 13
file_img = PhotoImage(file="buttons/start.gif")
global file_img_dl
file_img_dl = PhotoImage(file="buttons/download.png")
btn = Button(window, text="Начать",image=file_img, bd=0, command=clicked)
btn.place(x=258, y=140)


txt = Entry(window,width=60) 
txt.place(x=150,y=60)


window.mainloop()