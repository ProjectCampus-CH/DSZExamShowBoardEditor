import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

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

def add_exam_info():
    name = simpledialog.askstring("输入", "请输入考试科目名称：")
    if not name:
        return
    
    date = simpledialog.askstring("输入", "请输入考试日期（格式：YYYY-MM-DD 或 YYYY/MM/DD）：")
    if not date:
        messagebox.showerror("错误", "日期不能为空，请重新输入。")
        return
    try:
        date = format_date(date)
    except ValueError:
        messagebox.showerror("错误", "日期格式错误，请重新输入。")
        return
    
    start_time = simpledialog.askstring("输入", "请输入考试开始时间（格式：HH:MM:SS）：")
    if not start_time:
        messagebox.showerror("错误", "开始时间不能为空，请重新输入。")
        return
    
    end_time = simpledialog.askstring("输入", "请输入考试结束时间（格式：HH:MM:SS）：")
    if not end_time:
        messagebox.showerror("错误", "结束时间不能为空，请重新输入。")
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

def save_to_json():
    exam_name = simpledialog.askstring("输入", "请输入考试标题：")
    message = simpledialog.askstring("输入", "请输入考试副标题：")
    room = simpledialog.askstring("输入", "请输入考试教室：")
    
    exam_data = {
        "examName": exam_name,
        "message": message,
        "room": room,
        "examInfos": exam_infos
    }
    
    with open('exam_config.json', 'w', encoding='utf-8') as f:
        json.dump(exam_data, f, ensure_ascii=False, indent=4)
    
    messagebox.showinfo("成功", "JSON文件已生成：exam_config.json")

app = tk.Tk()
app.title("考试信息输入")
app.geometry("400x300")

exam_infos = []

add_button = tk.Button(app, text="添加考试信息", command=add_exam_info)
add_button.pack(pady=5)

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
