'''This is my 1st small project which I have created by using  chat gpt help will modify it in future As I grow in python understanding.'''

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import time
import threading

# Global variables to control the alarm set
alarm_triggered = False
snooze_time = 5 # snooze for 5 minute

# File path
image_path = "Getting started/Practice-Repo/100-days-challenge-python/Alarm clock/navi_image/Navi.jpg"
sound_path = "Getting started/Practice-Repo/100-days-challenge-python/Alarm clock/alarm_sound/wakeup-alarm.mp3"

# Function to play alarm sound
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

# Function to stop the alarm sound
def stop_sound():
    pygame.mixer.music.stop()

# Function to show alarm
def show_alarm():
    global alarm_triggered
    alarm_triggered = True

root = tk.Tk()
root.title("Alarm")

# Display image
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label= tk.Label(root,image=photo)
label.pack()

#Display Motivational Message
motivation_text = "I can Do it!"
text_label= tk.Label(root, text=motivation_text, font=("Helvetica", 16))
text_label.pack()

# Play sound
threading.Thread(target=play_sound).start()

# Function to snooze the alarm
def snooze_alarm():
    global alarm_triggered
    alarm_triggered = False
    root.destroy()
    stop_sound()
    time.sleep(snooze_time*60)
    show_alarm()

# Function to turn off the alarm
def turn_off_alarm():
    global alarm_triggered
    alarm_triggered = False
    root.destroy()
    stop_sound()

# Snooze button
snooze_button = tk.Button(root, text= "Snooze", command=snooze_alarm, font=("Helvetica",14))
snooze_button.pack(side=tk.LEFT, padx=20)

# Off button
off_button = tk.Button(root, text= "Off", command=turn_off_alarm,font=("Helvetica",14))
off_button.pack(side=tk.RIGHT, padx=20)

# Keep the window open
root.mainloop()

# Set alarm time(24-Hours format)
alarm_time = "15:05"

while True:
    current_time= time.strftime("%H:%M")
    if current_time ==alarm_time and not alarm_triggered:
        show_alarm()
    time.sleep(60)
