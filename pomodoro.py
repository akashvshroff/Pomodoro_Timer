
import time, sys, threading, webbrowser, keyboard

class timer_pomo:

    def __init__(self):
        print("Welcome to the Pomodoro Timer.")
        print("Set the time you want to work and take a break and leave the rest to me!")
        print("Once your work is over, I'll open a YouTube video that you set and close it after the break!")
        print("After that, you can choose to work more, set a different timer or close the app!")
        print("At any time if you wish to quit, please control - c on your keyboard!")
        print("-"*20)
        print("Please enter the url for the video to play!")
        self.url = input()
        print('\n')
        self.set_timer()

    def set_timer(self):
        print("Enter working time in minutes:seconds")
        self.work = input()
        print('\n')
        print("Enter break time in minutes:seconds")
        self.br = input()
        print('\n')
        self.load_timer(self.work, self.br)

    def load_timer(self, w, b):
        self.w = w
        self.b = b
        self.num_text = self.w.split(":")
        self.sec = int(self.num_text[0])*60 + int(self.num_text[1])
        print("To start working timer, press enter")
        n = input()
        self.start_timer(self.sec)
        print("To continue working, enter 1.")
        print("To change the time, enter 2.")
        print("To quit the app, enter 3.")
        self.a = input()
        if self.a == '1':
            self.load_timer(self.work, self.br)
        elif self.a == '2':
            self.set_timer()
        else:
            self.quit_timer()

    def start_timer(self, s):
        print("-"*20)
        print("Working time")
        self.s = s
        while self.s>0:
            self.min, self.sec = divmod(self.s,60)
            self.tf = '{:02d}:{:02d}'.format(self.min, self.sec)
            print(self.tf, end = '\r')
            time.sleep(1)
            self.s -= 1
        print("-"*20)
        print("Time for a break!")
        self.break_timer()
        return

    def break_timer(self):
        print("Take a walk and listen to the music, it will shut once your break ends!")
        print("-"*20)
        print("Break time")
        num_text = self.b.split(":")
        sec = int(num_text[0])*60 + int(num_text[1])
        webbrowser.open(self.url)
        self.b = sec
        while self.b>0:
            self.mb, self.sb = divmod(self.b,60)
            self.tfp = '{:02d}:{:02d}'.format(self.mb, self.sb)
            print(self.tfp, end = '\r')
            time.sleep(1)
            self.b -= 1
        keyboard.press_and_release("ctrl+w")
        print("Break Over!")
        print("-"*20)
        return

    def quit_timer(self):
        sys.exit()

if __name__ == '__main__':
    try:
        timer1 = timer_pomo()
    except KeyboardInterrupt:
        print("Closing system.")
        time.sleep(3)
        sys.exit()
