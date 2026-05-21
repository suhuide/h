import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import pathlib


def execute(args, check=True):
    args = [str(x) for x in args]
    cmd = ' '.join(args)
    print(f"  > {cmd}")
    complete = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if complete.returncode != 0:
        print(f"ret   : {complete.returncode}")
        print(f"stdout: {complete.stdout}")
        print(f"stderr: {complete.stderr}")
    if check and complete.returncode != 0:
        raise RuntimeError(f"Command failed [{cmd}]\n{complete.stderr}")
    return complete.returncode


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("S37 Bootloader + App Merger")
        self.root.geometry("620x240")
        self.root.resizable(True, False)

        f = ttk.Frame(root, padding="20 15 20 15")
        f.grid(row=0, column=0, sticky="nsew")
        root.columnconfigure(0, weight=1)
        f.columnconfigure(1, weight=1)

        # Bootloader
        ttk.Label(f, text="Bootloader:").grid(row=0, column=0, sticky="w", pady=(0, 2))
        bf = ttk.Frame(f)
        bf.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        self.boot_var = tk.StringVar()
        ttk.Entry(bf, textvariable=self.boot_var).pack(side="left", fill="x", expand=True)
        ttk.Button(bf, text="Browse...", command=self._browse_boot).pack(side="left", padx=(5, 0))

        # App
        ttk.Label(f, text="Application:").grid(row=2, column=0, sticky="w", pady=(0, 2))
        af = ttk.Frame(f)
        af.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        self.app_var = tk.StringVar()
        ttk.Entry(af, textvariable=self.app_var).pack(side="left", fill="x", expand=True)
        ttk.Button(af, text="Browse...", command=self._browse_app).pack(side="left", padx=(5, 0))

        # Output
        ttk.Label(f, text="Output:").grid(row=4, column=0, sticky="w", pady=(0, 2))
        of = ttk.Frame(f)
        of.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        self.out_var = tk.StringVar(value="full.s37")
        ttk.Entry(of, textvariable=self.out_var).pack(side="left", fill="x", expand=True)
        ttk.Button(of, text="Browse...", command=self._browse_out).pack(side="left", padx=(5, 0))

        # Merge button
        self.btn = ttk.Button(f, text="Merge → full.s37", command=self._merge)
        self.btn.grid(row=6, column=0, columnspan=2, pady=(0, 8))

        self.status = tk.StringVar(value="Ready")
        ttk.Label(f, textvariable=self.status, relief="sunken", anchor="w").grid(
            row=7, column=0, columnspan=2, sticky="ew")

    def _browse_boot(self):
        p = filedialog.askopenfilename(title="Select Bootloader", filetypes=[("S-Record", "*.s37 *.s19 *.s28"), ("All", "*.*")])
        if p:
            self.boot_var.set(p)

    def _browse_app(self):
        p = filedialog.askopenfilename(title="Select Application", filetypes=[("S-Record", "*.s37 *.s19 *.s28"), ("All", "*.*")])
        if p:
            self.app_var.set(p)

    def _browse_out(self):
        p = filedialog.asksaveasfilename(
            title="Save Merged File As", defaultextension=".s37",
            initialfile=self.out_var.get(),
            filetypes=[("S-Record", "*.s37"), ("All", "*.*")])
        if p:
            self.out_var.set(p)

    def _merge(self):
        boot = self.boot_var.get().strip()
        app = self.app_var.get().strip()
        out = self.out_var.get().strip()

        if not boot:
            messagebox.showerror("Error", "Please select Bootloader file")
            return
        if not app:
            messagebox.showerror("Error", "Please select Application file")
            return
        if not out:
            messagebox.showerror("Error", "Please specify Output file")
            return
        if not os.path.exists(boot):
            messagebox.showerror("Error", f"Bootloader not found:\n{boot}")
            return
        if not os.path.exists(app):
            messagebox.showerror("Error", f"Application not found:\n{app}")
            return

        self.status.set("Merging...")
        self.btn.config(state="disabled")
        self.root.update()

        try:
            execute([
                "commander", "convert",
                f'"{boot}"',
                f'"{app}"',
                "--outfile", f'"{out}"'
            ])
            self.status.set(f"Done: {out}")
            messagebox.showinfo("Done",
                f"Merged successfully!\n\n"
                f"Bootloader: {os.path.basename(boot)}\n"
                f"App:        {os.path.basename(app)}\n"
                f"Output:     {os.path.basename(out)}")
        except RuntimeError as e:
            self.status.set("Failed")
            messagebox.showerror("Error", str(e))
        finally:
            self.btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
