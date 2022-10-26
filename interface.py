# Online Python-3 Compiler (Interpreter)
#!/bin/bash
pip3 install tkinter

#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

root = tkinter.Tk()
root.title('Follower package')
root.geometry('960x540')

lbl = tkinter.Text(root, height=10)
lbl.pack()

h1Font = ('Ubuntu', 18, 'bold')
h2Font = ('Ubuntu', 16, 'bold')
h3Font = ('Ubuntu', 14, 'bold')
lblFont = ('Ubuntu', 12, 'bold')

root['bg'] = '#f2f2f7'

frm = Frame(root)
frm.pack

scroll = Scrollbar(frm)
scroll.pack(side=RIGHT, fill=Y)

tbl = root.Treeview(frm)

# load SQL here
tbl['columns'] = ('Last seen','MAC','','','','','ssid','bssid')

tbl.column("#0", width=0,  stretch=NO)
tbl.column("last_seen",anchor=CENTER, width=80)
tbl.column("MAC",anchor=CENTER, width=80)
tbl.column("",anchor=CENTER, width=80)
tbl.column("crypt",anchor=CENTER, width=80)
tbl.column("ssid",anchor=CENTER, width=80)
tbl.column("bssid",anchor=CENTER, width=80)

tbl.heading("#0",text="",anchor=CENTER)
tbl.heading("last_seen",text="Last Seen",anchor=CENTER)
tbl.heading("MAC",text="MAC Addr",anchor=CENTER)
tbl.heading("",text="",anchor=CENTER)
tbl.heading("",text="",anchor=CENTER)
tbl.heading("crypt",text="Crypto",anchor=CENTER)
tbl.heading("bssid",text="BSSID",anchor=CENTER)
tbl.heading("ssid",text="SSID",anchor=CENTER)

# SQL here
for row in rows:
    tbl.insert(parent='',iid=0,text='', values=(row[0],row[1],row[2],row[3], row[4]))

tbl.pack()


# Table refresh

root.mainloop()



def updateTable():
  selected = tbl.focus()
  























