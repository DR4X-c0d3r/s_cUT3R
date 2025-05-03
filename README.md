# <ins>***s_cUT3R***</ins>
**Before Using The Tool Please Check The Packages And Everything set Okay.**
               __________ __  __   ________  __________________  __
              / ___/ ___// / / /  / ____/ / / /_  __/ ____/ __ \/ /
              \__ \\__ \/ /_/ /  / /   / / / / / / / __/ / /_/ / / 
             ___/ /__/ / __  /  / /___/ /_/ / / / / /___/ _, _/_/  
            /____/____/_/ /_/   \____/\____/ /_/ /_____/_/ |_(_)   
                                                   _[ by DR4X ]_
usage: python3 ssh-bruteforcer.py --help

       python3 ssh-bruteforcer.py -h [hostname] -u [username] -w [wordlist]

       python3 ssh-bruteforcer.py --host [hostname] --username [username] --wordlist [wordlist]

     >> ssh brute forcer <<
**--------------------------------**
 **For Educational Purposes only!**
**--------------------------------**

positional arguments:
  Wordlist          By Default [/usr/share/wordlists/rockyou.txt] Make Sure For Path
  Threads           Low Threads=High_Speed But It Will Affect Your Result. !!!
  Unicodes          Make Sure About Your File Type Before Use -e !!!

optional arguments:
  --help            show this help message and exit
  -h , --host       Target Hostname!
  -u , --username   Target Username!
  -w , --wordlist   Take A Good Wordlist Like Rockyou.txt(default)
  -v, --verbose     Verbose For More Detail About Your Brute Force
  -p , --port       To Connect With Different Port
  -o , --output     To Save Your Result In Your File
  -T , --threads    To Make Your Brute Force Faster Choose [0, 1, 2, 3, 4] One Degit!
  -e , --unicode    To encode Your Wordlist With Your Unicodes

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
exemple: python3 ssh-bruteforcer.py --host 127.0.0.2 --username user --wordlist rockyou.txt -p 22 -v -e [Encoding Type]

**INSTALLATION :**
```
> $ sudo apt install git
> $ git clone https://github.com/DR4X-c0d3r/s_cUT3R.git
> $ cd s_cUT3R
> $ pip install -r requirements.txt
> $ chmod +x s_cUT3R.py | sudo cp s_cUT3R.py /usr/bin/s_cUT3R
```
**Now EveryThing Should Be Good**
**USAGE FOR HELP :**
> $ s_cUT3R --help
![first_pic](https://github.com/user-attachments/assets/6ba6f345-d961-472c-a865-6bef5d401ab0)

**USAGE :**
> $ s_cUT3R -h 127.0.0.1 -u drax -w Desktop/password_list
![second_pic](https://github.com/user-attachments/assets/f30fa33c-1ef2-4528-8515-ba79a6022828)

**VERBOSE MODE :**
> $ s_cUT3R -h 127.0.0.1 -u drax -w Desktop/password_list -v
![third_pic](https://github.com/user-attachments/assets/15942d12-a2e9-4fa5-92ff-83372b84b5e9)

**SAVE RESULT :**
> $ s_cUT3R -h 127.0.0.1 -u drax -w /usr/share/wordlists/rockyou.txt -v -o result.txt
![fourd_pic](https://github.com/user-attachments/assets/83f98016-8cdf-4117-b712-99b98284b4ff)

**SPEED MODE :**(<ins>If You Didn't Read Me In The Help Menu, I Say It Again "HighNumber=GoodResult But! VerySlow, LowNumber=Faster But! Affect Your Result</ins>)
> $ s_cUT3R -h 127.0.0.1 -u drax -w Desktop/password_list -v -T4 #LittleFaster,94%GoodResult
![fifth_pic](https://github.com/user-attachments/assets/fcdc607f-27a6-4b74-82d8-5ea4e3c5c88e)

That's It For Now And I Hope This Tool Makes Your Day Awesome, Remember With Great Power Comes Great Responsibility!
![gray0_ctp_on_line](https://github.com/user-attachments/assets/666442e5-7ae5-485d-9dff-2667aa8efb7e)
