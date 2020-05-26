# Outline:

- A clean and minimal command line application that functions as a pomodoro/countdown timer, allowing the user to set the working time and the time for a break as well as a YouTube URL to open for the duration of the break. A more detailed description lies below.

# Purpose:

- I desperately needed a timer application as the ones available had too many periphery features that were distracting and therefore I built a clean one myself. The program was one of the first few projects I built and therefore is slightly clunky and basic but it does the task and helped me understand the value of programming in automation.

# Description:

- The main feature countdown timer is based on the divmod and carriage returns as well as deriving readability from python string formatting.
- The user inputs the time they want to work and time for a break in the min:sec format.
- The timer loops through the countdown for work and displays the current time left following which it enters into the break timer, opening YouTube using the webbrowser module. After the break is over, the tab is shut using the python keyboard module (control + w).
- After this, the user has the option to either restart the current timer, change the timer or simply quit the app.
- The entirety of the timer is built on OOP principles and therefore is housed in a class called timer_pomo:
    - Within the class, there is an initial constructor, __init__:

        ```python
        def __init__(self):
                print("Welcome to the Pomodoro Timer.")
                print("Set the time you want to work and take a break and leave the rest to me!")
                print("Once your work is over, I'll open a YouTube video that you set and close it after the break!")
                print("After that, you can choose to work more, set a different timer or close the app!")
                print("At any time if you wish to quit, please control - c on your keyboard!")
                print("-"*20)
                self.set_timer()
        ```

    - Then is the set_timer method that accepts user values to set minutes and seconds for break and work:

        ```python
        def set_timer(self):
                print("Enter working time in minutes:seconds")
                self.work = input()
                print("Enter break time in minutes:seconds")
                self.br = input()
                print("Please enter the url for the video to play!")
                self.url = input()
                self.load_timer(self.work, self.br)
        ```

    - Then is a load_timer that is the driver for the code, it starts the work_time and break_time functions whilst also dictating the flow by calling next_step:

        ```python
        def load_timer(self, w, b):
                self.w = w
                self.b = b
                print("To start working timer, press enter")
                n = input()
                self.work_time(self.w)
                print("-"*20)
                self.break_time(self.b)
                self.next_step()
        ```

    - The next_step function follows which is called after one iteration of the timer and asks the user whether they want to restart, change the timer or quit the app and calls load_timer, set_timer and quit_timer respectively:

        ```python
        def next_step(self):
                print("To continue working, enter 1.")
                print("To change the time, enter 2.")
                print("To quit the app, enter 3.")
                self.a = input()
                print("-"*20)
                if self.a == '1':
                    self.load_timer(self.work, self.br)
                elif self.a == '2':
                    self.set_timer()
                else:
                    self.quit_timer()
        ```

    - The work_time function initialises the main start_timer function with the working time which it receives from load_timer:

        ```python
        def work_time(self, wtime):
                self.wtime = wtime
                self.num_text = self.wtime.split(":")
                self.wsec = int(self.num_text[0])*60 + int(self.num_text[1])
                print("-"*20)
                print("Working Time")
                self.start_timer(self.wsec)
                return
        ```

    - The break_time does the same as start_time but for the break period, moreover it also opens the url and closes the tab:

        ```python
        def break_time(self, btime):
                self.btime = btime
                self.num_text = self.btime.split(":")
                self.bsec = int(self.num_text[0])*60 + int(self.num_text[1])
                print("Take a walk and listen to the music, it will shut once your break ends!")
                print("-"*20)
                print("Break time")
                webbrowser.open(self.url)
                self.start_timer(self.bsec)
                keyboard.press_and_release("ctrl+w")
                print("Break Over!")
                print("-"*20)
                return
        ```

    - The start_timer which is the actual timer code and uses carriage returns and string formatting to create a timer:

        ```python
        def start_timer(self, s):
                self.s = s
                while self.s>0:
                    self.min, self.sec = divmod(self.s,60)
                    self.tf = '{:02d}:{:02d}'.format(self.min, self.sec)
                    print(self.tf, end = '\r')
                    time.sleep(1)
                    self.s -= 1
                return
        ```

    - The quit timer which performs a sys.exit():

        ```python
        def quit_timer(self):
                sys.exit()
        ```

    - The if __name__ function that creates the object and handles keyboard interrupt through a try and except block:

        ```python
        if __name__ == '__main__':
            try:
                timer1 = timer_pomo()
            except KeyboardInterrupt:
                print("Closing system.")
                time.sleep(3)
                sys.exit()
        ```
