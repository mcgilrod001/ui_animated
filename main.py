import customtkinter as ctk
class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

#         general atributes
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)
        print(self.width)

        #animation logic
        self.pos = start_pos
        self.in_start_pos =  True


#       layout
        self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=1)

    def animate(self):
        if self.in_start_pos:
            self.animate_forwards()
        else:
            self.animate_backwards()

    def animate_forwards(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_forwards)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True


def move_button():
    global button_x
    if button_x < 1.2:
        button_x += 0.01
        # button.place(relx=button_x, rely=0.5, anchor='center')
        # frame_x.configure()
        print(button_x)
        window.after(50, move_button)


window = ctk.CTk()
window.title("sliding ui")
window.geometry('600x400')
ctk.set_default_color_theme("dark-blue")


# animated panel
animated_panel = SlidePanel(window, 0, -0.3)
button_x = 0.5


button = ctk.CTkButton(window, text="toggle sidebar", command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, anchor='center')
# frame_x = ctk.CTkFrame(master=window, height=500, width=300, )

# frame_x.pack()





window.mainloop()