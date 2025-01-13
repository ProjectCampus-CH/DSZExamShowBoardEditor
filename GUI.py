import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def open_config_file():
    file_path = tk.filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not file_path:
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        config_data = json.load(f)

    exam_infos.clear()
    for info in config_data.get('examInfos', []):
        exam_infos.append(info)
    update_exam_list()
    messagebox.showinfo("成功", f"配置文件 {file_path} 已打开。")

def validate_datetime(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%dT%H:%M:%S")
        return True
    except ValueError:
        return False

def convert_colon(text):
    return text.replace('：', ':')

def format_date(date_text):
    date_text = date_text.replace('/', '-')
    parts = date_text.split('-')
    if len(parts) == 3:
        return f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"
    else:
        raise ValueError("日期格式错误")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def edit_exam_info():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("错误", "请选择要编辑的项目信息。")
        return
    index = selected[0]
    info = exam_infos[index]

    dialog = tk.Toplevel(app)
    dialog.title("编辑考试信息")
    dialog.geometry("300x320")
    center_window(dialog)

    name_label = tk.Label(dialog, text="考试科目名称：")
    name_label.pack(pady=5)
    name_entry = tk.Entry(dialog)
    name_entry.insert(0, info['name'])
    name_entry.pack(pady=5)

    date_label = tk.Label(dialog, text="考试日期（格式：YYYY-MM-DD 或 YYYY/MM/DD）：")
    date_label.pack(pady=5)
    date_entry = tk.Entry(dialog)
    date_entry.insert(0, info['start'].split('T')[0])
    date_entry.pack(pady=5)

    start_time_label = tk.Label(dialog, text="考试开始时间（格式：HH:MM:SS）：")
    start_time_label.pack(pady=5)
    start_time_entry = tk.Entry(dialog)
    start_time_entry.insert(0, info['start'].split('T')[1])
    start_time_entry.pack(pady=5)

    end_time_label = tk.Label(dialog, text="考试结束时间（格式：HH:MM:SS）：")
    end_time_label.pack(pady=5)
    end_time_entry = tk.Entry(dialog)
    end_time_entry.insert(0, info['end'].split('T')[1])
    end_time_entry.pack(pady=5)

    def confirm():
        name = name_entry.get()
        date = date_entry.get()
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()

        if not name or not date or not start_time or not end_time:
            messagebox.showerror("错误", "所有字段都不能为空，请重新输入。")
            return

        try:
            date = format_date(date)
        except ValueError:
            messagebox.showerror("错误", "日期格式错误，请重新输入。")
            return

        start = f"{date}T{convert_colon(start_time)}"
        end = f"{date}T{convert_colon(end_time)}"

        if not validate_datetime(start) or not validate_datetime(end):
            messagebox.showerror("错误", "时间格式错误，请重新输入。")
            return

        exam_infos[index] = {
            "name": name,
            "start": start,
            "end": end
        }
        update_exam_list()
        messagebox.showinfo("成功", "考试信息已更新。")
        dialog.destroy()

    confirm_button = tk.Button(dialog, text="确认", command=confirm)
    confirm_button.pack(pady=10)

    dialog.grab_set()

def add_exam_info():
    # 创建一个新的对话框窗口
    dialog = tk.Toplevel(app)
    dialog.title("添加考试信息")
    dialog.geometry("300x320")
    center_window(dialog)  # 居中显示窗口
    
    # 考试科目名称输入框
    name_label = tk.Label(dialog, text="考试科目名称：")
    name_label.pack(pady=5)
    name_entry = tk.Entry(dialog)
    name_entry.pack(pady=5)
    
    # 考试日期输入框
    date_label = tk.Label(dialog, text="考试日期（格式：YYYY-MM-DD 或 YYYY/MM/DD）：")
    date_label.pack(pady=5)
    date_entry = tk.Entry(dialog)
    date_entry.pack(pady=5)
    
    # 考试开始时间输入框
    start_time_label = tk.Label(dialog, text="考试开始时间（格式：HH:MM:SS）：")
    start_time_label.pack(pady=5)
    start_time_entry = tk.Entry(dialog)
    start_time_entry.pack(pady=5)
    
    # 考试结束时间输入框
    end_time_label = tk.Label(dialog, text="考试结束时间（格式：HH:MM:SS）：")
    end_time_label.pack(pady=5)
    end_time_entry = tk.Entry(dialog)
    end_time_entry.pack(pady=5)

    
    # 确认按钮
    def confirm():
        name = name_entry.get()
        date = date_entry.get()
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()
        
        if not name or not date or not start_time or not end_time:
            messagebox.showerror("错误", "所有字段都不能为空，请重新输入。")
            return
        
        try:
            date = format_date(date)
        except ValueError:
            messagebox.showerror("错误", "日期格式错误，请重新输入。")
            return
        
        start = f"{date}T{convert_colon(start_time)}"
        end = f"{date}T{convert_colon(end_time)}"
        
        if not validate_datetime(start) or not validate_datetime(end):
            messagebox.showerror("错误", "时间格式错误，请重新输入。")
            return
        
        exam_infos.append({
            "name": name,
            "start": start,
            "end": end
        })
        update_exam_list()
        messagebox.showinfo("成功", "考试信息已添加。")
        dialog.destroy()
    
    confirm_button = tk.Button(dialog, text="确认", command=confirm)
    confirm_button.pack(pady=10)
    
    dialog.grab_set()  # 阻止用户与主窗口交互

def save_to_json():
    # 创建一个新的对话框窗口
    dialog = tk.Toplevel(app)
    dialog.title("保存到JSON")
    dialog.geometry("300x250")
    center_window(dialog)  # 居中显示窗口
    
    # 考试标题输入框
    exam_name_label = tk.Label(dialog, text="考试标题：")
    exam_name_label.pack(pady=5)
    exam_name_entry = tk.Entry(dialog)
    exam_name_entry.pack(pady=5)
    
    # 考试副标题输入框
    message_label = tk.Label(dialog, text="考试副标题：")
    message_label.pack(pady=5)
    message_entry = tk.Entry(dialog)
    message_entry.pack(pady=5)
    
    # 考场输入框
    room_label = tk.Label(dialog, text="考场号：")
    room_label.pack(pady=5)
    room_entry = tk.Entry(dialog)
    room_entry.pack(pady=5)
    
    # 确认按钮
    def confirm():
        exam_name = exam_name_entry.get()
        message = message_entry.get()
        room = room_entry.get()
        
        if not exam_name or not message or not room:
            messagebox.showerror("错误", "所有字段都不能为空，请重新输入。")
            return
        
        exam_data = {
            "examName": exam_name,
            "message": message,
            "room": room,
            "examInfos": exam_infos
        }
        
        with open('exam_config.json', 'w', encoding='utf-8') as f:
            json.dump(exam_data, f, ensure_ascii=False, indent=4)
        
        messagebox.showinfo("成功", "JSON文件已生成：exam_config.json")
        dialog.destroy()
    
    confirm_button = tk.Button(dialog, text="确认", command=confirm)
    confirm_button.pack(pady=10)
    
    dialog.grab_set()  # 阻止用户与主窗口交互

def update_exam_list():
    listbox.delete(0, tk.END)
    for info in exam_infos:
        listbox.insert(tk.END, f"{info['name']} - {info['start']} to {info['end']}")

def delete_exam_info():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("错误", "请选择要删除的项目。")
        return
    index = selected[0]
    del exam_infos[index]
    update_exam_list()
    messagebox.showinfo("成功", "考试信息已删除。")

def move_up():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("错误", "请选择要移动的项目。")
        return
    index = selected[0]
    if index == 0:
        return
    exam_infos[index], exam_infos[index - 1] = exam_infos[index - 1], exam_infos[index]
    update_exam_list()
    listbox.select_set(index - 1)

def move_down():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("错误", "请选择要移动的项目。")
        return
    index = selected[0]
    if index == len(exam_infos) - 1:
        return
    exam_infos[index], exam_infos[index + 1] = exam_infos[index + 1], exam_infos[index]
    update_exam_list()
    listbox.select_set(index + 1)
app = tk.Tk()
app.title("考试看板配置生成")
app.geometry("400x350")

# 计算并设置主窗口的位置使其居中显示
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
x = (app.winfo_screenwidth() // 2) - (width // 2)
y = (app.winfo_screenheight() // 2) - (height // 2)
app.geometry('{}x{}+{}+{}'.format(width, height, x, y))

exam_infos = []

add_button = tk.Button(app, text="添加考试信息", command=add_exam_info)
add_button.pack(pady=5)

edit_button = tk.Button(app, text="编辑选中信息", command=edit_exam_info)
edit_button.pack(pady=5)

open_button = tk.Button(app, text="打开配置文件", command=open_config_file)
open_button.pack(pady=5)

delete_button = tk.Button(app, text="删除选中信息", command=delete_exam_info)
delete_button.pack(pady=5)

move_up_button = tk.Button(app, text="上移", command=move_up)
move_up_button.pack(pady=5)

move_down_button = tk.Button(app, text="下移", command=move_down)
move_down_button.pack(pady=5)

save_button = tk.Button(app, text="保存到JSON", command=save_to_json)
save_button.pack(pady=5)

listbox = tk.Listbox(app)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

app.mainloop()
