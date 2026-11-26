import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import os
import sys

class SignToolGUI:
    def __init__(self, root):
        self.root = root
        root.title("S37 Signature Tool")

        # Input file
        tk.Label(root, text="Input file (.s37):").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.input_file = tk.StringVar()
        tk.Entry(root, textvariable=self.input_file, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(root, text="Browse...", command=self.browse_input).grid(row=0, column=2, padx=5, pady=5)

        # Private key
        tk.Label(root, text="Private key (.pem):").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.key_file = tk.StringVar()
        tk.Entry(root, textvariable=self.key_file, width=50).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(root, text="Browse...", command=self.browse_key).grid(row=1, column=2, padx=5, pady=5)

        # Public key
        tk.Label(root, text="Public key (.pem):").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.pubkey_file = tk.StringVar()
        tk.Entry(root, textvariable=self.pubkey_file, width=50).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(root, text="Browse...", command=self.browse_pubkey).grid(row=2, column=2, padx=5, pady=5)

        # Output file (auto-generated, editable)
        tk.Label(root, text="Output file:").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.output_file = tk.StringVar()
        tk.Entry(root, textvariable=self.output_file, width=50).grid(row=3, column=1, padx=5, pady=5)

        # Execute button
        tk.Button(root, text="Execute Signature", command=self.run_sign, bg="lightblue", width=15).grid(row=4, column=1, pady=10)

        # Log output area
        self.log_text = scrolledtext.ScrolledText(root, width=80, height=15, state='normal')
        self.log_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        self.log_text.config(state='disabled')

        # Bind input file change to auto-update output name
        self.input_file.trace('w', self.update_output_name)

    def browse_input(self):
        filename = filedialog.askopenfilename(title="Select input file", filetypes=[("S37 files", "*.s37"), ("All files", "*.*")])
        if filename:
            self.input_file.set(filename)

    def browse_key(self):
        filename = filedialog.askopenfilename(title="Select private key file", filetypes=[("PEM files", "*.pem"), ("All files", "*.*")])
        if filename:
            self.key_file.set(filename)

    def browse_pubkey(self):
        filename = filedialog.askopenfilename(title="Select public key file", filetypes=[("PEM files", "*.pem"), ("All files", "*.*")])
        if filename:
            self.pubkey_file.set(filename)

    def update_output_name(self, *args):
        input_path = self.input_file.get()
        if input_path:
            dirname = os.path.dirname(input_path)
            basename = os.path.basename(input_path)
            name, ext = os.path.splitext(basename)
            # Append "-sign" before the extension
            new_name = f"{name}-sign{ext}"
            output_path = os.path.join(dirname, new_name)
            self.output_file.set(output_path)

    def log(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')

    def run_sign(self):
        # Validate all fields
        input_path = self.input_file.get().strip()
        key_path = self.key_file.get().strip()
        pub_path = self.pubkey_file.get().strip()
        out_path = self.output_file.get().strip()

        if not all([input_path, key_path, pub_path, out_path]):
            messagebox.showerror("Error", "All file paths must be filled in!")
            return

        for path in [input_path, key_path, pub_path]:
            if not os.path.isfile(path):
                messagebox.showerror("Error", f"File not found: {path}")
                return

        # Build the command
        cmd = [
            "commander", "convert",
            input_path,
            "--secureboot",
            "--keyfile", key_path,
            "--verify", pub_path,
            "--outfile", out_path
        ]

        self.log("=" * 50)
        self.log(f"Executing command: {' '.join(cmd)}")

        try:
            # Run the command and capture output
            result = subprocess.run(cmd, capture_output=True, text=True, shell=False)
            if result.stdout:
                self.log("[Standard Output]")
                self.log(result.stdout.strip())
            if result.stderr:
                self.log("[Standard Error]")
                self.log(result.stderr.strip())
            if result.returncode == 0:
                self.log("Signature succeeded!")
            else:
                self.log(f"Command failed with return code: {result.returncode}")
                messagebox.showerror("Execution Failed", f"Command returned code: {result.returncode}\nPlease check the log for details.")
        except FileNotFoundError:
            self.log("Error: 'commander' command not found. Make sure it is installed and in PATH.")
            messagebox.showerror("Command Not Found", "'commander' command not found. Please check your environment.")
        except Exception as e:
            self.log(f"Exception occurred: {e}")
            messagebox.showerror("Exception", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SignToolGUI(root)
    root.mainloop()