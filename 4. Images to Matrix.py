#Import the matplotlib package into the python file 
import matplotlib.image as img
import matplotlib.pyplot as plt

#use the imread(file_location) function to read the image.
#the image is read as a matrix with each element representing the value of the colour in that place

image = img.imread('image.jpg') 

#using the imshow property we display the image and we get the same image as before

plt.imshow(image)
plt.show()

#now to view the image as a matrix import the numpy package

import numpy as np 

#use the array function to view the image as a matrix and print it
image_matrix = np.array(image)

print(image_matrix)