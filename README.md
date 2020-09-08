# Malaria Detection Using Machine Learning

Let us first understand how actually is Malaria diagnosis  performed in medical field.

*To diagnose malaria under a microscope, a drop of the patient's blood is applied to a glass slide, which is then immersed in a staining solution to make parasites more easily visible under a conventional light microscope, usually with a 100× oil objective. The actual microscopic examination of a single blood slide, including quantitative parasite detection and species identification, takes a trained microscopist 15–30 minutes.*


> Same Idea will be applied in this project.

1.	**Image processing** 

We will read few of the cell samples from the folder and perform some processing techniques. 

•	Firstly read the cell image using OpenCV’s cv2.imread( ) function. 
•	Then convert the RGB format to grayscale image. 
•	After that apply any blurring technique, here I have used Gaussian Kernel for smoothening the image. 
•	Then apply thresholding. In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0,   otherwise, it is set to a maximum value (generally 255). 
•	After this the final process is to find contours. Once you have the contours, find the length of this contours. 
•	We are considering only 5 different length of contours.
•	* *Here we can make an assumption that if the cell is Infected then we would practically find more contours than compared to Uninfected cell sample.* *

2.	**Making dataset file .csv**

As we have seen the process of Image processing above, Now we will run the same method over all training cell samples ( i.e. Parasitized and Uninfected ) and create a .csv file.

3.	**Creating ML Model**

•	Here I have chosen Random Forest Classifier as my algorithm for detection. 
•	Then by the process of cross validation, choose the optimal values of n_estimators and max_depth. 
•	Then fitted the model with the dataset we create above. 
•	Also for checking the progress of the model, we have classification report and accuracy score.
•	* *To minimize the computational power and time, I have saved the model using joblib.* *


4.	**Predicting Test Cell Images**

•	Perform the Image processing technique on required cell sample. 
•	Then get the sorted list of areas of contours detected. Remember our model requires 2D array, so convert the list into NumPy 2D array. 
•	Finally just pass the array to our classifier for predictions. There is your predicted answer of your model !


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

>Technologies needed:

Backend: Scikit-learn, NumPy, Pandas, OpenCV, Joblib
Frontend: html, CSS, bootstrap, JavaScript, jQuery
