# -*- coding: GBK -*-
import tkinter as tk
import random
import time
import sys

class TipApp:
    def __init__(self):
        self.batch_windows = []
        self.single_window = None

    def show_single_tip(self):
        """初始单个界面"""
        self.single_window = tk.Tk()
        self.single_window.title('无隔提示')

        # 屏幕居中显示
        screen_width = self.single_window.winfo_screenwidth()
        screen_height = self.single_window.winfo_screenheight()
        window_width = 350
        window_height = 120
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.single_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 初始提示语
        tip = "小兔子?"
        bg = 'sky blue'
        
        # 尝试不同的字体设置
        try:
            # 尝试使用系统支持的中文字体
            label = tk.Label(
                self.single_window,
                text=tip,
                bg=bg,
                font=('Microsoft YaHei', 14),  # 使用英文字体名
                width=40,
                height=5,
                wraplength=320,
                justify='center'
            )
        except:
            # 如果上面失败，尝试其他字体
            label = tk.Label(
                self.single_window,
                text=tip,
                bg=bg,
                font=('SimHei', 14),  # 黑体
                width=40,
                height=5,
                wraplength=320,
                justify='center'
            )
        label.pack()

        self.single_window.bind('<space>', self.on_space_global)
        self.single_window.attributes('-topmost', True)
        self.single_window.protocol("WM_DELETE_WINDOW", self.start_batch_tips)
        self.single_window.mainloop()

    def create_batch_window(self, count):
        """创建批量弹窗的单个窗口"""
        if count <= 0:
            return

        window = tk.Toplevel()
        self.batch_windows.append(window)

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = 350
        window_height = 120

        x = random.randrange(0, screen_width - window_width)
        y = random.randrange(0, screen_height - window_height)
        window.title('温馨提示')
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        tips = [
            '这个冬天比以往更冷了，不过你来了，我就要和了。',
            '我有一个让今天变特别的方法。',
            '我爱你，我是说我爱你。',
            '原来爱是坠落，是在黄昏的缝隙，当所有意义开始流泪的时候，你抱住了我，让我踏实的坠落。',
            '原则上我不会阻挡你做任何事，但我会陪在你身旁。',
            '在冬天拾起枯叶时，也想起我吧。',
            '愿我的小姑娘，所待皆所念，所行化坦途。',
            '让我和你在做念中沉沦，直到死亡的火光将我们吞没。',
            '只要你相信，我就是你的咒语。',
            '无论你选择在我面前做什么样的人，我都会珍视那份心情。',
            '你永远都有拒绝的权利。',
            '只要你在，晴天或',
            '现在抱着你，就是最简单的娱乐。',
            '从前你是一个人，现在就有我陪你吧。',
            '我很幸运，我的月亮并不是脆弱的倒影。',
            '我将燃尽我的每一寸，为你带来生的路途。',
            '不要难过，我们还会再见的。',
            '无论何时，都可以呼唤我的名字，那是为你定制的咒语。',
            '你靠在我身边的样子我还记得，只可惜那天腾不出手来圈住你。',
            '我把我的手，我的心，我的一切都献给你。',
            '只有当你感到到我的时候，我的存在才有意义。',
            '以后无论发生了什么，我们都不会把彼此弄丢了。',
            '我相信我的小姑娘一定能完成她的目标。',
            '我希望你每天都比原来更坚强更自信，那样才是真正的美丽。',
            '在时空的裂隙中，我触碰到你，就遇见了永恒。',
            '我从不奢望生命给我任何惊喜，直至你出现的那一刻。',
            '在渺茫岁月里唯有你，是我命运的救赎和爱的归途。',
            '感谢你来到我的世界。',
            '我希望往后的一天都能见到你。'
        ]

        tip = random.choice(tips)
        bg_colors = [
            'Light pink', 'sky blue', 'Light green', 'lavender',
            'Light yellow', 'plum', 'coral', 'bisque', 'aquamarine',
        ]
        bg = random.choice(bg_colors)
        
        # 尝试不同的字体设置
        try:
            label = tk.Label(
                window,
                text=tip,
                bg=bg,
                font=('Microsoft YaHei', 14),
                width=40,
                height=3,
                wraplength=320,
                justify='center'
            )
        except:
            label = tk.Label(
                window,
                text=tip,
                bg=bg,
                font=('SimHei', 14),
                width=40,
                height=3,
                wraplength=320,
                justify='center'
            )
        label.pack()

        window.bind('<space>', self.on_space_global)
        window.attributes('-topmost', True)
        window.update()

        if count > 1:
            window.after(50, self.create_batch_window, count - 1)

    def start_batch_tips(self):
        """启动批量弹窗"""
        if self.single_window:
            self.single_window.destroy()
            self.single_window = None

        self.create_batch_window(100)

    def on_space_global(self, event=None):
        """全局空格键退出处理"""
        if self.single_window:
            self.single_window.destroy()

        for window in self.batch_windows:
            try:
                window.destroy()
            except:
                pass
        sys.exit()

if __name__ == '__main__':
    app = TipApp()
    app.show_single_tip()