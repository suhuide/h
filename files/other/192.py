import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import winreg
import subprocess
import re
import sys

class NetworkDriveManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Drive Mapper")
        self.root.geometry("750x400")

        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview for displaying mappings
        columns = ("Drive", "Remote Path", "Status")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=12)
        self.tree.heading("Drive", text="Drive")
        self.tree.heading("Remote Path", text="Remote Path")
        self.tree.heading("Status", text="Status")
        self.tree.column("Drive", width=60, anchor="center")
        self.tree.column("Remote Path", width=400, anchor="w")
        self.tree.column("Status", width=100, anchor="center")
        self.tree.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=4, sticky=(tk.N, tk.S))

        # Button frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=1, column=0, columnspan=5, pady=10)

        ttk.Button(btn_frame, text="Refresh", command=self.refresh).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Modify", command=self.modify_drive).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Add", command=self.add_drive).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_drive).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Exit", command=root.quit).pack(side=tk.LEFT, padx=5)

        # Initial load
        self.refresh()

    def get_net_use_status(self):
        """
        Call 'net use' to get current mapping status.
        Returns dict: {drive_letter: (remote_path, status_string)}
        Status can be 'OK' or 'Unavailable' (may vary by system language).
        """
        status_dict = {}
        try:
            output = subprocess.check_output("net use", shell=True, encoding=sys.getdefaultencoding(), errors='ignore')
            lines = output.splitlines()
            for line in lines:
                line = line.strip()
                if not line or line.startswith('---') or line.startswith('Status') or line.startswith('状态'):
                    continue
                # Split by two or more spaces
                parts = re.split(r'\s{2,}', line)
                if len(parts) >= 3:
                    status = parts[0].strip()
                    local = parts[1].strip()
                    remote = parts[2].strip()
                    if local.endswith(':') and (status.lower() in ['ok', 'unavailable', '不可用']):
                        drive_letter = local[0].upper()
                        status_dict[drive_letter] = (remote, status)
        except subprocess.CalledProcessError:
            pass
        return status_dict

    def get_registry_mappings(self):
        r"""Read all mappings from registry key HKCU\Network. Returns {drive: remote_path}"""
        mappings = {}
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Network")
            index = 0
            while True:
                try:
                    subkey_name = winreg.EnumKey(key, index)
                    subkey = winreg.OpenKey(key, subkey_name)
                    try:
                        remote_path, _ = winreg.QueryValueEx(subkey, "RemotePath")
                        mappings[subkey_name.upper()] = remote_path
                    except FileNotFoundError:
                        pass
                    winreg.CloseKey(subkey)
                    index += 1
                except OSError:
                    break
            winreg.CloseKey(key)
        except Exception:
            pass
        return mappings

    def get_all_mappings(self):
        """Combine registry and net use info. Returns list of dicts with keys: drive, path, status."""
        reg_maps = self.get_registry_mappings()
        net_status = self.get_net_use_status()
        result = []
        for drive, path in reg_maps.items():
            if drive in net_status:
                remote, status = net_status[drive]
                # Normalize status display
                status_text = "Connected" if status.lower() == "ok" else "Disconnected"
                result.append({'drive': drive, 'path': path, 'status': status_text})
            else:
                result.append({'drive': drive, 'path': path, 'status': "Disconnected"})
        return result

    def refresh(self):
        """Refresh the treeview"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        mappings = self.get_all_mappings()
        for m in mappings:
            self.tree.insert("", tk.END, values=(m['drive'], m['path'], m['status']))

    def get_selected_drive(self):
        """Get the drive letter of the selected row"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a mapping first.")
            return None
        item = selected[0]
        values = self.tree.item(item, 'values')
        return values[0]

    def modify_drive(self):
        """Modify the selected mapping"""
        drive = self.get_selected_drive()
        if not drive:
            return
        # Get current path from tree
        current_path = None
        for item in self.tree.get_children():
            vals = self.tree.item(item, 'values')
            if vals[0] == drive:
                current_path = vals[1]
                break
        if current_path is None:
            return
        new_path = simpledialog.askstring("Modify Mapping",
                                          f"Enter new remote path (current: {current_path}):",
                                          parent=self.root)
        if new_path is None or new_path.strip() == "":
            return
        new_path = new_path.strip()

        # Update registry
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Network", 0, winreg.KEY_SET_VALUE)
            subkey = winreg.OpenKey(key, drive, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(subkey, "RemotePath", 0, winreg.REG_SZ, new_path)
            winreg.CloseKey(subkey)
            winreg.CloseKey(key)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update registry: {e}")
            return

        # Apply the new mapping immediately
        self.apply_net_use(drive, new_path)
        self.refresh()
        messagebox.showinfo("Success", f"Mapping {drive}: updated to {new_path}")

    def add_drive(self):
        """Add a new network drive mapping"""
        drive = simpledialog.askstring("Add Mapping", "Enter new drive letter (e.g., Z):", parent=self.root)
        if not drive or drive.strip() == "":
            return
        drive = drive.strip().upper()
        if len(drive) != 1 or not drive.isalpha():
            messagebox.showerror("Error", "Drive letter must be a single letter.")
            return

        remote_path = simpledialog.askstring("Add Mapping",
                                             "Enter remote path (e.g., \\\\server\\share):",
                                             parent=self.root)
        if not remote_path or remote_path.strip() == "":
            return
        remote_path = remote_path.strip()

        # Check if already exists
        reg_maps = self.get_registry_mappings()
        if drive in reg_maps:
            if not messagebox.askyesno("Confirm", f"Drive {drive}: already exists. Overwrite?"):
                return

        # Write to registry
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Network", 0, winreg.KEY_SET_VALUE)
            subkey = winreg.CreateKey(key, drive)
            winreg.SetValueEx(subkey, "RemotePath", 0, winreg.REG_SZ, remote_path)
            winreg.SetValueEx(subkey, "ProviderName", 0, winreg.REG_SZ, "Microsoft Windows Network")
            winreg.SetValueEx(subkey, "UserName", 0, winreg.REG_SZ, "")
            winreg.CloseKey(subkey)
            winreg.CloseKey(key)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write registry: {e}")
            return

        # Establish the connection
        self.apply_net_use(drive, remote_path, delete_first=False)
        self.refresh()
        messagebox.showinfo("Success", f"Added mapping {drive}: -> {remote_path}")

    def delete_drive(self):
        """Delete the selected mapping"""
        drive = self.get_selected_drive()
        if not drive:
            return
        if not messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete mapping {drive}:?"):
            return

        # Delete registry key
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Network", 0, winreg.KEY_SET_VALUE)
            winreg.DeleteKey(key, drive)
            winreg.CloseKey(key)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete registry key: {e}")
            return

        # Disconnect the network drive
        try:
            subprocess.run(f"net use {drive}: /delete /y", shell=True, check=False, capture_output=True)
        except Exception:
            pass

        self.refresh()
        messagebox.showinfo("Success", f"Mapping {drive}: deleted.")

    def apply_net_use(self, drive, remote_path, delete_first=True):
        """Apply mapping using net use (delete existing if needed, then create)"""
        if delete_first:
            try:
                subprocess.run(f"net use {drive}: /delete /y", shell=True, check=False, capture_output=True)
            except Exception:
                pass
        try:
            result = subprocess.run(f"net use {drive}: {remote_path}", shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                messagebox.showwarning("Warning",
                                       f"Failed to establish network connection:\n{result.stderr.strip()}\n"
                                       "Please check the path or permissions.")
        except Exception as e:
            messagebox.showwarning("Warning", f"Error executing net use: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkDriveManager(root)
    root.mainloop()