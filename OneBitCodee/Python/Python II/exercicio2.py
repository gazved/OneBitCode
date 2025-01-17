import os
help('os')

os.system('shutdown /s')#desliga em 60 seg
os.system('shutdown /s /t 0')#desliga imediatamente

os.system('shutdown /a')#cancela o desligamento


def turn_off_one_hour():
    os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')

def cancel_shutdown():
    os.system('shutdown /a')