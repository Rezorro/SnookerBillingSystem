import tkinter
from tkinter import *
import csv
from tkinter import messagebox
import os
import os.path
import time

#declare variables to be used
window=tkinter.Tk()
global TableNo, MinChargelistBox, PeaklistBox
PeaklistBox = ""
MinChargelistBox = ""
CurrentPeakcharge = 1
CurrentMincharge = 5
TableNo = 0
Table1status = "off"
Table1peakcharge = "0"
Table1mincharge = "0"
Table1starttime = 0
Table1finishtime = 0
Table1timeplayed = 0

Table2status = "off"
Table2peakcharge = "0"
Table2mincharge = "0"
Table2starttime = 0
Table2finishtime = 0
Table2timeplayed = 0

Table3status = "off"
Table3peakcharge = "0"
Table3mincharge = "0"
Table3starttime = 0
Table3finishtime = 0
Table3timeplayed = 0

Table4status = "off"
Table4peakcharge = "0"
Table4mincharge = "0"
Table4starttime = 0
Table4finishtime = 0
Table4timeplayed = 0

Table5status = "off"
Table5peakcharge = "0"
Table5mincharge = "0"
Table5starttime = 0
Table5finishtime = 3
Table5timeplayed = 0

Table6status = "off"
Table6peakcharge = "0"
Table6mincharge = "0"
Table6starttime = 0
Table6finishtime = 0
Table6timeplayed = 0

Table7status = "off"
Table7peakcharge = "0"
Table7mincharge = "0"
Table7starttime = 0
Table7finishtime = 0
Table7timeplayed = 0

Table8status = "off"
Table8peakcharge = "0"
Table8mincharge = "0"
Table8starttime = 0
Table8finishtime = 0
Table8timeplayed = 0

Table9status = "off"
Table9peakcharge = "0"
Table9mincharge = "0"
Table9starttime = 0
Table9finishtime = 0
Table9timeplayed = 0

#create main frame
window.title("MEMS SNOOKER")
frame = tkinter.Frame(window)
frame.pack()


#get system timetime
def get_time():
    timeVar = time.strftime("%I:%M:%S:%p")
    clock.config(text = timeVar)
    clock.after(250, get_time)

#Submit button for setupPeaklistBox to setup minimum peak charge
def Peaksubmit():    
    global CurrentPeakcharge
    selection = PeaklistBox.curselection()
    if selection:
        selected_index = selection[0]
        CurrentPeakcharge = selected_index+1
        print(CurrentPeakcharge)
        displaypeak.config(text = "CurrentPeakcharge: £" + str(CurrentPeakcharge))


#Submit button for Minsubmit to setup SetupMinChargelistBox charge
def Minsubmit():    
    selection = MinChargelistBox.curselection()
    global CurrentMincharge
    if selection:
        selected_index = selection[0]
        CurrentMincharge = selected_index + 5
        print(CurrentMincharge)
        displaymin.config(text="CurrentMincharge: £" + str(CurrentMincharge))
    
    
#open table when table button 1-9 is pressed and assign set values
def OpenTable1():
    global Table1status, Table1peakcharge, Table1mincharge, Table1starttime, Table1finishtime, CurrentPeakcharge, CurrentMincharge
    Table1peakcharge = CurrentPeakcharge
    Table1mincharge = CurrentMincharge
    Table1starttime = time.strftime("%I%M%S")
    print(Table1status, Table1peakcharge, Table1mincharge, Table1starttime)

def OpenTable2():
    global Table2status, Table2peakcharge, Table2mincharge, Table2starttime, Table2finishtime, CurrentPeakcharge, CurrentMincharge
    Table2peakcharge = CurrentPeakcharge
    Table2mincharge = CurrentMincharge
    Table2starttime = time.strftime("%I%M%S")
    print(Table2status, Table2peakcharge, Table2mincharge, Table2starttime)

def OpenTable3():
    global Table3status, Table3peakcharge, Table3mincharge, Table3starttime, Table3finishtime, CurrentPeakcharge, CurrentMincharge
    Table3peakcharge = CurrentPeakcharge
    Table3mincharge = CurrentMincharge
    Table3starttime = time.strftime("%I%M%S")
    print(Table3status, Table3peakcharge, Table3mincharge, Table3starttime)

def OpenTable4():
    global Table4status, Table4peakcharge, Table4mincharge, Table4starttime, Table4finishtime, CurrentPeakcharge, CurrentMincharge
    Table4peakcharge = CurrentPeakcharge
    Table4mincharge = CurrentMincharge
    Table4starttime = time.strftime("%I%M%S")
    print(Table4status, Table4peakcharge, Table4mincharge, Table4starttime)

def OpenTable5():
    global Table5status, Table5peakcharge, Table5mincharge, Table5starttime, Table5finishtime, CurrentPeakcharge, CurrentMincharge
    Table5peakcharge = CurrentPeakcharge
    Table5mincharge = CurrentMincharge
    Table5starttime = time.strftime("%I%M%S")
    print(Table5status, Table5peakcharge, Table5mincharge, Table5starttime)

def OpenTable6():
    global Table6status, Table6peakcharge, Table6mincharge, Table6starttime, Table6finishtime, CurrentPeakcharge, CurrentMincharge
    Table6peakcharge = CurrentPeakcharge
    Table6mincharge = CurrentMincharge
    Table6starttime = time.strftime("%I%M%S")
    print(Table6status, Table6peakcharge, Table6mincharge, Table6starttime)

def OpenTable7():
    global Table7status, Table7peakcharge, Table7mincharge, Table7starttime, Table7finishtime, CurrentPeakcharge, CurrentMincharge
    Table7peakcharge = CurrentPeakcharge
    Table7mincharge = CurrentMincharge
    Table7starttime = time.strftime("%I%M%S")
    print(Table7status, Table7peakcharge, Table7mincharge, Table7starttime)

def OpenTable8():
    global Table8status, Table8peakcharge, Table8mincharge, Table8starttime, Table8finishtime, CurrentPeakcharge, CurrentMincharge
    Table8peakcharge = CurrentPeakcharge
    Table8mincharge = CurrentMincharge
    Table8starttime = time.strftime("%I%M%S")
    print(Table8status, Table8peakcharge, Table8mincharge, Table8starttime)

def OpenTable9():
    global Table9status, Table9peakcharge, Table9mincharge, Table9starttime, Table9finishtime, CurrentPeakcharge, CurrentMincharge
    Table9peakcharge = CurrentPeakcharge
    Table9mincharge = CurrentMincharge
    Table9starttime = time.strftime("%I%M%S")
    print(Table9status, Table9peakcharge, Table9mincharge, Table9starttime)


#close table when table button 1-9 is pressed: assign set values and calculate total
def CloseTable1():
    global TableName, Table1starttime, Table1finishtime, Table1timeplayed, Table1peakcharge, Table1mincharge
    Table1finishtime = time.strftime("%I%M%S")
    Table1timeplayed = (Table1peakcharge * (int(Table1finishtime)-int(Table1starttime)))
    if Table1timeplayed < Table1mincharge:
        Table1timeplayed = Table1timeplayed + Table1mincharge
        #message box to show play details and total
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table1peakcharge) + "\nMin Charge = £" + str(Table1mincharge) + 
                        "\nTime played =   " + str(int(Table1finishtime)-int(Table1starttime)) + "\n\nTOTAL TO PAY £" + str(Table1timeplayed) )
    #date to be written to csv file
    data = [TableName, str(Table1peakcharge), str(Table1mincharge), Table1starttime, Table1finishtime, str(int(Table1finishtime)-int(Table1starttime)),
                            str(Table1timeplayed)]

    with open('SnookerBilling.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    print("appended")
    billing() # call billing to update billing file

def CloseTable2():
    global TableName, Table2starttime, Table2finishtime, Table2timeplayed, Table2peakcharge, Table2mincharge
    Table2finishtime = time.strftime("%I%M%S")
    Table2timeplayed = (Table2peakcharge * (int(Table2finishtime)-int(Table2starttime)))
    if Table2timeplayed < Table2mincharge:
        Table2timeplayed = Table2timeplayed + Table2mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table2peakcharge) + "\nMin Charge = £" + str(Table2mincharge) + 
                        "\nTime played =   " + str(int(Table2finishtime)-int(Table2starttime)) + "\n\nTOTAL TO PAY £" + str(Table2timeplayed) )
    data = [TableName, str(Table2peakcharge), str(Table2mincharge), Table2starttime, Table2finishtime, str(int(Table2finishtime)-int(Table2starttime)),
                            str(Table2timeplayed)]

    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()

def CloseTable3():
    global TableName, Table3starttime, Table3finishtime, Table3timeplayed, Table3peakcharge, Table3mincharge
    Table3finishtime = time.strftime("%I%M%S")
    Table3timeplayed = (Table3peakcharge * (int(Table3finishtime)-int(Table3starttime)))
    if Table3timeplayed < Table3mincharge:
        Table3timeplayed = Table3timeplayed + Table3mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table3peakcharge) + "\nMin Charge = £" + str(Table3mincharge) + 
                        "\nTime played =   " + str(int(Table3finishtime)-int(Table3starttime)) + "\n\nTOTAL TO PAY £" + str(Table3timeplayed) )
    data = [TableName, str(Table3peakcharge), str(Table3mincharge), Table3starttime, Table3finishtime, str(int(Table3finishtime)-int(Table3starttime)),
                            str(Table3timeplayed)]
    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()

def CloseTable4():
    global TableName, Table4starttime, Table4finishtime, Table4timeplayed, Table4peakcharge, Table4mincharge
    Table4finishtime = time.strftime("%I%M%S")
    Table4timeplayed = (Table4peakcharge * (int(Table4finishtime)-int(Table4starttime)))
    if Table4timeplayed < Table4mincharge:
        Table4timeplayed = Table4timeplayed + Table4mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table4peakcharge) + "\nMin Charge = £" + str(Table4mincharge) + 
                        "\nTime played =   " + str(int(Table4finishtime)-int(Table4starttime)) + "\n\nTOTAL TO PAY £" + str(Table4timeplayed) )
    data = [TableName, str(Table4peakcharge), str(Table4mincharge), Table4starttime, Table4finishtime, str(int(Table4finishtime)-int(Table4starttime)),
                            str(Table4timeplayed)]

    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()


def CloseTable5():
    global TableName, Table5starttime, Table5finishtime, Table5timeplayed, Table5peakcharge, Table5mincharge
    Table5finishtime = time.strftime("%I%M%S")
    Table5timeplayed = (Table5peakcharge * (int(Table5finishtime)-int(Table5starttime)))
    if Table5timeplayed < Table5mincharge:
        Table5timeplayed = Table5timeplayed + Table5mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table5peakcharge) + "\nMin Charge = £" + str(Table5mincharge) + 
                        "\nTime played =   " + str(int(Table5finishtime)-int(Table5starttime)) + "\n\nTOTAL TO PAY £" + str(Table5timeplayed) )
    data = [TableName, str(Table5peakcharge), str(Table5mincharge), Table5starttime, Table5finishtime, str(int(Table5finishtime)-int(Table5starttime)),
                            str(Table5timeplayed)]
    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()

def CloseTable6():
    global TableName, Table6starttime, Table6finishtime, Table6timeplayed, Table6peakcharge, Table6mincharge
    Table6finishtime = time.strftime("%I%M%S")
    Table6timeplayed = (Table6peakcharge * (int(Table6finishtime)-int(Table6starttime)))
    if Table6timeplayed < Table6mincharge:
        Table6timeplayed = Table6timeplayed + Table6mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table6peakcharge) + "\nMin Charge = £" + str(Table6mincharge) + 
                        "\nTime played =   " + str(int(Table6finishtime)-int(Table6starttime)) + "\n\nTOTAL TO PAY £" + str(Table6timeplayed) )
    data = [TableName, str(Table6peakcharge), str(Table6mincharge), Table6starttime, Table6finishtime, str(int(Table6finishtime)-int(Table6starttime)),
                            str(Table6timeplayed)]
    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()


def CloseTable7():
    global TableName, Table7starttime, Table7finishtime, Table7timeplayed, Table7peakcharge, Table7mincharge
    Table7finishtime = time.strftime("%I%M%S")
    Table7timeplayed = (Table7peakcharge * (int(Table7finishtime)-int(Table7starttime)))
    if Table7timeplayed < Table7mincharge:
        Table7timeplayed = Table7timeplayed + Table7mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table7peakcharge) + "\nMin Charge = £" + str(Table7mincharge) + 
                        "\nTime played =   " + str(int(Table7finishtime)-int(Table7starttime)) + "\n\nTOTAL TO PAY £" + str(Table7timeplayed) )
    data = [TableName, str(Table7peakcharge), str(Table7mincharge), Table7starttime, Table7finishtime, str(int(Table7finishtime)-int(Table7starttime)),
                            str(Table7timeplayed)]
    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()

def CloseTable8():
    global TableName, Table8starttime, Table8finishtime, Table8timeplayed, Table8peakcharge, Table8mincharge
    Table8finishtime = time.strftime("%I%M%S")
    Table8timeplayed = (Table8peakcharge * (int(Table8finishtime)-int(Table8starttime)))
    if Table8timeplayed < Table8mincharge:
        Table8timeplayed = Table8timeplayed + Table8mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table8peakcharge) + "\nMin Charge = £" + str(Table8mincharge) + 
                        "\nTime played =   " + str(int(Table8finishtime)-int(Table8starttime)) + "\n\nTOTAL TO PAY £" + str(Table8timeplayed) )
    data = [TableName, str(Table8peakcharge), str(Table8mincharge), Table8starttime, Table8finishtime, str(int(Table8finishtime)-int(Table8starttime)),
                            str(Table8timeplayed)]
    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()

        
def CloseTable9():
    global TableName, Table9starttime, Table9finishtime, Table9timeplayed, Table9peakcharge, Table9mincharge
    Table9finishtime = time.strftime("%I%M%S")
    Table9timeplayed = (Table9peakcharge * (int(Table9finishtime)-int(Table9starttime)))
    if Table9timeplayed < Table9mincharge:
        Table9timeplayed = Table9timeplayed + Table9mincharge
    messagebox.showinfo(TableName, TableName + "\nPeak charge = £" + str(Table9peakcharge) + "\nMin Charge = £" + str(Table9mincharge) + 
                        "\nTime played =   " + str(int(Table9finishtime)-int(Table9starttime)) + "\n\nTOTAL TO PAY £" + str(Table9timeplayed) )
    data = [TableName, str(Table9peakcharge), str(Table9mincharge), Table9starttime, Table9finishtime, str(int(Table9finishtime)-int(Table9starttime)),
                            str(Table9timeplayed)]
    with open('SnookerBilling.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    print("appended")
    billing()


#exit button to exit application. all tables have to be closed for this function to work
def Exit():
    if (Table1status == "on" or Table2status == "on" or Table3status == "on" or Table4status == "on" or Table5status == "on"
        or Table6status == "on" or Table7status == "on" or Table8status == "on" or Table9status == "on"):
        messagebox.showerror("ERROR","Cannot close this window while tables are open.")
    else:
        window.destroy()
        



#creating labels to plac within the frame
buttons_label = tkinter.LabelFrame(frame, text="BILLING", font=('consolas',15))
buttons_label.grid(row=0, column=1, sticky="ew")
tables_label = tkinter.LabelFrame(frame, text="Mem's Snooker", font=('consolas',30))
tables_label.grid(row=0, column=4, sticky="news", padx=20, pady=10)
peakLabel = tkinter.LabelFrame(frame, text="Peak Charge", font=('consolas',15))
peakLabel.grid(row=0, column=6, sticky="ns")
minLabel = tkinter.LabelFrame(frame, text="Minimum Charge", font=('consolas',15))
minLabel.grid(row=0, column=7, sticky="ns")
infolabel = tkinter.LabelFrame(frame, text="Time", font=('consolas',20))
infolabel.grid(row=10, column=4)
clock = Label(infolabel, font=("consolas", 15), bg="gray")
clock.grid(row=2, column=1)

#exit button to close wndow. all tables need to be closed for this to work
Exit_button = Button(infolabel, text="Exit", font = ("consolas",20), fg="red", command=Exit) 
Exit_button.grid(row=2, column=2,sticky="news",padx=20, pady=20)


#minimum charge price list
MinChargelistBox = Listbox(minLabel, font = ("consolas",15), bg="gray")
MinChargelistBox.grid(row=0, column=0)
MinChargelistBox.insert(1, "£5.00p")
MinChargelistBox.insert(2, "£6.00p")
MinChargelistBox.insert(3, "£7.00p")
MinChargelistBox.insert(4, "£8.00p")
MinChargelistBox.insert(5, "£9.00p")
MinChargelistBox.insert(6, "£10.00p")
MinChargelistBox.config(height = MinChargelistBox.size(), width=10)
MinsubmitButton = Button(minLabel, text="Submit", font = ("consolas",10), command=Minsubmit) 
MinsubmitButton.grid(row=1, column=0)

#peak charge price list
PeaklistBox = Listbox(peakLabel, font=("consolas", 15), bg="gray")
PeaklistBox.grid(row=0, column=0)
PeaklistBox.insert(1, "£1.00p")
PeaklistBox.insert(2, "£2.00p")
PeaklistBox.insert(3, "£3.00p")
PeaklistBox.insert(4, "£4.00p")
PeaklistBox.insert(5, "£5.00p")
PeaklistBox.insert(6, "£6.00p")
PeaklistBox.config(height=PeaklistBox.size(), width=10)
PeaksubmitButton = Button(peakLabel, text="Submit",font = ("consolas",10), command=Peaksubmit) 
PeaksubmitButton.grid(row=1, column=0)

#display peak and minimum list window
displaypeak = Label(peakLabel, text="CurrentPeakcharge: £" + str(CurrentPeakcharge), font=("consolas", 13), bg="gray")
displaypeak.grid(row=2, column=0, sticky="news",padx=20, pady=10)
displaymin = Label(minLabel, text="CurrentMincharge: £" + str(CurrentMincharge), font=("consolas", 13), bg="gray")
displaymin.grid(row=2, column=0, sticky="news",padx=20, pady=10)


#Frame setup and button creation
#Snooker tables
tables = [[1,2,3],
           [4,5,6],
           [7,8,9]]
for row in range(3):
    for column in range(3):

        TableNo += 1
        TableName = "Table" + str(TableNo)
        tables[row][column] = Button(tables_label, text="Table " + str(TableNo), font=('consolas', 15), width=8, height=3,
                                  command= lambda row=row, column=column: next_table(row,column))
        tables[row][column].grid(row=row, column=column)


#this creates the csv window to display previous billing information and creates a file if it doesnt already exist
def billing():
# Read the CSV file and store the last 8 records with extra spacing between them for easy reading
    header = ['Table_Name', 'Tablepeakcharge', 'Tablemincharge', 'Starttime', 'Finishtime', 'Time_played', 'TOTAL_TO_PAY']
    if os.path.isfile("SnookerBilling.csv") == FALSE:
            with open('SnookerBilling.csv', 'a', newline='') as f:2
            writer = csv.writer(f)
            writer.writerow(header)
    with open("SnookerBilling.csv", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)[-8:]  # Store the last 10 records

    # Display the last 10 records in the tkinter window
    for r, col in enumerate(data):
        for c, row in enumerate(col):
            label = Label(
                buttons_label, width=7, height=2, text=row
            )
            label.grid(row=r, column=c)

#creates the tables and opens and closes them with loads of other conditions
def next_table(row, column):
    global TableName
    print([row] + [column], tables[row][column]['text'])
    TableName = tables[row][column]['text'] #assign table name to table name to pass to close table to print to file
    print(tables[row][column]['text'])
    global Table1status
    global Table2status
    global Table3status
    global Table4status
    global Table5status
    global Table6status
    global Table7status
    global Table8status
    global Table9status
    
    if tables[row][column]['text'] == 'Table 1' and Table1status == 'off':
        tables[0][0].config(bg="green")
        Table1status = "on"
        OpenTable1()
        return True
    elif tables[row][column]['text'] == 'Table 1'and Table1status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[0][0].config(bg="#F0F0F0")
            Table1status = "off"
            CloseTable1()

    elif    tables[row][column]['text'] == 'Table 2' and Table2status == 'off':
        tables[0][1].config(bg="green")
        Table2status = "on"
        OpenTable2()
        return True
    elif tables[row][column]['text'] == 'Table 2'and Table2status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[0][1].config(bg="#F0F0F0")
            Table2status = "off"
            CloseTable2()
    elif    tables[row][column]['text'] == 'Table 3' and Table3status == 'off':
        tables[0][2].config(bg="green")
        Table3status = "on"
        OpenTable3()
        return True
    elif tables[row][column]['text'] == 'Table 3'and Table3status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[0][2].config(bg="#F0F0F0")
            Table3status = "off"
            CloseTable3()

    elif    tables[row][column]['text'] == 'Table 4' and Table4status == 'off':
        tables[1][0].config(bg="green")
        Table4status = "on"
        OpenTable4()
        return True
    elif tables[row][column]['text'] == 'Table 4'and Table4status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[1][0].config(bg="#F0F0F0")
            Table4status = "off"
            CloseTable4()

    elif    tables[row][column]['text'] == 'Table 5' and Table5status == 'off':
        tables[1][1].config(bg="green")
        Table5status = "on"
        OpenTable5()
        return True
    elif tables[row][column]['text'] == 'Table 5'and Table5status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[1][1].config(bg="#F0F0F0")
            Table5status = "off"
            CloseTable5()

    elif    tables[row][column]['text'] == 'Table 6' and Table6status == 'off':
        tables[1][2].config(bg="green")
        Table6status = "on"
        OpenTable6()
        return True
    elif tables[row][column]['text'] == 'Table 6'and Table6status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[1][2].config(bg="#F0F0F0")
            Table6status = "off"
            CloseTable6()

    elif    tables[row][column]['text'] == 'Table 7' and Table7status == 'off':
        tables[2][0].config(bg="green")
        Table7status = "on"
        OpenTable7()
        return True
    elif tables[row][column]['text'] == 'Table 7'and Table7status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[2][0].config(bg="#F0F0F0")
            Table7status = "off"
            CloseTable7()

    elif    tables[row][column]['text'] == 'Table 8' and Table8status == 'off':
        tables[2][1].config(bg="green")
        Table8status = "on"
        OpenTable8()
        return True
    elif tables[row][column]['text'] == 'Table 8'and Table8status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[2][1].config(bg="#F0F0F0")
            Table8status = "off"
            CloseTable8()

    elif    tables[row][column]['text'] == 'Table 9' and Table9status == 'off':
        tables[2][2].config(bg="green")
        Table9status = "on"
        OpenTable9()
        return True
    elif tables[row][column]['text'] == 'Table 9'and Table9status == 'on':
        result = messagebox.askquestion("Close table", "Would you like to close the table?")
        if result == "yes":
            tables[2][2].config(bg="#F0F0F0")
            Table9status = "off"
            CloseTable9()                 
    else:
        return False

billing()
get_time()
frame.mainloop()


