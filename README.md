# bitcoin_thief

Firstly, thanks John G.Fisher, I saw your video and I liked the idea of your malware. I could not have written this without your video. 

To those interested his video is here: https://www.youtube.com/watch?v=ljXhijQU9Rk

Another important note, please do not actually spread this to users, it is merely for educational purposes. I am not responsible for your actions. 

This in no means is meant to be a functional virus. It is merely a POC. 

At the moment, code consumes as high as 30% CPU resources on my Intel i7 8565U CPU. Maybe you can try and optimize this? 

Virus would be better if it was 'hidden' in task manager or under another application name, there should be ways to do this some relatively straight forward. 

No registry keys are edited simply the executable is moved to Windows startup folder. This makes it less likely to bypass AV detection but this is just running automatically on restart, it is NOT persistence. 

I believe currently it should still be able to autorun even if not executed initially on admin account as it will just copy to the startup folder of the current user which I believe does not need admin rights, but maybe I am wrong. 

There is some tips for other platforms but the current implementation is mainly targeted at Windows. 

Again, this is merely a POC. 

Virus writing for me is something creative and exciting but it is not something I condone using on systems you are not authroised to use. 




Tips for using: 

1) Edit source code and add your own btc address.

2) Create an executable out of the source code using pyinstaller.

Recommended command: pyinstaller --onefile --windowed bitcoin_thief.py

3) The previous step creates a singular executable file like many of the .exe files you use on Windows. A simple double click will set the virus into motion. 
