# Akshay Subramanian CLass: FHSD Cap Stone Project #4 #
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def ping():
    url = url_entry.get()
    result = subprocess.run(['ping', '-c', '3', url], stdout=subprocess.PIPE)
    print(result.returncode)
    if result.returncode == 0:
        out_label = tk.Label(frame_URL,text = result.stdout)
        out_label.pack(side=tk.BOTTOM)
    else:
        out_label = tk.Label(frame_URL,text = result.stdout)
        out_label.pack(side=tk.BOTTOM)

def tracert():
    tracerturl = url_entry.get()
    result = subprocess.run(['traceroute', tracerturl], stdout = subprocess.PIPE)
    print(result.returncode)
    if result.returncode == 0:
        out_label = tk.Label(frame_URL,text = result.stdout)
        out_label.pack(side=tk.BOTTOM)
    else:
        out_label = tk.Label(frame_URL,text = result.stdout)
        out_label.pack(side=tk.BOTTOM)

def nslookup():
    nslookupurl = url_entry.get()
    result = subprocess.run(['nslookup', nslookupurl], stdout = subprocess.PIPE)
    if result.returncode == 0:
        out_label = tk.Label(frame_URL,text = result.stdout)
        out_label.pack(side=tk.BOTTOM)
    else:
        out_label = tk.Label(frame_URL,text = result.stdout)
        out_label.pack(side=tk.BOTTOM)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center", font=("comic sans", 14), bd=0, 
    relief=tk.FLAT, cursor="heart", fg="mediumpurple3", bg="black")  
url_label.pack(side=tk.LEFT)

url_entry = tk.Entry(frame_URL,font=("comic sans",14))
url_entry.pack(side=tk.LEFT)

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="ping", command=ping)
ping_btn.pack()
tracert_btn = tk.Button(frame, text="tracert", command = tracert)
tracert_btn.pack()
nslookup_btn = tk.Button(frame, text = "nslookup", command = nslookup)
nslookup_btn.pack()

frame = tk.Frame(root)
root.mainloop()