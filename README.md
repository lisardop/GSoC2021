
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
- Due to the need for access and availability of end-server admin, the final implementation in Univ. Oregon server is pending, but a functional URL is provided:

[Aztec Glyphs Recognition URL](https://aztecglyphrecognition.herokuapp.com)

NOTE: After one hour of non-use, the URL needs some seconds to wake up. If you get an error from browser, just reload the URL.

# 2. Implementation

There are two main environments:

## AZTECGLYPHS_LOCALHOST (for use in your local machine or VM)

The tool uses two main files:

- aztecglyphrecognition.py (Mobilenet prototype)

It's adapted from [Tarun's work](https://colab.research.google.com/drive/1rUA51e5Wz-VxsuNOXkfwIcD8PPasXMAG) to Flask. While the client doesn't upload any image, wait in 'blank.html' mode, if not, upload image(s), load and analyze them, get the 5 closes images, extract the features and load the results in an array.

- aztecglyphrecognition.html

There is a fancy label for upload files button. When pressed it's hidden and 'Clear results' is shown instead. Then gets the results of the array from Mobilenet .py with a websocket and print back them in the browser. In the meanwhile a gear gif is shown waiting the predictions.

## AZTECGLYPHS_SERVER_PRODUCTION (for deploy in a hosting server)

Use also two main files, the same as in localhost env but renamed and configured for production:

- app.py
- app.html

## VISUAL RESULT

- Main page

![aztecglyphrecognitionhtml](https://lisardop.github.io/assets/img/aztecglyphrecognitionhtml.jpg)

- Results after upload

![aztecglyphrecognition_result](https://lisardop.github.io/assets/img/aztecglyphrecognitionhtml_result.jpg)

# Updated

08-15-2021

You can have a look at [my GSoC blog](https://lisardop.github.io/) with all the timeline progress.

08-20-2021

Here is a functional URL for [Aztec Glyphs Recognition](https://aztecglyphrecognition.herokuapp.com)

# License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
