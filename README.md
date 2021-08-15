
# 2021GSoC_AztecGlyphs
This Google Sumer of Code project "Visual recognition and deciphering of Aztec glyphs using Keras " is contributed by Lisardo Pérez Lugones with Red Hen Lab. 

## Goal: 
My goal is to do server work between the DeepLearning app in Tensorflow developed by Tarun and the Web app of aztec glyphs in University of Oregon servers.

## Instructions: 

- Prerequisites: Python 3.9

*root folder = /var/www/html/*

*home folder = /var/www/html/aztecglyphs/*

- Go to your Home folder and create a virtual environment

~~~
python3 -m venv env
~~~

>

- Activate the environment

~~~
source env/bin/activate
~~~

>

- Install dependencies

~~~
pip3 install flask flask-executor Werkzeug flask-socketio keras==2.4 pillow
~~~

- Export app name and environment for Flask

~~~
export FLASK_APP=aztecglyphrecognition
export FLASK_ENV=deployment
~~~

>

- Run the project

~~~
python3 -m flask run
~~~

>

- Wait and open website in navigator via 5000 port

~~~
http://127.0.0.1:5000/
~~~

- Enjoy!
