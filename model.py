import pandas as pd 
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib


def create_dataframe(): 
    dataset = pd.read_csv("/Users/akshit/Flask Development/Projects/Malaria Detection Web App/datasets/final_dataset.csv")
    df = pd.DataFrame(dataset)

    for col in df.columns:
        if col == 'Unnamed: 6':
            df.drop('Unnamed: 6', axis=1, inplace=True)
    
    df.columns = ['area1', 'area2', 'area3', 'area4', 'area5', 'Target']

    df = df.sample(frac=1, random_state=0)

    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1]

    x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

    #print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

    return(x_train, x_test, y_train, y_test)


def Random_Forest_classifier(x_train, y_train):

    # creating random forest classifier
    clf = RandomForestClassifier(n_estimators=100, max_depth=5)
    clf.fit(x_train, y_train)
    
    joblib.dump(clf, '/Users/akshit/Flask Development/Projects/Malaria Detection Web App/randomforest.pkl')


def user_loaded_model():

    clf = joblib.load('/Users/akshit/Flask Development/Projects/Malaria Detection Web App/randomforest.pkl')

    return(clf)


def report_of_model(classifier, x_test, y_test, y_pred):

    clf_score = classifier.score(x_test, y_test)
    confusion_mat = confusion_matrix(y_test, y_pred)
    classfi_report = classification_report(y_test, y_pred)

    return(clf_score, confusion_mat, classfi_report)


def main():
    # start creating dataframe and split the data
    x_train, x_test, y_train, y_test = create_dataframe()

    # select the ML algorithm
    Random_Forest_classifier(x_train, y_train)

    


if __name__ == "__main__":
    main()

    






