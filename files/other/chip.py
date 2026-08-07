#!/usr/bin/env python3
"""
Matter over Thread Device Management Tool
Supports Thread network management, device commissioning, OTA upgrade, and more
"""

import subprocess
import threading
import queue
import time
import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from tkinter import font as tkfont

class MatterThreadTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Matter over Thread Device Management Tool v1.0")
        self.root.geometry("1400x900")
        
        # Setup styles
        self.setup_styles()
        
        # Command execution queue
        self.cmd_queue = queue.Queue()
        self.process_running = False
        
        # OTA related variables
        self.ota_file_path = None
        self.ota_provider_pid = None
        
        # Create widgets
        self.create_widgets()
        
        # Start log processing thread
        self.process_logs()
        
        # Initialize Thread network info
        self.refresh_network_info()
        
    def setup_styles(self):
        """Setup UI styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        self.bg_color = "#2b2b2b"
        self.fg_color = "#ffffff"
        self.accent_color = "#007acc"
        self.error_color = "#ff4444"
        self.success_color = "#44ff44"
        
        self.root.configure(bg=self.bg_color)
        
    def create_widgets(self):
        """Create UI components"""
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="5")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Create Notebook
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Tab pages
        self.create_thread_tab()
        self.create_pairing_tab()
        self.create_ota_tab()
        self.create_control_tab()
        self.create_log_tab()
        
        # Status bar
        self.status_bar = ttk.Label(main_frame, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=3, column=0, sticky=(tk.W, tk.E))
        
        # Network info display area
        info_frame = ttk.LabelFrame(main_frame, text="Network Status", padding="5")
        info_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.network_label = ttk.Label(info_frame, text="Thread Network: Not Connected", foreground=self.accent_color)
        self.network_label.pack(side=tk.LEFT, padx=5)
        
        self.refresh_btn = ttk.Button(info_frame, text="Refresh Network Info", command=self.refresh_network_info)
        self.refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Quick command buttons
        quick_frame = ttk.LabelFrame(main_frame, text="Quick Actions", padding="5")
        quick_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        quick_buttons = [
            ("Read Software Version", self.cmd_read_software_version),
            ("Read Device Type", self.cmd_read_device_type),
            ("Read Endpoints", self.cmd_read_endpoints),
            ("Turn On", self.cmd_onoff_on),
            ("Turn Off", self.cmd_onoff_off),
            ("Set Brightness 50%", self.cmd_level_50),
        ]
        
        for text, command in quick_buttons:
            btn = ttk.Button(quick_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=2)
            
    def create_thread_tab(self):
        """Thread Network Management Tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Thread Network Management")
        
        # Left control panel
        control_frame = ttk.LabelFrame(tab, text="Network Control", padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Create network
        ttk.Label(control_frame, text="Create New Network:").pack(anchor=tk.W, pady=5)
        self.network_name = ttk.Entry(control_frame, width=30)
        self.network_name.insert(0, "OpenThread-225f")
        self.network_name.pack(pady=2)
        
        ttk.Button(control_frame, text="Create Thread Network", command=self.create_thread_network).pack(pady=5)
        
        ttk.Separator(control_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Channel setting
        ttk.Label(control_frame, text="Change Channel:").pack(anchor=tk.W, pady=5)
        channel_frame = ttk.Frame(control_frame)
        channel_frame.pack(fill=tk.X, pady=2)
        
        self.channel_var = tk.StringVar(value="15")
        channels = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
        ttk.Combobox(channel_frame, textvariable=self.channel_var, values=channels, width=10).pack(side=tk.LEFT)
        ttk.Button(channel_frame, text="Set Channel", command=self.set_channel).pack(side=tk.LEFT, padx=5)
        
        ttk.Separator(control_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # PAN ID setting
        ttk.Label(control_frame, text="PAN ID:").pack(anchor=tk.W, pady=5)
        panid_frame = ttk.Frame(control_frame)
        panid_frame.pack(fill=tk.X, pady=2)
        
        self.panid_var = tk.StringVar()
        ttk.Entry(panid_frame, textvariable=self.panid_var, width=20).pack(side=tk.LEFT)
        ttk.Button(panid_frame, text="Set PAN ID", command=self.set_panid).pack(side=tk.LEFT, padx=5)
        
        ttk.Separator(control_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Network key
        ttk.Label(control_frame, text="Network Key:").pack(anchor=tk.W, pady=5)
        self.network_key = tk.Text(control_frame, height=3, width=35)
        self.network_key.pack(pady=2)
        
        # Right info display
        info_frame = ttk.LabelFrame(tab, text="Network Information", padding="10")
        info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Network info display area
        self.thread_info_text = scrolledtext.ScrolledText(info_frame, height=20, width=60, bg="#1e1e1e", fg="#ffffff")
        self.thread_info_text.pack(fill=tk.BOTH, expand=True)
        
        # Button area
        btn_frame = ttk.Frame(info_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="Get Active Dataset", command=self.get_active_dataset).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Get Network State", command=self.get_network_state).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Get Neighbor Table", command=self.get_neighbor_table).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Get Router Table", command=self.get_router_table).pack(side=tk.LEFT, padx=2)
        
    def create_pairing_tab(self):
        """Device Pairing Tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Device Pairing")
        
        # Pairing configuration
        config_frame = ttk.LabelFrame(tab, text="Pairing Parameters", padding="10")
        config_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Node ID
        ttk.Label(config_frame, text="Node ID:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.node_id = ttk.Entry(config_frame, width=15)
        self.node_id.insert(0, "2250")
        self.node_id.grid(row=0, column=1, padx=5)
        
        # Passcode
        ttk.Label(config_frame, text="Passcode:").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.passcode = ttk.Entry(config_frame, width=15)
        self.passcode.insert(0, "20202021")
        self.passcode.grid(row=0, column=3, padx=5)
        
        # Discriminator
        ttk.Label(config_frame, text="Discriminator:").grid(row=0, column=4, sticky=tk.W, padx=5)
        self.discriminator = ttk.Entry(config_frame, width=15)
        self.discriminator.insert(0, "3840")
        self.discriminator.grid(row=0, column=5, padx=5)
        
        # Setup Code
        ttk.Label(config_frame, text="Setup Code:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.setup_code = ttk.Entry(config_frame, width=30)
        self.setup_code.insert(0, "MT:SAGA442C00KA0648G00")
        self.setup_code.grid(row=1, column=1, columnspan=3, sticky=tk.W, padx=5)
        
        ttk.Button(config_frame, text="Parse Setup Payload", command=self.parse_setup_payload).grid(row=1, column=5, padx=5)
        
        # Thread Dataset
        ttk.Label(config_frame, text="Thread Dataset (hex):").grid(row=2, column=0, sticky=tk.W, padx=5)
        self.thread_dataset = tk.Text(config_frame, height=3, width=80)
        self.thread_dataset.grid(row=2, column=1, columnspan=5, padx=5, pady=5)
        
        # Get current dataset from system
        ttk.Button(config_frame, text="Load Current Dataset", command=self.load_current_dataset).grid(row=3, column=0, columnspan=2, pady=5)
        
        # Pairing buttons
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="BLE Thread Pairing", command=self.pair_ble_thread, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Onnetwork Pairing", command=self.pair_onnetwork, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear Temp Files", command=self.clear_temp_files, width=20).pack(side=tk.LEFT, padx=5)
        
        # Paired device list
        device_frame = ttk.LabelFrame(tab, text="Paired Devices", padding="5")
        device_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.device_list = tk.Listbox(device_frame, height=10, bg="#1e1e1e", fg="#ffffff")
        self.device_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        ttk.Button(device_frame, text="Refresh Device List", command=self.refresh_device_list).pack(pady=5)
        
    def create_ota_tab(self):
        """OTA Upgrade Tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="OTA Upgrade")
        
        # OTA Provider configuration
        provider_frame = ttk.LabelFrame(tab, text="OTA Provider Configuration", padding="10")
        provider_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Firmware file selection
        file_frame = ttk.Frame(provider_frame)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.ota_file_label = ttk.Label(file_frame, text="No OTA file selected", foreground="gray")
        self.ota_file_label.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(file_frame, text="Select OTA File", command=self.select_ota_file).pack(side=tk.LEFT, padx=5)
        
        # Provider node ID
        provider_node_frame = ttk.Frame(provider_frame)
        provider_node_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(provider_node_frame, text="Provider Node ID:").pack(side=tk.LEFT, padx=5)
        self.provider_node_id = ttk.Entry(provider_node_frame, width=15)
        self.provider_node_id.insert(0, "1")
        self.provider_node_id.pack(side=tk.LEFT, padx=5)
        
        # Action buttons
        provider_btn_frame = ttk.Frame(provider_frame)
        provider_btn_frame.pack(pady=5)
        
        ttk.Button(provider_btn_frame, text="Start OTA Provider", command=self.start_ota_provider, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(provider_btn_frame, text="Stop OTA Provider", command=self.stop_ota_provider, width=20).pack(side=tk.LEFT, padx=5)
        
        # OTA Requestor configuration
        requestor_frame = ttk.LabelFrame(tab, text="OTA Requestor Configuration", padding="10")
        requestor_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Target device
        target_frame = ttk.Frame(requestor_frame)
        target_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(target_frame, text="Target Device Node ID:").pack(side=tk.LEFT, padx=5)
        self.target_node_id = ttk.Entry(target_frame, width=15)
        self.target_node_id.insert(0, "2250")
        self.target_node_id.pack(side=tk.LEFT, padx=5)
        
        # Trigger OTA
        ttk.Button(requestor_frame, text="Trigger OTA Upgrade", command=self.trigger_ota, width=20).pack(pady=10)
        
        # Upgrade progress display
        progress_frame = ttk.LabelFrame(tab, text="Upgrade Progress", padding="10")
        progress_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.ota_progress = ttk.Progressbar(progress_frame, mode='determinate')
        self.ota_progress.pack(fill=tk.X, pady=5)
        
        self.ota_status_label = ttk.Label(progress_frame, text="Waiting for OTA upgrade...")
        self.ota_status_label.pack(pady=5)
        
        # OTA log
        self.ota_log_text = scrolledtext.ScrolledText(progress_frame, height=10, bg="#1e1e1e", fg="#ffffff")
        self.ota_log_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Version check
        ttk.Button(progress_frame, text="Check Device Version", command=self.check_device_version).pack(pady=5)
        
    def create_control_tab(self):
        """Device Control Tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Device Control")
        
        # Command input area
        cmd_frame = ttk.LabelFrame(tab, text="Custom Command", padding="10")
        cmd_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(cmd_frame, text="Command:").pack(anchor=tk.W)
        self.custom_cmd = ttk.Entry(cmd_frame, width=100)
        self.custom_cmd.pack(fill=tk.X, pady=2)
        
        cmd_btn_frame = ttk.Frame(cmd_frame)
        cmd_btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(cmd_btn_frame, text="Execute Command", command=self.execute_custom_cmd).pack(side=tk.LEFT, padx=5)
        ttk.Button(cmd_btn_frame, text="Clear Output", command=self.clear_log).pack(side=tk.LEFT, padx=5)
        
        # Command templates
        template_frame = ttk.LabelFrame(tab, text="Command Templates", padding="10")
        template_frame.pack(fill=tk.X, padx=5, pady=5)
        
        templates = [
            ("OnOff - On", "sudo ./chip-tool onoff on {node_id} {endpoint}"),
            ("OnOff - Off", "sudo ./chip-tool onoff off {node_id} {endpoint}"),
            ("LevelControl - Set Level", "sudo ./chip-tool levelcontrol move-to-level {level} 0 0 0 {node_id} {endpoint}"),
            ("ColorControl - Color Temperature", "sudo ./chip-tool colorcontrol move-to-color-temperature {temperature} 0 0 0 {node_id} {endpoint}"),
            ("Read Basic Info", "sudo ./chip-tool basicinformation read software-version-string {node_id} {endpoint}"),
            ("Read Current Level", "sudo ./chip-tool levelcontrol read current-level {node_id} {endpoint}"),
            ("Read All Attributes", "sudo ./chip-tool levelcontrol read all {node_id} {endpoint}"),
        ]
        
        self.template_var = tk.StringVar()
        ttk.Combobox(template_frame, textvariable=self.template_var, values=[t[0] for t in templates], width=40).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(template_frame, text="Apply Template", command=lambda: self.apply_template(dict(templates))).pack(side=tk.LEFT, padx=5)
        
        # Parameter configuration
        param_frame = ttk.LabelFrame(template_frame, text="Parameters", padding="5")
        param_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(param_frame, text="Node ID:").pack(side=tk.LEFT, padx=2)
        self.cmd_node_id = ttk.Entry(param_frame, width=10)
        self.cmd_node_id.insert(0, "2250")
        self.cmd_node_id.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(param_frame, text="Endpoint:").pack(side=tk.LEFT, padx=2)
        self.cmd_endpoint = ttk.Entry(param_frame, width=10)
        self.cmd_endpoint.insert(0, "3")
        self.cmd_endpoint.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(param_frame, text="Level/Temp Value:").pack(side=tk.LEFT, padx=2)
        self.cmd_value = ttk.Entry(param_frame, width=10)
        self.cmd_value.insert(0, "128")
        self.cmd_value.pack(side=tk.LEFT, padx=2)
        
    def create_log_tab(self):
        """Log Tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Log Output")
        
        self.log_text = scrolledtext.ScrolledText(tab, bg="#1e1e1e", fg="#ffffff", font=("Courier", 10))
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Log control buttons
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="Clear Log", command=self.clear_log).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Save Log", command=self.save_log).pack(side=tk.LEFT, padx=5)
        
    def log_message(self, message, level="INFO"):
        """Log message"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        color_map = {
            "INFO": "#ffffff",
            "ERROR": "#ff4444", 
            "SUCCESS": "#44ff44",
            "WARNING": "#ffff44"
        }
        
        formatted_msg = f"[{timestamp}] [{level}] {message}\n"
        
        # Update UI in main thread
        self.root.after(0, lambda: self._update_log(formatted_msg, color_map.get(level, "#ffffff")))
        
    def _update_log(self, message, color):
        """Update log display"""
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        
        # Set color
        start = self.log_text.index("end-2l")
        end = self.log_text.index("end-1l")
        self.log_text.tag_add(f"color_{datetime.now().timestamp()}", start, end)
        self.log_text.tag_config(f"color_{datetime.now().timestamp()}", foreground=color)
        
    def clear_log(self):
        """Clear log"""
        self.log_text.delete(1.0, tk.END)
        
    def save_log(self):
        """Save log"""
        file_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.log_text.get(1.0, tk.END))
            self.log_message(f"Log saved to: {file_path}", "SUCCESS")
            
    def execute_command(self, cmd, background=True, timeout=30):
        """Execute system command"""
        if background:
            thread = threading.Thread(target=self._run_command, args=(cmd, timeout))
            thread.daemon = True
            thread.start()
            return None
        else:
            return self._run_command_sync(cmd, timeout)
            
    def _run_command(self, cmd, timeout):
        """Run command in background"""
        try:
            self.log_message(f"Executing: {cmd}", "INFO")
            self.root.after(0, lambda: self.status_bar.config(text=f"Executing: {cmd[:50]}..."))
            
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Wait for command completion
            stdout, stderr = process.communicate(timeout=timeout)
            
            if process.returncode == 0:
                self.log_message(f"Command executed successfully", "SUCCESS")
                if stdout:
                    self.log_message(f"Output:\n{stdout}", "INFO")
            else:
                self.log_message(f"Command failed (return code: {process.returncode})", "ERROR")
                if stderr:
                    self.log_message(f"Error:\n{stderr}", "ERROR")
                    
            self.root.after(0, lambda: self.status_bar.config(text="Ready"))
            
        except subprocess.TimeoutExpired:
            process.kill()
            self.log_message(f"Command timeout ({timeout} seconds)", "ERROR")
            self.root.after(0, lambda: self.status_bar.config(text="Command timeout"))
        except Exception as e:
            self.log_message(f"Command execution error: {str(e)}", "ERROR")
            self.root.after(0, lambda: self.status_bar.config(text="Command failed"))
            
    def _run_command_sync(self, cmd, timeout):
        """Run command synchronously and return output"""
        try:
            self.log_message(f"Sync execution: {cmd}", "INFO")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
            if result.returncode == 0:
                return result.stdout
            else:
                self.log_message(f"Command failed: {result.stderr}", "ERROR")
                return None
        except Exception as e:
            self.log_message(f"Execution error: {str(e)}", "ERROR")
            return None
            
    def process_logs(self):
        """Process log queue"""
        try:
            while True:
                msg = self.cmd_queue.get_nowait()
                self.log_message(msg)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.process_logs)
            
    # Thread network management methods
    def refresh_network_info(self):
        """Refresh Thread network information"""
        self.log_message("Refreshing Thread network information...", "INFO")
        
        # Get active dataset
        cmd = "sudo ot-ctl dataset active -x"
        result = self.execute_command(cmd, background=False)
        
        if result:
            dataset = result.strip()
            self.thread_dataset.delete(1.0, tk.END)
            self.thread_dataset.insert(1.0, dataset)
            
            # Parse dataset info
            info_text = f"Active Dataset:\n{dataset}\n\n"
            
            # Get other network information
            commands = [
                ("ot-ctl state", "Device State"),
                ("ot-ctl channel", "Current Channel"),
                ("ot-ctl panid", "PAN ID"),
                ("ot-ctl extpanid", "Extended PAN ID"),
                ("ot-ctl networkname", "Network Name"),
            ]
            
            for cmd, desc in commands:
                result = self.execute_command(f"sudo {cmd}", background=False)
                if result:
                    info_text += f"{desc}: {result.strip()}\n"
                    
            # Update display
            self.thread_info_text.delete(1.0, tk.END)
            self.thread_info_text.insert(1.0, info_text)
            
            self.log_message("Thread network information refreshed", "SUCCESS")
            self.root.after(0, lambda: self.status_bar.config(text="Network info refreshed"))
            
    def create_thread_network(self):
        """Create Thread network"""
        network_name = self.network_name.get()
        self.log_message(f"Creating Thread network: {network_name}", "INFO")
        
        commands = [
            "sudo ot-ctl dataset init new",
            f"sudo ot-ctl dataset networkname {network_name}",
            "sudo ot-ctl dataset commit active",
            "sudo ot-ctl ifconfig up",
            "sudo ot-ctl thread start",
        ]
        
        for cmd in commands:
            self.execute_command(cmd)
            time.sleep(1)
            
        self.log_message("Thread network created successfully", "SUCCESS")
        time.sleep(2)
        self.refresh_network_info()
        
    def set_channel(self):
        """Set channel"""
        channel = self.channel_var.get()
        self.log_message(f"Setting channel to: {channel}", "INFO")
        
        commands = [
            f"sudo ot-ctl dataset channel {channel}",
            "sudo ot-ctl dataset commit active",
        ]
        
        for cmd in commands:
            self.execute_command(cmd)
            time.sleep(0.5)
            
        self.log_message(f"Channel set to: {channel}", "SUCCESS")
        self.refresh_network_info()
        
    def set_panid(self):
        """Set PAN ID"""
        panid = self.panid_var.get()
        if panid:
            self.log_message(f"Setting PAN ID: {panid}", "INFO")
            self.execute_command(f"sudo ot-ctl panid {panid}")
            self.log_message("PAN ID set successfully", "SUCCESS")
            self.refresh_network_info()
            
    def get_active_dataset(self):
        """Get Active Dataset"""
        self.execute_command("sudo ot-ctl dataset active -x")
        
    def get_network_state(self):
        """Get network state"""
        self.execute_command("sudo ot-ctl state")
        self.execute_command("sudo ot-ctl ipaddr")
        
    def get_neighbor_table(self):
        """Get neighbor table"""
        self.execute_command("sudo ot-ctl neighbor table")
        
    def get_router_table(self):
        """Get router table"""
        self.execute_command("sudo ot-ctl router table")
        
    # Device pairing methods
    def parse_setup_payload(self):
        """Parse Setup Payload"""
        setup_code = self.setup_code.get()
        cmd = f"sudo ./chip-tool payload parse-setup-payload {setup_code}"
        self.execute_command(cmd)
        
    def load_current_dataset(self):
        """Load current Thread Dataset"""
        result = self.execute_command("sudo ot-ctl dataset active -x", background=False)
        if result:
            dataset = result.strip()
            self.thread_dataset.delete(1.0, tk.END)
            self.thread_dataset.insert(1.0, dataset)
            self.log_message("Current Thread Dataset loaded", "SUCCESS")
            
    def pair_ble_thread(self):
        """BLE Thread pairing"""
        node_id = self.node_id.get()
        dataset = self.thread_dataset.get(1.0, tk.END).strip()
        passcode = self.passcode.get()
        discriminator = self.discriminator.get()
        
        if not dataset:
            self.log_message("Please get Thread Dataset first", "ERROR")
            return
            
        cmd = f"sudo ./chip-tool pairing ble-thread {node_id} hex:{dataset} {passcode} {discriminator}"
        self.log_message(f"Starting BLE Thread pairing, Node ID: {node_id}", "INFO")
        self.execute_command(cmd)
        
    def pair_onnetwork(self):
        """Onnetwork pairing"""
        node_id = self.node_id.get()
        passcode = self.passcode.get()
        cmd = f"sudo ./chip-tool pairing onnetwork {node_id} {passcode}"
        self.log_message(f"Starting Onnetwork pairing, Node ID: {node_id}", "INFO")
        self.execute_command(cmd)
        
    def clear_temp_files(self):
        """Clear temporary files"""
        self.execute_command("sudo rm -rf /tmp/chip_*")
        self.log_message("CHIP temporary files cleared", "SUCCESS")
        
    def refresh_device_list(self):
        """Refresh device list"""
        self.device_list.delete(0, tk.END)
        # Command to get paired device list can be added here
        # Simplified version, let user manually add
        self.log_message("Please manually enter device node ID for control", "INFO")
        
    # OTA related methods
    def select_ota_file(self):
        """Select OTA firmware file"""
        file_path = filedialog.askopenfilename(filetypes=[("OTA files", "*.ota"), ("All files", "*.*")])
        if file_path:
            self.ota_file_path = file_path
            self.ota_file_label.config(text=os.path.basename(file_path), foreground="green")
            self.log_message(f"OTA file selected: {file_path}", "SUCCESS")
            
    def start_ota_provider(self):
        """Start OTA Provider"""
        if not self.ota_file_path:
            self.log_message("Please select OTA file first", "ERROR")
            messagebox.showerror("Error", "Please select OTA firmware file first")
            return
            
        provider_node = self.provider_node_id.get()
        
        # Pair Provider
        self.log_message(f"Pairing OTA Provider, Node ID: {provider_node}", "INFO")
        pair_cmd = f"sudo ./chip-tool pairing onnetwork {provider_node} 20202021"
        self.execute_command(pair_cmd)
        time.sleep(3)
        
        # Configure ACL
        self.log_message("Configuring ACL permissions", "INFO")
        acl_cmd = f'sudo ./chip-tool accesscontrol write acl \'[{{"fabricIndex": 1, "privilege": 5, "authMode": 2, "subjects": [112233], "targets": null}}, {{"fabricIndex": 1, "privilege": 3, "authMode": 2, "subjects": null, "targets": null}}]\' {provider_node} 0'
        self.execute_command(acl_cmd)
        time.sleep(2)
        
        # Start Provider application
        self.log_message("Starting OTA Provider application", "INFO")
        provider_cmd = f"sudo ./chip-ota-provider-app --KVS /tmp/chip_kvs_provider -f {self.ota_file_path} &"
        
        # Start Provider in background
        try:
            process = subprocess.Popen(provider_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.ota_provider_pid = process.pid
            self.log_message(f"OTA Provider started (PID: {self.ota_provider_pid})", "SUCCESS")
            self.ota_status_label.config(text="OTA Provider Running")
        except Exception as e:
            self.log_message(f"Failed to start OTA Provider: {str(e)}", "ERROR")
            
    def stop_ota_provider(self):
        """Stop OTA Provider"""
        if self.ota_provider_pid:
            self.execute_command(f"sudo kill -9 {self.ota_provider_pid}")
            self.log_message("OTA Provider stopped", "SUCCESS")
            self.ota_status_label.config(text="OTA Provider Stopped")
        else:
            self.execute_command("sudo pkill -f chip-ota-provider-app")
            self.log_message("All OTA Provider processes stopped", "SUCCESS")
            
    def trigger_ota(self):
        """Trigger OTA upgrade"""
        target_node = self.target_node_id.get()
        provider_node = self.provider_node_id.get()
        
        self.log_message(f"Triggering OTA upgrade for target device: {target_node}", "INFO")
        cmd = f"sudo ./chip-tool otasoftwareupdaterequestor announce-otaprovider {provider_node} 0 0 0 {target_node} 0"
        self.execute_command(cmd)
        
        # Start monitoring upgrade progress
        self.monitor_ota_progress(target_node)
        
    def monitor_ota_progress(self, target_node):
        """Monitor OTA upgrade progress"""
        def check_progress():
            # Check device version
            version_cmd = f"sudo ./chip-tool basicinformation read software-version-string {target_node} 0"
            result = self.execute_command(version_cmd, background=False)
            
            if result:
                self.ota_log_text.insert(tk.END, f"Current version: {result}\n")
                self.ota_log_text.see(tk.END)
                
            # Check OTA status (simplified here)
            # Should read OTA-related attributes for actual progress
            
            # Simulate progress update
            for i in range(0, 101, 10):
                time.sleep(0.5)
                self.root.after(0, lambda v=i: self.ota_progress.configure(value=v))
                self.root.after(0, lambda v=i: self.ota_status_label.config(text=f"Upgrading... {v}%"))
                
            self.root.after(0, lambda: self.ota_status_label.config(text="Upgrade Complete!"))
            self.root.after(0, lambda: self.log_message("OTA upgrade completed", "SUCCESS"))
            
        thread = threading.Thread(target=check_progress)
        thread.daemon = True
        thread.start()
        
    def check_device_version(self):
        """Check device version"""
        target_node = self.target_node_id.get()
        self.log_message(f"Checking device {target_node} version information", "INFO")
        
        commands = [
            f"sudo ./chip-tool basicinformation read software-version {target_node} 0",
            f"sudo ./chip-tool basicinformation read software-version-string {target_node} 0",
        ]
        
        for cmd in commands:
            self.execute_command(cmd)
            
    # Device control methods
    def cmd_read_software_version(self):
        """Read software version"""
        node_id = self.cmd_node_id.get()
        endpoint = self.cmd_endpoint.get()
        cmd = f"sudo ./chip-tool basicinformation read software-version-string {node_id} {endpoint}"
        self.execute_command(cmd)
        
    def cmd_read_device_type(self):
        """Read device type"""
        node_id = self.cmd_node_id.get()
        endpoint = self.cmd_endpoint.get()
        cmd = f"sudo ./chip-tool descriptor read device-type-list {node_id} {endpoint}"
        self.execute_command(cmd)
        
    def cmd_read_endpoints(self):
        """Read endpoints list"""
        node_id = self.cmd_node_id.get()
        cmd = f"sudo ./chip-tool descriptor read parts-list {node_id} 0"
        self.execute_command(cmd)
        
    def cmd_onoff_on(self):
        """Turn on"""
        node_id = self.cmd_node_id.get()
        endpoint = self.cmd_endpoint.get()
        cmd = f"sudo ./chip-tool onoff on {node_id} {endpoint}"
        self.execute_command(cmd)
        
    def cmd_onoff_off(self):
        """Turn off"""
        node_id = self.cmd_node_id.get()
        endpoint = self.cmd_endpoint.get()
        cmd = f"sudo ./chip-tool onoff off {node_id} {endpoint}"
        self.execute_command(cmd)
        
    def cmd_level_50(self):
        """Set brightness to 50%"""
        node_id = self.cmd_node_id.get()
        endpoint = self.cmd_endpoint.get()
        cmd = f"sudo ./chip-tool levelcontrol move-to-level 128 0 0 0 {node_id} {endpoint}"
        self.execute_command(cmd)
        
    def execute_custom_cmd(self):
        """Execute custom command"""
        cmd = self.custom_cmd.get().strip()
        if cmd:
            # Replace variables
            cmd = cmd.replace("{node_id}", self.cmd_node_id.get())
            cmd = cmd.replace("{endpoint}", self.cmd_endpoint.get())
            cmd = cmd.replace("{level}", self.cmd_value.get())
            cmd = cmd.replace("{temperature}", self.cmd_value.get())
            self.execute_command(cmd)
        else:
            self.log_message("Please enter a command", "WARNING")
            
    def apply_template(self, templates):
        """Apply command template"""
        template_name = self.template_var.get()
        template_cmd = templates.get(template_name, "")
        if template_cmd:
            self.custom_cmd.delete(0, tk.END)
            self.custom_cmd.insert(0, template_cmd)
            self.log_message(f"Template applied: {template_name}", "INFO")

def main():
    root = tk.Tk()
    app = MatterThreadTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()