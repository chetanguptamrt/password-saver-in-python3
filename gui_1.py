from tkinter import *
import pickle
import random
from tkinter.messagebox import showerror,showinfo,showwarning

class password_dat:
    def __init__(self,starter,password,encode_data_list):
        self.starter=starter
        self.password=password
        self.encode_data_list=encode_data_list
def frame_des():
    global frame1
    try:
        frame1.destroy()
    except:
        pass
def frame6_save():
    global name_save,username_save,password_save,phoneno_save,emailid_save
    frame6_save_lst=[name_save.get(),username_save.get(),password_save.get(),phoneno_save.get(),emailid_save.get()]
    print(frame6_save_lst)
    with open("Data\\passwords.dat",mode='rb') as f:
        obj=pickle.load(f)
        temp_pass_save=obj.encode_data_list
   #print(temp_pass_save)
    temp_pass_save.append([])
    print(temp_pass_save)

    for j in frame6_save_lst:
        output___=''
        for i in j:
            output___+=encoding[i]

        decode=[]
        a=-1
        for i in range(len(output___)):
            if i%128==0:
                a+=1
                decode.append('')
            decode[a]+=output___[i]

        temp_pass_save[len(temp_pass_save)-1].append(decode)
    print(temp_pass_save)
    name_save.set('')
    username_save.set('')
    password_save.set('')
    phoneno_save.set('')
    emailid_save.set('')
    with open("data\\passwords.dat",mode='wb') as f:
        stu=password_dat(0,decode_user_pass,temp_pass_save)
        pickle.dump(stu,f)
def frame6_():
    global starter,frame1,name_save,username_save,password_save,phoneno_save,emailid_save
    name_save.set('')
    username_save.set('')
    password_save.set('')
    phoneno_save.set('')
    emailid_save.set('')
    frame_des()
    frame1=Frame(root,bd=6,relief="raised",width=700,height=480,bg='#2475B0')
    frame1.pack()
    frame6_1=Frame(frame1,bg='#2475B0')
    frame6_1.pack()
    frame6_2=Frame(frame1,bg='#2475B0',bd=3,relief='raised')
    frame6_2.pack()
    frame6_3=Frame(frame1,bg='#2475B0')
    frame6_3.pack()
    #------------------------------------------
    Label(frame6_1,text="Password Maker & Saver",font="elephant 24 bold underline",bg='#2475B0',fg="#000000",width=29,height=2).pack()
    #--------------------------------------------------------
    Label(frame6_2,text="Save Passsword",font="arial 16 bold",fg='#E44236',bg='#2475B0').pack(padx=25,pady=10)
    frame6_4=Frame(frame6_2,bg='#2475B0')
    frame6_4.pack()
    Label(frame6_4,text="Name",font="arial 12 bold",bg='#2475B0',padx=3,pady=3).grid(row=0,column=0,sticky='w')
    Entry(frame6_4,font='arial 12',textvariable=name_save).grid(row=0,column=1,sticky='w',padx=3,pady=3)
    Label(frame6_4,text="Username",font="arial 12 bold",bg='#2475B0',padx=3,pady=3).grid(row=0,column=2,sticky='w')
    Entry(frame6_4,font='arial 12',textvariable=username_save).grid(row=0,column=3,sticky='w',padx=3,pady=3)
    Label(frame6_4,text="Password",font="arial 12 bold",bg='#2475B0',padx=3,pady=3).grid(row=1,column=0,sticky='w')
    Entry(frame6_4,font='arial 12',textvariable=password_save).grid(row=1,column=1,sticky='w',padx=3,pady=3)
    Label(frame6_4,text="Phone No.",font="arial 12 bold",bg='#2475B0',padx=3,pady=3).grid(row=1,column=2,sticky='w')
    Entry(frame6_4,font='arial 12',textvariable=phoneno_save).grid(row=1,column=3,sticky='w',padx=3,pady=3)
    Label(frame6_4,text="Email id",font="arial 12 bold",bg='#2475B0',padx=3,pady=3).grid(row=2,column=0,sticky='w')
    Entry(frame6_4,font='arial 12',textvariable=emailid_save).grid(row=2,column=1,sticky='w',padx=3,pady=3)

    Button(frame6_2,text="Save",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame6_save).pack(padx=30,pady=12)
    #------------------------------------------------------
    Button(frame6_3,text="Back",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame3_).pack(padx=30,pady=20)
    Label(frame6_3,text="Hello guys, only remember 6 digit password and save any password.\nPlease don't forget this password.\nThis application provide encrypt security to save your password.",
                font='lucida 12',fg='#F4C724',bg='#000000',width=100,height=5).pack()
def random_pass():
    global digit_password,make_password
    make_pass_random=''
    #encoding_keys=encoding.keys()
    print()
    for i in range(digit_password.get()):
        make_pass_random+=str(random.choice(list(encoding.keys())))
    make_password.set(make_pass_random)
def frame5_():
    global starter,frame1,digit_password,make_password
    frame_des()
    make_password=StringVar()
    digit_password=IntVar()
    frame1=Frame(root,bd=6,relief="raised",width=700,height=480,bg='#2475B0')
    frame1.pack()
    frame5_1=Frame(frame1,bg='#2475B0')
    frame5_1.pack()
    frame5_2=Frame(frame1,bg='#2475B0',bd=3,relief='raised')
    frame5_2.pack()
    frame5_3=Frame(frame1,bg='#2475B0')
    frame5_3.pack()
    #------------------------------------------
    Label(frame5_1,text="Password Maker & Saver",font="elephant 24 bold underline",bg='#2475B0',fg="#000000",width=29,height=2).pack()
    Label(frame5_2,text="Make Randomly Passsword",font="arial 16 bold",fg='#E44236',bg='#2475B0').pack(padx=25,pady=12)
    #--------------------------------------------------------
    frame5_4=Frame(frame5_2,bg='#2475B0')
    frame5_4.pack()
    make_password.set("")
    digit_password.set(0)
    Radiobutton(frame5_4,text="6 Digit",font="arial 7",value=6,bg='#2475B0',variable=digit_password).grid(row=0,column=0,padx=3,pady=4)
    Radiobutton(frame5_4,text="8 Digit",font="arial 7",value=8,bg='#2475B0',variable=digit_password).grid(row=0,column=1,padx=3,pady=4)
    Radiobutton(frame5_4,text="12 Digit",font="arial 7",value=12,bg='#2475B0',variable=digit_password).grid(row=0,column=2,padx=3,pady=4)
    Entry(frame5_2,font="arial 13 bold",justify="center",textvariable=make_password).pack(padx=30,pady=13)
    Button(frame5_2,text="Generate password",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=random_pass).pack(padx=30,pady=(12,17))
    #------------------------------------------------------
    Button(frame5_3,text="Back",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame3_).pack(padx=30,pady=20)
    Label(frame5_3,text="Hello guys, only remember 6 digit password and save any password.\nPlease don't forget this password.\nThis application provide encrypt security to save your password.",
                font='lucida 12',fg='#F4C724',bg='#000000',width=100,height=5).pack()
def frame4_show():
    global frame4_6_1,frame4_6_2,frame4_6_3,frame4_6_4,frame4_6_5,frame4_listbox,all_password
    c=frame4_listbox.curselection()
    if c==():
        pass
    else:
        frame4_6_lst=[]
        try:
            for i in all_password[c[0]]:
                frame4_6__=''
                for j in i:
                    frame4_6__+=j
                frame4_6_lst.append(frame4_6__)
        except:
            pass
        print(frame4_6_lst)
        frame4_6_1.config(text=frame4_6_lst[0])
        frame4_6_2.config(text=frame4_6_lst[1])
        frame4_6_3.config(text=frame4_6_lst[2])
        frame4_6_4.config(text=frame4_6_lst[3])
        frame4_6_5.config(text=frame4_6_lst[4])
def frame4_delete():
    global frame4_listbox,all_password
    c=frame4_listbox.curselection()
    if c==():
        pass
    else:
        with open("Data\\passwords.dat",mode='rb') as f:
            obj=pickle.load(f)
            start=obj.starter
            encode_user_pass=obj.password
            temp_encode_data_list=obj.encode_data_list
        temp_encode_data_list.pop(c[0])
        frame4_listbox.delete(0,END)
        #------------------------------------------------------------------
        with open("Data\\passwords.dat",mode='wb') as f:
            pass_=password_dat(start,encode_user_pass,temp_encode_data_list)
            pickle.dump(pass_,f)
        #--------------------------------------------------------------- 
        with open("Data\\passwords.dat",mode='rb') as f:
            obj=pickle.load(f)
            all_password=[]
            for i in obj.encode_data_list:
                all_password.append([])
                for j in i:
                    all_password[len(all_password)-1].append([])
                    for k in j:
                        for l in encoding:
                            if k==encoding[l]:
                                all_password[len(all_password)-1][len(all_password[len(all_password)-1])-1]+=l
            try:
                for i in all_password:
                    all_password_output=''
                for k in i[0]:
                    all_password_output+=k
                    frame4_listbox.insert('end',all_password_output)
            except:
                pass

def frame4_():
    global starter,frame1,frame4_6_1,frame4_6_2,frame4_6_3,frame4_6_4,frame4_6_5,frame4_listbox,all_password
    frame_des()   
    with open('data\\passwords.dat',mode='rb') as f:
        obj=pickle.load(f)        
        all_password=[]
        for i in obj.encode_data_list:
            all_password.append([])
            for j in i:
                all_password[len(all_password)-1].append([])
                for k in j:
                    for l in encoding:
                        if k==encoding[l]:
                            all_password[len(all_password)-1][len(all_password[len(all_password)-1])-1]+=l
    frame1=Frame(root,bd=6,relief="raised",width=700,height=480,bg='#2475B0')
    frame1.pack()
    frame4_1=Frame(frame1,bg='#2475B0')
    frame4_1.pack()
    frame4_2=Frame(frame1,bg='#2475B0',bd=3,relief='raised')
    frame4_2.pack(pady=10,padx=10)
    frame4_3=Frame(frame1,bg='#2475B0')
    frame4_3.pack()
    #------------------------------------------------
    Label(frame4_1,text="Password Maker & Saver",font="elephant 24 bold underline",bg='#2475B0',fg="#000000",width=29,height=2).pack()
    #------------------------------------------------------------
    frame4_4=Frame(frame4_2,bg='#2475B0')
    frame4_4.pack(side=LEFT,padx=(12,0),pady=15)
    frame4_5=Frame(frame4_2,bg='#2475B0')
    frame4_5.pack(side=RIGHT,padx=12,pady=(15,0))
    frame4_1_sbr=Scrollbar(frame4_4)
    frame4_1_sbr.pack(side='right',fill='y')
    frame4_listbox=Listbox(frame4_4,width=16,height=8,font="arial 17 bold")
    for i in all_password:
        all_password_output=''
        for k in i[0]:
            all_password_output+=k
        frame4_listbox.insert('end',all_password_output)
    frame4_listbox.pack()
    frame4_1_sbr.config(command=frame4_listbox.yview)
    frame4_listbox.config(yscrollcommand=frame4_1_sbr.set)
    #---------------------------------------------------------------
    frame4_6=LabelFrame(frame4_5,text="Show Details",font="arial 10 bold",width=300,height=180,bd=3,relief="raised",bg='#2475B0')
    frame4_6.pack()
    j=0
    for i in ['Name','Username','Password','Phone No.','Email id']:
        Label(frame4_6,text=i,font='arial 10 bold',bg='#2475B0').grid(row=j,column=0,sticky='w',padx=2,pady=3)
        j+=1
    frame4_6_1=Label(frame4_6,text='',font='arial 10 bold',bg='#2475B0',width=25)
    frame4_6_1.grid(row=0,column=1,sticky='w',padx=2,pady=3)
    frame4_6_2=Label(frame4_6,text='',font='arial 10 bold',bg='#2475B0',width=25)
    frame4_6_2.grid(row=1,column=1,sticky='w',padx=2,pady=3)
    frame4_6_3=Label(frame4_6,text='',font='arial 10 bold',bg='#2475B0',width=25)
    frame4_6_3.grid(row=2,column=1,sticky='w',padx=2,pady=3)
    frame4_6_4=Label(frame4_6,text='',font='arial 10 bold',bg='#2475B0',width=25)
    frame4_6_4.grid(row=3,column=1,sticky='w',padx=2,pady=3)
    frame4_6_5=Label(frame4_6,text='',font='arial 10 bold',bg='#2475B0',width=25)
    frame4_6_5.grid(row=4,column=1,sticky='w',padx=2,pady=3)
    #--------------------------------------------------------------------
    frame4_7=Frame(frame4_5,bg='#2475B0')
    frame4_7.pack()
    Button(frame4_7,text="Show",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame4_show).grid(row=0,column=0,padx=5,pady=13)
    Button(frame4_7,text="Delete",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame4_delete).grid(row=0,column=1,padx=5,pady=13)
    Button(frame4_7,text="Back",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame3_).grid(row=0,column=2,padx=5,pady=13)
    #----------------------------------------------
    Label(frame4_3,text="Hello guys, only remember 6 digit password and save any password.\nPlease don't forget this password.\nThis application provide encrypt security to save your password.",
                font='lucida 12',fg='#F4C724',bg='#000000',width=100,height=5).pack()
def frame3_():
    global starter,frame1
    #first check password then go next
    frame_des()
    if starter==1:
        starter=0
        frame2_()
    elif starter==0:
        frame1=Frame(root,bd=6,relief="raised",width=700,height=480,bg='#2475B0')
        frame1.pack()
        frame3_1=Frame(frame1,bg='#2475B0')
        frame3_1.pack()
        frame3_2=Frame(frame1,bg='#2475B0',bd=3,relief='raised')
        frame3_2.pack()
        frame3_3=Frame(frame1,bg='#2475B0')
        frame3_3.pack()
        Label(frame3_1,text="Password Maker & Saver",font="elephant 24 bold underline",bg='#2475B0',fg="#000000",width=29,height=2).pack()
        Button(frame3_2,text="Make password",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame5_).pack(padx=30,pady=(17,12))
        Button(frame3_2,text="Save password",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame6_).pack(padx=30,pady=12)
        Button(frame3_2,text="Show password",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame4_).pack(padx=30,pady=(12,17))
        Button(frame3_3,text="Back",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=frame2_).pack(padx=30,pady=20)
        Label(frame3_3,text="Hello guys, only remember 6 digit password and save any password.\nPlease don't forget this password.\nThis application provide encrypt security to save your password.",
                font='lucida 12',fg='#F4C724',bg='#000000',width=100,height=5).pack()
def password_maker(event=0):
    global create_password,repeat_password
    if create_password.get()==repeat_password.get():
        if len(create_password.get())==6:
            #encode user password..............
            encode_user_pass=[]
            User_pass=''
            for i in create_password.get():
                User_pass+=encoding[i]
            a=-1
            for i in range(len(User_pass)):
                if i%128==0:
                    a+=1
                    encode_user_pass.append('')
                encode_user_pass[a]+=User_pass[i]
            with open("Data\\passwords.dat",mode='rb') as f:
                obj=pickle.load(f)
                temp_encode_data_list=obj.encode_data_list
            with open("Data\\passwords.dat",mode='wb') as f:
                pass_=password_dat(0,encode_user_pass,temp_encode_data_list)
                pickle.dump(pass_,f)
            #go to next frame------------------
            frame3_()
        else:
            showerror("Error","Password will be 6 digit...")
    else:
        showerror("Warning...","Create password and repeat password are not same...")
def frame1_show_password():
    global show_password_button,frame_1_entry1,frame_1_entry2
    if show_password_button.get()==0:
        frame_1_entry1.config(show="*")
        frame_1_entry2.config(show="*")
    elif show_password_button.get()==1:
        frame_1_entry1.config(show="")
        frame_1_entry2.config(show="")
def frame1_():
    global show_password_button,frame_1_entry1,frame_1_entry2,frame1,create_password,repeat_password
    frame1=Frame(root,bd=6,relief="raised",width=700,height=480,bg='#2475B0')
    frame1.pack()
    create_password=StringVar()
    repeat_password=StringVar()
    show_password_button=IntVar()
    frame1_1=Frame(frame1,bg='#2475B0')
    frame1_1.pack()
    frame1_2=Frame(frame1,bg='#2475B0',bd=3,relief='raised')
    frame1_2.pack()
    frame1_3=Frame(frame1,bg='#2475B0')
    frame1_3.pack()
    Label(frame1_1,text="Password Maker & Saver",font="elephant 24 bold underline",bg='#2475B0',fg="#000000",width=29,height=2).pack()
    Label(frame1_1,text="Create 6 digit password",bg='#2475B0',font="arial 12 bold").pack(pady=10)
    Label(frame1_1,text="Warning! If you forget this password, it means you forget your all password.",font='arial 9 bold underline',fg='#FF3031',bg='#2475B0').pack(pady=(0,30))
    Label(frame1_2,text="Create Password",font="Lucida 14",bg='#2475B0').grid(row=0,column=0,padx=(40,20),pady=5)
    frame_1_entry1=Entry(frame1_2,width=8,font="Lucida 14",justify='right',textvariable=create_password)
    frame_1_entry1.config(show="*")
    frame_1_entry1.bind('<Return>',password_maker)
    frame_1_entry1.grid(row=0,column=1,padx=(20,40),pady=5)
    Label(frame1_2,text="Repeat Password",font="Lucida 14",bg='#2475B0').grid(row=1,column=0,padx=(40,20),pady=5)
    frame_1_entry2=Entry(frame1_2,width=8,font="Lucida 14",justify='right',textvariable=repeat_password)
    frame_1_entry2.config(show="*")
    frame_1_entry2.bind('<Return>',password_maker)
    frame_1_entry2.grid(row=1,column=1,padx=(20,40),pady=3)
    Checkbutton(frame1_2,text="Show password",font="arial 7",bg='#2475B0',fg="#000000",command=frame1_show_password,variable=show_password_button).grid(row=2,column=1,pady=2,sticky='w')
    Button(frame1_3,text="Next",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=password_maker).pack(padx=30,pady=21)
    Label(frame1_3,text="Hello guys, only remember 6 digit password and save any password.\nPlease don't forget this password.\nThis application provide encrypt security to save your password.",
            font='lucida 12',fg='#F4C724',bg='#000000',width=100,height=5).pack()
def password_checker(event=0):
    global enter_your_password,decode_user_pass
    #decode user password...............
    with open("Data\\passwords.dat",mode='rb') as f:
        obj=pickle.load(f)
        decode_user_pass=obj.password
    decode_pass=''
    for j in decode_user_pass:
        for k in encoding:
            if j==encoding[k]:
                decode_pass+=k            
    #print(decode_pass,decode_user_pass)
    if decode_pass==enter_your_password.get():
        frame3_()
    else:
        showwarning('Warning...','Password is incorrect.')
def frame2_show_password():
    global show_password_button,frame_1_entry1
    if show_password_button.get()==0:
        frame_1_entry1.config(show="*")
    elif show_password_button.get()==1:
        frame_1_entry1.config(show="")
def frame2_():
    global show_password_button,frame_1_entry1,frame1,enter_your_password
    frame_des()
    frame1=Frame(root,bd=6,relief="raised",width=700,height=480,bg='#2475B0')
    frame1.pack()
    enter_your_password=StringVar()
    show_password_button=IntVar()
    frame1_1=Frame(frame1,bg='#2475B0')
    frame1_1.pack()
    frame1_2=Frame(frame1,bg='#2475B0',bd=3,relief='raised')
    frame1_2.pack()
    frame1_3=Frame(frame1,bg='#2475B0')
    frame1_3.pack()
    Label(frame1_1,text="Password Maker & Saver",font="elephant 24 bold underline",bg='#2475B0',fg="#000000",width=29,height=2).pack()
    Label(frame1_1,text="Enter 6 digit password",bg='#2475B0',font="arial 12 bold").pack(pady=10)
    Label(frame1_1,text="Forget password ?, it means you forget your all password.",font='arial 9 bold underline',fg='#FF3031',bg='#2475B0').pack(pady=(0,30))
    Label(frame1_2,text="Enter Your Password",font="Lucida 14",bg='#2475B0').grid(row=0,column=0,padx=(40,20),pady=17)
    frame_1_entry1=Entry(frame1_2,width=8,font="Lucida 14",justify='right',textvariable=enter_your_password)
    frame_1_entry1.config(show="*")
    frame_1_entry1.bind("<Return>",password_checker)
    frame_1_entry1.grid(row=0,column=1,padx=(20,40),pady=(5,0))
    Checkbutton(frame1_2,text="Show password",font="arial 7",bg='#2475B0',fg="#000000",variable=show_password_button,command=frame2_show_password).grid(row=1,column=1,pady=(0,5),sticky='w')
    Button(frame1_3,text="Next",font="arial 13 bold",bg='#74B9FF',bd=4,padx=15,pady=2,command=password_checker).pack(padx=30,pady=(30,25))
    Label(frame1_3,text="Hello guys, only remember 6 digit password and save any password.\nPlease don't forget this password.\nThis application provide encrypt security to save your password.",
            font='lucida 12',fg='#F4C724',bg='#000000',width=100,height=5).pack()
if __name__ == "__main__":

    encoding={'A': 'GcVt46 T&c502&tqAF0ZYIuEU#nkA%OpdH#%F#RWa7DmYlb3r8 OsJ*AMoD7OrXW@ZMl3QXxE67R*NO0RzJKFmQF0oRTaqtzys#QvadDEhnh1xCtTkObFgKt.GH@PUQh',
        'B': 'ZKZUc4jiU5wdANAisCAjs OC#4K9kzyyyeet @eukSQ7dT%7L rTQiJNCIza&#@xN1Ho%s8r@.RraFSI97vIW.HXLdf@gl1OilrHh9mY3cuYX12 lfw9&EqeROZJ41rO',
        'C': 'e8hBOTDrvOs dQYiHBNWl7ZqCopjBSa2NbS8DU#K#k%AbXdC*NYgDkE2pyHei8#9Ri7vkHiSU3kg5lvqd@Th06JLCW7Bovt*H83Q&05psvlcSKwbw7X..IOvAzFfcp0%',
        'D': 'cv*dBeY9kmIJyJmHx%Ew1SDUw5JovI@PZ@w1elxwE@QaHb 8gLWoKs6dkTDX1wzWYt8DYt8rCbSh2K8LaJP94SUe2oI8Hqv@Hu.4aeSAl9jt8.ucOScabqWyl6YovjyF', 
        'E': 'MWwmLe&vgsk7tb.b%nWS9@i BJtTPjc*nIsPUQ%as71ZjYoU3.vS2RKftKZdwyxdUxL1uTPCMjB *WDP7sF2OC3Na&z0 ZIClJdc6.IDFkF%*X88hRaXNgDV%wGqN%I0', 
        'F': '1iANdhCZ92V@xqQeK2fDX3Ibe2N#rIjeNHBFgp#*LshWk4Fh9nx0dBh*p4woZZQlgrUQN*SLtalQFuEY7 4YYFuk3B.IX60aRkGgQl sJ0w7dpOmkLQKrfGQQernV%N7', 
        'G': '9i@9ynpW@tUCEJMkVi@lE6EqlLBj8&Jb41Q@ULk8injIXvI6kc5xg87u1GM6rk1DNdtMuQRM04Ui xsdu0Yq.fuWGV0c7.ggw*bck21qd6Xzo#ltmKEx*MQ0MNFmMnSn', 
        'H': 'tq59lsaVZS3ctcv1kS0OxO%p5I3HzU12*GtJmoLRm8.C.ChF9.*gNRBm00CwPwL@4dfuomj%hzO.DoAY5RjC4Z2Hf.uvPyX4FKx#BxAnj@aoxLUj%VcpofAWMgtYLju&', 
        'I': 'tMFmnl4JbeGEx2#I0juc.ezeDhoMN7ME%&j 3A@EhS#tHMXDnMwl9hxrM6HcLKOC&.89jiLQu#P2elc&ZYwe9Q.SmID%TgKrCKhGDaCAibYCO3Npo@W2DQZ AZ0z%X0M', 
        'J': 'TdpGbDn0q8HbD1PyD#l8R4DXUJEgeGrd*vmSu&DDo9MOb8fDB%K jF%UWT* kmh0kE3@i36G0cTIlvc6ycJRoY SmvjLNxBl.axvKfDZ6zZnvYwNz 4HSgD.b l9AELu', 
        'K': 'zjzmHnJHQ4XhtUeuPsrx2aRl3LI0N*xfEF9L&c#hC&cdsXvitDpiJJQNzFgtVaYJ.w08oBqI5FlzQe5A.as8ZnpYya3FBPf6QAPanMrupjvFkSP2sYgxd57IYzz0xv %', 
        'L': 'Y0 cRhO* %usesi6xlx0FR&7 bFTAZcezDXFhQ594tTWzoXm p7c32.WtxtJwJ2.saVEKOiDF%Oh&Bjf*VOivCZ&wvV#E4dLa08V0i%rgp5eQmD6jP2S5vX3fNVCvtwg', 
        'M': 'uCrsZHA2exi*Cy.5VkRCPXo0Kg.W.p GdzzcGkG@F.LD.MWGmmlm@ldS9aO3B3lQ2Em*326IVA@ZY*ORW%0fHV5IlLzf2Hd3.CUVKss8IjudpyfOZVn.QLFss&wFntJj', 
        'N': '4J81rgu*zlcYLewEZlwCHa6Gtv31nzcxtG3f cy&lbudy@4#rfcHV4mhpPmPp7z5p0hUhTZX65m*1ClTHNbN3Lbdr.@tSJ4Ga1Hl5d@kgDyUu1l@DRu79dThTyqk#IG8', 
        'O': 'EBt73tydX6.fL6QqxLKE&e SKLH108RUAX*SGYG4OxlrN6y6fcQyeT6ZbLz vKY#RwDfK7FxqYdKagM@&2x jRFR58.EsEqb8Qn7Zt#2#Iof%Z3VeEuOfXrymXO0Ew&V', 
        'P': 'zyn1U5mK@vA9.ect 6w9gFeTg.Pfs2hNxDn72lQ.xI8I2BCsQNE*d0NGafCp6&Y%Fg2mpINXYz1ea.RfhHCDPhoT6%J7xfuTDOO1yPFDOAFhGD@dA1oqDAo.9G%NCP@M', 
        'Q': '1mD0x7&0KuO61V.Dp2T3WWJWzGyL9yIsRhQwJV.xfcW01RWh3srBnNc OkNxyLyPR6NPMVjAB6Wi1U30QFlNuwX7BO5*Es0Rl*Eo#CiCH#KU7xNC9lNLLwcu3ek%F0zb', 
        'R': '8Zv3hKdGBpV*Yn#G*sCNUUulU4Zv&Cuv670O0k@fe99N%rZpiu&LcvY4DqAB&QcBhuDcD40@m*WQgbzRVhs3Sj3*H1Il3 5ClBiC7AYAH0ELEV8kgDSStvdBFIbN4BGx', 
        'S': '@7Q%Uo4hpt*4NB4YFsubqO.PY0N8yIalxoOTXITyEsSIDPGyKONRgPfpf&A9 5RC5kpHME3T.vWWA&IbjnLw@77OIvlOKDK53VVZ23bwD4kiYyzdwhcMse5VCW5sgZ**', 
        'T': 'L@#FFV%.FQG 6q%54tSOHpt.bS&or148vOyLC%FFgrR1dxT@uGs3jq2%Pw%29RfYGpL7ZOHAuYRnbjXEZ%Mwz3jZ.zpTql@zB%jp0Z2PVQJ*OVohlWH5MoK%I Sk.YPL', 
        'U': 'oIdA1iyvJk6@nogl 15ZnBJklMDskBIMkuS0*E*3Hoe04YR6hLCgpl&&fsgEmG*6CQpNuF#Uc%@%Myjp8fRRlD7gOEJFug*d2sETC6g9Ld5X9ZNPJANiL2&HrgSkE@1p', 
        'V': 'Oi og5EPWV@kaxAusb2t@n@iELCOgNcaDwFyo0eBoZhA3zwwnewn8y#LgV&NkWy%.rZuPBs4EnQ9SsE9woGjKoz2zm@jG9BFcPnqj9Rqpm83ndMO7cQMZ1S754diWe2R', 
        'W': 'gXl*fH6vqbI.kxEpp7iTacq.xe5jz3IztzfbAByZ&Lzivpdvzej83K1%iNwqO LJgP*Id%lxouU SgD1.EggK V@0HWdJzn@k tXBEXRX2glpIdtj6ygzj Vmkx%OcyX', 
        'X': '1sEyfjfHJ#hkqdeIPm&%eRwaY#WM8Z7dJr*B7d3Xm.#lCOCALDA77M5u14 4@rLTyB9HKwTKLGlyF6liLk@I AtX Peu%juiopSI0UEPwUSGZO6Xy3.h%PYjnNESpAq0', 
        'Y': 'pbi@RWYH&55Yj9H3t1n3k@VPx1nyRWt6WlWITqnSr iW40sowXBp9smrd5DN1fIRrir7ktHO4ShSihm@3TF8&bAEOdebv&*aA2B*6O5UMA#u3VJYaSEDZpA#F6q3WM3U', 
        'Z': 'gxieGQlbyb4AdMgutWl5TyxXriFgUXohxqR*sgtmuvTiTrZRwnFcwR inV#THfwRYJsT8Qe.BYOBD6f6Cx3giPreCpPpH 6%h.me@CrRZqGbdl#3IfA x3O6Zk&CFGv2', 
        'a': 'HXtoUGD&Ag4yxDu#aX*vFQNkihShL*OWaBGzhiCAuIbXK.EG5UqCEdD7o46tLqzCApvlXhpmV&s811t&I5wx%q7Vsw%Ro3IBCxhGyw6udhefK%sSypWut#H6HbuLo2GC', 
        'b': 'Qyd&&HfQYnlMySXeKufHjG#Dbq6MhOf w@pfHVg9K2Xv 04jzLq*yy2WCK&odoT6gliDH4g0aMU65ds1dlf@4fTbPg4QrOa8BE32Ufz0XU1886zgO@VPNhyHqXSskc2w', 
        'c': 'y1ldCMM6s5vsYrBFOpW69q*ACC53Kk6ykoaY7@qdBpPzBp24LpN8ZemthvtVv6AVX*s.kY*JiHrJ2Gi&PlZMLVW4Zy0#1fP8miR4bsQrvN2#5K Z&53rua1.N&CUYznE', 
        'd': 'NlW8Uo.7yU0S8q#sd#ZFZY7@HmgC8Hfzbd7xS55frimMB4Qqh0TJiND%N18kcBo1K5daUhk2PGP6pqaO%5TsXSB QdzJm2F*Gi6abLQEmDY4pBwVUxklYakGTGe3K41R', 
        'e': 'YEOKHxJTrMyDJpa7@ce7RF&jRrMJ#7ZNe6O0POP8Z*lhLNBsmS8FSjADKX9lkO4%JjeYf6r#QnguS2#xp2jVniR5u7X#RInfkuxLJ8elCM6ciA%ExaObte7UvT2Sj IF', 
        'f': 'TQoGDwHbj J%j@GY5F2WpU%sNtRXs7TU6&D3inEczho7czlX@@HwX2xlFRfY*pd@ll6OSl3Iq%BHq%j1p0sa&2nYbb7F&dka#2y21%W4Ft1Ah4ggnTN3lHzznCFGWcBU', 
        'g': 'srQHCpkznRcWXxGtBvF11pNzgFA7qlEKLJm T#eyiMk fVZc5w&dteLk0%%kjlc##5vxsD*4ABwKGuGbw5HmNdehlDVtjb59kmaJ%HY9gvTRSmZJ1S.L947P%cQ6hXYo', 
        'h': 'DOSA#l7rxztudMEAqIHIha9cgtLklD8.IPtX4WeU1U0VPnSCbCrH1qii8epHgB*cJ#TpIwfLBDh 8VvoH zFnPSJOSnczKTb*S#YhDrkOYLJRyLiF%Lr1qCJhl7DmH0K', 
        'i': '4.SC1%FupS8hi0rvn%F3OHXaF4FCA.3dx5rjL0b@0x*5A87ote*Q%oxwoxaXjjsz3T1wQp*XwXfDVHXKLmHYYFLQXX25jEdiJsNI5M%IK4BRjKMgsgjNL9vNGoAx0*lE', 
        'j': '9XsnWksgW8#Zs1gZzW6yXv8L3T8z%wXXk9&PiNLmQ5nF@k*PCj0o*1ZyY&xSAFHyuvkywh#6Tt7qkrT6vlrZ0hTP9zItJGx3rq4oqDNtfnPoKpJi2Lp%WMSInyogckjH', 
        'k': 'S0O7Q4hMr*C19%oSagW5owN9r@nH3YUuR1cnSPbvAsy4%%WJ0JAvdonHu4A7j*zS7zf%fbFcdoJ#o9vPFhsNg HAO.KCB&GqfUD a71x%hlxXXW63&aAEaPO6FXmPa%b', 
        'l': 'wblT4VJfx9##hro%KGGwtDoXw@UFrpwc EarlRmsgg6X*KHY0jMgb4QsECH&6k0TNP52kYI4OW lgARl@3FJtkKvM78g@Im374mx&WUgc4tsIHinJmp0u5x.5Ai4N3Y3', 
        'm': 'ngOV7T1mMCAx*jSpyG@CUN@nkpOZkFv4UhGInGYyfX@7rP3Qd8Bv5PyorDfcRZyKKBQJwfz2SUl2v324#yp%k&*%qqmHK YcLvieeRLh0GxR53.RP2F IUNspIJljZSv', 
        'n': 'Rds1oPk7endi**Ca7q6DbA@OsvZAZ.AkitboQYv.#FrK%l87h@hu.SByw6&imfxHTL2so.7TAF07B &Gajtcv0rEzfEqq.HuYAEOY35rw6Gu9G4ylUNMS&hv6PpeYkKv', 
        'o': 'zZdxpDXXgtI@zO#ZfuXgaxI4h*hLDaqlxNMU32TA*r BU0uN#LsbS00wLuJpr@VoNsSiMop4*.bCUfvGoj.9qeaUHHnj8y#VKX0XCXmbTpsyL5qnCX#Kz&gxvNg42NcZ', 
        'p': 'FDGL4POUd7B3718 oo8sR*vnH7qb8FelE29Lacs7b9&IthgZb5COfhYWxj xC@9ebAZyvW@JUdgBkg4NuFIOt0lOv0a& aIH.yNbHtjEFg2PD11HgqM4r oqdVh&Opku', 
        'q': 'Ul0EbcuJ@ 6gQ3rRCVsC76TGlw.ZhaxyCORIasW&*7&z28GldV #g9OuL22pf5vC.TFxY7ahZg21z#rxcDIFhIPw co7s5spmPj4xGF#1dpP@z31eoRoxg8th11&E5U7', 
        'r': 'gHfukv&wwPJqjJ.RWlO0QLDN2RQCi9t9p7K BHv2Ow sSmo&Dq d0i6#WHDRfNfbfKlqv1dLt*tE 7H#PI6Ye7LU0T%&Yldpx0h S#UVJ2DwSoMRTKbLI58cS6uDBc6m', 
        's': '0OZBonj2#00S 5KjpxN8LpDB@oMo98@*R&W2B6H.kLMsIoQJW9kiLT2S%LUfKdMiF18XrT5L.rQV@hETwSVyVm439GEOtx4E UXAYp.o#0B9yy7@1MlmlRW8nqi#0HRs', 
        't': 'F6GUJl. s5&wR1@ynLnhh6%nF.&Vb&gaY0As%kKauAnr9du1@AFzIV#t#XfRc0v2FxRh.pBJ0reH6.59oK5903WvA.XZG9B6B6A%h#rxZwYFnA6ikMDquwG1J#dA08 m', 
        'u': 'feT8Omxuumn2P@IFWX12Wb%DG%TXkGJukYNEwBS57uv@yGDDRJGlUMEe&bIwBVpR1I.dpZ6bbOlr2eEuo*ojBdg4hGxchH&m#ZnmZHQZNlk1qmx593DcLpBTqilHDo6N', 
        'v': '*pHUY*jx3fsHhZqoNYaCH HwvK6v*jlogaVO85uR7J61*5 bbw&iT3Jb3SFtvdhfe*O#pfWY7V%r5xvzmik41.QC&JQsadwJItHWhkcK4BbtMlBp@oCCliGj@PtwshS6', 
        'w': '%afZm#4U3SzYSVRtXMDlhZ3P6sj apdzeWwNXUDDV@xpuhbEI3h98ywjCJqiE139.6XjI4kUDm32EMHIx@jpoaXcqwT5bmHPGMGTK8p*YRkQy&*TpTzjVRou8xL9coq9', 
        'x': 'MOzJrCl0QXf&wNhqswnORJ7oaL5CJQCJ510cpMq*U%FCF%ZnXbeDrVlO &5BMl#hzeKHzR36COm%8AByZsB*tuwmQy5qZxj&ZGu7#kF1gi6h9R3AtyxDMlGRC3xiCDA#', 
        'y': 'r@HVpRwlyM#ESaxptDOFSEwr5HnThtQxrFGGgom3Eq2V2RH9%q*HECMiFTAFKX@ydiIOjrOBITqv9a2X11C@Vf8GrXmUu4Pj22Pm86ue1lVzK 4*JXgjkOjNQZ0gv6X3', 
        'z': 'x3XH4XH UN*Irsw7kMN#vyPn&tQxJf#4gAP wSPD8PK2F7Tzr8Wv0ukV&Tb4jff*qPQF73HRIs#.iY3WIxXKVfyXvGlY2VhtNgD@81AZT5YmhF%msZ68aNFbTJJ9djBn', 
        '0': 'UB#fxzv6KBbvtSny5cvV1Fjz59Tjck@FKW6KB6B2&pT*yj1Nz4p&@ssMhslgMwhHEjFufhhEvon*FLTQ7PZlbSfXDwIoZk6X4kEhF4w5vB53Mw rznGDmHRXoeE0w9Ad', 
        '1': 'Cbj7JVcFgV3Hs43&Cl4EfCKrpwh*%GtkMrv@D4qruDV50S0TQW0l1oC.0cev9rjH1X&9HtYldCagbo#tzaDem3nrMe4WRyKfcnq&#y4lAE4QG3xuhB.93UhAZln@JSy5', 
        '2': 'vN3FKKC1Nfm5*xUmX%5JLKZX6ZH1sPksb8 e2cp5ha#SgvMLkc1dDksbZdA.eHBw# %gFU@@p.C0E8NxTuKlm97%sW0Hqz7vvacoLc1QRDGWWyU@bQR5nKMeRRNvCy0E', 
        '3': 'SiF7rkU#X5kH32@GtPzcmM9s6Gtv&vZGYtOYTS0sOUG@7Nuh9 OmlA0Ac&*BFqt22FZLLdM%@S3#2OSqV1wRyK98dQEH&F82Nswm66Rm5 99tlHQHf7R9TfiU%AeMK@Y', 
        '4': 'TfHkj4ee236gXd4X2e %5pn&O&u7fK*cbmL8Zzk@  d3aLY@5o3A1KUWRGJtLbh8KR7sl.*oQao#Xe.ssl5L4m6.4t*FtTh#zjki%TUWilZvuxjysRxX&&&Ii49V7u%m', 
        '5': 'hlsOuBnsdlgyOCflhy pNASUtszkWvlOl4I1vDhBdDlEEDz7S&Sgt@2c7Mm7cPQ*BRpEFqvYRVSGO9x8PXgEXbVlZKuTkEg9YDCJ#9ud5O3HlNoe2RLkexpeID*g*QUz', 
        '6': 'GLxxMzq3bLLq50.R@XxxGXRr7wKYb8NnoEas2kvMr2W4Yror7lK88wM.Ff1lHTs6kMW@hs9AAA4iNoYH924%sDtdacorDqKusclhUR8mcpCnRyEUh 99ZlOOMEfj570D', 
        '7': 'sXs9Xma783@guPS8ooVQJmwvs4L*5bjJqRnBH.tgbuNhGmW&os1fZU%YMo Arbvdfx@Pr9S7je6z7 IOMWAvO.16xKQ.lBFa.Xh&xc4cm7LVVrZ*#hX@yj9mYwr9&Qsa', 
        '8': 'nLoYTq#B8h5&qcZPTAOyW ntgdnZDR9%tRUC@gmHQZRK#Grtd#@ syz%17E 0*aPDQnBEF#R3Ss&Zj3pJaFzKeCTE59GEA8ZSX#mIcDqjgcpyLhRgD96dMCiZZlrZmY%', 
        '9': 'tujvfyXjJ9xI8& tTq4EBo5EnUPs5Yy%P8OENMg9u91c8%iNcpMYDmlO4zBAtbYsnj7rZ1uxS5jSzhMaIkE@**bFrJlatB%v6oturfY&x%4SB@M6#VlOnrF72LzgZJAU', 
        '@': 'DbAo7rgeT4chkGVx6A.86tVQjbFO23DKG3lQgIjApfvsoHIkr&sH8o8NL@.YfTlcfE@GBSqQab4fG SvX6Bjv@kYiGSX3b*r4AUC4z40R&UzRSmU&Lx*ZFKgL5s3WfgF', 
        '#': 'q0G@1OBjYItQ8r8OTwtCOTk@Lbk2&qbDQzQ20fMhv3jvht7Ai&O72lKK ZLfiafi%3OloXh@NLCYOKReWllTayg7B37IbMvdHj3JeFhTwE&qomRC3NkHubh8SN9aXLtx', 
        '%': 'Ps7sTkiY.Xw@K*3vm*P7fHtBjIMdN0cWkh4XZN#IRX*55jP6#FVEBSnD2kcYQrJh4 hwT#wmmnnF02525FYP0u8fV2zdPvOkQWpzRfdyidE3ddZ krm1miy65FtbsSB.', 
        '&': 'gTu9nWZP8HOGjpS.agW4ZZsBU*HIXd*0tW9DKdIvd*A.WDrTZ9F01Zh&IU5ti8*2aB&&dI8RJBx&*LGmFYXrK*HXqI2Y33W G9B8&tA14MSFwIZvH1Fz1@.ki&wlLJ1n', 
        '*': 'I5YA*UhnuzRsBqgMOxF6VI*qB179GxJKdWgNBg.CyWA2qY8EOwctRun&JhC2OjadBaWSzgujrvafWL.rvuRGH@z63jjRY0c1B.djyu2j69i0&7#rxz@a8v1vlGQmZv0*', 
        '.': '@JwznuaFGXPMcXQhv#rckZhwGss.f36KbcdEYN7XCtEWdE@ofL6g7&wTQF8M#9J36Oca*Ig8O8Eyh%NPnvgvFc@W#rSKY&n0#uJ4wjSfKIOvOUhhPNnRlI0R.*6vaM7v', 
        ' ': 'WGe6Vh2j9#Jc0rXA2R8iktk@oB*QYk*r5XoFAOQJgu&SS7YK0x.tgaIzs%cWmHGtogk 126&0vKjyH*CovScVXO2fgTg CGJag0zIllHvN0yFlI W*%f2rRDte6picLp'}
    root=Tk()
    root.geometry("700x480+350+110")
    root.title("Password saver")
    root.resizable(False,False)
    #---------------------------------------component-----------------------------------
    name_save=StringVar()
    username_save=StringVar()
    password_save=StringVar()
    phoneno_save=StringVar()
    emailid_save=StringVar()
    #--------------------------------------start--------------------------------
    with open("Data\\passwords.dat",mode='rb') as f:
        obj=pickle.load(f)
        starter=obj.starter
        if starter==1:
            frame1_()
        elif starter==0:
            frame2_()
        
    root.mainloop()