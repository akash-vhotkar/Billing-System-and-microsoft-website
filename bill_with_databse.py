from tkinter import *
from tkinter import messagebox
import math,random,os
from  tkinter import messagebox
import pymysql
class biling_system:
    def __init__(self,root):
        self.search_bill = StringVar()
        self.root=root
        self.root.geometry("1300x600+0+0")
        bg_color="#074463"
        title=Label(self.root,text="Biling Software",bd=12,bg=bg_color,fg="red",font=("times of new roman",30,"bold"),relief=GROOVE).pack(fill=X)

#=========================variables==========================================================
        #=======================cosmetic variables=================
        self.face_cream=IntVar()
        self.soap=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #==========================grocery variables======================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugsr=IntVar()
        self.tea=IntVar()
        #====================cold drink variables=======================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumsup=IntVar()
        self.limka=IntVar()
        self.sprite=IntVar()

        #===================customer variables=============================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_billno=StringVar()
        x=random.randint(1000,9999)
        self.c_billno.set(str(x))
        #=========================prize variables===============
        self.cosmetic_prize=StringVar()
        self.grocery_prize=StringVar()
        self.colddrink_prize=StringVar()
        #===================tax variable==============
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.colddrink_tax=StringVar()






 #==============================customer frame==========================================================
        f1=LabelFrame(self.root,text="customer details",font=("times of new roman",14,"bold"),fg="yellow",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)

#=============================label of customer name=======================================
        cname_lable=Label(f1,text="customer name",bg=bg_color,fg="white",font=("times of new roman",10,"bold")).grid(row=0,column=1,padx=10,pady=10)
        cname_text=Entry(f1,bg="white",width=30,textvariable=self.c_name,font=("times of new roman",10,"bold"),relief=GROOVE,bd=5).grid(row=0,column=2,padx=10,pady=10)
#============================phone no details=================================================
        cphone_lable = Label(f1, text="phone no", bg=bg_color, fg="white",font=("times of new roman", 10, "bold")).grid(row=0, column=3, padx=10, pady=10)
        cphone_text = Entry(f1, bg="white", width=30,textvariable=self.c_phone,font=("times of new roman", 10, "bold"), relief=GROOVE, bd=5).grid(row=0,column=4,padx=10,pady=10)
#======================================bill numbber label======================================
        cbillno_lable = Label(f1, text="BILL NO", bg=bg_color, fg="white",font=("times of new roman", 10, "bold")).grid(row=0, column=5, padx=10, pady=10)
        cbillno_text = Entry(f1, textvariable=self.search_bill,bg="white", width=30,font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=0, column=6, padx=10, pady=10)
#====================================search button in the f1==================================
        search_button = Button(f1, text="SEARCH", bg="white",command=self.find_bill ,fg="black",font=("times of new roman", 10, "bold")).grid(row=0, column=7, padx=60, pady=10)
#=============================frame of cosmetics======================================================
        f2 = LabelFrame(self.root, text="cosmetics product", font=("times of new roman", 14, "bold"), fg="yellow",bg=bg_color)
        f2.place(x=0, y=160,width=300,height=305)
#========================bath soap in frame f2=======================
        cbathsoap_lable = Label(f2, text="BATH SOAP", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=10)
        cbathsoap_text = Entry(f2, bg="white",textvariable=self.soap ,width=15, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=0, column=2, padx=10, pady=10)
#==================================face cream in frame f2=============================
        cfacecream_lable = Label(f2, text="FACE CREAM", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10)
        cfacecream_text = Entry(f2, bg="white",textvariable=self.face_cream ,width=15, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=1, column=2, padx=10, pady=10)
#========================================face wash============================
        cfacewash_lable = Label(f2, text="FACE WASH", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=10)
        cfacewash_text = Entry(f2, bg="white", width=15,textvariable=self.face_wash, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=2, column=2, padx=10, pady=10)
#======================================hair spray===============================
        chairspare_lable = Label(f2, text="HAIR SPRAY", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=3, column=1, padx=10, pady=10)
        chairspare_text = Entry(f2, bg="white", width=15,textvariable=self.spray, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=3, column=2, padx=10, pady=10)
#=============================================hair gell==================================
        chairgell_lable = Label(f2, text="hair gell", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=4, column=1, padx=10, pady=10)
        chairgell_text = Entry(f2, bg="white", width=15,textvariable=self.gell, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=4, column=2, padx=10, pady=10)
#====================================body lotion=============================================
        cbodylotion_lable = Label(f2, text="BODY LOTION", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=5, column=1, padx=10, pady=5)
        cbodylotion_text = Entry(f2, bg="white", width=15,textvariable=self.loshan, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=5, column=2, padx=10, pady=5)
#=========================================frame f3==============================================
        f3 = LabelFrame(self.root, text="grocery", font=("times of new roman", 14, "bold"), fg="yellow",bg=bg_color)
        f3.place(x=310, y=160, width=300, height=305)

#=========================ricee in f3=============================================
        crice_lable = Label(f3, text="RICE", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=10)
        crice_text = Entry(f3, bg="white",textvariable=self.rice, width=20, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=0,column=2, padx=10, pady=10)
#====================================food oil in the f3===============================
        cfoodoil_lable = Label(f3, text="FOOD OIL", bg=bg_color, fg="white", font=("times of new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10)
        cfoodoil_text = Entry(f3, bg="white", width=20,textvariable=self.food_oil, font=("times of new roman", 10, "bold"), relief=GROOVE, bd=5).grid(row=1, column=2, padx=10, pady=10)
#======================================daal in the f3==================================
        cdaal_lable = Label(f3, text="DAAL", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=10)
        cdaal_text = Entry(f3, bg="white", width=20,textvariable=self.daal, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=2, column=2, padx=10, pady=10)
#============================wheat in f3==================================
        cwheat_lable = Label(f3, text="WHEAT", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=3, column=1, padx=10, pady=10)
        cwheat_text = Entry(f3, bg="white", width=20,textvariable=self.wheat, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=3, column=2, padx=10, pady=10)
#======================================sugar in f3==============================
        csugar_lable = Label(f3, text="SUGAR", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=4, column=1, padx=10, pady=10)
        csugar_text = Entry(f3, bg="white", width=20,textvariable=self.sugsr, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=4, column=2, padx=10, pady=10)
#===================================tea in f3======================
        ctea_lable = Label(f3, text="TEA", bg=bg_color, fg="white",font=("times of new roman", 12, "bold")).grid(row=5, column=1, padx=10, pady=5)
        ctea_text = Entry(f3, bg="white", width=20,textvariable=self.tea, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=5, column=2, padx=10, pady=5)
#==================================frame  for f4===============================
        f4 = LabelFrame(self.root, text="cold drink", font=("times of new roman", 14, "bold"), fg="yellow", bg=bg_color)
        f4.place(x=620, y=160, width=300, height=305)
#==================maza coke fruti thumsup limka sprite====================
        cmaza_lable = Label(f4, text="MAZA", bg=bg_color, fg="white", font=("times of new roman", 12, "bold")).grid(row=0,column=1,padx=10,pady=10)
        cmaza_text = Entry(f4, bg="white", width=20,textvariable=self.maza, font=("times of new roman", 10, "bold"), relief=GROOVE, bd=5).grid(row=0, column=2, padx=10, pady=10)

        ccoke_lable = Label(f4, text="COKE", bg=bg_color, fg="white", font=("times of new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10)
        ccoke_text = Entry(f4, bg="white", width=20,textvariable=self.cock, font=("times of new roman", 10, "bold"), relief=GROOVE, bd=5).grid(row=1, column=2, padx=10, pady=10)

        cfrooti_lable = Label(f4, text="FROOTI", bg=bg_color, fg="white", font=("times of new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=10)
        cfrooti_text = Entry(f4, bg="white", width=20,textvariable=self.frooti, font=("times of new roman", 10, "bold"), relief=GROOVE, bd=5).grid(row=2, column=2, padx=10, pady=10)

        cthumsup_lable = Label(f4, text="THUMSUP", bg=bg_color, fg="white", font=("times of new roman", 12, "bold")).grid(row=3, column=1, padx=10, pady=10)
        cthumsup_text = Entry(f4, bg="white", width=20,textvariable=self.thumsup, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=3, column=2, padx=10, pady=10)

        climka_lable = Label(f4, text="LIMKA", bg=bg_color, fg="white", font=("times of new roman", 12, "bold")).grid(row=4, column=1, padx=10, pady=10)
        climka_text = Entry(f4, bg="white", width=20,textvariable=self.limka, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=4, column=2, padx=10, pady=10)

        cSPRITE_lable = Label(f4, text="SPRITE", bg=bg_color, fg="white", font=("times of new roman", 12, "bold")).grid(row=5, column=1, padx=10, pady=5)
        cSPIRITE_text = Entry(f4, bg="white", width=20,textvariable=self.sprite, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=5, column=2, padx=10, pady=5)
#==============================================bill frame  main =======================
        f5 = Frame(self.root, bg="white")
        f5.place(x=930, y=160, width=325, height=305)

#===============================label of the bill area===================================
        cbillarea = Label(f5, text="BILL AREA", bg="white",bd=3 ,width=20,fg="black", font=("times of new roman", 12, "bold"),relief=GROOVE)
        cbillarea.pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        scrol_x=Scrollbar(f5,orient=HORIZONTAL)
        scrol_x.pack(fill=X,side=BOTTOM)
        self.txtarea=Text(f5)
        scrol_y.pack(fill=Y,side=RIGHT)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH)

#======================================bill menu frame
        f6 = LabelFrame(self.root, text="bill menu", font=("times of new roman", 14, "bold"), fg="yellow", bg=bg_color)
        f6.place(x=0, y=470, width=800, height=150)

#========================labels of the bill menu frame=============================
        ccosmeticbill_label = Label(f6, text="TOTAL COSMETIC PRICE", bg=bg_color, fg="white", font=("times of new roman", 10, "bold")).grid(row=0, column=1, padx=5, pady=0)
        ccosmetic_text = Entry(f6, bg="white", width=10,textvariable=self.cosmetic_prize, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=0, column=2, padx=5, pady=0)

        cgrocerybill_label = Label(f6, text="TOTAL GROCERY PRICE", bg=bg_color, fg="white",font=("times of new roman", 10, "bold")).grid(row=1, column=1, padx=5, pady=0)
        cgrocerybill_text = Entry(f6, bg="white", width=10,textvariable=self.grocery_prize, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=1, column=2, padx=5, pady=0)

        ccolddrink_label = Label(f6, text="TOTAL COLD DRINK PRICE", bg=bg_color, fg="white",font=("times of new roman", 10, "bold")).grid(row=2, column=1, padx=5, pady=0)
        ccolddrink_text = Entry(f6, bg="white", width=10,textvariable=self.colddrink_prize, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=2, column=2, padx=5, pady=0)

        ccosmetictax_label = Label(f6, text="TOTAL COSMETIC TAX", bg=bg_color, fg="white",font=("times of new roman", 10, "bold")).grid(row=0, column=3, padx=50, pady=0)
        ccosmetictax_text = Entry(f6, bg="white", width=10,textvariable=self.cosmetic_tax, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=0, column=4, padx=50, pady=0)

        cgrocerytax_label = Label(f6, text="TOTAL GROCERY TAX", bg=bg_color, fg="white",font=("times of new roman", 10, "bold")).grid(row=1, column=3, padx=50, pady=5)
        cgrocerytax_text = Entry(f6, bg="white", width=10,textvariable=self.grocery_tax, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=1, column=4, padx=50, pady=5)

        ccolddrinktax_label = Label(f6, text="TOTAL cold drink tax", bg=bg_color, fg="white",font=("times of new roman", 10, "bold")).grid(row=2, column=3, padx=50, pady=5)
        ccolddrinktax_text = Entry(f6, bg="white", width=10,textvariable=self.colddrink_tax, font=("times of new roman", 10, "bold"), relief=GROOVE,bd=5).grid(row=2, column=4, padx=50, pady=5)


        #========================frame for total and ========================
        f7 = Frame(self.root, bg=bg_color)
        f7.place(x=810, y=470, width=450, height=150)

#=======================buttons in the f7================================
        totalbut=Button(f7,text="TOTAL",command=self.Total,font=("times of new roman",10,"bold"),bg="white",fg="black",width=10,height=5,relief=GROOVE).grid(row=0,column=1,padx=5,pady=25)
        generate=Button(f7,text="GENERATE BILL",command=self.biling,font=("times of new roman",10,"bold"),bg="white",fg="black",width=10,height=5,relief=GROOVE).grid(row=0,column=2,padx=5,pady=25)
        clear=Button(f7,text="CLEAR",command=self.clear_bill,font=( "times of new roman",10,"bold"),bg="white",fg="black",width=10,height=5,relief=GROOVE).grid(row=0,column=3,padx=5,pady=25)
        exite=Button(f7,text="EXIT",command=self.exit,font=("times of new roman",10,"bold"),bg="white",fg="black",width=10,height=5,relief=GROOVE).grid(row=0,column=4,padx=5,pady=25)
        self.welcome()

    def Total(self):
        self.c_s_p = self.soap.get() * 40
        self.c_f_p = self.face_wash.get() * 60
        self.c_fc_p = self.face_cream.get() * 80
        self.c_spray_p = self.spray.get() * 100
        self.c_ge_p = self.gell.get() * 120
        self.c_lo_p = self.loshan.get() * 140

        self.Total_cosmetic_prize=float(self.c_s_p+self.c_f_p+self.c_fc_p+self.c_spray_p+self.c_ge_p+self.c_lo_p)
        self.cosmetic_prize.set(str(self.Total_cosmetic_prize))

        self.g_r_p=self.rice.get()*30
        self.g_wh_p=self.wheat.get()*40
        self.g_d_p=self.daal.get()*74
        self.g_fo_p=self.food_oil.get()*32
        self.g_su_p=self.sugsr.get()*32
        self.g_t_p=self.tea.get()*140


        self.Total_grocery_prize = float(self.g_r_p+self.g_wh_p+self.g_d_p+self.g_fo_p+self.g_su_p+self.g_t_p)
        self.grocery_prize.set(str(self.Total_grocery_prize))
        self.co_ma_p=self.maza.get()*90
        self.co_co_p=self.cock.get()*50
        self.co_lim_p=self.limka.get()*80
        self.co_fr_p=self.frooti.get()*100
        self.co_sp_p=self.sprite.get()*103
        self.co_th_p=self.thumsup.get()*122
        self.Total_colddrink_prize = float(self.co_ma_p+self.co_lim_p+self.co_co_p+self.co_fr_p+self.co_sp_p+self.co_th_p)
        self.colddrink_prize.set(str(self.Total_colddrink_prize))
        self.c_tax=round(self.Total_cosmetic_prize*0.05)
        self.gr_tax=round(self.Total_grocery_prize*0.05)
        self.co_tax=round(self.Total_colddrink_prize*0.05)
        self.cosmetic_tax.set("Rs "+str(self.c_tax))
        self.grocery_tax.set("Rs "+str(self.gr_tax))
        self.colddrink_tax.set("Rs "+str(self.co_tax))
        self.Total_bill=float(self.Total_cosmetic_prize+self.Total_grocery_prize+self.Total_colddrink_prize+self.c_tax+self.gr_tax+self.co_tax)
        self.databse_for_bill()

    def welcome(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\twelcome to akash grocery")
        self.txtarea.insert(END,f"\n\nBill no :  {self.c_billno.get()}")
        self.txtarea.insert(END,f"\nCustomer name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nphone no : {self.c_phone.get()}")
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,"\nproduct\t\tquntity\t\tprice")
        self.txtarea.insert(END,"\n======================================")


    def biling(self):
        self.welcome()
#cosmetic bill generation======================
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\nsoap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\nface wash\t\t{self.face_wash.get()}\t\t{self.c_f_p}")
        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\nface cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        if self.gell.get()!=0:
            self.txtarea.insert(END,f"\ngell\t\t{self.gell.get()}\t\t{self.c_ge_p}")
        if self.loshan.get()!=0:
            self.txtarea.insert(END,f"\nloshan\t\t{self.loshan.get()}\t\t{self.c_lo_p}")
        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\nspray\t\t{self.spray.get()}\t\t{self.c_spray_p}")
#============================foe grocery======================================
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\nrice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\nwhaet\t\t{self.wheat.get()}\t\t{self.g_wh_p}")
        if self.daal.get()!=0:
            self.txtarea.insert(END,f"\ndaal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.sugsr.get()!=0:
            self.txtarea.insert(END,f"\nsugar\t\t{self.sugsr.get()}\t\t{self.g_su_p}")
        if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\nfood oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\ntea\t\t{self.tea.get()}\t\t{self.g_t_p}")
#===========================cold drink menu=====================================
        if self.maza.get()!=0:
            self.txtarea.insert(END,f"\nmaza\t\t{self.maza.get()}\t\t{self.co_ma_p}")
        if self.frooti.get()!=0:
            self.txtarea.insert(END,f"\nfrooti\t\t{self.frooti.get()}\t\t{self.co_fr_p}")
        if self.sprite.get()!=0:
            self.txtarea.insert(END,f"\nsprite\t\t{self.spirite.get()}\t\t{self.co_sp_p}")
        if self.thumsup.get()!=0:
            self.txtarea.insert(END,f"\nthumsup\t\t{self.thumsup.get()}\t\t{self.co_th_p}")
        if self.limka.get()!=0:
            self.txtarea.insert(END,f"\nlimka\t\t{self.limka.get()}\t\t{self.co_lim_p}")
        if self.cock.get()!=0:
            self.txtarea.insert(END,f"\ncoke\t\t{self.cock.get()}\t\t{self.co_co_p}")

        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n total cosmetic tax : \t {self.cosmetic_tax.get()}")
        self.txtarea.insert(END, f"\n total grocery tax  : \t {self.grocery_tax.get()}")
        self.txtarea.insert(END, f"\n cold drink tax :\t\t{self.colddrink_tax.get()}")
        self.txtarea.insert(END, f"\n------------------------------------")
        self.txtarea.insert(END,f"\n Total bill is :\t{str(self.Total_bill)}")
        self.txtarea.insert(END,"\n--------------------------------------")
        self.txtarea.insert(END,f"\nThanks and visit again")
        self.txtarea.insert(END,"\n\n\n\n\n\n")
        self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save data","do you want save data")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bill_backup/"+str(self.c_billno.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return

    def clear_bill(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.soap.set("0")
        self.face_cream.set("0")
        self.face_wash.set("0")
        self.gell.set("0")
        self.loshan.set("0")
        self.spray.set("0")

        self.rice.set("0")
        self.wheat.set("0")
        self.daal.set("0")
        self.food_oil.set("0")
        self.tea.set("0")
        self.sugsr.set("0")

        self.maza.set("0")
        self.frooti.set("0")
        self.sprite.set("0")
        self.cock.set("0")
        self.thumsup.set("0")
        self.limka.set("0")

        self.cosmetic_prize.set("0")
        self.cosmetic_tax.set("0")
        self.grocery_prize.set("0")
        self.grocery_tax.set("0")
        self.colddrink_tax.set("0")
        self.colddrink_prize.set("0")
    def exit(self):
        op=messagebox.askyesno("exit","do you want to exit the rom softwar?")
        if op>0:
            self.root.destroy()
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bill_backup/"):
            if i.split('.')[0]==str(self.search_bill.get()):
                f1=open(f"bill_backup/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"

        if present=="no":
            messagebox.showerror("error","invalid bill no")


    def databse_for_bill(self):
        mydb=pymysql.connect(host="localhost",user="root",passwd="123456",database="student")
        mysursor=mydb.cursor()
        mysursor.execute("insert into biling values(%s,%s,%s)",(self.c_name.get(),
                                                                  self.c_phone.get(),
                                                                 self.c_billno.get()))
        mydb.commit()
        mydb.close()


root=Tk()
obj=biling_system(root)
root.mainloop()
