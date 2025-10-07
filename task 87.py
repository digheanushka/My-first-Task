import tkinter as tk
from tkinter import messagebox

# Caesar cipher logic
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# GUI functionality
def encrypt_message():
    try:
        text = message_entry.get()
        shift = int(shift_entry.get())
        encrypted = caesar_encrypt(text, shift)
        result_label.config(text=f"Encrypted: {encrypted}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def decrypt_message():
    try:
        text = message_entry.get()
        shift = int(shift_entry.get())
        decrypted = caesar_decrypt(text, shift)
        result_label.config(text=f"Decrypted: {decrypted}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Create GUI
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x300")
window.resizable(False, False)

# Title Label
title_label = tk.Label(window, text="Caesar Cipher Encryption/Decryption", font=("Arial", 14))
title_label.pack(pady=10)

# Message entry
tk.Label(window, text="Enter message:").pack()
message_entry = tk.Entry(window, width=40)
message_entry.pack(pady=5)

# Shift entry
tk.Label(window, text="Enter shift value:").pack()
shift_entry = tk.Entry(window, width=10)
shift_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

encrypt_btn = tk.Button(button_frame, text="Encrypt", command=encrypt_message)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(button_frame, text="Decrypt", command=decrypt_message)
decrypt_btn.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Run the GUI loop
window.mainloop()
