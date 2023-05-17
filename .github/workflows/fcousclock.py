import tkinter as tk
import time

# 创建窗口
root = tk.Tk()
root.title("专注时钟")
root.geometry("300x150")

# 创建标签
timer_label = tk.Label(root, font=("Helvetica", 48))
timer_label.pack(pady=10)

# 定义计时器函数
def countdown(timer):
    while timer >= 0:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=timeformat)
        root.update()
        time.sleep(1)
        timer -= 1

# 启动计时器
countdown(25 * 60)  # 25分钟

# 运行窗口
root.mainloop()
