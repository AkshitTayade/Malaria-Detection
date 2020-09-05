import glob
import cv2
import os
import matplotlib.pyplot as plt
import random

mypath = '/Users/akshit/Flask Development/Projects/Malaria Detection Web App/datasets/train/'


def image_processing(img):

    img = cv2.imread(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 2)

    ret, thresh = cv2.threshold(img_blur, 127, 255, 0)
    _,contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    area_list = []

    for i in range(0, 5): 
        try:
            area = cv2.contourArea(contours[i])
            area_list.append(str(area))
        
        except:
            area_list.append('0')
        
    return(thresh, sorted(area_list, reverse=True))


def add_points_to_csv(label):
    file_name = open('/Users/akshit/Flask Development/Projects/Malaria Detection Web App/datasets/final_dataset.csv', 'a')


    for img_path in os.listdir(mypath + label):
        
        path = (mypath + label + '/' + img_path)
        img_thresh, areas = image_processing(path)
        
        for i in areas:
            file_name.write(i)
            file_name.write(',')
        
        file_name.write(label)
        file_name.write('\n')
    
    file_name.close()
    

if __name__ == "__main__":
  
    #label = 'Parasitized'
    #label = 'Uninfected'

    #try:
    print('Creating...')
    add_points_to_csv('Uninfected')
    print('CSV file succesfully created.')
    '''
    except:
        print('Error') 
    '''  