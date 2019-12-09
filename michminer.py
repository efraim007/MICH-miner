

print(" /$$      /$$ /$$$$$$  /$$$$$$  /$$   /$$       /$$      /$$ /$$")
print("| $$$    /$$$|_  $$_/ /$$__  $$| $$  | $$      | $$$    /$$$|__/")
print("| $$$$  /$$$$  | $$  | $$  \__/| $$  | $$      | $$$$  /$$$$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$")
print("| $$ $$/$$ $$  | $$  | $$      | $$$$$$$$      | $$ $$/$$ $$| $$| $$__  $$ /$$__  $$ /$$__  $$")
print("| $$  $$$| $$  | $$  | $$      | $$__  $$      | $$  $$$| $$| $$| $$  \ $$| $$$$$$$$| $$  \__/")
print("| $$\  $ | $$  | $$  | $$    $$| $$  | $$      | $$\  $ | $$| $$| $$  | $$| $$_____/| $$")
print("| $$ \/  | $$ /$$$$$$|  $$$$$$/| $$  | $$      | $$ \/  | $$| $$| $$  | $$|  $$$$$$$| $$")
print("|__/     |__/|______/ \______/ |__/  |__/      |__/     |__/|__/|__/  |__/ \_______/|__/")
print("github.com/efraim007 - efraim007@protonmail.com")

print ("\n\n")

#import schedule
#import time
import os
import subprocess

#first input paramteres

cleosCmdTr = raw_input('Maxiumum transaction nummber  allowed to MICH mining (1..100..or 1000 etc.): ')
cleosWalletName = raw_input('Please type Cleos Wallet names: ')
cleosAccName = raw_input('Please give your EOS account name: ')
cleosCmd = 'cleos wallet unlock --name '+cleosWalletName


os.system(cleosCmd)

#check the cputime - we need to in the next version

accountInfo = subprocess.check_output('cleos --url https://mainnet.meet.one get account '+cleosAccName, shell=True)
print (accountInfo)
print ("\n\n")

#cleos transfer command
cleosCommandTransfer = 'cleos --url https://mainnet.meet.one transfer '+cleosAccName+' eidosonecoin "0.0001 EOS" "MICH Mining by efraim007 - eoshungary.io"'

cleosMiningStart = raw_input('Do you start MICH mining? y/n ')

#check the integer or not
try:
    cleosCmdTr=int(cleosCmdTr)
except ValueError:
    print ("It is not integer number:"+cleosCmdTr)
else:
    #Start proccess
	if cleosMiningStart == "y":
		i = 1
		while i < cleosCmdTr:
			os.system(cleosCommandTransfer)
			i += 1

		cleosLockCmd = 'cleos wallet lock_all '
		os.system(cleosLockCmd)
		print("Have nice MICH :)! See you tomorrow!")
	else:
		print("Good By without MICH  Mining!"
