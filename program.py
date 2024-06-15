import tkinter as tk
from tkinter import filedialog, ttk

class InterfaceApplication:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Interface Application")
        self.root.geometry("600x400")

        # Base URL input
        tk.Label(self.root, text="Base URL:").pack()
        self.base_url_entry = tk.Entry(self.root, width=50)
        self.base_url_entry.pack()

        # API Key input
        tk.Label(self.root, text="API Key:").pack()
        self.api_key_entry = tk.Entry(self.root, width=50)
        self.api_key_entry.pack()

        # Prompt input
        tk.Label(self.root, text="Prompt:").pack()
        self.prompt_entry = tk.Entry(self.root, width=50)
        self.prompt_entry.pack()

        # Model selection
        tk.Label(self.root, text="Model Name:").pack()
        self.model_var = tk.StringVar()
        self.model_selector = ttk.Combobox(self.root, textvariable=self.model_var, width=47)
        self.model_selector['values'] = ('gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k')
        self.model_selector.pack()

        # File upload
        self.file_path = tk.StringVar()
        tk.Label(self.root, text="File Upload:").pack()
        tk.Button(self.root, text="Choose File", command=self.upload_file).pack()

        # Submit button
        tk.Button(self.root, text="Run", command=self.submit).pack()

        # Output display
        tk.Label(self.root, text="Output:").pack()
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)

    def submit(self):
        # Here you would process the input data
        # For demonstration, we'll just display the inputs in the output text area
        prompt = self.prompt_entry.get()
        model = self.model_var.get()
        file_path = self.file_path.get()
        output = f"Prompt: {prompt}\nModel: {model}\nFile: {file_path}"
        self.output_text.insert(tk.END, output + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApplication(root)
    root.mainloop()