from model import user_loaded_model
from make_csv import image_processing
import numpy as np 

# model choose by user
clf = user_loaded_model()

#/Users/akshit/Flask Development/Projects/Malaria Detection Web App/datasets/test/Uninfected/C6NThinF_IMG_20150609_122327_cell_119.png
#/Users/akshit/Flask Development/Projects/Malaria Detection Web App/datasets/test/Parasitized/ParasitizedC39P4thinF_original_IMG_20150622_105335_cell_17.png

def result(path):

    thresh, area_list = image_processing(path)

    predicted_op = np.array(area_list)
    predicted_op = np.reshape(predicted_op, (1, -1))

    output = clf.predict(predicted_op)
    return(output[0])

if __name__ == "__main__":
    result()