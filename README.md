# Raspberry-Pi-Video-Recorder
A video recording apps using Tkinter and OpenCV which will automatically delete files older than 14 days

## To build the repository from empty sd card:
1. Install raspberry pi os from [here](https://downloads.raspberrypi.org/imager/imager_latest.exe) (Use the 32bit recommended version)
2. In Menu -> Preferences -> Raspberry Pi Configuration -> Interfaces, Enable camera, VNC, and Serial Port
3. After restart, type ifconfig in the terminal, look for the ip address of the raspberry pi to VNC into the raspberry pi

## Install dependencies
1. Install Opencv and virtual environment by following this [tutorial](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) (Step 1 to Step 4a is enough)
2. pip install Pillow
3. pip install numpy

## Download repository
1. git clone https://github.com/Ganxiaonan/Raspberry-Pi-Video-Recorder.git
2. cd Raspberry-Pi-Video-Recorder
3. python main.py

The pirecorder should be running

## Enable autoboot at startup
In terminal
1. cd /etc/xdg/lxsession/LXDE-pi
2. sudo nano autostart
3. Add “@lxterminal” at the bottom of autostart, press Ctl+x then y to save and exit to terminal
4. sudo nano ~/.bashrc
5. Append these line at the bottom of the .bashrc file<br />
     #for virtual environment#<br />
     export WORKON_HOME=$HOME/.virtualenvs<br />
     export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3<br />
     source /usr/local/bin/virtualenvwrapper.sh<br />
     <br />
     #command to run every time terminal is lauched#<br />
     workon cv<br />
     cd /home/pi/Raspberry-Pi-Video-Recorder/<br />
     python main.py<br />
6. Ctl+x then y to save and exit to terminal
7. source ~/.bashrc
8. sudo reboot now

The pirecorder should be autoboot at startup now
