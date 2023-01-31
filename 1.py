from tkinter import *
b = [
'C','DEL','*','=',
'1','2','3','/',
'4','5','6','+',
'7','8','9','-',
'(','0',')','x^2'
]
def sv(form):
    if form == '':
        lbl['text']='0'
    else:
        lbl['text']=str(eval(form))
def lcalc(op):
    if op == 'C':
        sv('')
    elif op == 'DEL':
        sv(lbl['text'][0:-1])
    elif op == 'x^2':
        sv(str((eval(lbl['text']))**2))
    elif op == '=':
        sv(lbl['text'])
    else:
        if lbl['text'] == '0':
            lbl['text'] =''
        lbl['text'] = lbl['text']+op
x,y = 10,140
r = Tk()
r["bg"] = "black"
r.geometry("485x550+555+555")
r.title("Calculator")
r.resizable(False, False)
lbl=Label(r,text='0', font=("Calibri", 21, "bold"), bg="pink", fg="green")
lbl.place(x=11, y=50)
for bt in b:
    com = lambda x=bt: lcalc(x)
    Button(text=bt,bg='white',font=('Calibri',15),command=com).place(x=x,y=y,width=115,height=79)
    x +=117
    if x>400:
        x=10
        y+=81
r.mainloop()