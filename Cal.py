from tkinter import *


loanAmountVar = None
annualInterestRateVar = None
numberOfYearsVar = None
monthlyPaymentVar = None
totalPaymentVar = None


def getMonthlyPayment(loanAmount, monthlyInterestRate, numberOfYears):
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
    return monthlyPayment

def computePayment():
    monthlyPayment = getMonthlyPayment(
        float(loanAmountVar.get()),
        float(annualInterestRateVar.get()) / 1200,
        int(numberOfYearsVar.get())
    )
    monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
    totalPayment = float(monthlyPaymentVar.get()) * 12 * int(numberOfYearsVar.get())
    totalPaymentVar.set(format(totalPayment, '10.2f'))

def Bond():
    global loanAmountVar, annualInterestRateVar, numberOfYearsVar, monthlyPaymentVar, totalPaymentVar

    window = Tk()
    window.title("Home Loan Calculator")
    window.geometry("400x200")

    Label(window, text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
    Label(window, text="Number of Years").grid(row=2, column=1, sticky=W)
    Label(window, text="Loan Amount").grid(row=3, column=1, sticky=W)
    Label(window, text="Simple or Compound").grid(row=4, column=1, sticky=W)
    Label(window, text="Monthly Payment").grid(row=5, column=1, sticky=W)
    Label(window, text="Total Payment").grid(row=6, column=1, sticky=W)

    annualInterestRateVar = StringVar()
    Entry(window, textvariable=annualInterestRateVar, justify=LEFT).grid(row=1, column=2)

    numberOfYearsVar = StringVar()
    Entry(window, textvariable=numberOfYearsVar, justify=LEFT).grid(row=2, column=2)

    loanAmountVar = StringVar()
    Entry(window, textvariable=loanAmountVar, justify=LEFT).grid(row=3, column=2)

    simpleorcompoundVar = StringVar()
    Entry(window, textvariable=simpleorcompoundVar, justify=LEFT).grid(row=4, column=2)

    monthlyPaymentVar = StringVar()
    lblMonthlyPayment = Label(window, textvariable=monthlyPaymentVar).grid(row=5, column=2, sticky=E)

    totalPaymentVar = StringVar()
    lblTotalPayment = Label(window, textvariable=totalPaymentVar).grid(row=6, column=2, sticky=E)

    btComputePayment = Button(window, text="Calculate", command=computePayment).grid(row=6, column=3, sticky=E)

    window.mainloop()

def Investment ():
    root=Tk()
    root.title("Investment calculator")
    root.geometry("500x300")

    def Calculate():
        prin=int(principalentry.get())
        rat=int(rateentry.get())
        tim=int(timeentry.get())
        amount=(prin*rat*tim)/100
        Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)

    principal=Label(root,text="Principal:",font="arial 15")
    rate=Label(root,text="Rate of Interest:",font="arial 15")
    time=Label(root,text="Time:",font="arial 15")

    principal.place(x=50,y=20)
    rate.place(x=50,y=90)
    time.place(x=50,y=160)

    interest=Label(root,text="Interest:",font="arial 15")
    interest.place(x=50,y=230)

    principalvalue=StringVar()
    ratevalue=StringVar()
    timevalue=StringVar()

    principalentry=Entry(root,textvariable=principalvalue,font="arial 20",width=8)
    rateentry=Entry(root,textvariable=ratevalue,font="arial 20",width=8)
    timeentry=Entry(root,textvariable=timevalue,font="arial 20",width=8)

    principalentry.place(x=200,y=20)
    rateentry.place(x=200,y=90)
    timeentry.place(x=200,y=160)

    Button(text="Calculate",font="arial 15",command=Calculate).place(x=350,y=20)
    Button(root,text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=350,y=90)

    root.mainloop()

while True:
    a = input('Pick Investment or Bond')
    if a == 'Investment':
        Investment() 
    elif a == 'Bond':
        Bond()
    else:
        break
