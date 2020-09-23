from tkinter import *
from tkinter.ttk import Combobox 
import pytube


def download(quality, streams_list):
    btn_down.destroy()
    combo.destroy()
    lbl = Label(window, text="Видео загружается", font=("Arial Bold", 10))
    lbl.grid(column=1, row=9)
    window.update()

    quality = str(quality) + 'p'
    temp = 0
    print(quality)
    print(streams_list)
    for video in streams_list:
        if video.resolution==quality:
            temp = video
            break
    temp.download('downloads')
    



def clicked():
    res = txt.get()
    
    # https://www.youtube.com/watch?v=Joq6QU9Fm3Y
    try:
        video = pytube.YouTube(res)
        name = video.title
        videos = video.streams.filter(progressive=True).all()
    except:
        #print("Некорректная ссылка")
        error_message = Label(window, text="Некорректная ссылка", font=("Arial Bold",10))
        error_message.grid(column=1, row=10)
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
    
    lbl = Label(window, text=name, font=("Arial Bold", 10))
    lbl.grid(column=1, row=6)

    global btn_down, combo
    combo = Combobox(window)  
    combo['values'] = res_list  
    combo.current(0)
    combo.grid(column=1, row=7)
    print(res_list_p)
    
    btn_down = Button(window, text="Скачать", command=lambda: download(combo.get(), streams_list))
    btn_down.grid(column=1,row=8)
    txt.destroy()
    btn.destroy()
    window.update()

    
    
window = Tk()
window.resizable(height = False, width = False)
window.title("YouTube Downloader")
window.geometry('600x250') 


btn = Button(window, text="Начать", command=clicked)
btn.grid(column=1, row=2) 


txt = Entry(window,width=100)  
txt.grid(column=1, row=0)



window.mainloop()