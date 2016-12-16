import os, time

#connect to specific url and open it by Firefox browser
os.system("open -a 'Firefox' 'https://www.google.com'")

os.system('pgrep firefox > PID.txt') #store PID of opened browser to a text file

with open('PID.txt', 'r') as PIDfile: #read PID in the sotred text file
    PID=PIDfile.read().replace('\n', '')

time.sleep(5) #delay 5 seconds to open browser completely
os.system('kill '+PID) #close browser
os.system('rm PID.txt') #remove the PID text file


