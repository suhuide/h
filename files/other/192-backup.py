import os
import subprocess
import tkinter as tk
from tkinter import messagebox

class NetworkShareOpener:
    def __init__(self, root):
        self.root = root
        self.root.title("访问网络共享")
        self.root.geometry("500x120")
        self.root.resizable(False, False)

        # 标签
        tk.Label(root, text="请输入要访问的计算机地址（UNC格式）：", font=("微软雅黑", 10)).pack(pady=5)

        # 输入框（默认值）
        self.entry = tk.Entry(root, width=60, font=("Consolas", 10))
        self.entry.insert(0, r"\\192.168.100.74")   # 原始字符串避免转义
        self.entry.pack(pady=5)

        # 按钮框架
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="打开共享", command=self.open_share, width=12).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="清空输入", command=self.clear_entry, width=12).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="退出", command=root.quit, width=12).pack(side=tk.LEFT, padx=10)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def open_share(self):
        path = self.entry.get().strip()
        if not path:
            messagebox.showwarning("提示", "地址不能为空！")
            return

        # 如果用户只输入IP，自动补全双反斜杠（但保留用户输入的完整性）
        # 更稳健：检查是否以 \\ 开头，若没有则添加（但也要考虑可能输入的是本地路径）
        # 我们直接使用用户输入，不作自动修改，但给出提示
        if not path.startswith(r"\\") and not os.path.isabs(path):
            # 若不是UNC格式也不是本地绝对路径，可能是仅IP，帮用户补全
            reply = messagebox.askyesno("确认", f"您输入的地址不是以 \\\\ 开头，是否自动补全为 \\\\{path} ？")
            if reply:
                path = r"\\" + path
                self.entry.delete(0, tk.END)
                self.entry.insert(0, path)

        # Windows下打开资源管理器
        if os.name == 'nt':
            try:
                # 方法1：使用os.startfile（简单）
                # os.startfile(path)
                # 方法2：使用explorer进程（更稳定）
                subprocess.Popen(['explorer', path], shell=True)
            except Exception as e:
                messagebox.showerror("错误", f"无法打开共享路径：{e}\n请检查地址是否正确或网络是否可达。")
        else:
            messagebox.showerror("不支持", "该工具仅支持Windows系统。")

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkShareOpener(root)
    root.mainloop()