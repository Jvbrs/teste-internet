# import
from tkinter import*
from PIL import Image, ImageTk
import speedtest
#cores
co0 = "#000"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue
# criando visual
visual = Tk ()
visual.title ("")
visual.geometry('350x200')
visual.configure(background=co0)
visual.resizable(width=FALSE, height=FALSE)#tamanho fisico

# divisão logo

divisao_logo = Frame(visual, width=350, height=60, background=co4)
divisao_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
imagem = Image.open('icon.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

dimg = Label(divisao_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg= co4, fg=co3)
dimg.place(x=20, y=0)

diname = Label(divisao_logo, text='Speed Test', padx=10, anchor=NE, font=('Ivy 20'), bg=co4, fg=co3)
diname.place(x=75, y=10)

diline = Label(divisao_logo, width=350, anchor=NE, font=('Ivy 2'), bg=co1)
diline.place(x=0, y=57)


#divisão resto
divisao_resto = Frame(visual, width=350, height=140, background=co3)
divisao_resto.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#function
def main(): 
    speed = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"
     
    downloadtext['text'] = download
    uploadtext['text'] = upload

#upandown

downloadtext = Label(divisao_resto, text='', anchor=NW, font=('arial 18'), bg=co3, fg=co4)
downloadtext.place(x=44, y=25)
down = Label(divisao_resto, text='Mbps download', anchor=NW, font=('Ivy 10'), bg=co3, fg=co4)
down.place(x=30, y=70)

imagemdown = Image.open('down.png')
imagemdown = imagemdown.resize((55,55))
imagemdown = ImageTk.PhotoImage(imagemdown)
downimg = Label(divisao_resto, height=60, image=imagemdown, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg= co3, fg=co3)
downimg.place(x=130, y=35)

uploadtext = Label(divisao_resto, text='', anchor=NW, font=('arial 18'), bg=co3, fg=co4)
uploadtext.place(x=235, y=25)
up = Label(divisao_resto, text='Mbps upload', anchor=NW, font=('Ivy 10'), bg=co3, fg=co4)
up.place(x=230, y=70)

imagemup = Image.open('up.png')
imagemup = imagemup.resize((55,55))
imagemup = ImageTk.PhotoImage(imagemup)
upimg = Label(divisao_resto, height=60, image=imagemup, compound=RIGHT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg= co3, fg=co3)
upimg.place(x=170, y=35)

buttonstart = Button(divisao_resto, command=main, text='Verificar Velocidade', font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co4)
buttonstart.place(x=110, y=100)










visual.mainloop()