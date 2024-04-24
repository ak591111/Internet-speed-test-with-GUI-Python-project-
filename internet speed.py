
from tkinter import*
import speedtest
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downloading = str(round(sp.download()/(10**6),3)) + " Mbps"
    uploading = str(round(sp.upload()/(10**6),3)) + " Mbps"
    lab_down.config(text=downloading)
    lab_up.config(text=uploading)


sp = Tk()
sp.title("INTERNET SPEED TEST")
sp.geometry('800x600')


sp.config(bg='black')
lab = Label(sp,text="INTERNET SPEED TEST",font=("Time New Roman",30,"bold"),bg="White",fg="Red")
lab.place(x=100 ,y=40,height=50,width=480)


 
lab = Label(sp,text="DOWNLOAD SPEED",font=("Time New Roman",30,"bold"))
lab.place(x=100 ,y=130,height=50,width=480)



lab_down = Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_down.place(x=100 ,y=200,height=50,width=480)



lab = Label(sp,text="UPLOAD SPEED",font=("Time New Roman",30,"bold"))
lab.place(x=100 ,y=290,height=50,width=480)


lab_up = Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_up.place(x=100 ,y=360 ,height=50,width=480)


button = Button(sp, text="CHECK SPEED", font=("Time New Roman",30,"bold"), bg="Red", command=speedcheck)
button.place(x=100 ,y=460,height=50,width=480)

sp.mainloop()
