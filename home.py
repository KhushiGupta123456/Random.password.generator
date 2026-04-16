import tkinter as tk
import secrets
import string

def generate_password():
    # Get length from slider
    length = length_slider.get()
    
    # Define character pool
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Generate secure password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    # Clear the field and insert new password
    password_entry.config(state='normal') # Temporarily enable to edit
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly') # Set back to readonly so it can't be typed in

# --- UI Setup ---
root = tk.Tk()
root.title("Secure PassGen")
root.geometry("350x250")
root.resizable(False, False)

# Title
tk.Label(root, text="Secure Password Generator", font=("Arial", 14, "bold")).pack(pady=15)

# Length Slider
tk.Label(root, text="Set Password Length:").pack()
length_slider = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL, length=200)
length_slider.set(16)
length_slider.pack(pady=5)

# Password Display (Read-only so users can't accidentally type over it)
password_entry = tk.Entry(root, font=("Courier", 12), width=25, justify='center', state='readonly')
password_entry.pack(pady=15)

# Generate Button
generate_btn = tk.Button(root, text="Generate New Password", command=generate_password, 
                         bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=10)
generate_btn.pack(pady=10)

root.mainloop()
