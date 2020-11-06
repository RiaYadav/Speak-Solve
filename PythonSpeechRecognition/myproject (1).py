import pyttsx3
import random
import speech_recognition as sr
import datetime
import wikipedia
import wolframalpha
import os
import sys
import time
from tkinter import *
from PIL import ImageTk,Image

global query
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('KJ6LUW-EXVPWE64YV')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sayit(var):
    print(var)
    engine.say(var)
    engine.runAndWait()
def myCommand():
    global query1
    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 4000   
        audio = r.listen(source)
    try:
        query1 = r.recognize_google(audio, language='en-in')
        print('User: ' + query1 + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try speaking again')
        #query1 = str(input('Command: '))
        query1=myCommand()
    except sr.ValuError:
        speak('oops! we was not able to reconize it well')
    return query1
        


def buttonclick():
    #e1.delete(first=0,last=100)
    speak('Whats your query')
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 4000    
        audio = r.listen(source)
    try:
        global query
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        #Label(root,text=query,bg="plum1", fg="black").pack()
        #entry_text=StringVar()
        #e = Entry(root, width="30", textvariable=entry_text)
        #e.grid()
        #e.delete(first=0,last=100)
        #e.insert(0, query)
        #entry_text.set(query)
        
        if 'general' in query or 'general purpose calculator' in query:                  
            GENERAL()
        elif 'BMI' in query or 'bmi check' in query:    
            BMI()
        elif 'discount' in query or 'DISCOUNT check' in query:    
            DISCOUNT()
        elif 'temperature' in query or 'DISCOUNT check' in query:
            TEMPERATURE()
        elif 'finance' in query or 'finance based calculator' in query:
            FINANCE()
        elif 'GST' in query or 'GST counter' in query:
            GST()
        elif 'SPLIT BILL' in query or 'split' in query or 'bill' in query:
            SPLIT()
        elif 'temperature convertor' in query or 'temperature' in query:
            TEMPERATURE()
        else:
            query = query
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text 
                speak('WOLFRAM-ALPHA says - ')
                speak('Got it.')
                sayit(results)
                Label(root,text=results,bg="plum1", fg="black").pack()

            except:
                speak('Sorry sir,maam! I didn\'t get that! Try speaking again!')
                query = buttonclick()     
            speak('next command sir')
                
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try speaking again!')
        query = buttonclick()
        
    return query            

def GENERAL():
    global root2
    root2=Toplevel(root)
    root2.title("SPEAK & SOLVE (GENRAL PURPOSE CALCULATOR)")
    #root2.configure(bg="SlateGray3")                   
    speak('okay, we further have following options')
    lblgen=Label(root2,text="GENERAL PURPOSE CALCULATOR",bg="Black",fg="white",height="3",font=("Calibri",15)).grid(row=1,column=1,columnspan=3)
    Label(root2,text="").grid(row=2,column=1,columnspan=3)

    photo5=ImageTk.PhotoImage(Image.open("micpic.png"))
    mic=Button(root2,text="Speak" ,bg="black", fg="white",image=photo5,compound=TOP,command=buttonclick)
    mic.image=photo5
    mic.grid(row=3,column=1,columnspan=3)
    
    f1=Frame(root2)
    f1.grid(row=4,column=1,columnspan=3)
    Label(f1,text="").grid(row=5,column=1,columnspan=3)
    speak('BMI CHECK:')
    #Label(root,text="",bg="SlateGray3").grid(row=13,column=1,columnspan=3) 
    photo5=ImageTk.PhotoImage(Image.open("bmi.png"))
    b1=Button(f1,text="BMI" ,bg="black", fg="white",image=photo5,compound=TOP,command=BMI)
    b1.image=photo5
    b1.grid(row=6,column=1,padx=(0,20))
    

    speak('DISCOUNT CHECK:')
    #Label(root2,text="",bg="thistle")..grid(row=1,column=1,columnspan=3)
    photo6=ImageTk.PhotoImage(Image.open("discount.png"))
    b2=Button(f1,text="Discount",bg="black", fg="white", image=photo6,compound=TOP,command=DISCOUNT)
    b2.image=photo6
    b2.grid(row=6,column=2)
    
    
    speak('TEMPERATURE CONVERTER:')
    #Label(root2,text="",bg="thistle")..grid(row=1,column=1,columnspan=3)
    photo7=ImageTk.PhotoImage(Image.open("temp.png"))
    b3=Button(f1,text="Temprature" ,bg="black", fg="white",image=photo7,compound=TOP, command=TEMPERATURE)
    b3.image=photo7
    b3.grid(row=6,column=3,padx = (15,0))

def des():
    lf.destroy()
    lf.grid_forget()
def destroy_widget(widget):
    widget.destroy()

def BMI():
    #global root2
    #root2=Tk()
    #root2.title("SPEAK & SOLVE (GENRAL PURPOSE CALCULATOR)")
    #root2.configure(bg="thistle")
    global lf
    lf=LabelFrame(root2,text="BMI",padx=5,pady=5)
    lf.grid(row=5,column=1,columnspan=3)
    speak('whats your weight in kg:')
    Label(lf,text= "Whats your weight in kg:").grid(row=6,column=1)
    weight=myCommand()
    Label(lf,text=weight).grid(row=6,column=2)

    
    speak('whats your height in cm:')
    Label(lf,text="What's your height in cm:").grid(row=7,column=1)
    height=myCommand()
    #hr=StringVar()
    Label(lf,text=height).grid(row=7,column=2)
    weight1=float(weight)
    height1=float(height)
    height_m=height1/100
    bmi=weight1/(height_m * height_m)
    sayit(bmi)        
    if bmi<18.5:
        Label(lf,text=bmi).grid(row=8,column=1)
        speak('YOU ARE UNDERWEIGHT...HAVE A HEALTHY DIET ')
        Label(lf,text="YOU ARE UNDERWEIGHT...HAVE A HEALTHY DIET").grid(row=9,column=1)
    elif bmi>=18.5 and bmi<=24.9:
        Label(lf,text=bmi).grid(row=8,column=1)
        speak('YOU ARE HAVING A HEALTHY WEIGHT....GOOD GOING ')
        Label(lf,text="YOU ARE HAVING A HEALTHY WEIGHT....GOOD GOING").grid(row=9,column=1)
    elif bmi==25 and bmi<=29.9:
        Label(lf,text=bmi).grid(row=8,column=1)
        speak('YOU ARE OVERWEIGHT ....NEED TO SWITCH TO HEALTHY DIET:-)')
        Label(lf,text="YOU ARE OVERWEIGHT ....NEED TO SWITCH TO HEALTHY DIET:-)").grid(row=9,column=1)
    else:
        Label(lf,text=bmi).grid(row=8,column=1)
        speak('YOU ARE IN OBESE CATEGORY...REALLY NEED TO WORKOUT FOR HEALTHY LIFE...:-)')
        Label(lf,text="YOU ARE IN OBESE CATEGORY...REALLY NEED TO WORKOUT FOR HEALTHY LIFE...:-)").grid(row=9,column=1)
    Button(lf,text="Cancel",command=des).grid(row=9,column=2)
    root2.after(60000, destroy_widget, lf)
def DISCOUNT():
    #global root2
    #root2=Tk()
    #root2.title("SPEAK & SOLVE (GENRAL PURPOSE CALCULATOR)")
    #root2.configure(bg="thistle")
    #for widget in lf.winfo_children():
       #lf.destroy()

       #lf.pack_forget()
    global df
    df=LabelFrame(root2,text="DISCOUNT",padx=5,pady=5)
    df.grid(row=10,column=1,columnspan=3)
    try:
        speak("ENTER ORIGINAL AMOUNT BELOW")
        Label(df,text= "ENTER ORIGINAL AMOUNT BELOW:").grid(row=11,column=1)
        amount1=myCommand()
        Label(df,text=amount1).grid(row=11,column=2)
    except ValueError:                          
        speak("Could not understand audio")
    try:
        speak("enter discount (%OFF)")
        Label(df,text= "enter discount (%OFF):").grid(row=12,column=1)
        discount1=myCommand()
        Label(df,text=discount1).grid(row=12,column=2)
    except LookupError:                          
        speak("Could not understand audio")
        
    amount=float(amount1)
    discount=float(discount1)
    saved_money=amount*(discount/100)
    amount_paid=amount-saved_money            
    speak("you saved")
    sayit(saved_money)
    Label(df,text="Saved Money:").grid(row=13,column=1)
    Label(df,text=saved_money).grid(row=13,column=2)
    speak("you paid")
    sayit(amount_paid)
    Label(df,text="Amount Paid:").grid(row=14,column=1)
    Label(df,text= amount_paid).grid(row=14,column=2)
    root2.after(60000, destroy_widget, df)
def TEMPERATURE():#not working well
    #btncel=Button(root2,text="CELCIUS TO FAHRENHEIT" , width=20 ,bg="black", fg="white", command=BMI).pack()
    #btnfah=Button(root2,text="FAHRENHEIT TO CELCIUS " , width=20 ,bg="black", fg="white", command=BMI).pack()
    global tf
    tf=LabelFrame(root2,text="TEMPERATURE",padx=5,pady=5)
    tf.grid(row=16,column=1,columnspan=3)
    
    speak("Enter your temperature in CELSIUS")
    Label(tf,text= "Temperature in celcius:").grid(row=17,column=1)
    celcius=myCommand()
    celcius1=float(celcius)
    Label(tf,text= celcius1).grid(row=17,column=2)
    F=(celcius1*1.8)+32
    speak("temperature in fahrenheit is: ")
    Label(tf,text= "Calculated Temperature in Fahrenheit:").grid(row=18,column=1)
    Label(tf,text=F).grid(row=18,column=2)
    sayit(F)

    
    speak("Enter temperature in fahrenheit:")
    Label(tf,text= "Temperature in Fahrenehit:").grid(row=19,column=1)
    far=myCommand()
    far1=float(far)
    Label(tf,text= far1).grid(row=19,column=2)
    c=((far1-32)*(5/9))
    speak("temperature in celsius is:")
    Label(tf,text= "Calculated Temperature in Celcius:").grid(row=20,column=1)

    Label(tf,text=c).grid(row=20,column=2)
    sayit(c)          
    root2.after(60000, destroy_widget, tf)
def FINANCE():
    global root3
    root3=Toplevel(root)
    root3.title("SPEAK & SOLVE (FINANCE BASED CALCULATOR)")
    #root2.configure(bg="SlateGray3")                   
    speak('okay, we further have following options')
    lblgen=Label(root3,text="FINANCE BASED CALCULATOR",bg="Black",fg="white",height="3",font=("Calibri",15)).grid(row=1,column=1,columnspan=2)
    Label(root3,text="").grid(row=2,column=1,columnspan=2)

    photo5=ImageTk.PhotoImage(Image.open("micpic.png"))
    mic=Button(root3,text="Speak" ,bg="black", fg="white",image=photo5,compound=TOP,command=buttonclick)
    mic.image=photo5
    mic.grid(row=3,column=1,columnspan=2)
    Label(root3,text="").grid(row=4,column=1,columnspan=2)
    f1=Frame(root3)
    f1.grid(row=5,column=1,columnspan=2)

    speak('GST CHECK:')
    #Label(root,text="",bg="SlateGray3").grid(row=13,column=1,columnspan=3) 
    photo5=ImageTk.PhotoImage(Image.open("gst.png"))
    b1=Button(f1,text="GST" ,bg="black", fg="white",image=photo5,compound=TOP,command=GST)
    b1.image=photo5
    b1.grid(row=7,column=1,padx = (0,40))
    

    speak('SPLIT BILL:')
    #Label(root2,text="",bg="thistle")..grid(row=1,column=1,columnspan=3)
    photo6=ImageTk.PhotoImage(Image.open("splitbill.png"))
    b2=Button(f1,text="SplitBill",bg="black", fg="white", image=photo6,compound=TOP,command=SPLIT)
    b2.image=photo6
    b2.grid(row=7,column=2)
    
def GST():

    global gstf
    gstf=LabelFrame(root3,text="GST",padx=5,pady=5)
    gstf.grid(row=6,column=1,columnspan=3)
    speak("Enter your amount:")
    Label(gstf,text="YOUR ORIGINAL AMOUNT:").grid(row=7,column=1)
    a=myCommand()
    a1=float(a)
    Label(gstf,text=a1).grid(row=7,column=2)
    threepercent_gst=a1+(3*a1/100)
    fivepercent_gst=a1+(5*a1/100)
    twelvepercent_gst=a1+(12*a1/100)
    eighteenpercent_gst=a1+(18*a1/100)
            #ERROR aa raha h cant convert words into numeric value#
            #thousand bolnepe 1000 nhi hua one thousand bolna pdega#
    speak("by applying gst of 3% finalamount is")
    sayit(threepercent_gst)
    Label(gstf,text="threepercent_gst(3%):").grid(row=8,column=1)
    Label(gstf,text=threepercent_gst).grid(row=8,column=2)
    
    speak("by applying gst of 5% finalamount is")
    sayit(fivepercent_gst)
    Label(gstf,text="fivepercent_gst(5%):").grid(row=9,column=1)
    Label(gstf,text=fivepercent_gst).grid(row=9,column=2)
    
    speak("by applying gst of 12% finalamount is")
    sayit(twelvepercent_gst)
    Label(gstf,text="twelvepercent_gst(12%):").grid(row=10,column=1)
    Label(gstf,text=twelvepercent_gst).grid(row=10,column=2)
    
    speak("by applying gst of 18% finalamount is")
    sayit(eighteenpercent_gst)
    Label(gstf,text="eighteenpercent_gst(18%):").grid(row=11,column=1)
    Label(gstf,text=eighteenpercent_gst).grid(row=11,column=2)
    root3.after(60000, destroy_widget, gstf)
def SPLIT():
    global sf
    sf=LabelFrame(root3,text="SPLIT BILL",padx=5,pady=5)
    sf.grid(row=12,column=1,columnspan=2)
    speak("Enter your final amount")
    Final_amount=myCommand()
    Label(sf,text="Total Amount").grid(row=13,column=1)
    Label(sf,text=Final_amount).grid(row=13,column=2)
    
    speak("Enter total number of person")
    Num=myCommand()
    Label(sf,text="Total no. of person").grid(row=14,column=1)
    Label(sf,text=Num).grid(row=14,column=2)
    
    Distributed_Amount=float(Final_amount)/ float(Num)
    speak("Amount each should share is")
    sayit(Distributed_Amount)
    Label(sf,text="Amount eah should share is:").grid(row=15,column=1)
    Label(sf,text=Distributed_Amount).grid(row=15,column=2)
    root3.after(60000, destroy_widget, sf)
def BASIC():
    query = myCommand()
    n1=LabelFrame(root,text="Basic Calculations",padx=5,pady=5)
    n1.grid(row=11,column=1,columnspan=3)
    Label(n1,text="YOUR QUERY:").grid(row=12,column=1)
    Label(n1,text=query).grid(row=12,column=2)
    speak('Searching...')
    try:
        res = client.query(query)
        results = next(res.results).text 
        speak('WOLFRAM-ALPHA says - ')
        speak('Got it.')
        sayit(results)
        Label(n1,text="Result:").grid(row=13,column=1)
        Label(n1,text=results).grid(row=13,column=2)

    except:
        speak('Sorry sir,maam! I didn\'t get that! Try speaking again typing the command!')
        query = myCommand()
        #query=Entry(n1,).grid(row=14,column=1)
    #speak('next command sir')
    #return query  
    root.after(60000, destroy_widget, n1)
global root
root=Tk()
root.title("SPEAK & SOLVE")
root.configure(bg="SlateGray3")
lbl1=Label(root,text="WELCOME TO VOICE BASED CALCULATOR", fg="white",bg="black",height="3",font=("Calibri",18)).grid(row=1,column=1,columnspan=3)
currentH = int(datetime.datetime.now().hour)
if currentH >= 0 and currentH < 12:
    lbl2=Label(root,text="Good Morning",  fg="black", bg="SlateGray3", height="3", font=("Calibri",15) ).grid(row=2,column=1,columnspan=3)
    speak("Good morning")
if currentH >= 12 and currentH < 16:
    lbl2=Label(root,text="Good Afternoon",  fg="black", bg="SlateGray3", height="3", font=("Calibri",15) ).grid(row=2,column=1,columnspan=3)
    speak("Good afternoon")
if currentH >= 16 and currentH !=0:
    lbl2=Label(root,text="Good Evening",  fg="black", bg="SlateGray3", height="3", font=("Calibri",15) ).grid(row=2,column=1,columnspan=3)
    speak("Good evening ")
lbl2=Label(root,text="we have following options to help you",  fg="black" , bg="SlateGray3").grid(row=3,column=1,columnspan=3)
Label(root,text="",bg="SlateGray3").grid(row=4,column=1,columnspan=3)
#e1=Entry(root, width="30").pack()
#Label(root,text="",bg="plum1").pack()


photo=ImageTk.PhotoImage(Image.open("micpic.png"))
btn1=Button(root,text="speak" ,image=photo, compound=TOP,bg="black", fg="white" , command=buttonclick).grid(row=5,column=1,columnspan=3)
Label(root,text="",bg="SlateGray3").grid(row=6,column=1,columnspan=3)



frame1=Frame(root).grid(row=7,column=1,columnspan=3)
#Label(root,text="",bg="plum1").grid(row=8,column=1,columnspan=3)
photo2=ImageTk.PhotoImage(Image.open("calcu.png"))
btn1=Button(frame1,text="Basic" ,image=photo2,compound=TOP ,bg="black", fg="white",command=BASIC).grid(row=9,column=1)
#Label(root,text="",bg="plum1").grid(row=1,column=1)

photo3=ImageTk.PhotoImage(Image.open("gen.png"))
btn2=Button(frame1,text="General" , image=photo3 ,compound=TOP,bg="black", fg="white", command=GENERAL).grid(row=9,column=2)
#Label(root,text="",bg="plum1").grid(row=1,column=1)

photo4=ImageTk.PhotoImage(Image.open("fin.png"))
btn3=Button(frame1,text="Financial" , image=photo4,compound=TOP ,bg="black", fg="white",command=FINANCE).grid(row=9,column=3)
Label(root,text="",bg="SlateGray3").grid(row=10,column=1,columnspan=3)


root.mainloop()
        
