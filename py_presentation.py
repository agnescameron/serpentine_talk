import subprocess
# from window_terminal import WindowTerminal
import os
import time

def standard_slide(text, cmd):
	os.system(cmd)
	os.system('clear')
	input(text)

os.system("kill $(lsof -t -i:8080)")

standard_slide("1. hello.", "")
input("\n\nthis is a terminal")
os.system("open -a 'Sublime Text' py_presentation.py")
input("this is the code that's running this talk ->") # it's not very good...
input("\n\noutline:")
input("some things i've made ->")
input("-> some remarks about interfaces i use ->")
input("-> some thoughts about computers and intelligence")

standard_slide("2. fud digital \n\nwith gary zhexi zhang \ncomissioned by bloc projects", "open -a Firefox http://fud.global")
standard_slide("3. permaculture network \n\nwith gary zhexi zhang \nfor schloss solitude web residency", "open -a Firefox http://root.schloss-post.com")

os.system('clear')
input("4. slime moulds")
os.system('clear')
subprocess.call("./binaries/physarum")

os.system('clear')
input("5. artifical life simulation for conversions \n\nwith owen trueblood \nfor agnieszka kurant")
os.system('clear')
subprocess.call("./binaries/sugarscratch")
os.system('clear')
input("5. artifical life simulation for conversions \n\nwith owen trueblood \nfor agnieszka kurant")

os.system('clear')
standard_slide("6. bot or not \n\nwith foreign objects \nfor the mozilla creative media awards", "open -a Firefox 'https://botor.no'")
standard_slide("6. bot or not \n\nwith foreign objects \nfor the mozilla creative media awards", "open -a Firefox 'https://dialogflow.cloud.google.com/#/agent/c200103-challenge-truth-bot-wc/editIntent/bc0d6582-f7aa-45f7-9a33-3dd4470012d8/'")
###run bot in new window
cmd = """osascript -e 'tell application "Terminal" to do script with command "node /Users/agnes/Documents/WORK/talks/serpentine_art_ai/bot/index.js"'"""
os.system(cmd)
os.system('clear')
input("6. bot or not \n\nwith foreign objects \nfor the mozilla creative media awards")
os.system('clear')

standard_slide("7. what is it about terminals?", "open 'img/ssh-keygen.png' 'img/fud_market.png' 'img/ipfs.png'")
input("\nagency?")
input("machismo?")
input("entertainment?\n\n\n")
os.system("bunnysay 'idk'")
input("")

standard_slide("8. talking to computers on their own terms", "open img/pfeifer.pdf")
input("~ embodiment")
input("! emergence")
input("? situatedness")
input("what is computer intelligence anyway?")

standard_slide("final note: donate your spare devices!", "open -a Firefox https://www.lambethtechaid.org.uk/")
input("google 'london device donation scheme' to find one locally")
os.system("open -a Firefox 'https://www.google.com/search?hl=en&q=london%20device%20donation%20scheme'")
input("thanks!\n\n")
input("agnes fury cameron")
input("contact: agnesfcameron@gmail.com")
input("for a copy of the code that ran this talk, go to: https://github.com/agnescameron/serpentine_talk\n\n\n")

input("...press enter to quit")