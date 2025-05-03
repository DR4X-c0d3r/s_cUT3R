![gray0_ctp_on_line](https://github.com/user-attachments/assets/666442e5-7ae5-485d-9dff-2667aa8efb7e)# <ins>***s_cUT3R***</ins>
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

![U<svg width="600" height="75" viewBox="0 0 600 75" version="1.1" xmlns="http://www.w3.org/2000/svg" style="stroke-linecap: round; stroke-linejoin: round; stroke-miterlimit: 1.5;">
    <path transform="matrix(1,0,0,1,92.3579,4.11772)" d="M105.809,48.397C105.809,44.506 102.473,43.931 102.473,33.503" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 1.5px;"/>
    <path transform="matrix(1,0,0,1,92.3579,4.11772)" d="M109.397,38.324L109.397,48.321" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 1.5px;"/>
    <path transform="matrix(1,0,0,1,92.3579,4.11772)" d="M112.883,48.152C112.883,44.717 115.053,40.554 115.053,35.084C115.053,29.613 114.393,24.795 114.216,21.81" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 1.5px;"/>
    <path transform="matrix(1,0,0,1,92.3579,4.11772)" d="M112.951,22.241C112.951,22.241 116.335,21.976 117.504,16.695" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 1.5px;"/>
    <path transform="matrix(1,0,0,1,92.3579,4.11772)" d="M107.788,11.843C107.788,11.843 106.369,7.434 105.169,7.434C103.969,7.434 101.87,13.187 101.87,21.862C101.87,24.103 90.181,29.985 92.659,43.571C93.057,45.751 94.053,49.908 94.053,49.924C94.053,49.94 96.571,59.453 91.184,59.453C90.063,59.453 89.526,58.833 88.405,58.833C87.285,58.833 86.381,59.598 86.381,60.591C86.381,61.584 87.491,64.025 91.446,64.025C98.593,64.025 98.865,58.038 98.865,54.158C98.865,50.278 98.829,51.479 98.829,50.844C98.829,48.717 100.601,48.284 101.259,48.043" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 1.5px;"/>
    <ellipse transform="matrix(1.00474,-0.404483,0.370766,0.920982,85.4108,49.8267)" cx="111.892" cy="15.766" rx="1.032" ry="1.449" style="fill: rgb(47, 44, 62);"/>
    <path transform="matrix(1,0,0,1,92.3579,4.11772)" d="M110.074,10.347C113.617,10.347 114.448,14.635 117.14,14.635" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 1.5px;"/>
    <path transform="matrix(1,0,0,1,92.3579,4.11772)" d="M112.568,9.074C112.568,9.074 111.553,6.74 110.677,6.74C109.801,6.74 108.537,9.169 108.537,9.169" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 1.5px;"/>
    <path transform="matrix(3.96613,0,0,5.89452,-177.012,-336.835)" d="M93.717,66.428L195.647,66.428" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 0.3px;"/>
    <path transform="matrix(1.78906,0,0,2.78204,-166.7,-130.078)" d="M93.717,66.428L195.647,66.428" style="fill: none; stroke: rgb(110, 108, 126); stroke-width: 0.64px;"/>
</svg>ploading gray0_ctp_on_line.svg…]()
