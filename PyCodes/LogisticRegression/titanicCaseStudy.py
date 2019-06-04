import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def TitanicRegressionModel():
    # load data
    titanic_data = pd.read_csv("MarvellousTitanicDataset.csv")
    print("First 10 entries from loaded dataset")
    print(titanic_data.head(10))
    # analys data
    # print("visualize Survived and non Survived passangers")
    # figure()
    # target = "Survived"
    # countplot(data=titanic_data, x=target).set_title("Survived and non Survived passangers")
    # show()
    # figure()
    # target = "Survived"
    # countplot(data=titanic_data, x=target, hue="Sex").set_title("Survived and non Survived passangers based on gender")
    # show()
    # figure()
    # target = "Survived"
    # countplot(data=titanic_data, x=target, hue="Pclass").set_title("Survived and non Survived passangers based on Class")
    # show()
    # figure()
    # target = "Survived"
    # titanic_data["Age"].plot.hist().set_title("Survived and non Survived passangers based on Age")
    # show()
    # data cleanign
    titanic_data.drop("zero", axis=1, inplace=True)
    print("First 10 entries after removing zero column")
    print(titanic_data.head(10))
    print("values of sex column")
    print(pd.get_dummies(titanic_data["Sex"]))
    print("values of sex after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"], drop_first=True)
    print(Sex.head(10))
    print("values of sex after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"], drop_first=True)
    print(Sex.head(10))
    print("values of data sete after concatinate new columns")
    titanic_data = pd.concat([titanic_data, Sex, Pclass], axis=1)
    print(titanic_data.head(10))
    print("values of data set after removing irrelevant data")
    titanic_data.drop(["Sex", "sibsp", "Parch", "Embarked"], axis=1, inplace=True)
    print(titanic_data.head(10))
    x = titanic_data.drop("Survived", axis=1)
    y = titanic_data["Survived"]
    # Data training
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.5)
    logmodel = LogisticRegression()
    logmodel.fit(xtrain, ytrain)
    print("Train data")
    print(xtrain)
    print("Test data is")
    print(xtest)
    # Data Testing
    prediction = logmodel.predict([[2, 27.0, 87.2292, 3, 1, 0, 0]])
    #prediction = logmodel.predict([[585,28.00,8.7125,3,0 ,0,1]])
    #prediction = logmodel.predict([[112,14.50,14.4542,3,1,0,1]])
    # calculate accuracy
    # print("classification_report of Logistic regression is : ")
    # print(classification_report(ytest, prediction))
    # print("confusion_matrix of Logistic regression is : ")
    # print(confusion_matrix(ytest, prediction))
    # print("accuracy of Logistic regression is : ")
    # print(accuracy_score(ytest, prediction))
    print(prediction)


def main():
    print("Survived machine learning")
    TitanicRegressionModel()


if __name__ == "__main__":
    main()
