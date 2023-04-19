import tkinter as tk

def create_chat_window():

    # Create a root window
    root = tk.Tk()
    root.title('Tkinter Window with Message Area and Input Field')

    # Set window size and position
    root.geometry('400x200+50+50')

    # set the background of window
    root.configure(background='black')

    # Create a frame for the message area
    message_frame = tk.Frame(root, background='black')
    message_frame.grid(row=0, column=0, sticky='nsew')

    # Create a Text widget for the message area
    message_area = tk.Text(message_frame, wrap=tk.WORD, font=("Arial", 12),state='disabled', background='black', foreground='white')
    message_area.pack(expand=True, fill=tk.BOTH)

    # Function to append user input to the message area
    def process_input(event=None):
        user_text = user_input.get()
        message_area.config(state='normal')
        message_area.insert(tk.END, f"User: {user_text}\n")
        message_area.config(state='disabled')
        user_input.delete(0, tk.END)

    # Create a frame for the user input area
    input_frame = tk.Frame(root, background='black')
    input_frame.grid(row=1, column=0, sticky='ew')

    # Add an entry widget for user input at the bottom
    user_input = tk.Entry(input_frame, font=("Arial", 12), background='black', foreground='white')
    user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Bind the Enter key to the process_input function
    user_input.bind('<Return>', process_input)

    # Start the main event loop
    root.mainloop()
