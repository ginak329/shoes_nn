import os
import subprocess
from subprocess import check_output
import matplotlib.pyplot as plt

image_names=os.listdir("/Users/gina/shoes/shoes/images/full")
image_percentage = {}

for image in image_names:
    # print(image)
    cmd=['convert', '/Users/gina/shoes/shoes/images/full/'+image, '-threshold', '92%', '-format', "%[fx:100*image.mean]", 'info:']
    output = float(subprocess.check_output(cmd))

    image_percentage[image] = output
    # print(image_percentage)

    plt.hist(image_percentage.values())

for image in image_percentage:
    if image_percentage[image] >= 75:
        os.rename("/Users/gina/shoes/shoes/images/full/"+image, "/Users/gina/shoes/shoes/main_shoes/"+image)

