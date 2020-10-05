# Malaria Detection Using Machine Learning

 <video  style="display:block; width:100%; height:auto;" autoplay controls loop="loop">
       <source src="https://github.com/AkshitTayade/Malaria-Detection/blob/master/static/ML.mp4" type="video/mp4" />
 </video>

Manual diagnosis of blood smears is an intensive manual process that requires expertise in classifying and counting parasitized and uninfected cells. This process may not scale well, especially in regions where the right expertise is hard to find. Some advancements have been made in leveraging state-of-the-art image processing and analysis techniques to extract hand-engineered features and build machine learning-based classification models.

This project talks about one of the easier way of implementing medical analysis process via Machine learning algorithm. Step-by-Step guide is provided below.


**Let us first understand how actually is Malaria diagnosis  performed in medical field.**

*To diagnose malaria under a microscope, a drop of the patient's blood is applied to a glass slide, which is then immersed in a staining solution to make parasites more easily visible under a conventional light microscope, usually with a 100× oil objective. The actual microscopic examination of a single blood slide, including quantitative parasite detection and species identification, takes a trained microscopist 15–30 minutes.*


> Same Idea will be applied in this project.

> [Download Cell Samples](https://drive.google.com/file/d/1Yh4CWRH_Yx9ukwNQG-tNBlGXkk214GjC/view?usp=sharing)<br />

1.	**Image processing** 

     We will read few of the cell samples from the folder and perform some processing techniques. <br />

    •	Firstly read the cell image using OpenCV’s cv2.imread( ) function. <br />
    •	Then convert the RGB format to grayscale image. <br />
    •	After that apply any blurring technique, here I have used Gaussian Kernel for smoothening the image. <br />
    •	Then apply thresholding. In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is             set to 0, otherwise, it is set to a maximum value (generally 255). <br />
    •	After this the final process is to find contours. Once you have the contours, find the length of this contours. <br />
    •	We are considering only 5 different length of contours and then sorting them accordingly.<br />
    •	* *Here we can make an assumption that if the cell is Infected then we would practically find more contours than compared to Uninfected cell sample.* *<br />
     <br /> 

2.	**Making dataset file .csv**<br />
    >_Go to [file](https://github.com/AkshitTayade/Malaria-Detection/blob/master/make_csv.py)_<br />
    <br />
    As we have seen the process of Image processing above, Now we will run the same method over all training cell samples ( i.e. Parasitized and Uninfected ) and       create a .csv file.<br />

 <br /> 

3.	**Creating ML Model** <br />
     >_Go to [file](https://github.com/AkshitTayade/Malaria-Detection/blob/master/model.py)_<br />

    •	Here I have chosen Random Forest Classifier as my algorithm for detection. <br />
    •	Then by the process of cross validation, choose the optimal values of n_estimators and max_depth. <br />
    •	Then fitted the model with the dataset we create above. <br />
    •	Also for checking the progress of the model, we have classification report and accuracy score.<br />
    •	* *To minimize the computational power and time, I have saved the model using joblib.* *<br />


 <br /> 

4.	**Predicting Test Cell Images** <br />
     >_Go to [file](https://github.com/AkshitTayade/Malaria-Detection/blob/master/predictions.py)_<br />

    •	Perform the Image processing technique on required cell sample. <br />
    •	Then get the sorted list of areas of contours detected. Remember our model requires 2D array, so convert the list into NumPy 2D array. <br />
    •	Finally just pass the array to our classifier for predictions. There is your predicted answer of your model !<br />

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

>Technologies needed:

Backend: Scikit-learn, NumPy, Pandas, OpenCV, Joblib <br />
Frontend: html, CSS, bootstrap, JavaScript, jQuery
