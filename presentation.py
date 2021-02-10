import subprocess
# from window_terminal import WindowTerminal
import os
import time


def standard_slide(text, cmd):
	os.system(cmd)
	os.system('clear')
	input(text)

standard_slide("1. hello.", "")
standard_slide("2. fud digital", "open -a Firefox http://fud.global")
standard_slide("3. permaculture network", "open -a Firefox http://root.schloss-post.com")

os.system('clear')
input("4. slime moulds")
os.system('clear')
subprocess.call("./binaries/physarum")

os.system('clear')
input("5. artificial life")
subprocess.call("./binaries/sugarscratch")

os.system('clear')
input("6. talking to bots")
os.system('clear')
###run bot in new window
cmd = """osascript -e 'tell application "Terminal" to do script with command "node /Users/agnes/Documents/WORK/talks/serpentine_art_ai/bot/index.js"'"""
os.system(cmd)
input("Press Enter to continue...")


# print(out)
print("end")
