import Tkinter as tk
import tkMessageBox

window = tk.Tk()
window.title('GUI test')
window.geometry('450x300')

# var = tk.StringVar()
# l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
# l.pack()
# on_hit = False
# def hit_me():
# 	global on_hit
# 	if on_hit==False:
# 		on_hit = True
# 		var.set('you hit me')
# 	else:
# 		on_hit = False
# 		var.set('')
# b = tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
# b.pack()

# e = tk.Entry(window,show='*')
# e.pack()

# def insert_point():
# 	var = e.get()
# 	t.insert('insert', var)
# def insert_end():
# 	var = e.get()
# 	t.insert('end', var)

# b = tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
# b.pack()

# b2 = tk.Button(window,text='insert end',width=15,height=2,command=insert_end)
# b2.pack()

# t =tk.Text(window,height=2)
# t.pack()

# var1 = tk.StringVar()
# l = tk.Label(window,textvariable=var1,bg='yellow',font=('Arial',12),width=4,height=2)
# l.pack()

# def print_selection():
# 	value = lb.get(lb.curselection())
# 	var1.set(value)

# b = tk.Button(window,text='print selection',width=15,height=2,command=print_selection)
# b.pack()

# var2 = tk.StringVar()
# var2.set((1,2,3,4,5,6,7,8,9,0))
# lb = tk.Listbox(window,listvariable=var2)
# list_item = [12,34,56,789]
# for i in list_item:
# 	lb.insert('end',i)
# lb.insert(1,'first')
# lb.insert(2,'second')
# lb.delete(2)
# lb.pack()

# var = tk.StringVar()
# l = tk.Label(window,text='empty',bg='yellow',width=20)
# l.pack()

# def print_selection():
# 	l.config(text='you have selected'+var.get())

# r1 = tk.Radiobutton(window,text='Option 1',variable=var,value='A',command=print_selection )
# r1.pack()
# r2 = tk.Radiobutton(window,text='Option 2',variable=var,value='B',command=print_selection )
# r2.pack()
# r3 = tk.Radiobutton(window,text='Option 3',variable=var,value='C',command=print_selection )
# r3.pack()

# def print_selection(v):
# 	l.config(text='you have selected'+v)
# l = tk.Label(window,text='empty',bg='yellow',width=20)
# l.pack()

# s = tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=3,resolution=0.02,command=print_selection)
# s.pack()

# def print_selection():
# 	if var1.get()==1 and var2.get() == 0:
# 		l.config(text='love only python')
# 	elif var1.get()==0 and var2.get() == 1:
# 		l.config(text='love only C++')
# 	elif var1.get()==1 and var2.get() == 1:
# 		l.config(text='love both')
# 	else:
# 		l.config(text='love none')
# l = tk.Label(window,text='empty',bg='yellow',width=20)
# l.pack()

# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
# c2 = tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,command=print_selection)
# c1.pack()
# c2.pack()


# def moveit():
# 	canvas.move(rect,0,2)
# canvas = tk.Canvas(window,bg='blue',height=100,width=200)
# # img = tk.PhotoImage(file='C:/Users/ma.xiaobo/Desktop/image/FaceQ1494386494810.png')
# # img = canvas.create_image(0,0,anchor='NW',image=img)
# x0,y0,x1,y1 = 50,50,80,80
# line = canvas.create_line(x0,y0,x1,y1)
# oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
# arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
# rect = canvas.create_rectangle(100,30,100+20,30+20)
# canvas.pack()
# b = tk.Button(window,text='move',command=moveit)
# b.pack()


# count = 0
# def do_job():
# 	global count
# 	count += 1
# 	l.config(text='do'+str(count))
# l = tk.Label(window,text='empty',bg='yellow',width=20)
# l.pack()
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='File',menu=filemenu)
# filemenu.add_command(label='New',command=do_job)
# filemenu.add_command(label='Open',command=do_job)
# filemenu.add_command(label='Save',command=do_job)
# filemenu.add_separator()
# filemenu.add_command(label='Exit',command=window.quit)

# efilemenu = tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Edit',menu=efilemenu)
# efilemenu.add_command(label='Cut',command=do_job)
# efilemenu.add_command(label='Copy',command=do_job)
# efilemenu.add_command(label='Paste',command=do_job)

# submenu = tk.Menu(filemenu)
# filemenu.add_cascade(label='Import',menu=submenu,underline=0)
# submenu.add_command(label='Submenu',command=do_job)
# window.config(menu=menubar)


# tk.Label(window,text='on the window').pack()
# frm = tk.Frame(window)
# frm.pack()
# frml = tk.Frame(frm)
# frmr = tk.Frame(frm)
# frml.pack(side='left')
# frmr.pack(side='right')
# tk.Label(frml,text='on the frml1').pack()
# tk.Label(frml,text='on the frml2').pack()
# tk.Label(frmr,text='on the frmr').pack()

# def hit_me():
# 	# tkMessageBox.showinfo(title='Hi',message='hahaha')
# 	# tkMessageBox.showwarning(title='Hi',message='nonono')
# 	# tkMessageBox.showerror(title='Hi',message='Never')
# 	# tkMessageBox.askquestion(title='Hi',message='Never')
# 	# tkMessageBox.askyesno(title='Hi',message='Never')
# 	# tkMessageBox.askyesnocancel(title='Hi',message='Never')
# 	tkMessageBox.askokcancel(title='Hi',message='Never')
# tk.Button(window,text='hit me',command=hit_me).pack()


# tk.Label(window,text=1).pack(side='top')
# tk.Label(window,text=1).pack(side='bottom')
# tk.Label(window,text=1).pack(side='left')
# tk.Label(window,text=1).pack(side='right')

# for i in range(4):
	# for j in range(3):
		# tk.Label(window,text=1).grid(row=i,column=j,ipadx=10,ipady=10)
# tk.Label(window,text=1).place(x=150,y=150,anchor='nw')

# welcome image
# canvas = tk.Canvas(window, height=200, width=500)
# image_file = tk.PhotoImage(file='welcome.gif')
# image = canvas.create_image(0,0, anchor='nw', image=image_file)
# canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',message='how are you'+usr_name)
        else:
            tk.messagebox.showerror('Error,Wrong password')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                                                'You have not signed up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()
def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('User Sign Up')
    window_sign_up.geometry('400x300')
    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)


# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)


window.mainloop()