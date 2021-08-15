
# Google Summer of Code 2021 "Aztec Glyphs" Report
This Google Sumer of Code project "Visual recognition and deciphering of Aztec glyphs using Keras " is contributed by Lisardo Pérez Lugones with Red Hen Lab. 

## 1. Introduction: 
My goal was to adapt a DeepLearning Mobilenet app developed by Tarun for glyph recognition, create a user Form for image upload to the [Aztec hieroglyphs website](https://aztecglyphs.uoregon.edu/) -University of Oregon- or anywhere...

The main concept for the project was:

- Recreate aztecglyphs.uoregon.edu site
- Integrate a form or end-user webpage for upload images with browser (HTML Javascript JSON Socket-io).
- Provide images to the prototype using FLASK.
- Adapt a prototype working with CPU (non-GPU).
- The result of prediction comes back to the user via same webpage.
- New user images are stored on filesystem.

Server specifications:

- Virtual Machine with 2 cores and 4 GB RAM.
- RedHat 7 Enterprise or CentOS 7 for a non-GPU enviroment.
- Do not reach more than 40 GB of virtual disk availability.
- Aztec hieroglypghs website is developed with Drupal 7.

At the end these were the features:

- User access via 5000 port (i.e. http://127.0.0.1:5000/)
- User can select multiple images (png, jpg, jpeg, gif or webp only)
- User request gest an ID and webpage waits for the results.
- Mobilenet prototype finds the 5 most accurated images from its own dataset.
- Print back in browser with the results per each user image.
- User images are stored on the server for potentially increase the dataset.
- User can clear results and start over.

## 2. Implementation

The tool is made with two files:

- aztecglyphrecognition.py (Mobilenet prototype)

It's adapted from [Tarun's work](https://colab.research.google.com/drive/1rUA51e5Wz-VxsuNOXkfwIcD8PPasXMAG) to Flask. While the client doesn't upload any image, wait in 'blank' mode, if not, upload the image(s), load them and analyze them, get the 5 closes images, extract the features and load the results in an array.

- aztecglyphrecognition.html

There is a fancy label for upload files button. When pressed it's hidden and 'Clear results' is shown instead. Then gets the results of the array from Mobilenet .py with a socket and print back them in the browser. In the meanwhile a gear gif is shown while waiting the predictions.

# Instructions: 

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

## Make it works:

Prerequisites:

- Python 3.9 installed
- Port 5000 allowed
- ./static/uploads/ write permission

>

Again, in our home directory (for me: /var/www/html/aztecglyphs/)

- Creat a virtual environment

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

- Wait and open website in navigator via 5000 port (replace localhost IP with your address)


[http://127.0.0.1:5000/](http://127.0.0.1:5000)


- Enjoy!

08-15-2021

You can have a look at [my GSoC blog](https://lisardop.github.io/) with all the timeline progress.

# VISUAL RESULT

- Main page

![aztecglyphrecognitionhtml](https://raw.githubusercontent.com/lisardop/lisardop.github.io/master/assets/img/aztecglyphrecognitionhtml.jpg)

- Results after upload

![aztecglyphresults](https://lisardop.github.io/assets/img/mendoza_results.jpg)
