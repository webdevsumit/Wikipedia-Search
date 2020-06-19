from tkinter import *
from wikipedia import *
from tkinter.font import Font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
cur_file="no_file"
def fnt4():
	fonts.config(size=4)
def fnt8():
	fonts.config(size=8)
def fnt12():
	fonts.config(size=12)
def fnt16():
	fonts.config(size=16)
def fnt20():
	fonts.config(size=20)
def fnt24():
	fonts.config(size=24)
def fnt28():
	fonts.config(size=28)
def fnt32():
	fonts.config(size=32)
def fnt36():
	fonts.config(size=36)
def fnt40():
	fonts.config(size=40)
def fnt44():
	fonts.config(size=44)
def fnt48():
	fonts.config(size=48)
def fnt52():
	fonts.config(size=52)
def fnt56():
	fonts.config(size=56)
def fnt60():
	fonts.config(size=60)
def fnt64():
	fonts.config(size=64)
def fnt68():
	fonts.config(size=68)
def fnt72():
	fonts.config(size=72)

	
def abt():
	messagebox.showinfo("ABOUT","Wikipedia search with notepad \n by SUMIT DHAKAD")

def copy_txt():
	text.clipboard_clear()
	text.clipboard_append(text.selection_get())

def cut_txt():
	copy_txt()
	try:
		text.delete("sel.first" , "sel.last")
	except:
		pass
		
def paste_txt():
	text.insert(INSERT,text.clipboard_get())
	
def weigh():
	fonts.config(weight="normal")
def weigh2():
	fonts.config(weight="bold")
def sln():
	fonts.config(slant="roman")
def sln2():
	fonts.config(slant="italic")
	
def bclr():
	cllr=colorchooser.askcolor()
	text.config(background=cllr[1])

def fclr():
	cllr=colorchooser.askcolor()
	text.config(foreground=cllr[1])

def text_del():
	text.delete(1.0,END)
	
def quit_root():
	l=messagebox.askyesno("Confirming","Do you close it ?")
	if l==1:
		root.destroy()
def open_file():
	try:
		file=filedialog.askopenfile(initialdir="/sdcard",title="select file to open",filetypes=(("text files" , "*.txt"),("all files" , "*.*")))
		for item in file:
			text.insert(INSERT, item)
		file.close()
	except:
		pass

def save_as_file():
	try:
		file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
		if file is None:
			return
		file.write(text.get(1.0,END))
		messagebox.showinfo("Infoation","Saved Successfully")
		cur_file=file.name
		file.close()
	except:
		text.insert(INSERT," FIRST WRITE SOMETHING ! ")

def sh():
	text.delete(1.0,END)
	try:
		ans=summary(entry.get())
		text.insert(INSERT, ans)
	except:
		text.insert(INSERT,"Check your string or internet connection.")
def save_file():
	if cur_file=="no_file":
		save_as_file()
	else:
		fl=open(cur_file, "w+")
		fl.write(text.get(1.0,END))
def new_file():
	text_del()
	cur_file="no_file"
try:
	root=Tk()
	root.title("Wikipedia search")
	fonts=Font(family="",size=7,weight="normal",slant="roman")
	
	root.config(background="#414e4e")
	menu=Menu(root)
	
	root.config(menu=menu)
	submenu=Menu(menu)
	menu.add_cascade(label="File",menu=submenu)
	submenu.add_command(label="New",command=new_file)
	submenu.add_command(label="Open",command=open_file)
	submenu.add_command(label="Clear",command=text_del)
	submenu.add_separator()
	submenu.add_command(label="Save",command=save_file)
	submenu.add_command(label="Save as",command=save_as_file)
	submenu.add_separator()
	submenu.add_command(label="Quit",command=quit_root)
	
	editmenu=Menu(menu,tearoff=False)
	menu.add_cascade(label="Edit",menu=editmenu)
	editmenu.add_command(label="copy",command=copy_txt)
	editmenu.add_command(label="cut",command=cut_txt)
	editmenu.add_command(label="paste",command=paste_txt)
	
	formate=Menu(menu)
	menu.add_cascade(label="Formate",menu=formate)
	formate.add_command(label="Foreground colour",command=fclr)
	formate.add_command(label="Background colour",command=bclr)
	formate.add_separator()
	slan=Menu(formate)
	formate.add_cascade(label="Slant",menu=slan)
	slan.add_command(label="Normal",command=sln)
	slan.add_command(label="Italic",command=sln2)
	weight=Menu(formate)
	formate.add_cascade(label="Weight",menu=weight)
	weight.add_command(label="Normal",command=weigh)
	weight.add_command(label="Bold",command=weigh2)
	menu.config(background="#414e4e")
	menu.add_command(label="About",command=abt)
	fnt=Menu(formate)
	formate.add_cascade(label="Font",menu=fnt)
	fnt.add_command(label="4",command=fnt4)
	fnt.add_command(label="8",command=fnt8)
	fnt.add_command(label="12",command=fnt12)
	fnt.add_command(label="16",command=fnt16)
	fnt.add_command(label="20",command=fnt20)
	fnt.add_command(label="24",command=fnt24)
	fnt.add_command(label="28",command=fnt28)
	fnt.add_command(label="32",command=fnt32)
	fnt.add_command(label="36",command=fnt36)
	fnt.add_command(label="40",command=fnt40)
	fnt.add_command(label="44",command=fnt44)
	fnt.add_command(label="48",command=fnt48)
	fnt.add_command(label="52",command=fnt52)
	fnt.add_command(label="56",command=fnt56)
	fnt.add_command(label="60",command=fnt60)
	fnt.add_command(label="64",command=fnt64)
	fnt.add_command(label="68",command=fnt68)
	fnt.add_command(label="72",command=fnt72)
	
	tp=Frame(root,background="#414e4e")
	wk=Label(tp,text="WIKIPEDIA",font=Font(family="",size=30,weight="bold",underline=1),background="#414e4e").pack(side=TOP)
	sr=Label(tp,text="SEARCH",background="#414e4e",font=Font(family="",size=10,weight="bold",underline=1)).pack(side=RIGHT)
	
	tp.pack(side=TOP)
	
	top=Frame(root,background="#414e4e")
	entry=Entry(top,width=25)
	entry.pack(side=LEFT)
	button=Button(top,text="Search",fg="red",bg="black",command=sh)
	button.pack(side=LEFT)
	top.pack(side=TOP)
	
	bottom=Frame(root)
	scrol=Scrollbar(bottom,background="#414e4e")
	scrol.pack(side=RIGHT,fill=Y)
	text=Text(bottom,wrap=WORD,yscrollcommand=scrol.set,font=fonts,bd=8,background="#6e7888",undo=True)
	text.insert(INSERT,"Jai Mata Di !")
	text.pack()
	scrol.config(command=text.yview)
	bottom.pack()
	editmenu.add_separator()
	try:
		editmenu.add_command(label = "Undo" , command = text.edit_undo)
		editmenu.add_command(label = "Redo" , command = text.edit_redo)
	except:
		pass
	
	root.mainloop()
except:
	pass