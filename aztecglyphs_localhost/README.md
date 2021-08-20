# Test and implementation:


# 1. Implementation

The tool use two main files:

- aztecglyphrecognition.py (Mobilenet prototype)

It's adapted from [Tarun's work](https://colab.research.google.com/drive/1rUA51e5Wz-VxsuNOXkfwIcD8PPasXMAG) to Flask. While the client doesn't upload any image, wait in 'blank' mode, if not, upload the image(s), load them and analyze them, get the 5 closes images, extract the features and load the results in an array.

- aztecglyphrecognition.html

There is a fancy label for upload files button. When pressed it's hidden and 'Clear results' is shown instead. Then gets the results of the array from Mobilenet .py with a socket and print back them in the browser. In the meanwhile a gear gif is shown while waiting the predictions.

# 3. Main Instructions

*root folder = /var/www/html/*

*home folder = /var/www/html/aztecglyphs/*

- In the console, go to your Home folder and create the subfolders of the project:

./static/

./static/uploads/
*here user uploaded images will be stored*

./static/samples/
*add as folder or soft link to images dataset (for me: /var/www/html/aztecglyphs/sites/default/files/)*

./templates/

- Import the files (check "View Code" on the top of this website):

./aztecglyphrecognition.py
./static/gear.gif
./templates/azteclyphrecognition.html
./templates/blank.html

Prerequisites:

- Python 3.9 installed with pip
- Port 5000 allowed
- ./static/uploads/ write permission
- Remember get aliases for python3.9 and pip3.9

~~~
alias python3=python3.9
alias pip3=pip3.9
~~~

>

# 4. Make-it-works (development)

Again, in our home directory (for me: /var/www/html/aztecglyphs/)

- Create a virtual environment

~~~
python3 -m venv env
~~~

>

- Activate the environment

~~~
source env/bin/activate
~~~

>

- Install dependencies (requirements.txt)

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


[http://127.0.0.1:5000/](http://127.0.0.1:5000)


## VISUAL RESULT

- Main page

![aztecglyphrecognitionhtml](https://lisardop.github.io/assets/img/aztecglyphrecognitionhtml.jpg)

- Results after upload

![aztecglyphrecognition_result](https://lisardop.github.io/assets/img/aztecglyphrecognitionhtml_result.jpg)
