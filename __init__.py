"""
for any further query contact:-
--------------------------------------
Developers
Surjeet Lodhi 11904876
Anwar Kathat 11904758
---------------------------------------

#--Important Notice--#

Modules required for running this application completly  are:-

tkinter,tkcalender,random,pymysql,random

<All these modules you can easily downlaod by comming in this folder in your command prompt or shell and then execute the command pip install require.txt>

"""
#importing the all require moudles--start
try:
    from tkinter import *
except:
    print('error while importing the tkinter ')
try:
    from tkinter import messagebox
except:
    print('error while importing the messagebox from tkinter')
try:
    import random as rd
except:
    print('error while importing the random ')
try:
    import pymysql
except:
    print('error while importing the pymysql ')
try:
    from tkcalendar import *
except:
    print('error while importing the tkcalendar ')
try:
    from tkinter.ttk import Treeview
except:
    print('error while importing the TreeView')
try:
    from tkinter import ttk
except:
    print('error while importing the ttk')

#end
##-------------------------------------------------------##globalvariables
introlen=0
VERIFY_DB=0
mwintrolen=0
USER_CREDENTIALS={}
TOTAL_TABLE_COUNT=0

#################################################class for creaitng the login pannel for the user or the entry pannel
class Crime_login:
    def __init__(self,master):
        self.master=master
        self.master.title('Online Crime Reporting System')
        self.master.geometry('950x700+230+5')
        self.master.iconbitmap('1.ico')
        self.introvar=StringVar()
        self.introvar.set("ONLINE CRIME REPORTING LOGIN PANEL")
        self.introLabel=Label(self.master,text='',font=('roman',40,'bold'),borderwidth = 5,relief=RIDGE)
        self.introLabel.place(x=25,y=-10,height=120,width=900)
        self.connectdbbtn=Button(self.master,text="Connect To DataBase",bg="green",activebackground="maroon",activeforeground="white",border=5,font=('roman',30,'italic bold'),command=self.crraetedbOrCursor)
        self.connectdbbtn.place(x=125,y=610,width=700,height=90)
        self.frame=Frame(self.master,bg="powder blue",width=700,height=500)
        self.frame.place(x=125,y=111)
        self.Intro_color_changer()
        ##____________________________________________________________##creating the labels for the login menu
        self.messageslabel=Label(self.frame,text="Enter the details below",bg="gold2",font=('roman',30,'bold'))
        self.messageslabel.place(x=0,y=0,height=50,width=700)
        self.usernamelabel=Label(self.frame,bd=5,text="Useremail*",borderwidth=2,bg="powder blue",font=('roman',40,'bold'))
        self.usernamelabel.place(x=235,y=60)
        self.passwordlabel = Label(self.frame, bd=5,text="Password*", borderwidth=2, bg="powder blue",
                                   font=('roman', 40, 'bold'))
        self.passwordlabel.place(x=235, y=230,width=230)
        ##-------------------------------------------------------------------##adding the entry boxes
        self.lguservar=StringVar()
        self.lgpassvar=StringVar()
        self.userentry=Entry(self.frame,bg="green1",textvariable=self.lguservar,font=('roman',35,'bold'),justify='right')
        self.userentry.place(x=125,y=130)
        self.userentry.focus_set()
        self.userentry = Entry(self.frame,bg="green1", textvariable=self.lgpassvar,show="*", font=('roman', 35, 'bold'), justify='right')
        self.userentry.place(x=125, y=300)

        ##---------------------------------------------------------------------------------##creating the button fot the loggin page
        self.loginbtn=Button(master=self.frame,bg="red",activebackground="blue",activeforeground="white",bd=10,text="Login",font=("roman" ,30,'bold'),command=self.login_vaildation)
        self.loginbtn.place(x=0,y=400,width=230)
        self.loginbtn.bind('<Enter>',self.loginbtnentered)
        self.loginbtn.bind('<Leave>',self.loginbtnleave)

        self.clearbtn = Button(master=self.frame, bg="blue", activebackground="green", activeforeground="white", bd=10,
                               command=self.erasevarvalues,text="Clear", font=("roman", 30, 'bold'))
        self.clearbtn.place(x=234, y=400, width=230)
        self.clearbtn.bind('<Enter>', self.clearbtnentered)
        self.clearbtn.bind('<Leave>', self.clearbtnleave)

        self.registerbtn = Button(master=self.frame, bg="blue", activebackground="red", activeforeground="white", bd=10,
                              command= self.registerPanel,text="Register", font=("roman", 30, 'bold'))
        self.registerbtn.place(x=468, y=400, width=230)
        self.registerbtn.bind('<Enter>', self.registerbtnentered)
        self.registerbtn.bind('<Leave>', self.registerbtnleave)
        self.runIntro()
    ##--------------------------------------methods ofr hover effect on the login btn on enter
    def loginbtnentered(self,event):
        self.loginbtn.config(bg="orange")
    ##--------------------------------------methods ofr hover effect on the login btn color on leave
    def loginbtnleave(self,event):
        self.loginbtn.config(bg='red')
    ##--------------------------------------methods ofr hover effect on the clear btn color on enter
    def clearbtnentered(self,event):
        self.clearbtn.config(bg="gold2")
    ##--------------------------------------methods ofr hover effect on the clear btn color on leave
    def clearbtnleave(self,event):
        self.clearbtn.config(bg="green")
    ##--------------------------------------methods ofr hover effect on the register btn color on enter
    def registerbtnentered(self, event):
        self.registerbtn.config(bg="silver")
    ##--------------------------------------methods ofr hover effect on the register btn color on leave
    def registerbtnleave(self, event):
        self.registerbtn.config(bg="blue")
    ##---------------------------------function for deleting the value inside the entry vars
    def erasevarvalues(self):
        self.lgpassvar.set('')
        self.lguservar.set('')

    ##-----------------------------------------for making the intro runnable
    def runIntro(self):
        global introlen
        val=self.introvar.get()
        if introlen>len(self.introvar.get()):
            introlen=0
        introlen += 1
        self.introLabel.config(text=val[0:introlen])
        self.introLabel.after(200,self.runIntro)
    ##---------------------------function for creating the datbase
    def crraetedbOrCursor(self):
        self.databaseroot=Toplevel(self.master)
        self.databaseroot.grab_set()
        self.databaseroot.iconbitmap('1.ico')
        self.databaseroot.resizable(False,False)
        self.databaseroot.title("Online Crime Reporting System")
        self.databaseroot.geometry('500x400+450+100')
        ##--------------------------------------------------labels
        self.host=Label(self.databaseroot,relief=GROOVE,text="Hostname",font=('arial',20,'bold'))
        self.host.place(x=10,y=40)
        self.root = Label(self.databaseroot,relief=GROOVE, text="Username", font=('arial', 20, 'bold'))
        self.root.place(x=10, y=150)
        self.password = Label(self.databaseroot,relief=GROOVE, text="Password", font=('arial', 20, 'bold'))
        self.password.place(x=10, y=250)
        ##---------------------------------------------------##entry fro taking inpput itnto the database
        self.dbhostvar=StringVar()
        self.dbpassvar=StringVar()
        self.dbuservar=StringVar()
        ####--------------------------------------------------------------###entry for the  databseconnection
        self.hostentry=Entry(self.databaseroot,textvariable=self.dbhostvar,justify='right',font=('arial', 20, 'bold'))
        self.hostentry.place(x=170,y=40)
        self.userentry=Entry(self.databaseroot,textvariable=self.dbuservar,justify='right',font=('arial', 20, 'bold'))
        self.userentry.place(x=170,y=150)
        self.passentry=Entry(self.databaseroot,show="*",textvariable=self.dbpassvar,justify='right',font=('arial', 20, 'bold'))
        self.passentry.place(x=170,y=250)
        self.dbloginbtn=Button(self.databaseroot,command=self.connectdatabase,bd=5,bg="red",text="Connect",font=('arial', 20, 'bold'))
        self.dbloginbtn.place(x=5,y=340,width=490)

    ##------------------------------------------------------------------## IntroFunction for the mainwindow
    def runmwIntro(self):
        global mwintrolen
        val = self.mwintrovar.get()
        if mwintrolen > len(self.mwintrovar.get()):
            mwintrolen = 0
        mwintrolen += 1
        self.mwintroLabel.config(text=val[0:mwintrolen])
        self.mwintroLabel.after(200, self.runmwIntro)

     ##################################################################mainwindow for filing fir or checking the status for previous file filr
    def mainwindow(self):
        self.master.withdraw()
        self.mw_create_file_fir_database()
        self.mainmaster=Toplevel(self.master)
        self.mainmaster.geometry('1000x690+230+5')
        self.mainmaster.resizable(False,False)
        self.mainmaster.iconbitmap('1.ico')
        self.mainmaster.grab_set()
        self.mainmaster.focus_set()
        self.mainmaster.protocol("WM_DELETE_WINDOW", self.on_closing)
        ###-------------------------------------------------------------intro label
        self.mwintrovar=StringVar()
        self.mwintrovar.set('ONLINE CRIME REPORTING  PANEL')
        self.mwintroLabel=Label(self.mainmaster,text='',font=('roman',40,'bold'),borderwidth = 5,relief=RIDGE,bg='red')
        self.mwintroLabel.place(x=0,y=0,height=90,width=1000)
        self.runmwIntro()
        self.mwIntro_color_changer()
        ##-------------------------------------------------- Embedding the frame into the mainwindow
        self.mwleftframe=Frame(self.mainmaster,bd=3,relief=GROOVE,bg="gold2")
        self.mwleftframe.place(x=0,y=90,height=910,width=310)
        self.mwrightframe=Frame(self.mainmaster,borderwidth=3,bg="snow3",relief=GROOVE)
        self.mwrightframe.place(x=310,y=90,height=600,width=690)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('roman', 20, 'bold'), foreground='blue')
        style.configure('Treeview', font=('roman', 12, 'bold'),rowheight=50,rowwidth=300, foreground='blue', bg='powder blue')


        mwscrollrightframe_x = Scrollbar(self.mwrightframe, orient=HORIZONTAL)
        mwscrollrightframe_y = Scrollbar(self.mwrightframe, orient=VERTICAL)


        self.mwfirtable = Treeview(self.mwrightframe, columns=(
        'Complaint Id', 'Title', 'CrimeDate', 'CrimeLocation', 'Fir Status'),
                                   yscrollcommand=mwscrollrightframe_y.set,
                                   xscrollcommand=mwscrollrightframe_x.set)
        mwscrollrightframe_x.pack(side=BOTTOM, fill=X)
        mwscrollrightframe_y.pack(side=RIGHT, fill=Y)
        mwscrollrightframe_x.config(command=self.mwfirtable.xview)
        mwscrollrightframe_y.config(command=self.mwfirtable.yview)
        self.mwfirtable.heading('Complaint Id',text='Complaint Id')
        self.mwfirtable.heading('Title',text='Title')
        self.mwfirtable.heading('CrimeDate',text='CrimeDate')
        self.mwfirtable.heading('CrimeLocation',text='CrimeLocation')
        self.mwfirtable.heading('Fir Status',text='Status')
        """
        #self.mwfirtable.heading('Register By',text='Filed By')
        """
        self.mwfirtable['show']='headings'
        self.mwfirtable.pack(fill=BOTH, expand=1)


        ##----------------------------------------------------------### different buttons for the leftframe
        self.mwnewreport = Button(self.mwleftframe, bd=5, relief=GROOVE, activebackground='red', text='New Complaint',
                                  font=('roman', 20, 'italic bold'), bg='blue', foreground='white',command=self.mw_fir_registration_form)
        self.mwnewreport.place(x=5, y=50, height=70, width=290)


        self.mwyourcomplaints=Button(self.mwleftframe,bd=5,relief=GROOVE,activebackground='red',text='Check Your Comaplaints',font=('roman',20,'italic bold'),bg='blue',foreground='white',command=self.select_your_firs)
        self.mwyourcomplaints.place(x=5,y=150,height=70,width=290)

        self.mwallcomplaints = Button(self.mwleftframe, bd=5, relief=GROOVE, activebackground='red', text='All Complaints',
                                  font=('roman', 20, 'italic bold'), bg='blue',command=self.select_all_firs, foreground='white')
        self.mwallcomplaints.place(x=5, y=250, height=70, width=290)

        self.mwenterdangerareas= Button(self.mwleftframe, bd=5, relief=GROOVE, activebackground='red', text='Suggest Dangour Areas',
                                  font=('roman', 20, 'italic bold'),command=self.dangerous_place_frame, bg='blue', foreground='white')
        self.mwenterdangerareas.place(x=5, y=350, height=70, width=290)

        self.mwcheckdangerareas = Button(self.mwleftframe, bd=5, relief=GROOVE, activebackground='red', text='Check Danger Areas',
                                  font=('roman', 20, 'italic bold'), command=self.danger_areas_name,bg='blue', foreground='white')
        self.mwcheckdangerareas.place(x=5, y=450, height=70, width=290)
    ##---------------------------------------------------------------------------showwing the all danger areas frame
    def danger_areas_name(self):
        self.dgshowroot=Toplevel(self.mainmaster)
        self.dgshowroot.geometry('500x500+500+100')
        self.dgshowroot.resizable(False,False)
        self.dgshowroot.iconbitmap('1.ico')
        self.dgshowroot.grab_set()
        self.dgnameframe=Frame(self.dgshowroot,bg='gold2',borderwidth=3,relief=GROOVE)
        self.dgnameframe.place(x=0,y=0,width=500,height=500)
        ##-----------------------------------------------------------##creating the tree view of the window
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('roman', 20, 'bold'), foreground='black')
        style.configure('Treeview', font=('roman', 12, 'bold'), rowheight=50, foreground='blue', bg='powder blue')
        mwscrollrightdgframe_x = Scrollbar(self.dgnameframe, orient=HORIZONTAL)
        mwscrollrightdgframe_y = Scrollbar(self.dgnameframe, orient=VERTICAL)

        self.mwcitytable = Treeview(self.dgnameframe, columns=(
        'Names',),yscrollcommand=mwscrollrightdgframe_y.set,
        xscrollcommand=mwscrollrightdgframe_x.set)
        mwscrollrightdgframe_x.pack(side=BOTTOM, fill=X)
        mwscrollrightdgframe_y.pack(side=RIGHT, fill=Y)
        mwscrollrightdgframe_x.config(command=self.mwcitytable.xview)
        mwscrollrightdgframe_y.config(command=self.mwcitytable.yview)
        self.mwcitytable.heading('Names', text='Danger Areas Name')
        self.mwcitytable['show'] = 'headings'
        self.mwcitytable.pack(fill=BOTH, expand=1)
        self.get_dgcity_names()


    ###-------------------------------------------------------------------------------------for selecting the city name from the database
    def get_dgcity_names(self):
        global connection,my_cursor
        try:
            sql='SELECT `name` FROM `dangerous_city` GROUP BY NAME;'
            my_cursor.execute(sql)
            data=my_cursor.fetchall()
            if data==():
                raise
            for i in data:
                vv=["                              "+i[0]]
                self.mwcitytable.insert('',END,values=vv)
        except:
            messagebox.showinfo('Notification','We Haven\'t have the City Names')

    ##-----------------------------------------------------------------------function for making root visible again
    def on_closing(self):
        self.mainmaster.destroy()
        self.master.deiconify()


    ####-----------------------------------------------------------------------------------------##Methods for taking the all name of the all dangerous places
    def dangerous_place_frame(self):
        self.dangerous_city_database_create()
        self.dangerarearoot=Toplevel(self.mwrightframe)
        self.dangerarearoot.geometry('500x330+500+250')
        self.dangerarearoot.iconbitmap('1.ico')
        self.dangerarearoot.grab_set()
        self.dangerarearoot.title('Online Crime Reporting Sysytem')
        self.dangerarearoot.config(bg='grey')
        self.dangerarearoot.resizable(False,False)
        ##--------------------------------------------------------------------label for the daner area windows
        self.dglabel=Label(self.dangerarearoot,text='Please Suggest Danger Areas in Your City To Help Others',font=('roman',15,'bold'),bg='purple')
        self.dglabel.place(x=9,y=0,height=90)
        ##-------------------------------------var for entry box
        self.dgvar=StringVar()
        ##-----------------------------------------------------------------------------------------entry Box For taking input of danger areas
        self.dgEntry=Entry(self.dangerarearoot,bd=4,textvariable=self.dgvar,justify='right',relief=GROOVE,font=('roman',30,'italic bold'),bg='white')
        self.dgEntry.place(x=25,y=110,width=450,height=70)
        self.dgEntry.focus_set()

        ###----------------------------------------------------------------------##SubmitDangerarea
        self.dgbtn=Button(self.dangerarearoot,text='Submit',command=self.danger_city_submit_database,activebackground='powder blue',font=('roman',30,'italic bold'),bg='red')
        self.dgbtn.place(x=4,y=240,width=490)

        self.dgbtn.bind('<Enter>',self.bg_submit_enter)
        self.dgbtn.bind('<Leave>',self.bg_submit_leave)
    ###-----------------------------------------------inseting the city into the database
    def danger_city_submit_database(self):
        global connection,my_cursor
        city=self.dgvar.get()
        symbols=['.',',','*','#','@','!',')','(','&','%','+','=','-','_','|','/',';',':','`','~','<','>','1','2','3','4','5','6','7','8','9','0']
        try:
            for i in symbols:
                if i in city:
                    messagebox.showerror('Error', 'PLease Enter A Valid Name Without Special Character')
                    return
            sql="""INSERT INTO `dangerous_city` (`id`, `name`, `user_id`) VALUES(%s , %s, %s);"""
            values=('',city,USER_CREDENTIALS['id'])
            my_cursor.execute(sql,values)
            connection.commit()
        except:
            messagebox.showinfo('Notification','Error While Execution')

    ##-------------------------------------------------------------##database creation for the danger city
    def dangerous_city_database_create(self):
        global connection,my_cursor
        try:
            sql=""" create table `dangerous_city`( `id` int(10) primary key auto_increment, `name` varchar(20),`user_id` int(10),foreign key(user_id) references  onlinecrimereporting(registration));"""
            my_cursor.execute(sql)
            connection.commit()
        except:
            pass
    ###---------------------------------------------------------##methof to create the hover effect on the btn
    def bg_submit_enter(self,event):
        self.dgbtn.config(bg='gold2')
    def bg_submit_leave(self,event):
        self.dgbtn.config(bg='red')
    #####------------------------------------------------------------------##method for biding with button of daner areas

    ###------------------------------------------------------------------###methdo for taking all value from database
    def select_your_firs(self):
        global connection,my_cursor
        try:
            sql='SELECT * FROM `file_fir` WHERE `user_id`=%s'
            value=(USER_CREDENTIALS['id'],)
            my_cursor.execute(sql,value)
            datas=my_cursor.fetchall()
            self.mwfirtable.delete(*self.mwfirtable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[5]]
                self.mwfirtable.insert('',END,values=vv)
            if datas==():
                raise
            messagebox.showinfo('Notification', 'All Pending And Processing Complaints', parent=self.mainmaster)
        except:
            messagebox.showinfo('Notification',"You Haven't filed Any Complaints", parent=self.mainmaster)
    ####------------------------------------------------------------------------###method for showing the all filled report which are peding or processing
    def select_all_firs(self):
        global connection,my_cursor
        try:
            sql='SELECT * FROM `file_fir` WHERE `STATUS`=%s or `STATUS`=%s '
            value=('pending','processing')
            my_cursor.execute(sql,value)
            datas=my_cursor.fetchall()
            self.mwfirtable.delete(*self.mwfirtable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[5]]
                self.mwfirtable.insert('',END,values=vv)
            if datas == ():
                raise
            messagebox.showinfo('Notification','All Pending And Processing Complaints',parent=self.mainmaster)
        except:
            messagebox.showinfo('Notification',"Thier Is No Any Pending Or Processing Complaints", parent=self.mainmaster)
    ##########################-------------------------------------------------method for fir registration
    def mw_fir_registration_form(self):
        self.newfirregister=Toplevel(self.mwrightframe)
        self.newfirregister.geometry('500x500+600+80')
        self.newfirregister.title('FIll FIR FORM')
        self.newfirregister.resizable(False,False)
        self.newfirregister.iconbitmap('1.ico')
        self.newfirregister.grab_set()
        self.newfirregister.config(bg="pink1")
        ##------------------------------------------------------------------------labels for the filing the fir
        self.mwfirtitle=Label(self.newfirregister,text='Title',bd=3,relief=GROOVE,font=('roman',25,'bold'))
        self.mwfirtitle.place(x=10,y=20,height=50,width=160)
        self.mwfircrimedate = Label(self.newfirregister, text='Date', bd=3, relief=GROOVE, font=('roman', 25, 'bold'))
        self.mwfircrimedate.place(x=10, y=110, height=50, width=160)
        self.mwfircrimelocation = Label(self.newfirregister, text='Location', bd=3, relief=GROOVE, font=('roman', 25, 'bold'))
        self.mwfircrimelocation.place(x=10, y=200, height=50, width=160)
        self.mwfirdescription = Label(self.newfirregister, text='Description', bd=3, relief=GROOVE, font=('roman', 25, 'bold'))
        self.mwfirdescription.place(x=10, y=290, height=50, width=160)
        ####-------------------------------------------------------------------------------##stringvariablesfor the form
        self.mwtitlevar=StringVar()
        #self.mwcrimedatevar=StringVar()
        self.mwcrimelocationvar=StringVar()
        #####-------------------------------------------------------------------------entry and text are for the main_window fir form

        self.mwfirtitleentry=Entry(self.newfirregister,textvariable=self.mwtitlevar,font=('roman',20,'bold'),bd=3,relief=GROOVE)
        self.mwfirtitleentry.place(x=200,y=20,width=300,height=50)
        self.mwfirtitleentry.focus_set()
        self.mwfircrimedate=DateEntry(self.newfirregister,height=300)
        self.mwfircrimedate.place(x=250,y=110)

        """
        self.mwfircrimedateentry = Entry(self.newfirregister, textvariable=self.mwcrimedatevar, font=('roman', 20, 'bold'),
                                     bd=3, relief=GROOVE)
        self.mwfircrimedateentry.place(x=200, y=110, width=300, height=50)"""

        self.mwfircrimelocationentry = Entry(self.newfirregister, textvariable=self.mwcrimelocationvar, font=('roman', 20, 'bold'),
                                     bd=3, relief=GROOVE)
        self.mwfircrimelocationentry.place(x=200, y=200, width=300, height=50)
        self.mwdescriptionentry=Text(self.newfirregister,height=4,width=20,font=("roman", 20, 'bold'))
        self.mwdescriptionentry.place(x=200,y=290)
        self.mwrgscroll = Scrollbar(self.newfirregister, command=self.mwdescriptionentry.yview)
        self.mwrgscroll.place(x=465,y=290,height=130)
        ###----------------------------------------------------------------buttons for fir form
        self.mwfirsubmitbtn=Button(self.newfirregister,bg="blue",command=self.fir_submmit,activebackground="red",activeforeground="white",bd=4,relief=GROOVE,text='Submit',font=('roman',20,'bold'))
        self.mwfirsubmitbtn.place(x=10,y=440,height=50,width=130)
        self.mwfircleartbtn = Button(self.newfirregister,bg="green",activebackground="orange",command=self.clear_fir_var,activeforeground="white", text='Clear',bd=4,relief=GROOVE, font=('roman', 20, 'bold'))
        self.mwfircleartbtn.place(x=160, y=440, height=50, width=130)
    #########################################################################method for clearing the var of fir forms
    def clear_fir_var(self):
        self.mwtitlevar.set('')
        self.mwcrimelocationvar.set('')
        self.mwdescriptionentry.delete('1.0', END)
    def fir_submmit(self):
        global connection,my_cursor
        title=self.mwtitlevar.get()
        crimedate=self.mwfircrimedate.get()
        crimeloaction=self.mwcrimelocationvar.get()
        description=self.mwdescriptionentry.get("1.0",END)
        try:
            sql="""INSERT INTO `file_fir` (`ID`, `TITLE`, `CRIMEDATE`, `CRIMELOCATION`, `DESCRIPTION`, `STATUS`, `USER_ID`) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            values=('',title,crimedate,crimeloaction,description,'pending',USER_CREDENTIALS['id'])
            my_cursor.execute(sql,values)
            connection.commit()
            messagebox.showinfo('Notification','Your Complaint Is Pending')
            return
        except:
            print('Notification','We Have Some Problem While Saving Your Information in DataBase Try After Some Time')


    ######---------------------------------------------------------------------------------###creating the database when the window opened
    def mw_create_file_fir_database(self):
        global connection,my_cursor
        try:
            sql="""CREATE TABLE FILE_FIR( ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,TITLE VARCHAR(20) NOT NULL,
            CRIMEDATE VARCHAR(20) NOT NULL,
            CRIMELOCATION VARCHAR(20) NOT NULL,
            DESCRIPTION VARCHAR(100) NOT NULL,
            STATUS VARCHAR(20) NOT NULL,
            USER_ID INT NOT NULL,
            FOREIGN KEY(USER_ID) REFERENCES onlinecrimereporting(registration));"""
            my_cursor.execute(sql);
            connection.commit();
            messagebox.showinfo('Notification','Your information will remain hide from others')
        except:
            messagebox.showinfo('Notification', 'Your information will remain hide from others')

    #########################################################method for validating the user (under progress)
    def login_vaildation(self):
        global connection, my_cursor, VERIFY_DB
        FLAG=False
        email = self.lguservar.get()
        password = self.lgpassvar.get()
        try:
            if VERIFY_DB==0:
                messagebox.showinfo('Notification','Please Connect To Database First')
                return
            if len(password)==0 or len(email)==0:
                raise
            sql = "SELECT * FROM onlinecrimereporting WHERE email=%s and password=%s"
            values = (email, password)
            my_cursor.execute(sql, values)
            connection.commit()
            records = my_cursor.fetchall()
            if records:
                for row in records:
                    USER_CREDENTIALS['id']=row[0]
                    USER_CREDENTIALS['name']=row[1]
                    USER_CREDENTIALS['email']=row[2]
                    USER_CREDENTIALS['password']=row[3]
                    USER_CREDENTIALS['mobile']=row[4]
                    USER_CREDENTIALS['address']=row[5]
                    self.mainwindow()
            else:
                messagebox.showerror("Warning","Please Enter Right Credentials")
        except:
            messagebox.showinfo("Notification",'Please Fill All Input Fileds')

    #method for connecting to the database22---------------------------------##
    def connectdatabase(self):
        global connection,my_cursor,VERIFY_DB
        hostname=self.dbhostvar.get()
        username=self.dbuservar.get()
        password=self.dbpassvar.get()
        try:
            connection=pymysql.connect(hostname,username,password)
            my_cursor=connection.cursor()
            messagebox.showinfo("Notification","Database successfully Connected")
            try:
                sql = "CREATE DATABASE ONLINECRIMEREPORTINGSYSTEM"
                my_cursor.execute(sql)
                sql = "USE ONLINECRIMEREPORTINGSYSTEM"
                my_cursor.execute(sql)
                sql = 'CREATE TABLE `onlinecrimereporting` ( `registration` INT(8) NOT NULL AUTO_INCREMENT , `name` VARCHAR(20) NOT NULL , `email` VARCHAR(20) NOT NULL , `password` VARCHAR(20) NOT NULL , `mobile` VARCHAR(10) NOT NULL , `address` VARCHAR(100) NOT NULL , PRIMARY KEY (`registration`), UNIQUE (`email`))'
                my_cursor.execute(sql)
                VERIFY_DB = 1
            except:
                sql = "USE ONLINECRIMEREPORTINGSYSTEM"
                my_cursor.execute(sql)
                connection.commit()
                VERIFY_DB = 1


        except:
            messagebox.showerror('Error','Please Enter Right options')
            self.dbpassvar.set('')
            self.dbuservar.set('')
            self.dbhostvar.set('')
    ##-------------------------------------------------------------#method for making the mwindows top bacground color change
    def mwIntro_color_changer(self):
        self.colors=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    ]
        self.mwintroLabel.config(bg=self.colors[rd.randint(0,(len(self.colors)-1))])
        self.mwintroLabel.after(1000,self.mwIntro_color_changer)
    ##----------------------------------------------------------------##method for making the login window top cahnge color
    def Intro_color_changer(self):
        self.colors=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
]
        self.introLabel.config(bg=self.colors[rd.randint(0,(len(self.colors)-1))])
        self.introLabel.after(1000,self.Intro_color_changer)
    ##------------------------------------------------------------##method for showing the register panel to the user
    def registerPanel(self):

        ##------------------------------------------------------functin for register into teh database
        def registertodb():
            global connection, my_cursor,VERIFY_DB
            name=self.rgnamevar.get()
            email=self.rgemailvar.get()
            password=self.rgpassvar.get()
            mobile=self.rgmobilevar.get()
            address=self.rgentryaddress.get("1.0",END)
            if VERIFY_DB==1:
                if (email[-1:-11:-1].lower() == "moc.liamg@" and len(email) > 9) or email[-1:-13:-1].lower() == "moc.liamtoh@" and len(email) > 9 or email[-1:-11:-1].lower() == "moc.oohay@" and len(email) > 9:
                    pass
                elif len(email) == 0:
                    messagebox.showinfo('Notification', 'Please Fill Email Address',parent=self.rgroot)
                    return
                else:
                    messagebox.showinfo('Notification', 'Enter a right email address ',parent=self.rgroot)
                    return
                if  len(password)>6 or len(password)==0:
                    pass
                else:
                    messagebox.showinfo('Notification', 'Choose a Strong Password',parent=self.rgroot)
                    return
                if len(mobile)<10:
                    messagebox.showinfo('Notitfication','Please Enter valid mobile number',parent=self.rgroot)
                    return

                try:
                    sql = "INSERT INTO onlinecrimereporting(registration, name, email, password, mobile, address) VALUES (%s, %s, %s, %s, %s, %s)"
                    values=('',name,email,password,mobile,address)
                    my_cursor.execute(sql,values)
                    connection.commit()
                    messagebox.showinfo('Success', 'You Have Registered Successfully',parent=self.rgroot)
                except:
                    messagebox.showinfo('Notification','This Email  is Taken Please Enter Right One',parent=self.rgroot)
            else:
                messagebox.showinfo('Notification', 'Please Connect to the database first',parent=self.rgroot)

        ##----------------------------------------#####################################################3
        self.rgroot=Toplevel(master=self.master)
        self.rgroot.grab_set()
        self.rgroot.config(bg="Blue")
        self.rgroot.resizable(False,False)
        self.rgroot.iconbitmap('1.ico')
        self.rgroot.title('Online Crime Reporting System')
        self.rgroot.geometry('500x500+450+60')

        ##-------------------------------------------------------------##creating the labels for the register page
        self.rgname=Label(self.rgroot,text="Name",font=("roman",20,'bold'))
        self.rgname.place(x=20,y=30,height=40,width=120)
        self.rgemail = Label(self.rgroot, text="Email", font=("roman", 20, 'bold'))
        self.rgemail.place(x=20, y=100,height=40,width=120)
        self.rgpass= Label(self.rgroot, text="Password", font=("roman", 20, 'bold'))
        self.rgpass.place(x=20, y=170,height=40,width=120)
        self.rgmobile = Label(self.rgroot, text="Mobile", font=("roman", 20, 'bold'))
        self.rgmobile.place(x=20, y=240,height=40,width=120)
        self.rgaddress = Label(self.rgroot, text="Address", font=("roman", 20, 'bold'))
        self.rgaddress.place(x=20, y=310,height=40,width=120)
        ##---------------------------------------------------------------------------entruboxes for the register
        self.rgnamevar=StringVar()
        self.rgemailvar=StringVar()
        self.rgpassvar=StringVar()
        self.rgmobilevar=StringVar()
        self.rgaddress=StringVar()
        self.rgentryname=Entry(self.rgroot,justify="left",bd=5,textvariable=self.rgnamevar,font=("roman", 20, 'bold'))
        self.rgentryname.place(x=190,y=30,width=300)
        self.rgentryemail=Entry(self.rgroot,justify="left",bd=5,textvariable=self.rgemailvar,font=("roman", 20, 'bold'))
        self.rgentryemail.place(x=190,y=100,width=300)
        self.rgentrypass=Entry(self.rgroot,justify="left",bd=5,textvariable=self.rgpassvar,font=("roman", 20, 'bold'))
        self.rgentrypass.place(x=190,y=170,width=300)
        self.rgentrymobile=Entry(self.rgroot,justify="left",bd=5,textvariable=self.rgmobilevar,font=("roman", 20, 'bold'))
        self.rgentrymobile.place(x=190,y=240,width=300)
        self.rgentryaddress=Text(self.rgroot,height=3,width=20,font=("roman", 20, 'bold'))
        self.rgentryaddress.place(x=190,y=310)
        self.rgscroll = Scrollbar(self.rgroot,command=self.rgentryaddress.yview)
        self.rgscroll.place(x=455,y=310,height=97)
        self.rgentryaddress.config(yscrollcommand=self.rgscroll.set)
        self.rgregisterbtn=Button(self.rgroot,bd=5,bg="maroon1",activebackground='orange red',activeforeground='white',command=registertodb,text='Register',font=("roman", 20, 'bold'))
        self.rgregisterbtn.place(x=0,y=430,width=500,height=70)


################################################main method startting point of the program
def main():
    global FLAG
    root=Tk()
    root.resizable(False,False)
    login=Crime_login(root)
    root.mainloop()




if __name__=="__main__":
    main()