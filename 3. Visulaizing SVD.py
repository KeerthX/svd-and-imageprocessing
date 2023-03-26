import numpy as np
import matplotlib.pyplot as plt

#Creating a matrix that looks like a sword using arrays from numpy

x = np.array([[0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,2,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,2,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,2,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,2,0,0,0,2,1,1,1,1,1,1,1,1,1,2],
            [1,1,1,1,1,1,2,0,0,0,2,1,1,1,1,1,1,1,2,2],
            [1,1,1,1,1,1,1,2,0,0,0,2,1,1,1,1,1,2,2,2],
            [1,1,1,1,1,1,1,1,2,0,0,0,2,1,1,1,2,2,2,3],
            [1,1,1,1,1,1,1,1,1,2,0,0,0,2,1,2,2,2,3,1],
            [1,1,1,1,1,1,1,1,1,1,2,0,0,0,2,2,2,3,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,2,3,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,2,3,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,1,1],
            [1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,3,1],
            [1,1,1,1,1,1,1,1,1,2,2,2,3,1,1,3,3,3,3,3],
            [1,1,1,1,1,1,1,1,2,2,2,3,1,1,1,1,3,3,3,3],
            [1,1,1,1,1,1,1,2,2,2,3,1,1,1,1,1,1,3,3,3],])

#Define a simple function to perform SVD on a square matrix

def svdiezer(n):
    U,s,VT=np.linalg.svd(x)
    for i in range (n,20): #The 20 in the following example is basically the resolution through 
        #which we will itterate, it is important because it shows how many pixles of the original matrix or image we will use for the compression 
        for j in range (n,20):
            U[i][j] = 0
            VT[j][i] = 0
            VT[i][i] = 0
    r=U@np.diag(s)@VT
    return r

#Itterating through various values of the selection in SVD to Compress the matrix

for n in range (0,21):
    d = svdiezer(n)
    c = np.absolute(d)
    print(n)
    plt.imshow(d)  #Showing the image of the matrix using matplotlib's imshow function that plots a matrix as an image
    plt.show() 

#I prefer to use Spyder because it gives an automatic visualization, the video on how it is done is provided with this git repo.


plt.plot(w,c)
plt.show()
