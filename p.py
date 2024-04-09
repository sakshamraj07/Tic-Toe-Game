from tkinter import *
from tkinter import messagebox
import random

class TIC_TAC_TOE_AI:
    def __init__(self, root):
        self.window = root
        self.make_canvas = Canvas(self.window, background="#141414", relief=RAISED, bd=3)
        self.make_canvas.pack(fill=BOTH, expand=1)

        self.machine_cover = []
        self.human_cover = []
        self.prob = []
        self.sign_store = {}
        
        self.chance_counter = 0
        self.technique = -1
        
        self.surrounding_store = {1: (2,3,4,7), 2:(1,3), 3:(1,2,6,9), 4:(1,7), 5: (2,4,6,8), 6: (3,9), 7:(1,4,8,9), 8:(7,9), 9:(7,8,6,3)}            

        self.decorating()

    def decorating(self):
        Label(self.make_canvas, text="Tic-Tac-Toe AI", bg="#141414", fg="#00FF00", font=("Lato", 25, "bold")).place(x=110, y=10)
        self.activate_btn = []
        for i in range(3):
            for j in range(3):
                btn = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda i=i, j=j: self.__human_play(3*i+j+1), state=DISABLED)
                btn.place(x=20+j*170, y=100+i*100)
                self.activate_btn.append(btn)

        self.machine_first_control = Button(self.make_canvas, text="Machine vs Human", font=("Arial", 15, "bold", "italic"), bg="#262626", activebackground="#262626", fg="#9d9dff", relief=RAISED, bd=3, command=lambda: self.control_give("machine_first"))
        self.machine_first_control.place(x=15, y=380)

        self.human_first_control = Button(self.make_canvas, text="Human vs Machine", font=("Arial", 15, "bold", "italic"), bg="#262626", activebackground="#262626", fg="#9d9dff", relief=RAISED, bd=3, command=lambda: self.control_give("human_first"))
        self.human_first_control.place(x=240, y=380)

        self.reset_btn = Button(self.make_canvas, text="Reset", font=("Arial", 15, "bold", "italic"), bg="#262626", activebackground="#262626", disabledforeground="grey", fg="#9d9dff", relief=RAISED, bd=3, command=self.reset, state=DISABLED)
        self.reset_btn.place(x=190, y=440)

    def reset(self):
        self.machine_cover.clear()
        self.human_cover.clear()
        self.sign_store.clear()
        self.prob.clear()
        self.technique = -1
        self.chance_counter = 0
        for btn in self.activate_btn:
            btn.config(text="")
            btn.config(state=DISABLED)
        self.machine_first_control['state'] = NORMAL
        self.human_first_control['state'] = NORMAL
        self.reset_btn['state'] = DISABLED
    
    def game_over_management(self):
        for btn in self.activate_btn:
            btn.config(state=DISABLED)
        self.reset_btn['state'] = NORMAL
    
    def control_give(self, indicator="human_first"):
        self.machine_first_control.config(state=DISABLED, disabledforeground="grey")
        self.human_first_control.config(state=DISABLED, disabledforeground="grey")
        self.reset_btn.config(state=DISABLED, disabledforeground="grey")
        for btn in self.activate_btn:
            btn.config(state=NORMAL)
        if indicator == "machine_first":
            self.__machine_play()
        
    def __sign_insert(self, btn_indicator, sign_is="X"):
        if sign_is == "X":
            self.activate_btn[btn_indicator - 1].config(text=sign_is, state=DISABLED, disabledforeground="#00FF00")
        else:
            self.activate_btn[btn_indicator - 1].config(text=sign_is, state=DISABLED, disabledforeground="red")
        self.sign_store[btn_indicator] = sign_is
    
    def __machine_play(self):
        self.chance_counter+=1
        if self.chance_counter == 1:
            self.__sign_insert(9)
            self.machine_cover.append(9)

        elif self.chance_counter == 2:
            human_last = self.human_cover[-1]
            if human_last != 5:
                self.technique = 1
                self.__sign_insert(5)
                self.machine_cover.append(5)
            else:
                self.technique = 2
                self.__sign_insert(9)
                self.machine_cover.append(9)
                    
        # Continue with the rest of the game logic...
    
    def __human_play(self, chance):
        self.chance_counter+=1
        self.__sign_insert(chance, "O")
        self.human_cover.append(chance)
        if self.chance_counter == 9:
            self.human_line_match()
        else:    
            self.__machine_play()
    
    def machine_line_match(self):
        # Implement machine line matching logic
        pass
    
    def human_line_match(self):
        # Implement human line matching logic
        pass

if __name__ == "__main__":
    window = Tk()
    window.title("AI Tic-Tac-Toe")
    window.config(bg="#141414")
    window.geometry("450x500")
    window.maxsize(450,500)
    window.minsize(450,500)
    TIC_TAC_TOE_AI(window)
    window.mainloop()
