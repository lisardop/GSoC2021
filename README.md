
# Google Summer of Code 2021 "Aztec Glyphs" Report
This Google Sumer of Code project ["Visual recognition and deciphering of Aztec glyphs using Keras"](https://summerofcode.withgoogle.com/projects/#5201622306652160) is contributed by Lisardo Pérez Lugones with [Red Hen Lab](https://sites.google.com/site/distributedlittleredhen/summer-of-code/red-hen-lab-gsoc-2021-projects).

- Code Team: [Tarun Nagdeve ](https://trunnmosby.github.io/GSoC-2021/) & [Lisardo Pérez Lugones](https://lisardop.github.io/)
- Mentors: Stephanie Wood, Jungseock Joo & Juan José Batalla Rosado

# 1. Introduction
My goal was to adapt a DeepLearning Mobilenet app developed by Tarun for glyph recognition, create a user Form for image upload to the [Aztec hieroglyphs website](https://aztecglyphs.uoregon.edu/) -University of Oregon- or anywhere...

The main concept for the project was:

- Recreate aztecglyphs.uoregon.edu site
- Adapt a prototype working with CPU (non-GPU).
- Integrate a form or end-user webpage for upload images with browser (HTML Javascript JSON Socket-io).
- Provide images to the prototype and get the prediction using FLASK.
- The result of prediction comes back to the user via same webpage.
- New user images are stored on a filesystem subfolder.

Server specifications:

- Virtual Machine with 2 cores and 4 GB RAM.
- RedHat 7 Enterprise or CentOS 7 for a non-GPU enviroment.
- Do not reach more than 40 GB of virtual disk availability.
- Aztec hieroglypghs website is developed with Drupal 7.

At the end these were the features (development environment):

- User access via 5000 port (i.e. http://127.0.0.1:5000/)
- User can select multiple images (png, jpg, jpeg, gif or webp only)
- User request gets an ID and webpage waits for the results.
- Mobilenet prototype finds the 5 most accurated images from its own dataset.
- Print back in browser with the results per each user image.
- User images are stored on the server for potentially increase the dataset.
- User can clear results and start over.

Test and implementation:

- This project was tested in a local VM with same server specifications.
- Due to the need for access and availability of end-server admin, the final implementation is still pending but further instructions are provided in this document.

# 2. Implementation

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


[http://127.0.0.1:5000/](http://127.0.0.1:5000)


# 5. Make-it-works (production) as adminuser with root-like privileges

Let's use Apache + WSGI + FLASK with virtual environment

- Go to your home directoy (for me: /var/www/http/aztecglyphs/) and run:

~~~
sudo yum install mod_wsgi
~~~

> 

~~~
pip3 install virtualenv
~~~

> 

Still in your home directory, run:

~~~
virtualenv env_aztecglyphrecognition -p python3
~~~

> 

~~~
source env_name/bin/activate
~~~

> 

~~~
pip3 install flask
~~~

> 

WSGI config

> 

~~~
vi aztecglyphrecognition.wsgi
~~~

> 

edit with:

> 

~~~
from aztecglyphrecongition import app as application

aztecglyphrecognition = '/var/www/html/aztecglyphs/aztecglyphrecognition.py'
execfile(aztecglyphrecognition, dict(__file__=aztecglyphrecognition))
~~~

> 

Now configure Apache for allow directory where VirtualHost config files are.

> 

~~~
vi /etc/httpd/conf/httpd.conf
~~~

> 

If not, add:

~~~
IncludeOptional sites-enabled/*.conf
~~~

> 

Make sure directories /etc/httpd/sites-available/ & /etc/httpd/sites-enabled/ exists

> 

~~~
vi /etc/httpd/sites-available/aztecglyphrecognition.conf
~~~

> 

edit with:

> 

~~~
<VirtualHost *:5000>

        WSGIDaemonProcess azctecglyphrecognition user=apache group=apache threads=5 python-path=/var/www/html/aztecglyphs/env_aztecglyphrecognition:/var/www/html/aztecglyphs/env_aztecglyphrecognition/lib/python3.9/site-packages
  WSGIScriptAlias / /var/www/html/aztecglyphs/aztecglyphrecognition.wsgi
        # You have to add every Flask route as WSGI alias:
        WSGIScriptAlias /(.*) /var/www/html/aztecglyphs/env_aztecglyphrecognition/(.*)
        <Directory /var/www/html/flask>
                WSGIProcessGroup aztecglyphrecognition
                WSGIApplicationGroup %{GLOBAL}
                Order deny,allow
                Allow from all
        </Directory>

        ServerName aztecglyphs.uoregon.edu
        ServerAdmin adminuser@aztecglyphs.uoregon.edu
        DocumentRoot /var/www/html/aztecglyphs
        LogLevel warn
        ErrorLog /var/log/httpd/aztecglyphrecognition-error.log
        CustomLog /var/log/httpd/aztecglyphrecognition-access.log combined

</VirtualHost>
~~~

> 

Create a sof link with enabled sites:

> 

~~~
ln -s /etc/httpd/sites-available/aztecglyphrecognition.conf /etc/httpd/sites-enabled/aztecglyphrecognition.conf
~~~

> 

Check "Apache" user has proper permission under /var/www/html/aztecglyphs/

and restart Apache server:

> 

~~~
sudo service httpd restart
~~~

> 

Now, it should be ready for user (https://yourdomain.here:5000)

> 

## VISUAL RESULT

- Main page

![aztecglyphrecognitionhtml](https://lisardop.github.io/assets/img/aztecglyphrecognitionhtml.jpg)

- Results after upload

![aztecglyphrecognition_result](https://lisardop.github.io/assets/img/aztecglyphrecognitionhtml_result.jpg)

# Updated

08-15-2021

You can have a look at [my GSoC blog](https://lisardop.github.io/) with all the timeline progress.

# License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
