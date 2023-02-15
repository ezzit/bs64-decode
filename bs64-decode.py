import os
import base64
import tkinter as tk
from tkinter import filedialog

# b64-decode
# () ezzit
# 02/2023 released

# directory for modify
def execute_modification():
    directory = directory_entry.get()
    for filename in os.listdir(directory):
        # xml file
        if filename.endswith('.xml'):
            filepath = os.path.join(directory, filename)
            # decode
            with open(filepath, 'rb') as f:
                encoded_data = f.read()
                decoded_data = base64.b64decode(encoded_data)
                # write over
                with open(filepath, 'wb') as f:
                    f.write(decoded_data)
            # uppercase name
            os.rename(filepath, os.path.join(directory, filename.upper()))
    # sucess message
    tk.Label(root, text='Success!').grid(row=2, column=2)

# define directory
def browse_folder():
    filename = filedialog.askdirectory()
    directory_entry.delete(0,tk.END)
    directory_entry.insert(0,filename)

# interface
root = tk.Tk()
# program dimensions
root.geometry("270x60")
root.resizable(False, False)
# title
root.title('XML Decode')
# label
tk.Label(root, text='Directory: ').grid(row=0, column=0)
# requests
directory_entry = tk.Entry(root)
directory_entry.grid(row=0, column=1)
# button select directory
browse_button = tk.Button(root, text='Select Folder', command=browse_folder)
browse_button.grid(row=0, column=2)
# button execute changes
execute_button = tk.Button(root, text='Execute', command=execute_modification)
execute_button.grid(row=2, column=1)
# loop
root.mainloop()