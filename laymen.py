import tkinter as t
def reset():
	e1.delete(0,t.END)
	e2.delete(0,t.END)
	e3.delete(0,t.END)
	e4.delete(0,t.END)
	e5.delete(0,t.END)
	e6.delete(0,t.END)
	
def encode():
	s=e1.get()
	s1=int(e2.get())
	c=list(s)#list of all  individual characters in string s 

	l=[]#to store the cipher text characters

	for i in c:#taking every character(i) in list c	
		if(ord(i)>=97 and ord(i)<=122): #a-b
			x=(ord(i)+s1-97)%26  
			l.append(chr(x+97))
		elif(ord(i)>=65 and ord(i)<=90): #A-Z
			x=(ord(i)+s1-65)%26  
			l.append(chr(x+65))
		elif(ord(i)>=48 and ord(i)<=57): #0-9
			x=(ord(i)+s1-48)%10  
			l.append(chr(x+48))
		elif(ord(i)>=58 and ord(i)<=64): #( : , ; , < , = , > , ? , @ )
			x=(ord(i)+s1-58)%7  
			l.append(chr(x+58))
		elif(ord(i)>=32 and ord(i)<=47): #(space, ! , " ,#,$,%,&, ' ,(,),*,+, , , - , . , / )
			x=(ord(i)+s1-32)%16  
			l.append(chr(x+32))
		elif(ord(i)>=123 and ord(i)<=126): #( { , | , } , ~ )
			x=(ord(i)+s1-123)%4  
			l.append(chr(x+123))
		else:
			if(ord(i)>=91 and ord(i)<=96): #( [ , \ , ] , ^ , _ , ` )
				x=(ord(i)+s1-91)%6  
				l.append(chr(x+91))	


	mess="".join(l)#join the characters in list l and convert into string
	e3.delete(0,t.END)
	e3.insert(0,mess)
	e4.delete(0,t.END)
	e4.insert(0,mess)
def decode():
	m=e3.get()
	l=list(m)
	l2=[]#to store decoded text characters
	s2=int(e5.get())

	for i in l:#taking every character(i) in list c	
		if(ord(i)>=97 and ord(i)<=122): #a-b
			x=(ord(i)-s2-97)%26  
			l2.append(chr(x+97))
		elif(ord(i)>=65 and ord(i)<=90): #A-Z
			x=(ord(i)-s2-65)%26  
			l2.append(chr(x+65))
		elif(ord(i)>=48 and ord(i)<=57): #0-9
			x=(ord(i)-s2-48)%10  
			l2.append(chr(x+48))
		elif(ord(i)>=58 and ord(i)<=64): #( : , ; , < , = , > , ? , @ )
			x=(ord(i)-s2-58)%7  
			l2.append(chr(x+58))
		elif(ord(i)>=32 and ord(i)<=47): #(space, ! , " ,#,$,%,&, ' ,(,),*,+, , , - , . , / )
			x=(ord(i)-s2-32)%16  
			l2.append(chr(x+32))
		elif(ord(i)>=123 and ord(i)<=126): #( { , | , } , ~ )
			x=(ord(i)-s2-123)%4  
			l2.append(chr(x+123))
		else:
			if(ord(i)>=91 and ord(i)<=96): #( [ , \ , ] , ^ , _ , ` )
				x=(ord(i)-s2-91)%6  
				l2.append(chr(x+91))	
	e6.delete(0,t.END)	
	e6.insert(0,"".join(l2))
frame=t.Tk()
frame.title("PROJECT")
l1=t.Label(frame,text="MESSAGE",bg="red")
l2=t.Label(frame,text="SHIFT KEY",bg="red")
l3=t.Label(frame,text="CIPHER TEXT",bg="red")

e1=t.Entry(frame,font=('Arial',11))
e2=t.Entry(frame,font=('Arial',11))
e3=t.Entry(frame,font=('Arial',11))

b1=t.Button(frame,text="ENCODE",command=encode,bg="green")

l1.place(x=100,y=100,width=70,height=30)
l2.place(x=100,y=140,width=70,height=30)
l3.place(x=100,y=180,width=70,height=30)

e1.place(x=200,y=100,width=200,height=30)
e2.place(x=200,y=140,width=70,height=30)
e3.place(x=200,y=180,width=200,height=30)

b1.place(x=150,y=220,width=60,height=30)

l4=t.Label(frame,text="CIPHER TEXT",bg="red")
l5=t.Label(frame,text="SHIFT KEY",bg="red")
l6=t.Label(frame,text="DECODED TEXT",bg="red")

e4=t.Entry(frame,font=('Arial',11))
e5=t.Entry(frame,font=('Arial',11))
e6=t.Entry(frame,font=('Arial',11))

l4.place(x=450,y=100,width=83,height=30)
l5.place(x=450,y=140,width=83,height=30)
l6.place(x=450,y=180,width=83,height=30)

e4.place(x=550,y=100,width=200,height=30)
e5.place(x=550,y=140,width=70,height=30)
e6.place(x=550,y=180,width=200,height=30)

b2=t.Button(frame,text="DECODE",command=decode,bg="green")
b2.place(x=500,y=220,width=60,height=30)

b3=t.Button(frame,text="RESET",bg="skyblue",command=reset)
b3.place(x=320,y=280,width=60,height=30)

frame.mainloop()
